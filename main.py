from pytubefix import YouTube 
import pytubefix
import os
import sys

def main():
    url, fname = get_url_and_name()
    # download_vid(url, fname)
    vid_resolutions(url)
    

def get_url_and_name():
    url = input("Please enter the url of the video to be downloaded: ")
    name = input("Please enter the new filename of the video: ")
    return url, name

def vid_resolutions(url):
    try:
        yt = YouTube(url)
    except pytubefix.exceptions.RegexMatchError:
        sys.exit("url not valid")
    print(f"Video: {yt.title}\nchoose one of the available resolutions:")
    vid_streams = yt.streams.filter(file_extension='mp4', adaptive=True, only_video = True).order_by("resolution")
    resolutions = []
    # store all resolutions
    for stream in vid_streams:
        resolutions.append(stream.resolution)
        
    # this line is to remove duplicates as dicts cant have any duplicates
    resolutions = list(dict.fromkeys(resolutions))
    i = 1
    for resolution in resolutions:
        print(f"{i}. {resolution}")
        i+=1
        

def download_vid(url, fname):
    yt = YouTube(url)
    # create seperate streams for audio and video
    vid_streams = yt.streams.filter(file_extension='mp4', adaptive=True, only_video = True)
    aud_streams = yt.streams.filter(file_extension='mp4', adaptive=True, only_audio = True)

    if fname is None:
        fname = yt.title    

    if vid_streams:
        vid = vid_streams.order_by("resolution").last()
        print("using the get highest resolution function", vid)
        video_path = vid.download(output_path="D:\Coding\mini_projects\musicRemover\original", filename = f"{fname}_vid.mp4")
        print(video_path)
        
    if aud_streams:
        aud = aud_streams.order_by("abr").last()
        print("using the highest abr rate", aud)
        audio_path = aud.download(output_path = "D:\Coding\mini_projects\musicRemover\original", filename = f"{fname}_aud.mp3")
        print(audio_path)
        
    output_path = f"D:/Coding/mini_projects/musicRemover/original/{fname}.mp4"
    # Use ffmpeg to merge and re-encode the video and audio streams
    os.system(f'ffmpeg -i {video_path} -i {audio_path} "{output_path}"')

    os.remove(audio_path)
    os.remove(video_path)
    
if __name__ == "__main__":
    main()