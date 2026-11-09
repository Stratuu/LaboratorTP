import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )
)

from arsenal.aparare.parse_auth import citeste_esecuri, pe_ip

# B1
def suspecti(counts, prag=10):
    if prag < 1:
        raise ValueError(f"prag invalid: {prag} (cel putin 1)")
    return [(ip, n) for ip, n in counts.most_common() if n >= prag]
 
from collections import Counter
c = Counter({"203.0.113.9": 13, "198.51.100.7": 2})
print(suspecti(c))
print(suspecti(c, prag=2))

# B3
import argparse, json
from collections import Counter
from arsenal.aparare.parse_auth import citeste_esecuri
 
def main():
    p = argparse.ArgumentParser()
    p.add_argument("log")
    p.add_argument("--prag", type=int, default=10)
    p.add_argument("--json", action="store_true")
    p.add_argument("--fereastra", type=int)
    p.add_argument("--top", type=int)
    a = p.parse_args()
    esecuri = citeste_esecuri(a.log)
    if a.fereastra is not None and esecuri:
        ultimul = max(e["timp"] for e in esecuri if e["timp"] is not None)

        esecuri = [
         e for e in esecuri
          if e["timp"] is not None
          and (ultimul - e["timp"]).total_seconds() <= a.fereastra
        ]
    counts = Counter(e["ip"] for e in esecuri)
    if a.top is not None:
        counts = Counter(dict(counts.most_common(a.top)))
    sus = suspecti(counts, a.prag)
    if a.json:
        raport = {
            "esecuri": len(esecuri),
            "pe_ip": dict(counts),
            "suspecti": sus
        }
        print(json.dumps(raport, indent=2, ensure_ascii=False))
        return
    print("Esecuri de autentificare:", len(esecuri))
    for ip, n in counts.most_common():
        print(f"  {ip}: {n}")
    print(f"Suspecti (prag {a.prag}):")
    for ip, n in sus:
        print(f"  {ip}  ({n} incercari)  BRUTE FORCE")
if __name__ == "__main__":
    main()