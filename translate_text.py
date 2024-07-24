import os
import time
from deep_translator import GoogleTranslator

def split_text(text, max_length):
    # Split text into chunks of max_length characters
    chunks = []
    while len(text) > max_length:
        # Find the last space within the limit to avoid splitting words
        split_index = text.rfind(' ', 0, max_length)
        if split_index == -1:  # No space found, force split at max_length
            split_index = max_length
        chunks.append(text[:split_index])
        text = text[split_index:].strip()
    chunks.append(text)  # Append the last chunk
    return chunks

# Define file paths
video_file_name = 'Ludik and the Runaway Mountain - John Ilho.txt'
video_file_dir = r'C:\Users\tr211\Downloads'
abs_file_path = os.path.join(video_file_dir, video_file_name)

# Check if the file exists
if not os.path.isfile(abs_file_path):
    raise FileNotFoundError(f"The file {abs_file_path} does not exist.")

# Read the content of the file
with open(abs_file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Split the content into chunks
max_characters = 5000
text_chunks = split_text(content, max_characters)

# Initialize the translator
translator = GoogleTranslator(source='en', target='ru')

# Translate the chunks with delay to avoid rate limits
translated_chunks = []
for chunk in text_chunks:
    try:
        translated_chunk = translator.translate(chunk)
        translated_chunks.append(translated_chunk)
        time.sleep(1)  # Introduce a delay of 1 second between requests
    except Exception as e:
        print(f"An error occurred: {e}")
        break

# Combine the translated chunks and save to a new file
translated_text = ' '.join(translated_chunks)
with open("trnsl.txt", 'w', encoding='utf-8') as tr_text:
    tr_text.write(translated_text)
