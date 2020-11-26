import speech_recognition as sr
import os
import playsound
import random
from gtts import gTTS
import pyaudio
import time
import pyttsx3
import tkinter as ttk

r = sr.Recognizer()

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def active():
    with sr.Microphone() as source:
        speak('Hello, How Can I Help?')
        audio = r.listen(source)
        time.sleep(5)
        try:
            voice_data = r.recognize_google(audio)
            speak('Just Now You Say, ' + voice_data)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, My Speech Service is Down')
    return None

def Keluar():
    exit()

root = ttk.Tk()

startButton = ttk.Button(root, text='Klik Tombol Untuk Mengaktifkan Stella', command=active)
exitButton = ttk.Button(root, text='Klik Untuk Keluar', command=Keluar)
startButton.pack()
exitButton.pack()

root.mainloop()