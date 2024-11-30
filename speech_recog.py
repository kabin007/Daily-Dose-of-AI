"""
This Python script recognizes speech from the microphone as input
and prints out the text translation of the speech.
"""

import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

while True:
    try:
        # Use microphone as the source
        with sr.Microphone() as mic:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening...")
            
            # Capture audio from the microphone
            audio = recognizer.listen(mic)
            
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            print(f"Recognized: {text}\n")
            
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio. Please try again.")
        continue
