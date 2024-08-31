# Voice Controlled Home Automation using Raspberry Pi
This Voice Controlled Home Automation system interprets voice commands captured by the microphone and allows 
control over the 4-channel relay. This relay controls the breadboard that 
controls the LED circuit. Integrating voltage sensor into the LED circuitry 
adds another level of sophistication. This sensor continuously monitor and 
collect data, which is sent to ThingSpeak for real-time graphical display. By 
integrating voice control, this project not only provides convenience but also 
introduces an interactive way to visualize home automation. Users can easily 
manage multiple aspects of their environment through voice instructions. 
ThingSpeak integration adds monitoring functionality that allows users to 
visualize and analyze voltage trends in the LED circuits used.

- Raspberry Pi 4B: Raspberry Pi 4B acts as the central processing unit 
and is responsible for processing voice commands, relay control, and 
managing the entire system. GPIO pins facilitate communication with 
relay systems, sensors, and other connected components.

- 4-Channel Relay System: 4-Channel Relay System is important for 
control and managing the LED circuits on the breadboard. The 
modular structure of the relay system allows for efficient control of 
multiple devices, increasing the scalability of your home automation 
system.

- Microphone: The microphone captures voice commands from the user 
and represents the primary mode of interaction with the system. 
Special voice recognition algorithms process these commands, 
allowing precise and responsive control.

- LED Circuits: LED circuits consist of multiple LEDs that are connected 
to a relay switch and dynamically respond to user commands. This 
component adds a practical and visual dimension to your home 
automation experience.

- Voltage sensor: Integration of voltage sensor into LED circuits allows 
real-time monitoring of electrical parameters. This sensor
continuously collect data and provide insights into the performance 
and health of connected devices.

- ADC and I2C Module Integration: An ADC module is integrated 
into the project, which allows converting analog sensor data into 
digital signals. Raspberry Pi read data from this module, providing a 
more diverse set of input parameters for the monitoring system.

- I2C Communication: The I2C (inter-integrated circuit) 
communication protocol is used to communicate between the ADC and
Raspberry Pi. This two-wire serial communication between the 
microprocessor and ADC module. It expands the range of sensors that 
can be integrated into the system.
