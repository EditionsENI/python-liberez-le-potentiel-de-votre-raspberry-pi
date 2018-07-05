from random import randint


class BaseChiffrement(object):

    def _check_input(self, texte, cle):
        if not texte.isalpha():
            raise ValueError(
                '"texte" doit contenir que des lettres alphabetiques.')
        if cle is not None:
            if len(texte) != len(cle):
                raise ValueError('La cle doit avoir le meme nombre de '
                                 'caracteres que le texte a encode.')
            if not cle.isalpha():
                raise ValueError(
                    '"cle" doit contenir que des lettres alphabetiques.')

    def encoder(self, texte_clair, cle=None):
        self._check_input(texte_clair, cle)
        if cle is None:
            return self._encoder(texte_clair)
        else:
            return self._encoder(texte_clair, cle)

    def decoder(self, texte_chiffre, cle=None):
        self._check_input(texte_chiffre, cle)
        if cle is None:
            return self._decoder(texte_chiffre)
        else:
            return self._decoder(texte_chiffre, cle)


class ChiffrementDecalage(BaseChiffrement):

    def __init__(self, decalage=None):
        if decalage is None:
            self.decalage = randint(0, 26)
        else:
            self.decalage = decalage
        self.encode_dict = {chr(ord('a') + i):
                            chr(ord('a') + (i + self.decalage) % 26)
                            for i in range(26)}
        self.decode_dict = {chr(ord('a') + i):
                            chr(ord('a') + (i - self.decalage) % 26)
                            for i in range(26)}

    def _encoder(self, texte_clair):
        resultat = [self.encode_dict[caractere] for caractere in texte_clair]
        return ''.join(resultat)

    def _decoder(self, texte_chiffre):
        resultat = [self.decode_dict[caractere] for caractere in texte_chiffre]
        return ''.join(resultat)


class ChiffrementVignere(BaseChiffrement):

    def _encoder(self, texte_clair, cle=None):
        if cle is None:
            caracteres_int = [randint(0, 26) for i in range(len(texte_clair))]
            cle = ''.join([chr(ord('a') + caractere)
                           for caractere in caracteres_int])

        return (''.join([chr(ord('a') +
                             ((ord(t) - ord('a')) + (ord(c) - ord('a'))) % 26)
                         for t, c in zip(texte_clair, cle)]),
                cle)

    def _decoder(self, texte_chiffre, cle):
        return ''.join([chr(ord('a') +
                            ((ord(t) - ord('a')) - (ord(c) - ord('a'))) % 26)
                        for t, c in zip(texte_chiffre, cle)])
