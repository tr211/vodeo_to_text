import os
import pyttsx3 
# from translate_text import translated_data
from gtts import gTTS

video_file_name = 'translated_text.txt'
video_file_dir = r'C:\Users\tr211\Новая папка\video_translator'
abs_file_path = os.path.join(video_file_dir, video_file_name)

text_data = open(abs_file_path, 'r')
for i in text_data:
    text_data = gTTS(text=i, slow=False)
    text_data.save('translated_text.mp3') 



# def SpeakText(command):
#     engine = pyttsx3.init()
#     engine.say(command) 
#     engine.runAndWait()

# with open('translated_text.txt', 'r') as text_data:
#     text_data.read()
# text_data = open(abs_file_path, 'r')
# for i in text_data:
#     SpeakText(i)