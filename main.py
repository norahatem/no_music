from vidDownloader import vidDownloader
from remove_music import remove_music, rename_and_reposition


def main():

    # first get the url from the user and the name of the to-be-saved file
    url, fname = get_url_and_name()
    # initiate an object of the type videoDownloader with the url and filename
    downloader = vidDownloader(url=url, fname=fname)
    # validate data
    downloader.validate_url()
    downloader.check_fname()
    # get all resolutions and corresponding streams
    downloader.available_resolutions()
    # get the users choice of recommended resolution tp-be-downloaded
    downloader.get_res_choice()
    # download both audio and video files
    downloader.download_video()
    downloader.download_audio()
    old_path = f"./original/htdemucs/{downloader.fname}_aud/vocals.wav"
    new_path = f"./original/{downloader.fname}_aud.wav"
    # we will have a step in here where we will get the only vocals mp3/war and that is the one to be merged
    remove_music(new_path)
    rename_and_reposition(old_path, new_path)
    downloader.merge()


def get_url_and_name():
    url = input("Please enter the url of the video to be downloaded: ")
    name = input("Please enter the new filename of the video: ")
    return url, name if name else None


if __name__ == "__main__":
    main()
