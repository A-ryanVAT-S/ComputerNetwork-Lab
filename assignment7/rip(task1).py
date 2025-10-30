import sys
import copy

class RIP:
    def __init__(self, topo):
        self.g = topo
        self.n = list(topo.keys())
        self.rt = {r: {d: float('inf') for d in self.n} for r in self.n}
        for r in self.n:
            self.rt[r][r] = 0
            for nb, c in self.g[r].items():
                self.rt[r][nb] = c
        self.nh = {r: {d: None for d in self.n} for r in self.n}
        for r in self.n:
            self.nh[r][r] = r
            for nb in self.g[r]:
                self.nh[r][nb] = nb
    
    def update(self):
        ch = False
        for r in self.n:
            for nb in self.g[r]:
                for d in self.n:
                    nd = self.rt[nb][d] + self.g[r][nb]
                    if nd < self.rt[r][d] and nd < 16:
                        self.rt[r][d] = nd
                        self.nh[r][d] = nb
                        ch = True
        return ch
    
    def run(self, mx=50):
        print("RIP Simulation")
        it = 0
        while it < mx:
            if not self.update():
                print(f"Converged after {it} iterations")
                break
            it += 1
        else:
            print(f"Stopped after {mx} iterations")
        self.display()
    
    def display(self):
        print("\nRouting Tables:")
        for r in sorted(self.n):
            print(f"\nRouter {r}:")
            print(f"{'Dest':<10} {'Cost':<10} {'Next Hop':<10}")
            for d in sorted(self.n):
                c = self.rt[r][d]
                cs = str(int(c)) if c != float('inf') else "INF"
                nh = self.nh[r][d] if self.nh[r][d] else "-"
                print(f"{d:<10} {cs:<10} {nh:<10}")

if __name__ == "__main__":
    t = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1, 'E': 3},
        'E': {'D': 3}
    }
    
    print("Network Topology:")
    for r, nb in t.items():
        print(f"{r}: {nb}")
    print()
    
    rip = RIP(t)
    rip.run()
  
