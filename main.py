from pytubefix import YouTube 

# Initialize YouTube object with the video URL
yt = YouTube("https://www.youtube.com/watch?v=McFCv5yiTUs")

# Filter for mp4 streams with both video and audio
mp4_streams = yt.streams.filter(file_extension='mp4', progressive=True)

# Check if any streams are found
if mp4_streams:
    # Get the video with the highest resolution
    d_video = mp4_streams.get_highest_resolution()
    
    # Download the video
    d_video.download(output_path="D:\Coding\mini_projects\musicRemover\original")
else:
    print("No suitable streams found")