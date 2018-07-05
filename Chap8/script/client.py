import socket as skt


s_client = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
print("creation de la socket")
s_client.connect(('localhost', 12088))
print("connecté au serveur")

message_clavier = b""
count = 0
while count < 5:
    message_clavier = input()
    message_clavier = message_clavier.encode()
    s_client.send(message_clavier)
    count += 1
    print("Nombre message envoyé : ", count)


s_client.close()
