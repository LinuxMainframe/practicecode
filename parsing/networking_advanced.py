"""
# Challenge 10: Build a service detector
def detect_service(host, port):
    
    Connect to port, grab banner, identify service
    
    Examples:
    - Port 22: Read banner, detect "SSH-2.0-OpenSSH_8.2"
    - Port 80: Send "GET / HTTP/1.0\r\n\r\n", read response
    - Port 25: Read SMTP greeting
    
    Return: (service_name, version, banner)
    
    pass

# Can you detect services on 5 different port types?
"""

