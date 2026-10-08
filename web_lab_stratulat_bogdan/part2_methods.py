# Laborator: funcții, metode și importuri pe web
# Student: Stratulat Bogdan
 
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

# #Exercitiu 9
# import requests
# response=requests.get(BASE_URL,timeout=TIMEOUT)
# print(response.status_code)  # atribut
# print(response.ok)           # atribut
# print(response.url)          # atribut
# print(response.encoding)     # atribut

# #Exercitiu 10
# import requests
# response=requests.get(BASE_URL,timeout=TIMEOUT)
# response.raise_for_status()
# try:
#     response=requests.get(BASE_URL + "/this-page-does-not-exist")
#     response.raise_for_status()
#     print("Pagina exista")
# except requests.HTTPError:
#     print("Pagina nu există sau a apărut o eroare HTTP.")

# #Exercitiu 11
# import requests
# response = requests.get(BASE_URL, timeout=TIMEOUT)
# for nume, valoare in response.headers.items():
#     print(nume + ":", valoare)

# #Exercitiu 12
# import requests
# response = requests.get(BASE_URL, timeout=TIMEOUT)
# print("Server:", response.headers.get("Server", "lipsește"))
# print("Content-Type:", response.headers.get("Content-Type", "lipsește"))
# print("content-type:", response.headers.get("content-type", "lipsește"))

# #Exercitiu 13
# import requests
# response=requests.get(BASE_URL, timeout=TIMEOUT)
# print(response.text.lower().count("cyber"))
# # Putem înlănțui .lower() și .count() deoarece .lower()
# # returnează tot un șir de caractere, iar pe acel șir putem aplica .count().

# #Exercitiu 14
# import requests
# response = requests.get(BASE_URL, timeout=TIMEOUT)
# html = response.text
# start = html.find("<title>") + len("<title>")
# end = html.find("</title>")
# titlu = html[start:end].strip()
# print(titlu)

# #Exercitiu 15
# import requests
# response = requests.get(BASE_URL, timeout=TIMEOUT)
# lines = response.text.splitlines()
# print("Nr. linii" ,len(lines))
# cea_mai_lunga = max(lines, key=len)
# print("Lungimea celei mai lungi linii:", len(cea_mai_lunga))

# #Exercitiu 16
# import requests
# response = requests.get(BASE_URL, timeout=TIMEOUT)
# if response.url.startswith("https://"):
#     print ("Conexiune securizată")
# else: print ("Conexiune nesecurizată")

# #Exerxitiu 17
# import requests
# response = requests.get("http://cybercor.org", timeout=TIMEOUT)
# for r in response.history:
#     print (r.status_code, r.url)
# print("URL final:", response.url)

# #Exercitiu 18
# import requests
# head_response = requests.head(BASE_URL, timeout=TIMEOUT)
# get_response = requests.get(BASE_URL, timeout=TIMEOUT)
# print("HEAD:", len(head_response.content))
# print("GET:", len(get_response.content))
# # HEAD primește doar antetele răspunsului, fără conținutul paginii.
# # GET primește și antetele, și conținutul paginii HTML.
# # De aceea, lungimea pentru HEAD este de obicei 0, iar pentru GET este mai mare.

# #Exercitiu 19
# import requests
# response = requests.get(BASE_URL, timeout=TIMEOUT)
# if response.cookies:
#     for c in response.cookies:
#         print (c.name, c.secure)
# else:
#     print("Niciun cookie setat")

# #Exercitiul 20
# import requests
# session = requests.Session()
# session.headers.update({"User-Agent": "WebLab-Stratulat Bogdan"})
# response = session.get(ECHO_URL + "/headers")
# print(response.text)