import os
from deep_translator import GoogleTranslator
# from text_from_video import converter_mp4, text_from_video

video_file_name = 'text_from_video.txt'
video_file_dir = r'C:\Users\tr211\Новая папка\video_translator'
abs_file_path = os.path.join(video_file_dir, video_file_name)

translated = GoogleTranslator(source='auto', target='en').translate_file(abs_file_path)


with open('translated_text.txt', 'w') as tr_text:
    translated_data = tr_text.write(translated)

# if __name__=='__main__':
#     pass