# calculator_server.py

import socket  # Import the socket module to create TCP connections
import json    # Import JSON module to parse and send data in JSON format

HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 80       # Use port 80 for this server (common for web apps)

def handle_request(data, addr):
    # Log the request
    print(f"Client IP: {addr[0]} | Data received: {data}")
    
    try: 
        payload = json.loads(data)  # Convert JSON string to Python dictionary
        operation = payload.get("operation")
        a, b = payload.get("a"), payload.get("b")  # Extract 'a' and 'b' from dictionary

        # Check if parameters are missing
        if operation is None or a is None or b is None:
            return {"error": "Parametros perdidos", "code": 400, "log": f"Client IP: {addr[0]} | Missing parameters"}

        # Check if parameters are numbers
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return {"error": "Nunmeros no validos", "code": 422, "log": f"Client IP: {addr[0]} | Invalid input"}

        # Perform the operation
        if operation == "add":
            return {"result": a + b, "code": 200, "log": f"Client IP: {addr[0]} | Operation: {operation} | a: {a} | b: {b}"}
        elif operation == "sub":
            return {"result": a - b, "code": 200, "log": f"Client IP: {addr[0]} | Operation: {operation} | a: {a} | b: {b}"}
        elif operation == "mul":
            return {"result": a * b, "code": 200, "log": f"Client IP: {addr[0]} | Operation: {operation} | a: {a} | b: {b}"}
        elif operation == "div":
            if b == 0:
                return {"error": "No puedes dividir para 0", "code": 422, "log": f"Client IP: {addr[0]} | Division by zero"}
            return {"result": a / b, "code": 200, "log": f"Client IP: {addr[0]} | Operation: {operation} | a: {a} | b: {b}"}
        else:
            return {"error": "Operacion no valida. Usa add, sub, mul, div", "code": 400, "log": f"Client IP: {addr[0]} | Invalid operation: {operation}"}

    except json.JSONDecodeError:
        return {"error": "Invalid JSON", "code": 400, "log": f"Client IP: {addr[0]} | Invalid JSON"}

# Socket setup
server_socket = socket.socket()        # Create a TCP socket (IPv4 + TCP)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of the address
server_socket.bind((HOST, PORT))      # Bind socket to HOST and PORT
server_socket.listen(5)                # Listen for connections. '5' = max queued connections
print(f"Calculator server running on {HOST}:{PORT}")  # Inform server is ready

# Main loop to accept clients
while True:
    conn, addr = server_socket.accept()  # Wait for a client to connect (blocking)
    data = conn.recv(1024).decode()      # Receive up to 1024 bytes and decode from bytes to string
    response = handle_request(data, addr)      # Process the request and get response dictionary
    conn.send(json.dumps(response).encode())  # Convert/serialize response to JSON string, encode to bytes, and send
    conn.close()                         # Close connection with the client
