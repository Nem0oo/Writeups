#Writeup "Le chant des Etoiles" par Nem0oo
#Hackagou 2024
###########################################
#Codé vite fait pour répondre au problème, surement plein de choses a faire mieux
###########################################
#Probleme simplifié : 
#On se connecte a un serveur qui nous donne 2 nombres et une operation.
#On doit y repondre et il le fait 6 fois en tout
#Les nombres varient
#Les operations se présentent toujours dans le meme ordre : &, |, +, *, <<, >>

import socket
import time

# Adresse IP ou nom de domaine de la machine distante
adresse_ip = "challenges.hackagou.nc"
# Numéro de port sur lequel vous souhaitez vous connecter
port = 5009  # Port HTTP par défaut

# Créer un objet socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Se connecter et lire les donnees recues
client_socket.connect((adresse_ip, port))
data = client_socket.recv(1024)
msg = data.decode("utf-8")
print(msg)

#Operation AND
#On isole les nombres recus
ind_1 = msg.find("Nombre 1 : ")
ind_2 = msg.find("Nombre 2 : ")
n1 = msg[ind_1+11:ind_1+19]
n2 = msg[ind_2+11:ind_2+19]

#on le fait suir des entier
and_int = int(n1, 2)&int(n2, 2)

#on format en string binaire
and_bin = "{0:b}".format(and_int)

#Affichage pour confirmer ce qu'on envoie
print(and_bin.zfill(8))

#on envoie au serveur sans oublié le "\n" a la fin de la string
client_socket.send(bytes(and_bin.zfill(8), 'utf-8')+ b"\n")

#Meme demarche pour la suite avec les autrre calculs
data = client_socket.recv(1024)
msg = data.decode("utf-8")
print(msg)

#Operation OR
ind_1 = msg.find("valeur de ")
n1 = msg[ind_1+10:ind_1+18]
n2 = msg[ind_1+21:ind_1+29]

or_int = int(n1, 2)|int(n2, 2)
or_bin = "{0:b}".format(or_int)

print(or_bin.zfill(8))
client_socket.send(bytes(or_bin.zfill(8), 'utf-8')+ b"\n")

data = client_socket.recv(1024)
msg = data.decode("utf-8")
print(msg)

#SOMME
ind_1 = msg.find("somme de ")
n1 = msg[ind_1+9:ind_1+18]
n2 = msg[ind_1+20:ind_1+29]

add_int = int(n1, 2)+int(n2, 2)
add_bin = "{0:b}".format(add_int)

print(add_bin.zfill(8))
client_socket.send(bytes(add_bin.zfill(8), 'utf-8')+ b"\n")

data = client_socket.recv(1024)
msg = data.decode("utf-8")
print(msg)

#Multiplication
ind_1 = msg.find("valeur de ")

n1 = msg[ind_1+10:ind_1+18]
n2 = msg[ind_1+21:ind_1+29]

mult_int = int(n1, 2)*int(n2, 2)
mult_bin = "{0:b}".format(mult_int)

print(mult_bin.zfill(8))
client_socket.send(bytes(mult_bin.zfill(8), 'utf-8')+ b"\n")

data = client_socket.recv(1024)
msg = data.decode("utf-8")
print(msg)

#Gauche
ind_1 = msg.find("valeur de ")

n1 = msg[ind_1+10:ind_1+18]
n2 = msg[ind_1+22:ind_1+23]

gauche_int = int(n1, 2)<<int(n2)
gauche_bin = "{0:b}".format(gauche_int)

print(gauche_bin.zfill(8))
client_socket.send(bytes(gauche_bin.zfill(8), 'utf-8')+ b"\n")

data = client_socket.recv(1024)
msg = data.decode("utf-8")
print(msg)


#Droite
ind_1 = msg.find("valeur de ")

n1 = msg[ind_1+10:ind_1+18]
n2 = msg[ind_1+22:ind_1+23]

droite_int = int(n1, 2)>>int(n2)
droite_bin = "{0:b}".format(droite_int)

print(droite_bin.zfill(8))
client_socket.send(bytes(droite_bin.zfill(8), 'utf-8')+ b"\n")

data = client_socket.recv(1024)
msg = data.decode("utf-8")
print(msg)


#flag : OPENNC{B1n4rY_1s_F0r_31337_0nLY}
