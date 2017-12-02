import os
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    temperatura=(int(temperature))
    
    if temperatura > 25:
        os.system("mpg321 gmi2.mp3")
                  