import queue
import sounddevice as sd
from vosk import Model,KaldiRecognizer
import pyttsx3
import json
import datetime

model=Model("model")
recognizer= KaldiRecognizer(model,16000)
audio_queue=queue.Queue()
ttss_engine=pyttsx3.init()

def callback(indata,frames,times,status):
  if status:
    print(status)
  audio_queue.put(bytes(indata))
  
def process_query(query):
  query=query.lower()
  if "time" in query:
    now =datetime.datetime.now().strftime("%H:%M")
    return f"The current time is {now}"
  elif "date" in query:
    now =datetime.datetime.now().strftime("%B %d, %Y")
    return f"The current day is {now}"
  elif "exit" in query or "quit" in query:
    return"Goofbye."
  else:
    return("I'm sorry ,I didnt undserstand that.")
print ("Listenign ..... Say 'time,date, or exit")

with sd.RawInputStream(
  sample_rate=16000,
  blocksize=8000,
  dtype="int16",
  channels=16000,
  callback=callback,
  ):
    while True:
      data=audio_queue.get()
      
      if recognizer.AcceptWaveform(data):
        result=json.loads(recognizer.Result())
        text=result.get("text","")
        
        if text:
          print(f"You said :{text}")
          response=process_query(text)
          print(f"Assistant: {response}")
          
          ttss_engine.say(response)
          ttss_engine.runAndWait()
          
          if "goodbye" in response.lower():
            break
          
          