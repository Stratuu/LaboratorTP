# A1
import argparse, json, os
 
def citeste_linii(cale):
    with open(cale, encoding="utf-8") as f:
        return [linie.strip() for linie in f if linie.strip() and not linie.strip().startswith("#")]
 
cai = citeste_linii("start/suid.txt")
print("linii SUID:", len(cai))


# A2
def nume(cale):
    return cale.rsplit("/", 1)[-1]
nume_unice = {nume(c) for c in cai}    # set comprehension
print("SUID distincte:", len(nume_unice))


# A3
GTFO = {"find", "vim.basic", "vim", "nmap", "cp", "bash",
        "less", "awk", "python3", "perl"}
 
def suid_constatari(cale):
    cai = citeste_linii(cale)
    return [
        {"cale" : c,
        "nume" : nume(c),
        "risc" : "mare" if nume(c) in GTFO else "normal"
        }
    for c in sorted(set(cai))
    ]
 
suid = suid_constatari("start/suid.txt")
mari = [c for c in suid if c["risc"] == "mare"]
print(len(suid), "SUID,", len(mari), "cu risc mare")
print(sorted(c["nume"] for c in mari))


# A4
def sudo_constatari(cale):
    out = []

    for ln in citeste_linii(cale):
        user, drept = ln.split(" : ", 1)
        out.append({
            "user": user.strip(),
            "drept": drept.strip(),
            "risc": "mare" if "NOPASSWD" in drept else "normal"
        })

    return out
 
def cron_constatari(cale):
    out = []

    for ln in citeste_linii(cale):
        campuri = ln.split()
        user = campuri[5]
        comanda = " ".join(campuri[6:])

        out.append({
            "user": user,
            "comanda": comanda
        })

    return out

def enumereaza(d):
    return {
        "suid": suid_constatari(os.path.join(d, "suid.txt")),
        "sudo": sudo_constatari(os.path.join(d, "sudo.txt")),
        "cron": cron_constatari(os.path.join(d, "crontab.txt")),
    }
print(sorted(c["nume"] for c in mari))


# A5
def main():
    p = argparse.ArgumentParser()
    p.add_argument("capturi", nargs="?", default="start")
    p.add_argument("--risc", choices=["mare"])
    p.add_argument("--json", action="store_true")
    a = p.parse_args()

    raport = enumereaza(a.capturi)
    if a.risc == "mare":
        raport = {
            categorie: [c for c in lista if c.get("risc") == "mare"]
            for categorie, lista in raport.items()
        }
    if a.json:
        print(json.dumps(raport, indent=2, ensure_ascii=False))
        return

    for categorie, lista in raport.items():
        mari = [c for c in lista if c.get("risc") == "mare"]
        print(f"{categorie}: {len(lista)} gasite, {len(mari)} cu risc mare")

    useri_sudo = {c["user"] for c in raport["sudo"]}
    useri_cron = {c["user"] for c in raport["cron"]}

    utilizatori = useri_sudo | useri_cron

    print("utilizatori implicati:", ", ".join(sorted(utilizatori)))

    with open("arsenal/privesc/enum.json", "w", encoding="utf-8") as f:
        json.dump(raport, f, indent=2, ensure_ascii=False)

    print("Raport salvat in enum.json")


if __name__ == "__main__":
    main()

# Pentru varful salii

import subprocess

def suid_real():
    r = subprocess.run(
        ["find", "/", "-perm", "-4000", "-type", "f"],
        capture_output=True,
        text=True
    )

    return [linie.strip() for linie in r.stdout.splitlines() if linie.strip()]


def grupare_risc():
    grupare = {}
    raport = enumereaza("start")

    for categorie, lista in raport.items():
        for c in lista:
            risc = c.get("risc", "normal")

            if "nume" in c:
                valoare = c["nume"]
            elif "user" in c:
                valoare = c["user"]
            else:
                valoare = str(c)

            grupare.setdefault(risc, []).append(valoare)

    return grupare

print("SUID gasite pe sistemul real:")
print(suid_real())

print("Grupare dupa risc:")
print(grupare_risc())