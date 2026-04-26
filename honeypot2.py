import socket
import threading
import datetime

HOST = '2.24.31.61'  # Listen on all interfaces
PORT = 2222       # Change to any port > 1024 if you don't want to use sudo
LOG_FILE = 'honeypot.log'

def log_activity(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[{timestamp}] {message}")

def handle_client(client_socket, client_address):
    log_activity(f"Connection from {client_address[0]}:{client_address[1]}")
    try:
        client_socket.sendall(b"Welcome to the honeypot!\n")
        data = client_socket.recv(1024)
        if data:
            log_activity(f"Data from {client_address[0]}: {data.decode(errors='ignore').strip()}")
    except Exception as e:
        log_activity(f"Error with {client_address[0]}: {e}")
    finally:
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    log_activity(f"Honeypot listening on port {PORT}")
    try:
        while True:
            client, addr = server.accept()
            threading.Thread(target=handle_client, args=(client, addr), daemon=True).start()
    except KeyboardInterrupt:
        log_activity("Honeypot shutting down.")
    finally:
        server.close()

if __name__ == "__main__":
    main()