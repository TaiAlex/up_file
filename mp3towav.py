# pythonbasics.org
from pydub import AudioSegment
from os import path

# files                                                                         
# src = (r"D:\Student\AI\Speech to Text with Python\Audio_mp3\345.mp3")
# dst = (r"D:\Student\AI\Speech to Text with Python\Audio_wav\test4.wav")

def wav_to_mp3(sound):# convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")