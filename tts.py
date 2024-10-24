# Import the required module for text 
# to speech conversion
from gtts import gTTS
import string
from string import ascii_lowercase
import re
# Import pygame for playing the converted audio
#import pygame

# The text that you want to convert to audio

with open(r"C:\Users\Serbz\Desktop\document.txt", "r", encoding="utf8") as f:
    mytext = f.read()
f.close()
mytext = re.sub('(?i)(.*)\s.*\.[jpm][np][g4]', '\g<1>', mytext)

def Merge(dict1, dict2):
    return {*dict1, *dict2}
print(ascii_lowercase)
Ascii = [f'{each}' for each in ascii_lowercase]
Ascii.append(" ")
Cases = ["-", "_", "0", "9", "8", "7", "6", "5", "4", "3", "2", "1", ":", "?", ".", ";", "\n", "\r\n", "-"]
mytext2 = ""
Ascii = Merge(Ascii, Cases)
for each in mytext:
    for eache in Ascii:
        if each.lower() == eache.lower():
            mytext2 += each
            break
print(mytext2)
# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext2, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save(r"C:\Users\Serbz\Desktop\Document.mp3")

# Initialize the mixer module
#pygame.mixer.init()

# Load the mp3 file
#pygame.mixer.music.load("welcome.mp3")

# Play the loaded mp3 file
#pygame.mixer.music.play()
quit()
