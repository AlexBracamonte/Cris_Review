from libraries import LorenzAttractor
from libraries import Embedded
from libraries import accel
import BME280
import time


def list2str(numbers_list: list) -> str:
    aux = list(map(str, numbers_list))
    res = " ".join(aux)
    return res


def str2list(t1: str) -> list:
    l1 = t1.split()
    l2 = list(map(int, l1))
    return l2


if __name__ == '__main__':
    uc = Embedded()
    uc.config_UART(number=2, tx=17, rx=16)
    uc.config_UART(number=2, tx=17, rx=16)
    uc.config_I2C(sda=21, scl=22)
    uc.config_I2C(sda=21, scl=22)
    uc.config_pin_out(number=2)
    uc.config_pin_out(number=5)
    uc.config_ADC(number=34)

    entity = LorenzAttractor(secret='ElectroVigia2020')
    entity.get_key2(offset=512)

    bmp = BMP280(uc.i2c)
    accel = accel(uc.i2c)

    data2send = {'L35_temp': "", 'BMP_temp': "", 'MPU_temp': "",
                 'BMP_pres': "", 'MPU_giro': "", 'msg': 'Hola mundo cifrado en MicroPython'}

    print("Valor= ", entity.encrypt_text2(data2send['msg']))
    print("Key= ", list2str(entity.key))

    while True:
        uc.pin_state(number=2, state=1)

        Girosco = accel.get_values()
        Giros_values = str(int(Girosco.get("GyX"))) + ', ' + str(int(Girosco.get("GyY"))) + ', ' + str(int(Girosco.get("GyZ")))

        data2send['L35_temp'] = str(((3.3 * uc.read_ADC(number=34) / (4095 * 2)) - 0.00) * 100)
        data2send['BMP_temp'] = str(bmp.temperature)
        data2send['MPU_temp'] = str(Girosco.get("Tmp"))
        data2send['BMP_pres'] = str(bmp.pressure)
        data2send['MPU_giro'] = str(Giros_values)

        print("\n--> Nuevo <--")

        uc.pin_state(number=5, state=1)
        for key in data2send:
            cryp_text = list2str(entity.encrypt_text2(data2send.get(key)))
            uc.send_uart(kind=key, value=cryp_text)

        uc.pin_state(number=5, state=0)
        uc.pin_state(number=2, state=0)
        time.sleep(2)
