import socket
import threading

# Lock to prevent print collisions in threads
print_lock = threading.Lock()

# Scan a single port
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Timeout for faster scanning
            result = s.connect_ex((ip, port))
            if result == 0:
                with print_lock:
                    print(f"[+] Port {port} is OPEN")
    except Exception as e:
        pass

# Launch threads to scan a range of ports
def scan_ports(ip, start_port, end_port):
    print(f"Scanning {ip} from port {start_port} to {end_port}...\n")
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nScanning complete.")

# Example usage
if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))

    scan_ports(target_ip, start, end)
