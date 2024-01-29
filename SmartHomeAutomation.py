from espeak import espeak
import speech_recognition as sr
import pyaudio
import time
import pvporcupine
import struct

import RPi.GPIO as GPIO

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import thingspeak

channel_id = 2396009
write_api_key = 'VY4MNRFXIBX3EAU1'

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

voltage_sensor = AnalogIn(ads, ADS.P0)

GPIO.setmode(GPIO.BCM)

IN1_PIN = 5
IN2_PIN = 6

GPIO.setup(IN1_PIN, GPIO.OUT, initial = True)
GPIO.setup(IN2_PIN, GPIO.OUT, initial = True)


# Text to Speech
def speak(text): 
    print("J.A.R.V.I.S.: " + text + " \n")
    espeak.synth(text)


# Speech to Text
def takeCommand() : 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...", end="")
        audio = r.record(source, duration=5)
        query = ''
        transcribed_text = ""
        speak("Recognizing")
        try:
            print("Recognizing...", end="")
            query = r.recognize_google(audio, language= 'en-US', show_all= True)
            alternatives = query.get('alternative', [])
            transcribed_text = " ".join([alternative.get('transcript', '') for alternative in alternatives])
            print(f"User said: {transcribed_text}")
        except Exception as e:
            print ("Exception: " + str(e))
        speak("beep")
        time.sleep(1)

    return transcribed_text.lower()

def LEDControl():
    print("in LEDControl")
    userSaid = takeCommand()
    if "on LED" in userSaid or "on led" in userSaid:
        speak("Turning On LED")
        if "one" in userSaid or "1" in userSaid:
            speak("Turning on LED One")
            GPIO.output(IN1_PIN, False)
            voltage = voltage_sensor.voltage
            print(f"Voltage: {voltage} V")
            channel = thingspeak.Channel(id=channel_id)
            channel.api_key = write_api_key
            #channel = thingspeak.Channel(id=channel_id, write_key=write_api_key)
            response = channel.update({'field1': voltage})
            print(response)
            time.sleep(1)
            
        elif "two" in userSaid or "2" in userSaid:
            speak("Turning on LED Two")
            GPIO.output(IN2_PIN, False)
            time.sleep(1) 
        else:
            speak("No such LED present in circuit!")

    elif "off LED" in userSaid or "off led" in userSaid:
        speak("Turning Off LED")
        if "one" in userSaid or "1" in userSaid:
            speak("Turning off LED One")
            GPIO.output(IN1_PIN, True)
            voltage = voltage_sensor.voltage
            print(f"Voltage: {voltage} V")
            channel = thingspeak.Channel(id=channel_id)
            channel.api_key = write_api_key
            #channel = thingspeak.Channel(id=channel_id, write_key=write_api_key)
            response = channel.update({'field1': voltage})
            time.sleep(1) 
        elif "two" in userSaid or "2" in userSaid:
            speak("Turning off LED Two")
            GPIO.output(IN2_PIN, True)
            time.sleep(1) 
        else:
            speak("No such LED present in circuit!")
    else:
        speak("No such command exists!")


    
def main():
    print("main")
    porcupine = None
    pa = None
    audio_stream = None

    
    print("J.A.R.V.I.S. version 1.2 - Online and Ready!")
    print('**********************************************************')
    print("J.A.R.V.I.S.: Awaiting your call")
    
    try:
        porcupine = pvporcupine.create(access_key = "ZkQ/pFyhVEzFm3XsJwPCgVY0NWCl48PkSJAoz0eZ721AVxuirhCdmg==", keywords=["jarvis"])
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

        while True:
                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

                keyword_index = porcupine.process(pcm)
                if keyword_index >= 0:
                    print("Hotword Detected..", end="")
                    speak("Yes")
                    LEDControl()    
                        
                    time.sleep(1)
                    print("J. A. R. V. I.S.: Awaiting your call")
                    

    finally:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()
        #GPIO.cleanup

main()
