# import ffmpeg
import subprocess
import os


def remove_music(audio_path):
    # input_audio = audio_path
    input_audio = "./original/yeman_aud.wav"

    command = [
        "python3", 
        "-m", 
        "demucs.separate", 
        "--two-stems=vocals", 
        audio_path, 
        "--out", 
        "./original"
    ]

    # Execute the command
    subprocess.run(command)
    
def rename_and_reposition(old_audio_path, new_audio_path):
    # os.rename(old_audio_path, new_audio_path)
    
    command = [
        "mv",
        old_audio_path,
        new_audio_path
    ]
    # Execute the command
    subprocess.run(command)
