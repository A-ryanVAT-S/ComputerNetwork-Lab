import cv2
import socket
import math
import time

# Configuration
host_ip = "127.0.0.1"
port = 9999
max_chunk_size = 4096

# Create socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open video file (or 0 for webcam)
video_capture = cv2.VideoCapture("video.mp4")
frames_per_second = video_capture.get(cv2.CAP_PROP_FPS) or 25
interval = 1.0 / frames_per_second

print("Streaming video...")

while video_capture.isOpened():
    success, frame = video_capture.read()
    if not success:
        break

    # Resize frame for faster transfer
    frame_resized = cv2.resize(frame, (640, 480))

    # Encode frame to JPEG
    success, buffer = cv2.imencode(".jpg", frame_resized)
    byte_data = buffer.tobytes()

    # Split into chunks
    num_chunks = math.ceil(len(byte_data) / max_chunk_size)
    for idx in range(num_chunks):
        start_idx = idx * max_chunk_size
        end_idx = start_idx + max_chunk_size
        data_chunk = byte_data[start_idx:end_idx]

        # Add marker: b'1' if last chunk, else b'0'
        marker_byte = b'1' if idx == num_chunks - 1 else b'0'
        udp_socket.sendto(marker_byte + data_chunk, (host_ip, port))

    time.sleep(interval)

video_capture.release()
udp_socket.close()
print("Streaming stopped.")

