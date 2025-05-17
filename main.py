from utime import sleep_ms
from machine import Pin
from LoRaWANHandler import LoRaWANHandler
from LoRaWANHandler import getBoardID
from LoRaConfig import LoRaConfig

def blink(duration=100):
    led.on
    sleep_ms(duration)
    led.off()

print("\n--- LoRaWAN TTN Test ---\n")

getBoardID()

counter =  0
led = Pin("LED", Pin.OUT)

# Initialise LoRaWAN
lh = LoRaWANHandler(LoRaConfig)
blink()

# Connect to TTN 
lh.otaa()
blink()

while(True):
    # count up to 99 and then reset
    counter += 1
    if counter > 99: 
        counter = 0

    print("\nCounter: " + str(counter) + "\n")

    # Convert counter to byte array and then to string. This is a workaround for the fact that the 
    # LoRaWANHandler.send() method only accepts strings and not byte arrays
    cnt_arr = bytearray(counter.to_bytes(4, 'little'))
    msg = str(cnt_arr[0])

    # Send the message to TTN (unconfirmed)
    lh.send(msg, False)

    # blink the LED to indicate that the message was sent
    blink(500)

    # Wait for 10 seconds before sending the next message
    sleep_ms(10000)