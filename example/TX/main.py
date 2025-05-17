from radio.sx1262 import SX1262
import time
from machine import Pin

# RP Pico 2
CLK = 'GPIO10'
MOSI = 'GPIO11'
MISO = 'GPIO12'
CS = const(3)
DIO1 = const(20)
BUSY = const(2)
RESET = const(15)

sx = SX1262(cs=CS,irq=DIO1,rst=RESET,gpio=BUSY,clk=CLK,mosi=MOSI,miso=MISO)

print("- main-13-class-done -")
# LoRa
sx.begin(freq=868, bw=250.0, sf=12, cr=8, syncWord=0x12,
         power=-5, currentLimit=60.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=False, blocking=True)

# FSK
##sx.beginFSK(freq=923, br=48.0, freqDev=50.0, rxBw=156.2, power=-5, currentLimit=60.0,
##            preambleLength=16, dataShaping=0.5, syncWord=[0x2D, 0x01], syncBitsLength=16,
##            addrFilter=SX126X_GFSK_ADDRESS_FILT_OFF, addr=0x00, crcLength=2, crcInitial=0x1D0F, crcPolynomial=0x1021,
##            crcInverted=True, whiteningOn=True, whiteningInitial=0x0100,
##            fixedPacketLength=False, packetLength=0xFF, preambleDetectorLength=SX126X_GFSK_PREAMBLE_DETECT_16,
##            tcxoVoltage=1.6, useRegulatorLDO=False,
##            blocking=True)

pin = Pin("LED", Pin.OUT)
while True:
    pin.toggle()
    sx.send(b'Hello World!')
    time.sleep(3)


