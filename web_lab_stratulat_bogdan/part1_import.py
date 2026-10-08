# Laborator: funcții, metode și importuri pe web
# Student: Stratulat Bogdan
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


# #Exercitiu 1
# import requests
# print(requests.__version__)
# import urllib.request
# # Modulul requests nu face parte din biblioteca standard Python, de aceea trebuie instalat separat cu comanda: pip install requests.
# # Modulul urllib face parte din biblioteca standard Python, deci este instalat automat împreună cu Python și nu necesită pip install.

# #Exercitiu 2
# # Stilul 1
# import requests
# raspuns = requests.get(BASE_URL, timeout=TIMEOUT)
# print(raspuns.status_code)
# # Avantaj: este clar că funcția get() aparține bibliotecii requests.
# # Stilul 2
# from requests import get
# raspuns = get(BASE_URL, timeout=TIMEOUT)
# print(raspuns.status_code)
# # Avantaj: codul este mai scurt, deoarece nu mai trebuie să scriem requests.get()

# #Exercitiu 3
# import requests as rq 
# print(rq.get(BASE_URL, timeout=TIMEOUT))
# # Aliasul face codul mai ușor de citit atunci când scurtează numele unui modul
# # folosit des. Îl poate face mai greu de citit dacă aliasul este neclar
# # sau nu arată ce modul reprezintă.

# #Exercitiu 4
# import urllib.request
# raspuns = urllib.request.urlopen(ECHO_URL)
# print("Status:", raspuns.status)
# continut = raspuns.read().decode("utf-8")
# print(continut[:200])

# #Exercitiu 5
# import requests
# print(dir(requests))
# # get - funcție
# # Session - clasă
# # exceptions - modul

# #Exercitiu 6
# import requests
# help(requests.get)
# print(requests.get(BASE_URL, timeout=TIMEOUT).status_code)

# #Exercitiu 7
# import time
# import requests
# start=time.perf_counter()
# response = requests.get(BASE_URL,timeout=TIMEOUT)
# stop=time.perf_counter()
# timp=stop-start
# print("Timp cu perf_counter:", timp, "secunde")
# print("Timp cu response.elapsed:", response.elapsed.total_seconds(), "secunde")

# #Exercitiu 8
# try:
#     import bs4
# except ImportError:
#     print("Instalați modulul cu: pip install beautifulsoup4")