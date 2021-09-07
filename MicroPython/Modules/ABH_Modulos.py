from machine import UART
from machine import Pin
from machine import ADC
from machine import I2C
from machine import SPI
import network

import onewire
import dht
import machine
import ds18x20, time

import ubinascii



class DS18X20:
    def __init__(self, pin):
        self.ds = ds18x20.DS18X20(pin)

    def leer_todos_los_sensores(self):
        roms = self.ds.scan()
        self.ds.convert_temp()
        time.sleep_ms(750)
        aux = []
        for rom in roms:
            print(self.ds.read_temp(rom))
            aux.append(self.ds.read_temp(rom))
        return aux

class Max6675:
    def __init__(self, spi):
        self.spi = spi
        self.max6675 = {}

    def config_max6675(self, pin: int):
        aux2 = 'MAX6675_' + str(pin)
        aux = Pin(pin, Pin.OUT)
        aux.value(1)
        self.max6675.update({aux2: aux})

    def leer_max6675(self, pin: int):
        aux2 = 'MAX6675_' + str(pin)
        aux = self.max6675.get(aux2)
        aux.value(0)
        data = 0
        data = self.spi.read(2)
        a = ubinascii.hexlify(data).decode()
        b = (int(a, 16))
        c = bin(b >> 3)
        d = int(c, 2) * .25

        aux.value(1)
        # return data, a, b, c, d
        return d


class Embedded:
    def __init__(self):
        self.pins = {}
        self.adcs = {}
        self.dh22 = {}

        self.onew = None
        self.uart = None
        self.i2c = None
        self.spi = None
        self.wlan = None

    def config_pin_out(self, number: int):
        aux = Pin(number, Pin.OUT)
        aux2 = 'Pin' + str(number)
        self.pins.update({aux2: aux})

    def pin_state(self, number: int, state: int):
        aux2 = 'Pin' + str(number)
        a = self.pins.get(aux2)
        a.value(state)

    def config_UART(self, number: int, tx: int, rx: int):
        self.uart = UART(number, tx=tx, rx=rx)
        self.uart.init(baudrate=9600, bits=8, parity=None, stop=1)

    def send_uart(self, kind: str, value: str):
        send = kind + '= ' + value + '\0'
        self.uart.write(send)

    def config_ADC(self, number: int):
        adc = ADC(Pin(number))
        adc.atten(ADC.ATTN_11DB)
        aux2 = 'ADC' + str(number)
        self.adcs.update({aux2: adc})

    def read_ADC(self, number: int) -> int:
        aux2 = 'ADC' + str(number)
        a = self.adcs.get(aux2)
        value = a.read()
        return value

    def config_I2C(self, sda: int, scl: int):
        self.i2c = I2C(1, sda=Pin(sda), scl=Pin(scl))

    def config_SPI(self, freq: int, sck: int, mosi:int, miso: int):
        self.spi = SPI(1, 10000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
        #self.spi.init(baudrate=200000) # set the baudrate
        # self.spi = SPI(1, freq, sck=Pin(sck), mosi=Pin(mosi), miso=Pin(miso))

    def config_dh22(self, pin: int):
        # aux = dht.DHT22(machine.Pin(pin, machine.Pin.PULL_UP))
        aux = dht.DHT22(machine.Pin(pin))
        aux2 = 'DH22_' + str(pin)
        self.dh22.update({aux2: aux})

    def leer_dh22(self, pin: int):
        aux2 = 'DH22_' + str(pin)
        d = self.dh22.get(aux2)
        try:
            d.measure()
            return d.temperature(), d.humidity()
        except:
            print("Algo salio mal")

    def config_one_wire(self, pin: int):
        self.onew = onewire.OneWire(Pin(pin))

    def config_wifi(self, ssid: str, password: int):
        self.wlan = network.WLAN(network.STA_IF)  # create station interface
        self.wlan.active(True)  # activate the interface
        if not self.wlan.isconnected():
            print('Conectando a...')
            self.wlan.connect(ssid, password)
            while not self.wlan.isconnected():
                pass
        print('Conexion realizada. IP:', self.wlan.ifconfig(), ", ", self.wlan.config('mac'))

class SensorOxigeno:
    def __init__(self, _uart: object):
        self.pin = None
        self.uart = _uart
        self.sensor = {}

    def config_atlas(self, pin: int):
        aux2 = 'Sensor_' + str(pin)
        aux = Pin(pin, Pin.OUT)
        aux.value(0)
        self.sensor.update({aux2: aux})

    def leer_sensor(self, pin: int):
        aux2 = 'Sensor_' + str(pin)
        aux = self.sensor.get(aux2)
        aux.value(1)
        data = None
        while True:
            data = self.uart.read()
            if data:
                break
        a = data.decode()
        aux.value(0)
        return a
