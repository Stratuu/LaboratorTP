# Laborator: funcții, metode și importuri pe web
# Student: Stratulat Bogdan
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import requests
def get_status(url):
    """Returnează codul de stare HTTP pentru adresa url."""
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code


# #Exercitiu 21
import requests
def fetch(url):
    return requests.get(url, timeout=TIMEOUT)
# response = fetch(BASE_URL)
# print(response.status_code)

# #Exercitiu 22
# import time
# status1 = get_status(BASE_URL + "/")
# print("/", status1)
# time.sleep(1)
# status2 = get_status(BASE_URL + "/robots.txt")
# print("/robots.txt", status2)
# time.sleep(1)
# status3 = get_status(BASE_URL + "/sitemap.xml")
# print("/sitemap.xml", status3)

# #Exercitiul 23
# def fetch(url, timeout=10):
#     response = requests.get(url, timeout=timeout)
#     return response
# response1 = fetch(BASE_URL)
# print(response1.status_code)
# response2 = fetch(BASE_URL, timeout=3)
# print(response2.status_code)

#Exercitiu 24
def get_title(html):
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    return html[start:end].strip()
response = fetch(BASE_URL)
# titlu = get_title(response.text)
# print(titlu)

# #Exercitiu 25
# def get_title(html):
#     """Returnează titlul unei pagini HTML."""
#     start = html.find("<title>") + len("<title>")
#     end = html.find("</title>")
#     return html[start:end].strip()
# help(get_title)

# #Exercitiu 26
# def get_status(url: str) -> int:
#     """Returnează codul de stare HTTP pentru adresa url."""
#     response = requests.get(url, timeout=TIMEOUT)
#     return response.status_code
# get_status(123)

#Exercitiu 27
def page_exists(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        return True
    except requests.RequestException:
        return False
# print(page_exists(BASE_URL))
# print(page_exists("https://this-domain-does-not-exist.invalid"))

#Exercitiu 28
def check_paths(base, paths):
    rezultate = {}
    for path in paths:
        rezultate[path] = get_status(base + path)
    return rezultate
# paths = ["/", "/robots.txt", "/sitemap.xml"]
# rezultate = check_paths(BASE_URL, paths)
# print(rezultate)

#Exercitiu 29
def get_header(url, name, default="lipsește"):
    response = requests.get(url, timeout=TIMEOUT)
    return response.headers.get(name, default)
rezultat = get_header(BASE_URL, name="Server")
# print(rezultat)

#Exercitiu 30
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
# print(security_headers(BASE_URL))

#Exercitiu 31
def score_headers(results):
    scor = sum(results.values())
    total = len(results)
    return str(scor) + "/" + str(total)
# print(score_headers(security_headers(BASE_URL)))

# #Exercitiu 32
def fetch_robots(base):
    try:
        response = requests.get(base + "/robots.txt", timeout=TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None
def disallowed_paths(robots_text):
    if robots_text is None:
        return []
    rezultate = []
    for linie in robots_text.splitlines():
        if linie.startswith("Disallow:"):
            path = linie.replace("Disallow:", "").strip()
            rezultate.append(path)
    return rezultate
# robots = fetch_robots(BASE_URL)
# print(disallowed_paths(robots))

# #Exercitiu 33
# import time
# def response_times(*urls):
#     rezultate = {}
#     for url in urls:
#         timp = time.perf_counter()
#         requests.get(url, timeout=TIMEOUT)
#         timp = time.perf_counter() - timp
#         rezultate[url] = timp
#     return rezultate
# print(response_times(BASE_URL, ECHO_URL))

# #Exercitiu 34
# def log(message, **details):
#     text = message
#     for nume, valoare in details.items():
#         text += " | " + nume + "=" + str(valoare)
#     print(text)
# log("verificat", url=BASE_URL, status=200)