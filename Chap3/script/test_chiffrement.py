from chiffrement import ChiffrementVignere
from chiffrement import ChiffrementDecalage


vignere = ChiffrementVignere()
decalage = ChiffrementDecalage(12)

chaine = "bonjour"

chaine_encode_v = vignere.encoder(chaine, "abbpoau")
print("Chaine encodée avec Vignère : ", chaine_encode_v[0])
chaine_decode_v = vignere.decoder(chaine_encode_v[0], "abbpoau")
print("Chaine décodée avec Vignère : ", chaine_decode_v)

chaine_encode_d = decalage.encoder(chaine)
print("Chaine encodée avec décalage : ", chaine_encode_d)
chaine_decode_d = decalage.decoder(chaine_encode_d)
print("Chaine décodée avec décalage : ", chaine_decode_d)
