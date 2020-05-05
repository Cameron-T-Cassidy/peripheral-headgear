# Peripheral-Headgear for Blind Spot Monitoring
This repository is for team headgear peripheral, a team from the 2020 CSCE 482 capstone course at Texas A&M University. The project consists of a LIDAR sensor sending distance data to a Raspberry Pi 4 running the Raspian OS. When the distance to an object is below a certain threshold, the Pi will trigger a vibration notification to the user. All components are mounted on a helmet for use while downhill skiing or snowboarding.

To run our final project, connect a LIDAR to the I2C pins on a Raspberry Pi and a vibration motor to GPIO pin 23.
Then run:
```
sudo python3 lidar_and_haptic.py
```

For more technical information about the project and our stretch goals that were not integrated in our final project, please view our [Wiki](https://github.com/rossmichaelyoung/peripheral-headgear/wiki).
