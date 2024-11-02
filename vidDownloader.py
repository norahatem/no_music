from pytubefix import YouTube
import pytubefix
import os
import sys
import subprocess
import logging

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
        self.path = "./music_free"
        # initialising available resolutions and streams
        self._resolutions = []
        # this is the variable where we store the no-duplicate video streams, the other one vid_streams is for all of the,
        self.video_streams = dict()

    # getter method for resolutions
    @property
    def resolutions(self) -> None:
        return self._resolutions

    def validate_url(self) -> None:
        # try to open the url and exit if it is invalid
        try:
            self.yt = YouTube(self.url)
        except pytubefix.exceptions.RegexMatchError:
            sys.exit("url not valid")

    def check_fname(self) -> None:
        # check if the file name is empty, if so let be the title of the video
        if self.fname is None:
            self.fname = self.yt.title

    # function to store all available resolution plus the equivalent streams - no duplicates
    def available_resolutions(self) -> None:
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
        try:
            self.res = int(input("Choose a resolution: "))
        except ValueError:
            sys.exit("Invalid choice")
        if 1 <= self.res < i:
            self.res -= 1
            # now self.res stores the actual resolution, eg: "144p", it is a str
            self.res = self.resolutions[self.res]
            # print(self.resolutions[self.res])
        else:
            sys.exit("Invalid resolution")

    def download_audio(self) -> None:
        self.audio_path = self.aud_stream.download(
            output_path=self.path, filename=f"{self.fname}_aud.wav"
        )

    def download_video(self) -> None:
        video_stream = self.video_streams[self.res]

        self.video_path = video_stream.download(
            output_path=self.path, filename=f"{self.fname}_vid.mp4"
        )

    def merge(self) -> None:
        # output_path = f"{self.path}/{self.fname}.mp4"
        output_path = os.path.join(self.path, f"{self.fname}.mp4")
        # Use ffmpeg to merge and re-encode the video and audio streams
        merge_command = [
            "ffmpeg",
            "-i",
            self.video_path,
            "-i",
            self.audio_path,
            output_path,
        ]
        try:
            # check=True automatically handles errors
            subprocess.run(merge_command, check=True)
        except subprocess.CalledProcessError:
            sys.exit("Error merging files")
        finally:
            # remove mp4 and mp3 file after merging
            os.remove(self.audio_path)
            os.remove(self.video_path)
    def remove_unnecessary_files(self):
        os.remove(f"./music_free/htdemucs/{self.title}_aud/vocals.wav")
        os.remove(f"./music_free/htdemucs/{self.title}_aud/no_vocals.wav")
        os.rmdir("./music_free/htdemucs/")
