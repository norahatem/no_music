from pytubefix import YouTube 
import os

yt = YouTube("https://www.youtube.com/watch?v=z1dzByPXd3U")

# create seperate streams for audio and video
vid_streams = yt.streams.filter(file_extension='mp4', adaptive=True, only_video = True)
aud_streams = yt.streams.filter(file_extension='mp4', adaptive=True, only_audio = True)


if vid_streams:
    vid = vid_streams.order_by("resolution").last()
    print("using the get highest resolution function", vid)
    video_path = vid.download(output_path="D:\Coding\mini_projects\musicRemover\original", filename = "vid.mp4")
    print(video_path)
    
if aud_streams:
    aud = aud_streams.order_by("abr").last()
    print("using the highest abr rate", aud)
    audio_path = aud.download(output_path = "D:\Coding\mini_projects\musicRemover\original", filename = "aud.mp3")
    print(audio_path)
    
output_path = f"D:/Coding/mini_projects/musicRemover/original/video.mp4"
os.system(f'ffmpeg -i {video_path} -i {audio_path} -c copy {output_path}')

os.remove(audio_path)
os.remove(video_path)