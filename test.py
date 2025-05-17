import machine
from radio.sx1262 import SX1262
import time
import utime

# Pico 2 pins for Waveshare SX1262 LoRaWAN module
CS = const(3)
DIO1 = const(20)
BUSY = const(2)
RESET = const(15)

MOSI = '11'
MISO = '12'
SCLK = '10'

boardID = machine.unique_id()



################################################################################

# print("This is the ", boardName, "board.")
print("Unique board ID: ")
for i in boardID:
    print(hex(i), " ", end='')
print(" ")

print("Initializing SX1262 radio module")
sx = SX1262(cs=CS,irq=DIO1,rst=RESET,gpio=BUSY,clk=SCLK,mosi=MOSI,miso=MISO)


# LoRa
# freq = 867.1, 867.3, 867.5, 867.7, 867.9, 868.1, (868.3), 868.5
# bw = 125.0, 250.0
# sf = 5 - 12
# cr = 5 - 8
# power = -9 - (-5) - +22
# preambleLength = 8
sx.begin(freq=868.3, bw=250.0, sf=7, cr=8, syncWord=0x12,
         power=5, currentLimit=60.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=True, blocking=True)

# FSK
##sx.beginFSK(freq=923, br=48.0, freqDev=50.0, rxBw=156.2, power=-5, currentLimit=60.0,
##            preambleLength=16, dataShaping=0.5, syncWord=[0x2D, 0x01], syncBitsLength=16,
##            addrFilter=SX126X_GFSK_ADDRESS_FILT_OFF, addr=0x00, crcLength=2, crcInitial=0x1D0F, crcPolynomial=0x1021,
##            crcInverted=True, whiteningOn=True, whiteningInitial=0x0100,
##            fixedPacketLength=False, packetLength=0xFF, preambleDetectorLength=SX126X_GFSK_PREAMBLE_DETECT_16,
##            tcxoVoltage=1.6, useRegulatorLDO=False,
##            blocking=True)

def send(count, delay=10, msg=b'Hello'):
    for i in range(count):
        print("\nSending ", i+1, "/", count, "  message\n------------------------\n")
        sx.send(msg)
        print("\nMessage ", i+1, "/", count, " sent\n--------------------\n")
        time.sleep(delay)

