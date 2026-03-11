# calculator_client.py

import socket       # Import socket library for network communication
import json         # Import JSON library to serialize/deserialize data

HOST = "34.235.155.245"   # Server IP address
PORT = 80               # Server port (must be the same as the server)

while True:
    print("\nCalculadora de Yeis")
    print("1. add  2. sub  3. mul  4. div  5. salir")

    choice = input("Elige operación (1-5): ")

    if choice == "5":
        print("Adios")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Opción inválida")
        continue

    ops = {"1": "add", "2": "sub", "3": "mul", "4": "div"}
    operation = ops[choice]

    # Ask user for numbers first
    a_input = input("Enter first number: ")   # Prompt user for first number
    b_input = input("Enter second number: ")  # Prompt user for second number

    # Convert input to float (so server receives a number, not a regular string)
    try:
        a = float(a_input)   # Try to convert first input to float
        b = float(b_input)   # Try to convert second input to float
    except ValueError:        # If conversion fails (non-numeric input)
        print("Invalid input! Please enter numeric values.")  # Show error message
        continue

    # Prepare payload (data to send to server)
    payload = {"operation": operation, "a": a, "b": b}           # Create dictionary with the numbers
    payload_json = json.dumps(payload)   # Convert dictionary to JSON string

    # Connect to server and send data
    client_socket = socket.socket()                 # Create a TCP socket object
    try:
        client_socket.connect((HOST, PORT))         # Establish connection to server
        client_socket.send(payload_json.encode())   # Send JSON string encoded as bytes

        # Receive response from server
        response_data = client_socket.recv(1024)     # Receive up to 1024 bytes
        response = json.loads(response_data.decode()) # Decode bytes → str, then parse JSON → dict

        # Print result depending on server's response
        if response.get("code") == 200:   # If status code is OK
            print(f"\nLogs")
            print(response.get("log"))
            print(f"Result from server: {response['result']}")
        else:
            print(f"\nLogs")
            print(response.get("log"))
            print(f"Error from server: {response.get('error')} (code {response.get('code')})")

    except ConnectionRefusedError:
        print("Could not connect to the server. Is it running?")
    finally:
        client_socket.close()