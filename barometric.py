import board
import busio
import adafruit_bmp280

# Initialize I2C bus interface and BMP280 object
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
bmp280.sea_level_pressure = 1013.25

def read_bmp280():
    try:
        temperature = bmp280.temperature
        pressure = bmp280.pressure
        altitude = bmp280.altitude
        return temperature, pressure, altitude
    except Exception as e:
        print(f"Failed to read from BMP280 sensor: {e}")
        return None, None, None
