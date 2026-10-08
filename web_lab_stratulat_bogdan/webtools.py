# Laborator: funcții, metode și importuri pe web
# Student: Stratulat Bogdan
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

#Exercitiu 44
import requests
import time

def get_status(url):
    """Returnează codul de stare HTTP pentru adresa url."""
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code

# def fetch(url):
#     return requests.get(url, timeout=TIMEOUT)

def get_title(html):
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()

def security_headers(url):
    response = requests.get(url, timeout=TIMEOUT)
    antete = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]
    rezultate = {}
    for antet in antete:
        rezultate[antet] = antet in response.headers
    return rezultate

#Exercitiu 46
if __name__ == "__main__":
    print("Autotest:", get_status("https://cybercor.org"))
# Autotestul rulează doar când webtools.py este executat direct.
# Dacă modulul este importat în main.py, __name__ este "webtools",
# deci blocul if nu se execută.

#Exercitiu 47
DEFAULT_HEADERS = {"User-Agent": "WebLab-StratulatBogdan"}
def fetch(url, timeout=10):
    response = requests.get(url, timeout=timeout, headers=DEFAULT_HEADERS)
    return response

#Exercitiu 49
def check_paths(base, paths):
    rezultate = {}
    for path in paths:
        rezultate[path] = get_status(base + path)
    return rezultate

#Exercitiu 50
import socket
import json
import urllib.parse
from part4_modules import resolve, cert_days_left, extract_links, split_links
from part3_functions import score_headers, fetch_robots, disallowed_paths

def site_report(url):
    response = fetch(url)

    # 1. Cod de stare și URL final
    status = response.status_code
    final_url = response.url

    # 2. Titlu
    titlu = get_title(response.text)

    # Domeniul final
    hostname = urllib.parse.urlparse(final_url).hostname
    domain = urllib.parse.urlparse(final_url).netloc

    # 3. Adresa IP
    ip = resolve(hostname)

    # 4. Redirecționări pornind de la http://
    http_url = final_url.replace("https://", "http://", 1)
    redirect_response = fetch(http_url)

    redirects = []

    for r in redirect_response.history:
        locatie = r.headers.get("Location", "")
        redirects.append(str(r.status_code) + " -> " + locatie)

    # 5. Scor securitate
    securitate = security_headers(final_url)
    scor = score_headers(securitate)

    # 6. Certificat
    zile = cert_days_left(hostname)

    # 7. Legături interne și externe
    links = extract_links(response.text)
    interne, externe = split_links(links, domain)

    # 8. robots.txt
    robots = fetch_robots(final_url)
    cai = disallowed_paths(robots)

    raport = {
        "status": status,
        "url_final": final_url,
        "titlu": titlu,
        "ip": ip,
        "redirectionari": redirects,
        "scor_securitate": scor,
        "certificat_zile": zile,
        "legaturi_interne": len(interne),
        "legaturi_externe": len(externe),
        "cai_interzise": cai
    }

    print("=== Raport site:", final_url, "===")
    print("Cod de stare:", status)
    print("URL final:", final_url)
    print("Titlu:", titlu)
    print("Adresă IP:", ip)
    print("Redirecționări:", redirects)
    print("Scor securitate:", scor)
    print("Certificat:", zile, "de zile rămase")
    print("Legături:", len(interne), "interne,", len(externe), "externe")
    print("Căi interzise:", cai)

    with open("report.json", "w") as file:
        json.dump(raport, file, indent=2)

    print("Salvat în report.json")

    return raport