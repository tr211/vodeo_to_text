import os
from deep_translator import GoogleTranslator
from moviepy.editor import VideoFileClip
import moviepy.editor as mp
import speech_recognition as sr

# Specify the video file name and the directory where it is located
video_file_name = 'IMG_6905.MP4'
video_file_dir = r'C:\Users\tr211\Downloads\Telegram Desktop'

# Specify the language code (e.g., 'ru-RU' for Russian, 'es-ES' for Spanish, etc.)
language_code = 'ru-RU'


def converter_mp4(video_file_dir: str, video_file_name: str, language: str):
    text_from_video = ''
    # Get the absolute file path
    abs_file_path = os.path.join(video_file_dir, video_file_name)
    # Load file
    video_load = mp.VideoFileClip(abs_file_path)
    # Extract audio
    audio_file_path = 'audio_line.wav'
    video_load.audio.write_audiofile(audio_file_path)

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        data = recognizer.record(source)
    # Convert to text
    try:
        text = recognizer.recognize_google(data, language=language)
        with open('text_from_video.txt', 'w', encoding='utf-8') as text_fi:
            text_from_video = text_fi.write(text)
            # text_fi.write(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        
        return text_from_video, audio_file_path

text_fi = converter_mp4(video_file_dir: str, video_file_name: str, language: str)
# Translate text
translated = GoogleTranslator(source='auto', target='en').translate_file(text_fi)

with open('translated_text.txt', 'w') as tr_text:
    translated_data = tr_text.write(translated)

file_name = 'audio_line.wav'
file_dir = ''
audio_background_path = os.path.join(file_dir, file_name)

# Load video clip
my_clip = mp.VideoFileClip(my_clip_path)

# Load audio background
audio_background = mp.AudioFileClip(audio_background_path)

# Create final audio by combining the original audio with the background audio
final_audio = mp.CompositeAudioClip([my_clip.audio, audio_background])

# Set the final audio to the video clip
final_clip = my_clip.set_audio(final_audio)

# Write the final video file
final_clip.write_videofile(final_v_path)

