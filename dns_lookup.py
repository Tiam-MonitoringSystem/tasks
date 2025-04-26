import socket
from typing import Optional

def dns_lookup(domain: str) -> Optional[str]:
    """
    Performs a DNS lookup for the given domain name and returns its IP address.

    Parameters:
        domain (str): The domain name to resolve.

    Returns:
        Optional[str]: The resolved IP address, or None if the lookup fails.
    """
    try:
        # Perform DNS lookup
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        print(f"Error: Unable to resolve domain '{domain}'. {e}")
        return None

def dns_lookup_task(**kwargs):
    return dns_lookup(kwargs['host'])


if __name__ == "__main__":
    # Example usage
    domain_name = input("Enter the domain name: ")
    ip = dns_lookup(domain_name)

    if ip:
        print(f"The IP address for {domain_name} is: {ip}")
    else:
        print(f"Failed to resolve the IP address for {domain_name}.")
