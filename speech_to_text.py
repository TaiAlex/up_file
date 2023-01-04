import speech_recognition as sr

def stt(filename):
# filename=(r"ulatroi.mp3")
# initialize the recognizer
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio, language="vi-VI")
        with open('log.txt', mode='w', encoding='UTF-8') as f:
            f.write(str(text))
            print(str(text))
