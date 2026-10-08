# Laborator: funcții, metode și importuri pe web
# Student: Stratulat Bogdan
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde



# #Exercitiu 35
# import urllib
# response = urllib.parse.urlparse("https://cybercor.org/path?x=1#top")
# print(response.scheme)
# print(response.netloc)
# print(response.path)
# print(response.query)
# print(response.fragment)

# #Exercitiu 36
# import urllib
# link1 = urllib.parse.urljoin(BASE_URL, "/about")
# link2 = urllib.parse.urljoin(BASE_URL, "contact.html")
# link3 = urllib.parse.urljoin(BASE_URL, "..index.html")
# print(link1)
# print(link2)
# print(link3)

# #Exercitiu 37
import requests
import re
def extract_links(html):
    links = re.findall(r'href="([^"]+)"', html)
    return list(set(links))
response = requests.get(BASE_URL, timeout=TIMEOUT)
# print(extract_links(response.text))

#Exercitiu 38
import urllib
def split_links(links, domain):
    interne = []
    externe = []
    for link in links:
        link_complet = urllib.parse.urljoin(BASE_URL, link)
        domeniu_link = urllib.parse.urlparse(link_complet).netloc
        if domeniu_link == domain:
            interne.append(link_complet)
        else:
            externe.append(link_complet)
    return interne, externe
response = requests.get(BASE_URL, timeout=TIMEOUT)
links = extract_links(response.text)
domain = urllib.parse.urlparse(BASE_URL).netloc
interne, externe = split_links(links, domain)
# print("Interne:", interne)
# print("Externe:", externe)

#Exercitiu 39
from html.parser import HTMLParser
class ImageFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            src = dict(attrs).get("src")
            if src:
                self.images.append(src)
response = requests.get(BASE_URL, timeout=TIMEOUT)
finder = ImageFinder()
finder.feed(response.text)
# print(finder.images)

#Exercitiu 40
import hashlib
def page_fingerprint(url):
    response = requests.get(url, timeout=TIMEOUT)
    return hashlib.sha256(response.content).hexdigest()
amprenta1 = page_fingerprint(BASE_URL)
amprenta2 = page_fingerprint(BASE_URL)
# print(amprenta1)
# print(amprenta2)
# if amprenta1 == amprenta2:
#     print("Amprentele sunt identice.")
# else:
#     print("Amprentele sunt diferite.")
# # Amprentele vor fi diferite dacă se schimbă conținutul paginii între cele două cereri.


#Exercitiu 41
import json
# response = requests.get(BASE_URL, timeout=TIMEOUT)
# with open("headers.json", "w") as file:
#     json.dump(dict(response.headers), file, indent=2)
# with open("headers.json", "r") as file:
#     headers = json.load(file)
# print("Content-Type:", headers.get("Content-Type", "lipsește"))

# #Exercitiu 42
import socket
def resolve(hostname):
    return socket.gethostbyname(hostname)
# ip = resolve("cybercor.org")
# print("IP:", ip)

#Exercitiu 43
import ssl
import time
def cert_days_left(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=TIMEOUT) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
            certificat = secure_sock.getpeercert()
    expirare = ssl.cert_time_to_seconds(certificat["notAfter"])
    zile = int((expirare - time.time()) / 86400)
    return zile
# print("Zile până la expirare:", cert_days_left("cybercor.org"))

# handle_starttag() este apelată automat de HTMLParser
# atunci când metoda feed() găsește un tag de început în HTML.