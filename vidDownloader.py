from pytubefix import YouTube
import pytubefix
import os
import sys
import subprocess

# i kinda know the problem nw??
# since the file path is hardcoded it does this 


class vidDownloader:
    def __init__(self, url, fname) -> None:
        # initialise the file name and the url
        self.fname = fname
        self.url = url
        # initialise the commaon conditions instead of writing them!
        self.conditions = {"file_extension": "mp4", "adaptive": True}
        # the path that the downloaded stuff will be stored in
        # self.path = "D:/Coding/mini_projects/musicRemover/original"
        self.path = "./original"
        # initialising available resolutions and streams
        self._resolutions = []
        # this is the variable where we store the no-duplicate video streams, the other one vid_streams is for all of the,
        self.video_streams = dict()

    # getter method for resolutions
    @property
    def resolutions(self) -> None:
        return self._resolutions

    # function to store all available resolution plus the equivalent streams - no duplicates
    def available_resolutions(self) -> None:
        # try to open the url and exit if it is invalid
        try:
            self.yt = YouTube(self.url)
        except pytubefix.exceptions.RegexMatchError:
            sys.exit("url not valid")
            
        # check if the file name is empty, if so let be the title of the video
        if self.fname is None:
            self.fname = self.yt.title

        # get all video and audio streams and store them in their respective para
        # notice that this is because we use adaptive streams where video and audio are seperate
        self.vid_streams = self.yt.streams.filter(
            **self.conditions, only_video=True
        ).order_by("resolution")
        self.aud_stream = (
            self.yt.streams.filter(**self.conditions, only_audio=True)
            .order_by("abr")
            .last()
        )

        # store all available resolutions - no duplicates
        # store corresponding stream
        for stream in self.vid_streams:
            if stream.resolution not in self.video_streams:
                self.video_streams[stream.resolution] = stream
                self.resolutions.append(stream.resolution)

    def get_res_choice(self) -> None:
        i = 1
        for res in self.resolutions:
            print(f"{i}. {res}")
            i += 1
        self.res = int(input("Choose a resolution: "))

        if 1 <= self.res < i:
            self.res -= 1
            # now self.res stores the actual resolution, eg: "144p", it is a str
            self.res = self.resolutions[self.res]
            # print(self.resolutions[self.res])
        else:
            sys.exit("Invalid resolution")

    def download_files(self) -> None:
        
        # this is the actual chosen video stream with the correct resolution
        video_stream = self.video_streams[self.res]
        
        self.video_path = video_stream.download(
            output_path=self.path, filename=f"{self.fname}_vid.mp4"
        )
        self.audio_path = self.aud_stream.download(
            output_path=self.path, filename=f"{self.fname}_aud.wav"
        )
        print(self.audio_path)
        

    def merge(self) -> None:
        output_path = f"{self.path}/{self.fname}.mp4"
        # Use ffmpeg to merge and re-encode the video and audio streams
        subprocess.run(["ffmpeg", "-i", self.video_path, "-i", self.audio_path, output_path])
        # os.system(f'ffmpeg -i "{video_path}" -i "{audio_path}" "{output_path}"')
        
        # remove mp4 and mp3 file after merging
        # os.remove(self.audio_path)
        os.remove(self.video_path)
