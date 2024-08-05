from pytubefix import YouTube 
import pytubefix
import os
import sys

fname = ""

def main():
    global fname
    url, fname = get_url_and_name()
    vid_streams, aud_stream , resolutions = vid_resolutions(url)
    res = get_resolution(resolutions)
    res = resolutions[res]
    # print(vid_streams[res])
    download_vid(vid_stream= vid_streams[res], audio_stream= aud_stream)
    

def get_url_and_name():
    url = input("Please enter the url of the video to be downloaded: ")
    name = input("Please enter the new filename of the video: ")
    return url, name if name else None

def get_resolution(available_resolutions):
    i=1
    print("AVAILABLE RESOLUTIONS: ")
    for res in available_resolutions:
        print(f"{i}. {res}")
        i+=1
    
    choice = int(input("Choose a resolution: "))
    
    if 1 <= choice < i :
        return choice -1
    else:
        sys.exit("Invalid resolution")

def vid_resolutions(url):
    global fname
    try:
        yt = YouTube(url)
    except pytubefix.exceptions.RegexMatchError:
        sys.exit("url not valid")
    if fname is None:
        fname = yt.title
    # print(f"Video: {yt.title}\nAvailable resolutions:")
    vid_streams = yt.streams.filter(file_extension='mp4', adaptive=True, only_video = True).order_by("resolution")
    aud_stream = yt.streams.filter(file_extension='mp4', adaptive=True, only_audio = True).order_by("abr").last()
    resolutions = []
    video_streams = {}

    # store all available resolutions
    for stream in vid_streams:
        # print("before filtering", stream)
        if stream.resolution not in video_streams:
            video_streams[stream.resolution] = stream
            resolutions.append(stream.resolution)
            # print("after filtering", stream)
    return video_streams, aud_stream, resolutions


def download_vid(vid_stream, audio_stream):
        
    video_path = vid_stream.download(output_path="D:\Coding\mini_projects\musicRemover\original", filename = f"{fname}_vid.mp4")
        
    audio_path = audio_stream.download(output_path = "D:\Coding\mini_projects\musicRemover\original", filename = f"{fname}_aud.mp3")
    output_path = f"D:/Coding/mini_projects/musicRemover/original/{fname}.mp4"
    
    # Use ffmpeg to merge and re-encode the video and audio streams
    os.system(f'ffmpeg -i "{video_path}" -i "{audio_path}" "{output_path}"')

    # remove mp4 and mp3 file after merging
    os.remove(audio_path)
    os.remove(video_path)
    
if __name__ == "__main__":
    main()