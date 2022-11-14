
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


def response(voice):
   if "Seni kim yarattı"in voice:Speak("Ben trakya üniversitesi ikinci sınıf öğrencisi yiğit ve emrenin dönem sonu projesiyim")
   elif "Sistemi kapat"in voice:
      Speak("görüşmek üzere")
      playsound("C:/Users/Yigit/Downloads/kapanma(online-audio-convert.com).mpeg")
      exit()
   elif "ne haber"in voice or "nasılsın"in voice:
      Speak("ben iyiyim sen nasılsın")
      searchhhh=record()
      print(searchhhh)
      if "iyiyim" in searchhhh:
         Speak("buna çok sevindim")
      elif "kötüyüm" in searchhhh:Speak("niye bölye hissediyosun bilmiyorum umarım yakında düzelirsin")
   elif "saat kaç"in voice:Speak(datetime.now().strftime("%H,%M"))
   
   elif "arama yap"in voice:
      Speak("Ne aramamı istiyorsun")
      
      search=record()
      url="https://google.com/search?q="+search
      Speak(search+"için bunları buldum")
      webbrowser.get().open(url)
      
   elif "şarkı ara"in  voice:
     Speak("Hangi şarkı ")
     searchh=record()
     print(searchh)
     time.sleep(1)
     
     urll="https://www.youtube.com/results?search_query="+searchh
     webbrowser.get().open(urll)

     webbrowser.get().open(urll)
     Speak(searchh+"için bunları buldum")
   

   elif "mesaj kaydet" in voice:
    Speak("Not almak istediğiniz şeyi bana söyleyin")
    cevap=record()
    dosya=open("C:/Users/Yigit/OneDrive/Masaüstü/Benimnotum.txt","a")
    dosya.write("\n"+cevap+" "+"-------Bu not şu saatte oluşturuldu :"+datetime.now().strftime("%H,%M"))

      
    Speak("işlem tamam masaüstüne Benim notum adlı bir metin belgesi oluşturdum")
   else:
    Speak("Söylediğiniz şey benim komut listemde bulunmuyor lütfen bir daha deneyin")
      
   





  





while True:
 time.sleep(0.5)
 Speak("Komut verin")
 voice=record()
 
 print(voice)
 response(voice)
 
 continue
 
 
 
 
 
 
 
 
    
 
 

    
    
      
 
      


   
      
   
      
   
   



    

 
 



      
   

