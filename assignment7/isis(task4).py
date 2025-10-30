import heapq
import copy

class ISIS:
    def __init__(self, topo):
        self.g = topo
        self.n = list(topo.keys())
        self.lsdb = {r: {} for r in self.n}
    
    def flood_lsp(self):
        for r in self.n:
            for nb, c in self.g[r].items():
                self.lsdb[r][nb] = c
    
    def sync_db(self):
        for _ in range(len(self.n)):
            for r in self.n:
                for nb in self.g[r]:
                    for n in self.lsdb[nb]:
                        if n not in self.lsdb[r]:
                            self.lsdb[r][n] = self.lsdb[nb][n]
    
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
    
    def compute_routes(self):
        self.spt = {}
        self.rt = {}
        
        for r in self.n:
            d, p = self.dijkstra(r)
            self.spt[r] = p
            self.rt[r] = d
    
    def run(self):
        print("IS-IS Simulation")
        
        print("Flooding LSPs...")
        self.flood_lsp()
        
        print("Synchronizing Link-State Database...")
        self.sync_db()
        
        print("Computing routes using Dijkstra...")
        self.compute_routes()
        
        self.display()
    
    def display(self):
        print("\nLink State Database:")
        for r in sorted(self.n):
            print(f"\nRouter {r}:")
            if self.lsdb[r]:
                for nb, c in sorted(self.lsdb[r].items()):
                    print(f"  {nb}: {c}")
            else:
                print("  Empty")
        
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
        'IS1': {'IS2': 3, 'IS3': 6},
        'IS2': {'IS1': 3, 'IS3': 2, 'IS4': 4},
        'IS3': {'IS1': 6, 'IS2': 2, 'IS4': 1, 'IS5': 5},
        'IS4': {'IS2': 4, 'IS3': 1, 'IS5': 2},
        'IS5': {'IS3': 5, 'IS4': 2}
    }
    
    print("Network Topology:")
    for r, nb in t.items():
        print(f"{r}: {nb}")
    print()
    
    isis = ISIS(t)
    isis.run()
