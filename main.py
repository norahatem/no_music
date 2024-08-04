from pytubefix import YouTube 

yt = YouTube("https://www.youtube.com/watch?v=H09PmP5tsy8")

# mp4_streams = yt.streams.filter(file_extension='mp4', progressive=True)
mp4_streams = yt.streams.filter(file_extension='mp4', adaptive=True, only_audio = True)

for stream in mp4_streams.order_by('resolution'):
    print(stream)

if mp4_streams:
    # the get highest resolution function doesn't work for some reason so have to do it manually
    # d_video = mp4_streams.get_highest_resolution()
    # print("using the get highest resolution function", d_video)
    d_video = max(mp4_streams, key=lambda s: int(s.resolution[:-1]) if s.resolution else 0)
    # d_video = mp4_streams.order_by('resolution').last()
    print("using the max function",d_video)
    
    d_video.download(output_path="D:\Coding\mini_projects\musicRemover\original", filename = yt.title)
else:
    print("No suitable streams found")