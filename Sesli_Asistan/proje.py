
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import random
import os
import time
from datetime import datetime
import webbrowser


def Speak(string):
   tts=gTTS(string,lang="tr")
   rand=random.randint(1,10000)
   file=("audio-"+str(rand)+".mp3")
   tts.save(file)
   playsound(file)
   os.remove(file)
def SpeakEng(string):
   tts=gTTS(string,lang="en")
   rand=random.randint(1,10000)
   file=("audio-"+str(rand)+".mp3")
   tts.save(file)
   playsound(file)
   os.remove(file)

   
   


s=sr.Recognizer()
def record(ask=False):
   

   with sr.Microphone() as source:
    audio= s.listen(source)
    if ask:Speak(ask)
    voice=""
    try:
       voice=s.recognize_google(audio,language="tr-TR")
    except sr.UnknownValueError:
        Speak("ne dediğinizi anlayamadım lütfen algılayabileceğim sesler çıkartın")
    except sr.RequestError:
       Speak("sistem bir sebepten ötürü hata veriyor")
    return voice
def recordeng(ask=False):
   

   with sr.Microphone() as source:
    audio= s.listen(source)
    if ask:Speak(ask)
    voice=""
    try:
       voice=s.recognize_google(audio,language="en-EN")
    except sr.UnknownValueError:
        SpeakEng("Please check your microphone or give answers that i can understand")
    except sr.RequestError:
       SpeakEng("an error occured")
    return voice

def aratma(degisken):
   Speak("Ne lazım ?")
   degisken=record(False)
   print(degisken)
   url="https://google.com/search?q="+degisken
   Speak(degisken+"için bunları buldum")
   webbrowser.get().open(url)
   
def response(voice):
   if "Sen kimsin"in voice:Speak("Ben sesli asistanım")
   elif "Sistemi kapat"in voice:
      Speak("görüşmek üzere")
      
      exit()
   elif "ne haber"in voice or "nasılsın"in voice:
      Speak("ben iyiyim teşekkürler")
      
      
   elif "saat kaç"in voice:Speak(datetime.now().strftime("%H,%M"))
   
   elif "arama yap"in voice:
      Speak("Ne aramamı istiyorsun")
      
      search=record(False)
      print(search)
      url="https://google.com/search?q="+search
      Speak(search+"için bunları buldum")
      webbrowser.get().open(url)
   elif "şarkı ara"in voice:
      Speak("Ne ariyim")
      
      search=str(input("BURAYA GİRİN :"))
      print(search)
      url="https://www.youtube.com/results?search_query="+search
      Speak(search+"için bunları buldum")
      webbrowser.get().open(url)
def responseEng(voice):
   if "who are you"in voice:SpeakEng("I am your virttual asisstant")
   elif "turn off"in voice:
      SpeakEng("okay see you soon")
      
      exit()
   elif "how are you"in voice:
      SpeakEng("I am good thanks for asking")
      
      
   elif "what time is it"in voice:SpeakEng(datetime.now().strftime("%H,%M"))
   
   elif "look it up"in voice:
      SpeakEng("what do u want me to search")
      
      search=recordeng(False)
      print(search)
      url="https://google.com/search?q="+search
      SpeakEng("I have found these for"+search)
      webbrowser.get().open(url)
   elif "play music"in voice:
      SpeakEng("which song")
      
      search=str(input(":"))
      print(search)
      url="https://www.youtube.com/results?search_query="+search
      SpeakEng("there you go"+search)
      webbrowser.get().open(url)
   
   
     
Speak("Sesli asistana hoşgeldiniz türkçe devam etmek için lütfen biri tuşlayınız")
SpeakEng("If you want to continue on english please press two")
dil=int(input(":"))
if dil==1:
   while True:
     Speak("size nasıl yardımcı ollabilirim")
     voice=record(False)
     print(voice)
     response(voice)
elif dil==2:
   while True:
     SpeakEng("how may i help you")
     voice=recordeng()
     print(voice)
     responseEng(voice)
SpeakEng("how may i help you")
voice=recordeng()
print(voice)
responseEng(voice)



   
 
 
 
 
 
 
 
    
 
 

    
    
      
 
      


   
      
   
      
   
   



    

 
 



      
   

