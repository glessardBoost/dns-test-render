import socket

try:
    ip = socket.gethostbyname("api.esignatures.io")
    print(f"Résolution DNS réussie : {ip}")
except Exception as e:
    print("DNS Résolution échouée :", e)
