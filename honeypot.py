
import socket
import datetime
 
# --- Configuration ---
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 23         # Port to listen on (23 is the default for Telnet)
LOG_FILE = 'honeypot_log.txt'
FAKE_BANNER = "Welcome to the Telnet server!\r\nUser: "
 
def log_activity(message):
    """Logs the activity to the console and a file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    print(full_message)
    with open(LOG_FILE, 'a') as f:
        f.write(full_message + '\n')
 
def run_honeypot():
    """Initializes and runs the honeypot listener."""
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    # Allow reusing the address to avoid "Address already in use" errors
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   
    try:
        # Bind the socket to the host and port
        server_socket.bind((HOST, PORT))
       
        # Start listening for incoming connections
        server_socket.listen(5)
        log_activity(f"Honeypot listening for connections on port {PORT}...")
 
        while True:
            # Wait for a connection
            client_socket, client_address = server_socket.accept()
           
            # Log the connection attempt
            log_activity(f"Connection received from: {client_address[0]}:{client_address[1]}")
           
            try:
                # Send a fake banner to the attacker
                client_socket.send(FAKE_BANNER.encode('utf-8'))
               
                # Receive and log data from the attacker
                data = client_socket.recv(1024)
                if data:
                    log_activity(f"Data received from {client_address[0]}: {data.decode('utf-8', errors='ignore').strip()}")
               
            except socket.error as e:
                log_activity(f"Socket error with {client_address[0]}: {e}")
            finally:
                # Close the connection
                client_socket.close()
 
    except PermissionError:
        log_activity(f"Permission denied to bind to port {PORT}. Try running with sudo or use a port > 1024.")
    except KeyboardInterrupt:
        log_activity("Honeypot shutting down.")
    except Exception as e:
        log_activity(f"Error occurred: {e}", LOG_FILE)

import socket
import datetime
import argparse
 
def log_activity(message, log_file):
    """Logs a message to the console and a specified log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    print(full_message)
    try:
        with open(log_file, 'a') as f:
            f.write(full_message + '\n')
    except IOError as e:
        print(f"Error: Could not write to log file {log_file}. {e}")
 
def run_honeypot(host, port, log_file):
    """Initializes and runs the honeypot listener."""
   
    log_activity(f"Starting honeypot...", log_file)
   
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    # Allow reusing the address to avoid "Address already in use" errors
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        log_activity(f"Honeypot listening for connections on {host}:{port}", log_file)
 
        while True:
            client_socket, client_address = server_socket.accept()
            log_activity(f"Connection received from: {client_address}:{client_address}", log_file)
           
            try:
                # Send a fake banner to make the service look real
                client_socket.send("Welcome to the Telnet server!\r\nUser: ".encode('utf-8'))
               
                # Receive and log any data sent by the client
                data = client_socket.recv(1024)
                if data:
                    decoded_data = data.decode('utf-8', errors='ignore').strip()
                    log_activity(f"Data received from {client_address}: {decoded_data}", log_file)
                   
            except socket.error as e:
                log_activity(f"Socket error with {client_address}: {e}", log_file)
            finally:
                client_socket.close()
 
    except PermissionError:
        log_activity(f"Permission denied to bind to port {port}. Try running with 'sudo' or use a port > 1024.", log_file)
    except OSError as e:
        log_activity(f"OSError: {e}. The port may already be in use.", log_file)
    except KeyboardInterrupt:
        log_activity("Honeypot shutting down.", log_file)
    finally:
        server_socket.close()
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple Python Honeypot.")
    parser.add_argument('--host', default='0.0.0.0', help="Host to bind the honeypot to. (Default: 0.0.0.0)")
    parser.add_argument('--port', type=int, default=23, help="Port to listen on. (Default: 23 - Telnet)")
    parser.add_argument('--logfile', default='honeypot_log.txt', help="File to write logs to. (Default: honeypot_log.txt)")
   
    args = parser.parse_args()
   
    run_honeypot(args.host, args.port, args.logfile)
 