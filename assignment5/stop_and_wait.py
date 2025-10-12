import random, time
def simulate_stop_and_wait(total_frames, p_loss):
    frame = 0
    while frame < total_frames:
        print(f"Sending Frame {frame}")
        if random.random() < p_loss:
            print(f"Frame {frame} lost, retransmitting...")
            time.sleep(0.01)
            continue
        if random.random() < p_loss:
            print(f"ACK for Frame {frame} lost, retransmitting...")
            time.sleep(0.01)
            continue
        print(f"ACK {frame} received")
        frame += 1
        time.sleep(0.01)
if __name__ == "__main__":
    simulate_stop_and_wait(5, 0.3)
