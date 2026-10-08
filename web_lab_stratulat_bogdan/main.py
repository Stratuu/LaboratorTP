# Laborator: funcții, metode și importuri pe web
# Student: Stratulat Bogdan
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

# #Exercitiu 44
# import webtools
# titlu = webtools.get_title(webtools.fetch(BASE_URL).text)
# print(titlu)

# #Exercitiu 45
# import requests
# from webtools import get_title, security_headers
# response = requests.get(BASE_URL, timeout=10)
# print(get_title(response.text))
# print(security_headers(BASE_URL))
# Dacă main.py ar avea și o funcție proprie numită get_title,
# una dintre ele ar suprascrie-o pe cealaltă, în funcție de ordinea definirii/importului.

#Exercitiu 46
# Autotestul rulează doar când webtools.py este executat direct.
# Dacă modulul este importat în main.py, __name__ este "webtools",
# deci blocul if nu se execută.

# #Exercitiu 47
# from webtools import get_title, security_headers, DEFAULT_HEADERS
# print(DEFAULT_HEADERS)

# #Exercitiu 48
# import argparse
# from webtools import fetch, get_title, security_headers
# parser = argparse.ArgumentParser()
# parser.add_argument("url")
# args = parser.parse_args()
# response = fetch(args.url)
# print("Titlu:", get_title(response.text))
# print("Antete de securitate:", security_headers(args.url))
# #python main.py https://cybercor.org

# #Exercitiu 49
# import csv
# from datetime import datetime
# from webtools import check_paths
# paths = ["/", "/robots.txt", "/sitemap.xml"]
# rezultate = check_paths(BASE_URL, paths)
# with open("report.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["path", "status", "checked_at"])
#     for path, status in rezultate.items():
#         writer.writerow([path, status, datetime.now().isoformat()])
# print("Raportul a fost salvat în report.csv")

#Exercitiu 50
from webtools import site_report
site_report(BASE_URL)