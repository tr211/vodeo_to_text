# import os
# import moviepy.editor as mp
# # from moviepy.editor import VideoFileClip
# # background audio
# audio_file_name = 'translated_text.mp3'
# audio_file_name_file_dir = r'C:\Users\tr211\Новая папка\video_translator'
# audio_background = os.path.join(audio_file_name_file_dir, audio_file_name)

# video_file_name = 'IMG_6905.MP4'
# video_file_dir = r'C:\Users\tr211\Downloads\Telegram Desktop'
# my_clip_path = os.path.join(video_file_dir, video_file_name)

# final_v_n = 'final_cut.mp4'
# final_v_dir = r'C:\Users\tr211\Новая папка\video_translator'
# final_v_path = os.path.join(final_v_dir, final_v_n)


# # without audio
# # videoclip = VideoFileClip(my_clip_path)
# # new_clip = videoclip.without_audio()
# # new_clip.write_videofile("final_cut.mp4")
# # add auodio in to video
# my_clip = mp.VideoFileClip(final_v_path)
# audio_background = mp.AudioFileClip(audio_background)
# final_audio = mp.CompositeAudioClip([my_clip.audio, audio_background])
# final_clip = my_clip.set_audio(final_audio)
# final_clip.write_videofile("final_v.mp4")

# # final_clip.write_audiofile(audio_file_path)

import os
import moviepy.editor as mp

# File paths
audio_file_name = 'translated_text.mp3'
audio_file_name_file_dir = r'C:\Users\tr211\Новая папка\video_translator'
audio_background_path = os.path.join(audio_file_name_file_dir, audio_file_name)

video_file_name = 'IMG_6905.MP4'
video_file_dir = r'C:\Users\tr211\Downloads\Telegram Desktop'
my_clip_path = os.path.join(video_file_dir, video_file_name)

final_v_n = 'final_cut.mp4'
final_v_dir = r'C:\Users\tr211\Новая папка\video_translator'
final_v_path = os.path.join(final_v_dir, final_v_n)

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
