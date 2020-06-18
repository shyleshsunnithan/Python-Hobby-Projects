from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
YourText = input("Enter Your Text")
sp = gTTS(text = YourText, lang = language,slow=False)

sp.save(audio)
playsound(audio)