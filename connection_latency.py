import socket
import time
import math


def tcp_connection_latency(host, port, timeout=5):
    """
    Measures the TCP dial delay for establishing a connection to a given host and port.

    :param host: The hostname or IP address of the target server.
    :param port: The port number of the target server.
    :param timeout: Connection timeout in seconds (default is 5 seconds).
    :return: TCP dial delay in seconds, or None if the connection could not be established.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        # Record the start time
        start_time = time.time()

        # Try to connect to the host and port
        sock.connect((host, port))

        # Record the end time
        end_time = time.time()

        # Calculate the TCP dial delay
        dial_delay = end_time - start_time

        print(f"TCP dial delay to {host}:{port} is {dial_delay:.4f} seconds")
        return dial_delay

    except Exception as e:
        print(f"Failed to connect to {host}:{port}. Error: {e}")
        return math.inf

    finally:
        # Ensure the socket is closed
        sock.close()


def tcp_connection_latency_task(**kwargs):
    return tcp_connection_latency(kwargs['host'], 443)


if __name__ == "__main__":
    # Example usage
    domain_name = input("Enter the domain name: ")
    port = input("Enter port number: ")

    latency = tcp_connection_latency(domain_name, port)

    print(f"Latency of TCP connection is : {latency}")
