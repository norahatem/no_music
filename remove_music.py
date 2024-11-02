# import ffmpeg
import subprocess
import os
import sys


def remove_music(audio_path):

    command = [
        "python3",
        "-m",
        "demucs.separate",
        "--two-stems=vocals",
        audio_path,
        "--out",
        "./music_free",
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        sys.exit("Error removing music")


def rename_and_reposition(old_audio_path, new_audio_path):
    # os.rename(old_audio_path, new_audio_path)

    command = ["mv", old_audio_path, new_audio_path]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        sys.exit("Error renaming and/or changing path")
