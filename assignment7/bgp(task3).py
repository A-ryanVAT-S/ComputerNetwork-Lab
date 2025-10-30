import copy

class BGP:
    def __init__(self, topo, asn):
        self.g = topo
        self.asn = asn
        self.n = list(asn.keys())
        self.rt = {r: {} for r in self.n}
        
        for r in self.n:
            self.rt[r][r] = {'path': [self.asn[r]], 'nh': r}
    
    def update(self):
        ch = False
        for r in self.n:
            for nb in self.g[r]:
                for d in self.rt[nb]:
                    if d == r:
                        continue
                    
                    p = self.rt[nb][d]['path']
                    
                    if self.asn[r] in p:
                        continue
                    
                    np = [self.asn[r]] + p
                    
                    if d not in self.rt[r]:
                        self.rt[r][d] = {'path': np, 'nh': nb}
                        ch = True
                    else:
                        if len(np) < len(self.rt[r][d]['path']):
                            self.rt[r][d] = {'path': np, 'nh': nb}
                            ch = True
        
        return ch
    
    def run(self, mx=50):
        print("BGP Simulation")
        
        print("\nAS Assignments:")
        for r, a in sorted(self.asn.items()):
            print(f"Router {r} -> AS{a}")
        
        it = 0
        while it < mx:
            if not self.update():
                print(f"\nConverged after {it} iterations")
                break
            it += 1
        else:
            print(f"Stopped after {mx} iterations")
        
        self.display()
    
    def display(self):
        print("\nBGP Routing Tables:")
        for r in sorted(self.n):
            print(f"\nRouter {r} (AS{self.asn[r]}):")
            print(f"{'Dest':<10} {'AS Path':<30} {'Next Hop':<10}")
            for d in sorted(self.rt[r].keys()):
                p = ' -> '.join(map(str, self.rt[r][d]['path']))
                nh = self.rt[r][d]['nh']
                print(f"{d:<10} {p:<30} {nh:<10}")

if __name__ == "__main__":
    t = {
        'R1': ['R2'],
        'R2': ['R1', 'R3', 'R4'],
        'R3': ['R2', 'R5'],
        'R4': ['R2', 'R5', 'R6'],
        'R5': ['R3', 'R4'],
        'R6': ['R4']
    }
    
    asn = {
        'R1': 100,
        'R2': 200,
        'R3': 300,
        'R4': 200,
        'R5': 400,
        'R6': 500
    }
    
    print("Network Topology:")
    for r, nb in t.items():
        print(f"{r}: {nb}")
    print()
    
    bgp = BGP(t, asn)
    bgp.run()
