# Voice Controlled Home Automation using Raspberry Pi
This Voice Controlled Home Automation system interprets voice commands captured by the microphone using Porcupine for wake word detection and Google's Speech-to-Text API for converting speech into text commands. These commands allow control over a 4-channel relay, which manages the LED circuitry on a breadboard. The integration of sensors into the LED circuitry adds another level of sophistication by continuously monitoring and collecting data, which is sent to ThingSpeak for real-time graphical display. By integrating voice control, this project not only provides convenience but also introduces an interactive way to visualize home automation. Users can easily manage multiple aspects of their environment through voice instructions, while ThingSpeak integration adds monitoring functionality that allows users to visualize and analyze sensor trends in the LED circuits.

- Raspberry Pi 4B: Acts as the central processing unit responsible for processing voice commands, controlling the relay, and managing the entire system. GPIO pins facilitate communication with relay systems, sensors, and other connected components.

- 4-Channel Relay System: Essential for controlling and managing the LED circuits on the breadboard. Its modular structure allows efficient control of multiple devices, enhancing the scalability of the home automation system.

- Microphone: Captures voice commands from the user, serving as the primary mode of interaction with the system. Porcupine detects wake words, and Google's Speech-to-Text API converts the recognized speech into text, enabling precise and responsive control.

- LED Circuit: Consist of multiple LEDs connected to a relay switch, which dynamically respond to user commands. This component adds a practical and visual dimension to the home automation experience.

- Sensors: Integrated into the LED circuits to allow real-time monitoring of electrical parameters. The sensors continuously collects data, providing insights into the performance and health of connected devices.

- ADC and I2C Module Integration: An ADC module converts analog sensor data into digital signals, which the Raspberry Pi reads to provide a more diverse set of input parameters for the monitoring system.

- I2C Communication: Used between the ADC and Raspberry Pi, this two-wire serial communication protocol expands the range of sensors that can be integrated into the system.
