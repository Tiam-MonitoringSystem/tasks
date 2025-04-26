import subprocess
import re
from typing import Optional

def ping_report_rtt(host: str, count: int = 4) -> Optional[float]:
    """
    Pings a website and reports the average round-trip time (RTT).

    Parameters:
        host (str): The website or IP address to ping.
        count (int): Number of ping attempts (default is 4).

    Returns:
        Optional[float]: The average RTT in milliseconds or None if an error occurs.
    """
    try:
        # Execute the ping command
        result = subprocess.run(
            ["ping", "-c", str(count), host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10  # Add timeout to prevent hanging
        )

        # Check if the ping command was successful
        if result.returncode != 0:
            print(f"Error: Unable to reach {host}.")
            print(result.stderr)
            return None

        # Extract all RTT values using regex
        times = re.findall(r'time=(\d+\.?\d*)', result.stdout)
        
        if not times:
            print(f"No successful pings to {host}")
            return None

        # Convert to floats and calculate average
        times = [float(t) for t in times]
        avg_rtt = sum(times) / len(times)
        return avg_rtt
        
    except subprocess.TimeoutExpired:
        print(f"Ping to {host} timed out")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def ping_rtt_task(**kwargs):
    return ping_report_rtt(kwargs['host'])

if __name__ == "__main__":
    host: str = input("Enter the website or IP address to ping: ")
    avg_rtt: Optional[float] = ping_report_rtt(host)

    if avg_rtt is not None:
        print(f"Average RTT for {host}: {avg_rtt} ms")
