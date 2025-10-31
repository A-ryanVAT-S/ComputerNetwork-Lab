# File: ip_utils.py

def ip_to_binary(ip_address: str) -> str:
  
    # Split the IP into its four octets
    octets = ip_address.split('.')
    
    # Convert each octet to an 8-bit binary string, padding with leading zeros
    binary_octets = [bin(int(o))[2:].zfill(8) for o in octets]
    
    # Join the 8-bit strings to create the full 32-bit binary string
    return "".join(binary_octets)

def get_network_prefix(ip_cidr: str) -> str:
 
    # Split the CIDR string into the IP and the prefix length
    ip, prefix_len_str = ip_cidr.split('/')
    prefix_len = int(prefix_len_str)
    
    # Convert the IP part to its full 32-bit binary representation
    binary_ip = ip_to_binary(ip)
    
    # Return only the network prefix part (the first 'prefix_len' bits)
    return binary_ip[:prefix_len]


if __name__ == "__main__":
    print("--- Testing ip_utils.py ---")
    
    # Test ip_to_binary
    ip1 = "192.168.1.1"
    bin_ip1 = ip_to_binary(ip1)
    print(f"IP: {ip1} -> Binary: {bin_ip1}")
    
    ip2 = "200.23.16.0"
    bin_ip2 = ip_to_binary(ip2)
    print(f"IP: {ip2} -> Binary: {bin_ip2}")

    # Test get_network_prefix
    cidr = "200.23.16.0/23"
    prefix = get_network_prefix(cidr)
    print(f"CIDR: {cidr} -> Prefix: {prefix}")
    print(f"Prefix Length: {len(prefix)}")
