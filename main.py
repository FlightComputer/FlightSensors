import datetime
import os
import time
from barometric import read_bmp280
# from imu import IMU
# from gps import read_gps

# Create timestamped log file
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"sensor_data_{timestamp}.txt"
desktop_dir = "/tmp/"  # Change to your desired directory
full_path = os.path.join(desktop_dir, filename)

# Open a new file for writing
log_file = open(full_path, 'w')
log_file.write("Timestamp, Temperature (C), Pressure (hPa), Altitude (m), Gyro X, Gyro Y, Gyro Z, Accel X, Accel Y, Accel Z, Temperature (IMU), Latitude, Longitude, Altitude (GPS), Speed (knots), Satellites\n")
print(f"Log file created at '{full_path}'")

# # Initialize IMU
# imu = IMU('/dev/ttyUSB0', 1250000)

try:
    while True:
        # Read from BMP280
        bmp_temperature, bmp_pressure, bmp_altitude = read_bmp280()

#         # Read from IMU
#         imu.get()
#         gyro_x = imu.gyro_axis_x
#         gyro_y = imu.gyro_axis_y
#         gyro_z = imu.gyro_axis_z
#         accel_x = imu.accelerometer_axis_x
#         accel_y = imu.accelerometer_axis_y
#         accel_z = imu.accelerometer_axis_z
#         imu_temperature = imu.temperature
# 
#         # Read from GPS
#         latitude, longitude, gps_altitude, speed_knots, satellites = read_gps()

        # Generate a timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log data
        log_file.write(f"{timestamp}, {bmp_temperature}, {bmp_pressure}, {bmp_altitude}\n")

#         , {gyro_x}, {gyro_y}, {gyro_z}, {accel_x}, {accel_y}, {accel_z}, {imu_temperature}, {latitude}, {longitude}, {gps_altitude}, {speed_knots}, {satellites}
#         \n")
        log_file.flush()

        # Print data to console
        print(f"Timestamp: {timestamp}")
        print(f"Temperature: {bmp_temperature:.2f} C, Pressure: {bmp_pressure:.2f} hPa, Altitude: {bmp_altitude:.2f} m")
#         print(f"Gyro X: {gyro_x:.2f}, Gyro Y: {gyro_y:.2f}, Gyro Z: {gyro_z:.2f}")
#         print(f"Accel X: {accel_x:.2f}, Accel Y: {accel_y:.2f}, Accel Z: {accel_z:.2f}")
#         print(f"IMU Temperature: {imu_temperature:.2f} C")
#         if latitude is not None:
#             print(f"GPS Latitude: {latitude:.6f}, Longitude: {longitude:.6f}, Altitude: {gps_altitude:.2f} m, Speed: {speed_knots:.2f} knots, Satellites: {satellites}")
#         else:
#             print("GPS data not available")
        
        # Delay to match GPS update rate
        time.sleep(1)
except Exception:
    print("execption")
except KeyboardInterrupt:
        print("Data logging stopped.")
finally:
    log_file.close()
