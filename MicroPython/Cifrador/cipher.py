import uhashlib
"""

            temporary = self.runge_kutta2(self.states[0][-1], self.states[1][-1], self.states[2][-1], h)
            for number in [0, 1, 2]:
                self.states[number].append(temporary[number])

            for number in temporary:
                self.states[temporary.index(number)].append(number)

"""


class LorenzAttractor:
    def __init__(self, secret: str):
        self.constants = [28.0, 10.0, 8.0 / 3.0]  # [Rho, Sigma, Beta]
        self.states = [0, 0, 0, 0]
        self.key = []
        self.password = secret
        self.h = 0.01

    def fx(self, x, y, z) -> float:
        dxdt = self.constants[1] * (y - x)  # Sigma
        return dxdt

    def fy(self, x, y, z) -> float:
        dydt = x * (self.constants[0] - z) - y  # RHo
        return dydt

    def fz(self, x, y, z) -> float:
        dzdt = x * y - self.constants[2] * z  # Beta
        return dzdt

    def runge_kutta2(self, x, y, z, h) -> list:
        k1x = h * self.fx(x, y, z)
        k1y = h * self.fy(x, y, z)
        k1z = h * self.fz(x, y, z)

        k2x = h * self.fx(x + k1x / 2, y + k1y / 2, z + k1z / 2)
        k2y = h * self.fy(x + k1x / 2, y + k1y / 2, z + k1z / 2)
        k2z = h * self.fz(x + k1x / 2, y + k1y / 2, z + k1z / 2)

        k3x = h * self.fx(x + k2x / 2, y + k2y / 2, z + k2z / 2)
        k3y = h * self.fy(x + k2x / 2, y + k2y / 2, z + k2z / 2)
        k3z = h * self.fz(x + k2x / 2, y + k2y / 2, z + k2z / 2)

        k4x = h * self.fx(x + k3x, y + k3y, z + k3z)
        k4y = h * self.fy(x + k3x, y + k3y, z + k3z)
        k4z = h * self.fz(x + k3x, y + k3y, z + k3z)

        kx = x + ((k1x + 2 * k2x + 2 * k3x + k4x) / 6)
        ky = y + ((k1y + 2 * k2y + 2 * k3y + k4y) / 6)
        kz = z + ((k1z + 2 * k2z + 2 * k3z + k4z) / 6)

        return [kx, ky, kz, int(kx) ^ int(ky) ^ int(kz)]
        #return [kx, ky, kz, kx * ky * kz]

    def get_key(self, offset):
        self.states = [0, 0, 0, 0]
        self.key = []

        dig = uhashlib.sha256()
        text = self.password.encode('utf-8')
        dig.update(text)
        digests = dig.digest()

        for byte in digests[0:9]:
            self.states[0] ^= byte
        for byte in digests[10:19]:
            self.states[1] ^= byte
        for byte in digests[20:29]:
            self.states[2] ^= byte

        aux = digests[30] ^ digests[31]

        self.h = 0.015 - (abs(aux / 25555))

        for t in range(1, 810 + offset):
            self.states = self.runge_kutta2(self.states[0], self.states[1], self.states[2], abs(self.h))
            if t > 800:
                self.key.append(int(self.states[3]))

    def encrypt_text(self, aux: str) -> list:

        text = aux.encode('utf-8')

        msg = len(text)

        self.get_key(offset=msg)
        encrypted = []

        try:
            encrypted = list(map(lambda m, k: int(m) ^ k, text, self.key))
        except (RuntimeError, TypeError, NameError):
            print('Algo salio mal al cifrar')
            print(Exception)
        finally:
            return encrypted

    def decrypt_text(self, text: list) -> str:

        large = len(text)
        self.get_key(offset=large)
        aux = []
        try:
            aux = list(map(lambda k, m: chr(abs(k ^ int(m))), self.key, text))
        except (RuntimeError, TypeError, NameError):
            print("El mensaje recibido es: ", text)
            print("Algo salio mal al descifrar, revisa la contraseña")
            print(Exception)
        finally:
            msg = "".join(aux)
            return msg


