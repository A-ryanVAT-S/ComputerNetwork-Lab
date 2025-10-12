import matplotlib.pyplot as plt
import random
def simulate_tcp_cc(max_rounds, ssthresh_initial):
    cwnd, ssthresh, cwnd_history = 1.0, ssthresh_initial, []
    for r in range(1, max_rounds + 1):
        cwnd_history.append(cwnd)
        num_acks = int(cwnd)
        if random.random() < 0.1 and r > 5:
            print(f"Loss at Round {r}: cwnd={cwnd:.2f}")
            ssthresh = max(int(cwnd / 2), 2)
            cwnd = 1.0
            print(f"Reset: ssthresh={ssthresh}, cwnd={cwnd:.2f}")
            continue
        if cwnd < ssthresh:
            cwnd += num_acks
            print(f"Round {r}: Slow Start, cwnd={cwnd:.2f}")
        else:                                                                                                                   
            cwnd += num_acks * (1.0 / cwnd)
            print(f"Round {r}: Congestion Avoidance, cwnd={cwnd:.2f}")

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, max_rounds + 1), cwnd_history, marker='o', linestyle='-', color='b')
    plt.title('TCP Congestion Window (cwnd) Simulation')
    plt.xlabel('Transmission Rounds')
    plt.ylabel('Congestion Window (cwnd)')
    plt.grid(True)
    plt.savefig('cwnd_plot.png')
    print("Plot generated: cwnd_plot.png")
    
if __name__ == "__main__":
    simulate_tcp_cc(25, 8)
