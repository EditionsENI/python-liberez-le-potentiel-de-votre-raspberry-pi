import socket as skt


s_connexion = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
print("Creation soket")
s_connexion.bind(('', 12088))
print("connection du serveur")
s_connexion.listen(3)
lien_client, info_lien = s_connexion.accept()
print("serveur disponible")

message_client = b""
count = 0

while count < 5:
    message_client = lien_client.recv(1024).decode()
    print(message_client)
    count += 1

print("Fermeture du serveur")
s_connexion.close()
lien_client.close()
