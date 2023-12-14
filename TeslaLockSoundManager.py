import os
import shutil
from pydub import AudioSegment

def ensure_path_exists(path):
    """Create the directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        # print(f"Created directory: {path}")

def copy_file(src, dest):
    """Copy a file from src to dest."""
    ensure_path_exists(os.path.dirname(dest))
    shutil.copy(src, dest)
    # print(f'Copied {os.path.basename(src)} to {dest}')

def move_file(src, dest):
    """Move a file from src to dest."""
    ensure_path_exists(os.path.dirname(dest))
    shutil.move(src, dest)
    # print(f'Moved {os.path.basename(src)} to {dest}')

def delete_directory_if_empty(directory):
    """Delete the directory if it is empty."""
    if os.path.exists(directory) and not os.listdir(directory):
        os.rmdir(directory)
        # print(f"Deleted empty directory: {directory}")

def convert_mp3_to_wav(mp3_in_folder, wav_out_folder, archive_mp3_folder):
    print("Starting MP3 to WAV conversion...")

    # Process each file in the mp3_in folder
    for filename in os.listdir(mp3_in_folder):
        if filename.endswith('.mp3'):
            mp3_path = os.path.join(mp3_in_folder, filename)
            wav_path = os.path.join(wav_out_folder, filename.replace('.mp3', '.wav'))

            # Convert mp3 to wav
            ensure_path_exists(wav_out_folder)
            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format='wav')
            # print(f'Converted {filename} to WAV and saved in {wav_out_folder}')

            # Move the MP3 file to archive
            move_file(mp3_path, os.path.join(archive_mp3_folder, filename))

def process_wav_files(wav_out_folder, payload_folder, archive_wav_folder, too_big_folder):
    print("Processing WAV files...")

    for filename in os.listdir(wav_out_folder):
        if filename.endswith('.wav'):
            wav_path = os.path.join(wav_out_folder, filename)

            # Check if file size is 1MB or smaller
            if os.path.getsize(wav_path) <= 1 * 1024 * 1024:  # 1MB in bytes
                # Copy to payload and archive
                copy_file(wav_path, os.path.join(payload_folder, filename))
                copy_file(wav_path, os.path.join(archive_wav_folder, filename))

                # Delete from wav_out
                os.remove(wav_path)
                # print(f'Deleted {filename} from {wav_out_folder}')
            else:
                # Move to 'too_big' folder
                move_file(wav_path, os.path.join(too_big_folder, filename))
                # print(f'Warning: {filename} exceeds the maximum size (1MB) for a Tesla lock sound, file moved to {too_big_dir}')

    # Delete the wav_out directory if it is empty
    delete_directory_if_empty(wav_out_folder)

# Define the directories
mp3_in_dir = './mp3_in'
wav_out_dir = './tmp'
payload_dir = './payload'
too_big_dir = './too_big'
archive_dir = './archive'
archive_mp3_dir = './archive/mp3'
archive_wav_dir = './archive/wav'

# Convert MP3 files to WAV
convert_mp3_to_wav(mp3_in_dir, wav_out_dir, archive_mp3_dir)

# Process WAV files
process_wav_files(wav_out_dir, payload_dir, archive_wav_dir, too_big_dir)

# Print results
too_big_list = os.listdir(too_big_dir)
if os.path.exists(too_big_dir) and too_big_list:
    print(f'Warning: the {too_big_dir} directory contains files that exceeded the maximum size (1MB) for a Tesla lock sound:\n{too_big_list}')

payload_list = os.listdir(payload_dir)
if os.path.exists(payload_dir) and payload_list:
    print(f'Success: files in the {payload_dir} directory are ready for upload to Tesla drive:\n{payload_list}')
