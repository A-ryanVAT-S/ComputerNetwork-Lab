# File: scheduler.py

from dataclasses import dataclass

@dataclass
class Packet:

    source_ip: str
    dest_ip: str
    payload: str
    priority: int

    # This makes printing the packet list more readable
    def __repr__(self):
        return f"Packet(payload='{self.payload}', priority={self.priority})"


def fifo_scheduler(packet_list: list) -> list:
    
    # We simply return a new list containing the packets
    # in their original arrival order.
    return list(packet_list)

def priority_scheduler(packet_list: list) -> list:
   
    # Sort the list based on the 'priority' attribute of each packet
    return sorted(packet_list, key=lambda packet: packet.priority)


# --- Main execution block to run the Test Case ---
if __name__ == "__main__":
    print("\n--- Testing scheduler.py ---")
    
    # Create the test case list of packets (in arrival order)
    # (Using dummy IPs as they don't affect scheduling)
    arrival_order = [
        Packet("10.0.0.1", "8.8.8.8", "Data Packet 1", 2), # Low
        Packet("10.0.0.2", "8.8.8.8", "Data Packet 2", 2), # Low
        Packet("10.0.0.3", "8.8.8.8", "VOIP Packet 1", 0), # High
        Packet("10.0.0.4", "8.8.8.8", "Video Packet 1", 1),# Medium
        Packet("10.0.0.5", "8.8.8.8", "VOIP Packet 2", 0)  # High
    ]
    
    print(f"Arrival Order:\n  {arrival_order}\n")
    
    # 1. Test FIFO Scheduler
    fifo_output = fifo_scheduler(arrival_order)
    print(f"FIFO Send Order:")
    for p in fifo_output:
        print(f"  {p.payload}")
        
    # Verify FIFO results
    fifo_payloads = [p.payload for p in fifo_output]
    assert fifo_payloads == [
        "Data Packet 1", "Data Packet 2", "VOIP Packet 1", 
        "Video Packet 1", "VOIP Packet 2"
    ]

    # 2. Test Priority Scheduler
    priority_output = priority_scheduler(arrival_order)
    print(f"\nPriority Send Order:")
    for p in priority_output:
        print(f"  {p.payload}")
        
    # Verify Priority results
    priority_payloads = [p.payload for p in priority_output]
    assert priority_payloads == [
        "VOIP Packet 1", "VOIP Packet 2", # Priority 0 (stable)
        "Video Packet 1",                # Priority 1
        "Data Packet 1", "Data Packet 2"  # Priority 2 (stable)
    ]
    
    print("\nAll test cases passed.")
