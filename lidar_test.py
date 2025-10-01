import sys
import math
from rplidar import RPLidar

import matplotlib.pyplot as plt

PORT_NAME = '/dev/ttyUSB0'  # Change if your lidar uses a different port

def run():
    lidar = RPLidar(PORT_NAME)
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    scan_data = [0]*360

    try:
        for scan in lidar.iter_scans():
            for (_, angle, distance) in scan:
                scan_data[min([359, int(math.floor(angle))])] = distance
            ax.clear()
            ax.set_theta_zero_location('N')
            ax.set_theta_direction(-1)
            angles = [math.radians(i) for i in range(360)]
            ax.plot(angles, scan_data)
            plt.pause(0.001)
    except KeyboardInterrupt:
        print('Stopping...')
    finally:
        lidar.stop()
        lidar.disconnect()

if __name__ == '__main__':
    run()