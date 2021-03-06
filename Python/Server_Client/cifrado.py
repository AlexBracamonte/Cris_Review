from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
import binascii
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s-',
)


class Entity:
    def __init__(self):
        self.__priv_key = generate_eth_key()
        self.__privkeyhex = self.__priv_key.to_hex()
        self.pubkey = self.__priv_key.public_key.to_hex()
        self.__keychain = {}
        self.message = ""

    def get_public_key(self, key: str, value: str):
        self.__keychain.update({key: value})

    def encrypt_text(self, person, text):
        btext = bytes(text, 'utf-8')
        __key = self.__keychain.get(person)
        encrypted_text = binascii.hexlify(encrypt(__key, btext))
        return encrypted_text

    def encrypt_text_with_mykey(self, text):
        btext = bytes(text, 'utf-8')
        __key = self.__privkeyhex
        encrypted_text = binascii.hexlify(encrypt(__key, btext))
        return encrypted_text

    def desencrypt_text(self, text):
        print(f"El mensaje a descifrar es: {text.decode('utf-8')}")
        plaine_text = decrypt(self.__privkeyhex, binascii.unhexlify(text))
        self.message = plaine_text.decode("utf-8")
        return self.message

    def desencrypt_text_with_pubkey(self, person: str, text: str):
        print(f"El mensaje a descifrar es: {text.decode('utf-8')}")
        __key = self.__keychain.get(person)
        plaine_text = decrypt(__key, binascii.unhexlify(text))
        self.message = plaine_text.decode("utf-8")
        return self.message

    def __str__(self):
        return f"Entidad, con llave publica {self.pubkey} y ultimo mensaje recibodo: {self.message}"


def try_to_read():
    try:
        Alex.__privkey()
    except Exception:
        print("El valor solicitado es ")


if __name__ == "__main__":
    logging.debug('0. Primero se crean los objetos a partir de las clases')

    Alex = Entity()
    Pepe = Entity()
    print('Esta es mi llave', Pepe.pubkey)

    Alex.get_public_key('Pepe', Pepe.pubkey)            # Se comparten la llave p??blica para poder descifrar
    Pepe.get_public_key('Alex', Alex.pubkey)            # Se comparten la llave p??blica para poder descifrar
    mensaje = Alex.encrypt_text('Pepe', 'Tori Vega')
    print(f"Texto cifrado {mensaje}")

    mensaje2 = Pepe.desencrypt_text(mensaje)
    print(f"Texto descifrado {mensaje2}")
