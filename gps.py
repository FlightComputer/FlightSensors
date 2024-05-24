import serial
import adafruit_gps

# Create a serial connection for the GPS module
uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=10)

# Create a GPS module instance
gps = adafruit_gps.GPS(uart, debug=False)

# Initialize the GPS module
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")

def read_gps():
    gps.update()
    if gps.has_fix:
        latitude = gps.latitude
        longitude = gps.longitude
        altitude = gps.altitude_m
        speed_knots = gps.speed_knots
        satellites = gps.satellites
    else:
        latitude = longitude = altitude = speed_knots = satellites = None
    return latitude, longitude, altitude, speed_knots, satellites
