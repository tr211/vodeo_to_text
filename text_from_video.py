import os
from moviepy.editor import VideoFileClip
import moviepy.editor as mp
import speech_recognition as sr

# Specify the video file name and the directory where it is located
video_file_name = 'IMG_6905.MP4'
video_file_dir = r'C:\Users\tr211\Downloads\Telegram Desktop'

def converter_mp4(video_file_dir: str, video_file_name: str, language: str):
    # Get the absolute file path
    abs_file_path = os.path.join(video_file_dir, video_file_name)

    # Load file
    video_load = mp.VideoFileClip(abs_file_path)
    
    # Extract audio
    audio_file_path = 'video_file.wav'
    video_load.audio.write_audiofile(audio_file_path)

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        data = recognizer.record(source)
    
    # Convert to text
    try:
        text = recognizer.recognize_google(data, language=language)
        with open('text_from_video.txt', 'w', encoding='utf-8') as text_fi:
            # text_from_video = text_fi.write(text)
            text_fi.write(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        
        # return text_from_video



if __name__ == '__main__':
    # Specify the language code (e.g., 'ru-RU' for Russian, 'es-ES' for Spanish, etc.)
    language_code = 'ru-RU'
    converter_mp4(video_file_dir, video_file_name, language_code)
