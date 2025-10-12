import random, time
def simulate_go_back_n(total_frames, window_size, p_loss):
    base, next_seq = 0, 0
    while base < total_frames:
        send_list = []
        while next_seq < total_frames and next_seq < base + window_size:
            send_list.append(str(next_seq))
            next_seq += 1
        
        if send_list:
            print(f"Sending frames {' '.join(send_list)}")
            
        time.sleep(0.1)

        if random.random() < p_loss and base < total_frames:
            retransmit_start = base
            retransmit_end = next_seq - 1
            print(f"Frame {base} lost, retransmitting frames {retransmit_start} - {retransmit_end}")
            next_seq = retransmit_start
            time.sleep(0.1)
            continue
        
        if base < total_frames:
            acked_frame = base + 1
            new_window_end = base + window_size
            print(f"ACK {acked_frame} received. Window slides to {base + 1} - {new_window_end}")
            base = acked_frame
            time.sleep(0.05)

if __name__ == "__main__":
    simulate_go_back_n(15, 4, 0.2)
