import ssl
import socket
from datetime import datetime


def get_tls_certificate_validity(host, port=443):
    """
    Establishes a TLS connection to the given host and port and retrieves the server's certificate validity period.

    :param host: The hostname (e.g., "example.com") to connect to.
    :param port: The port number to connect to (default is 443 for HTTPS).
    :return: A tuple containing the validity start date and end date (both as datetime objects).
    """
    try:
        # Create a socket and wrap it with SSL
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Get the certificate
                cert = ssock.getpeercert()

                # Extract validity period
                start_date = datetime.strptime(
                    cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
                end_date = datetime.strptime(
                    cert['notAfter'], "%b %d %H:%M:%S %Y %Z")

                print(
                    f"Certificate for {host}:{port} is valid from {start_date} to {end_date}")
                return start_date, end_date

    except Exception as e:
        print(f"Failed to retrieve certificate from {host}:{port}. Error: {e}")
        return None, None


def tls_certificate_validity_task(**kwargs):
    _, end = get_tls_certificate_validity(kwargs['host'], 443)
    return end.isoformat()


# Example usage:
if __name__ == "__main__":
    host = input("Enter the domain name: ")
    port = 443
    start, end = get_tls_certificate_validity(host, port)
    if start and end:
        print(f"Certificate Validity Period: {start} to {end}")
