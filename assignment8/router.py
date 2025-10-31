from ip_utils import ip_to_binary, get_network_prefix

class Router:
  
    def __init__(self, routes: list):
        
        # This will store our optimized forwarding table
        self.forwarding_table = []
        self._build_forwarding_table(routes)

    def _build_forwarding_table(self, routes: list):
        
        temp_table = []
        for cidr, link in routes:
            # Get the binary prefix for each CIDR route
            binary_prefix = get_network_prefix(cidr)
            temp_table.append((binary_prefix, link))
        
        # Sort the table by the length of the binary prefix (x[0]),
        # from longest to shortest (reverse=True).
        self.forwarding_table = sorted(temp_table, key=lambda x: len(x[0]), reverse=True)
        
        print("Built Forwarding Table (Longest to Shortest):")
        for prefix, link in self.forwarding_table:
             print(f"  {prefix} (len {len(prefix)}) -> {link}")

    def route_packet(self, dest_ip: str) -> str:
        
        # 1. Convert the destination IP to its 32-bit binary representation
        binary_dest_ip = ip_to_binary(dest_ip)
        
        # 2. Iterate through the sorted forwarding table
        for prefix, link in self.forwarding_table:
            
            # 3. Check if the binary destination IP starts with the prefix
            if binary_dest_ip.startswith(prefix):
                
                # 4. First match is the longest match, so return the link
                return link
        
        # If no match is found after checking all routes
        return "Default Gateway"

if __name__ == "__main__":
    print("\n--- Testing router.py ---")
    
    # Initialize the router with the test case routes
    routes_list = [
        ("223.1.1.0/24", "Link 0"),
        ("223.1.2.0/24", "Link 1"),
        ("223.1.3.0/24", "Link 2"),
        ("223.1.0.0/16", "Link 4 (ISP)")
    ]
    
    my_router = Router(routes_list)
    
    # Test cases
    test_ips = [
        "223.1.1.100",  # Should match "Link 0"
        "223.1.2.5",    # Should match "Link 1"
        "223.1.250.1",  # Should match "Link 4 (ISP)"
        "198.51.100.1"  # Should match "Default Gateway"
    ]
    
    print("Routing packets:")
    for ip in test_ips:
        link = my_router.route_packet(ip)
        print(f"  IP: {ip} -> Output: {link}")

    # Verify expected results
    assert my_router.route_packet("223.1.1.100") == "Link 0"
    assert my_router.route_packet("223.1.2.5") == "Link 1"
    assert my_router.route_packet("223.1.250.1") == "Link 4 (ISP)"
    assert my_router.route_packet("198.51.100.1") == "Default Gateway"
    
    print("All test cases passed.")
