import heapq
import sys

class OSPF:
    def __init__(self, topo):
        self.g = topo
        self.n = list(topo.keys())
        self.lsdb = {r: {} for r in self.n}
        
    def flood_lsa(self):
        for r in self.n:
            for nb, c in self.g[r].items():
                self.lsdb[r][nb] = c
    
    def dijkstra(self, src):
        d = {n: float('inf') for n in self.n}
        p = {n: None for n in self.n}
        d[src] = 0
        pq = [(0, src)]
        v = set()
        
        while pq:
            cd, u = heapq.heappop(pq)
            if u in v:
                continue
            v.add(u)
            
            if u not in self.g:
                continue
                
            for nb, w in self.g[u].items():
                nd = cd + w
                if nd < d[nb]:
                    d[nb] = nd
                    p[nb] = u
                    heapq.heappush(pq, (nd, nb))
        
        return d, p
    
    def build_spt(self):
        self.spt = {}
        self.rt = {}
        
        for r in self.n:
            d, p = self.dijkstra(r)
            self.spt[r] = p
            self.rt[r] = d
    
    def run(self):
        print("OSPF Simulation")
        print("Flooding LSAs...")
        self.flood_lsa()
        print("Building SPT using Dijkstra...")
        self.build_spt()
        self.display()
    
    def display(self):
        print("\nLink State Database:")
        for r in sorted(self.n):
            print(f"Router {r}: {self.lsdb[r]}")
        
        print("\nShortest Path Trees:")
        for r in sorted(self.n):
            print(f"\nRouter {r}:")
            print(f"{'Node':<10} {'Parent':<10}")
            for n in sorted(self.n):
                pr = self.spt[r][n] if self.spt[r][n] else "-"
                print(f"{n:<10} {pr:<10}")
        
        print("\nRouting Tables:")
        for r in sorted(self.n):
            print(f"\nRouter {r}:")
            print(f"{'Dest':<10} {'Cost':<10} {'Next Hop':<10}")
            for d in sorted(self.n):
                c = self.rt[r][d]
                cs = str(int(c)) if c != float('inf') else "INF"
                
                nh = d
                curr = d
                while self.spt[r][curr] and self.spt[r][curr] != r:
                    curr = self.spt[r][curr]
                if self.spt[r][curr] == r:
                    nh = curr
                else:
                    nh = "-" if d != r else r
                
                print(f"{d:<10} {cs:<10} {nh:<10}")

if __name__ == "__main__":
    t = {
        'R1': {'R2': 2, 'R3': 5},
        'R2': {'R1': 2, 'R3': 1, 'R4': 3},
        'R3': {'R1': 5, 'R2': 1, 'R4': 2, 'R5': 4},
        'R4': {'R2': 3, 'R3': 2, 'R5': 1},
        'R5': {'R3': 4, 'R4': 1}
    }
    
    print("Network Topology:")
    for r, nb in t.items():
        print(f"{r}: {nb}")
    print()
    
    ospf = OSPF(t)
    ospf.run()
