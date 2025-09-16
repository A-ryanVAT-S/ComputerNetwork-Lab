import cv2
import socket
import numpy as np

# Client setup
host_ip = "0.0.0.0"
port = 9999
max_chunk_size = 4096

# Create socket and bind
socket_instance = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_instance.bind((host_ip, port))

print("Waiting for data... Press 'q' to exit.")

data_buffer = b""

while True:
    data_packet, _ = socket_instance.recvfrom(max_chunk_size + 1)
    flag, data_chunk = data_packet[0:1], data_packet[1:]
    data_buffer += data_chunk

    if flag == b'1':
        # Decode and display frame
        decoded_frame = cv2.imdecode(np.frombuffer(data_buffer, np.uint8), cv2.IMREAD_COLOR)
        data_buffer = b""

        if decoded_frame is not None:
            cv2.imshow("Video Stream", decoded_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

socket_instance.close()
cv2.destroyAllWindows()
print("Connection closed.")

