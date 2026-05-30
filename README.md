# Computer Networks Labs — TCP Client-Server

Academic laboratory assignments for the **Computer Networks** course at Yachay Tech University, deployed and tested on **Amazon EC2** virtual machines via AWS Academy.

## Projects

### TCP Client-Server (`client/` & `server/`)
A basic TCP client-server communication system built with Python sockets and Docker.

- Server deployed on **Amazon EC2**, listens on port `12345` and accepts incoming connections
- Client connects and receives messages from the server
- Each component is containerized with **Docker** for isolated deployment

### Calculator Client-Server (`lab3.3/`)
A distributed calculator application using TCP sockets.

- `calculator_server.py` — receives arithmetic operations and returns results
- `calculator_client.py` — sends operations to the server and displays output

## Technologies

- **Python** — socket programming
- **Docker** — containerization of client and server
- **TCP/IP** — transport layer communication
- **Amazon EC2** — deployed and tested on AWS virtual machines (AWS Academy)

## How to Run

### With Docker
```bash
# Build and run server
cd server
docker build -t tcp-server .
docker run tcp-server

# Build and run client
cd client
docker build -t tcp-client .
docker run tcp-client
```

### Without Docker
```bash
python server/server.py
python client/client.py
```

## Course Info

**Course:** Computer Networks  
**University:** Yachay Tech University  
**Language:** Python
