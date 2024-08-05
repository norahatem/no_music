from vidDownloader import vidDownloader


def main():

    url, fname = get_url_and_name()
    downloader = vidDownloader(url=url, fname=fname)
    downloader.available_resolutions()
    downloader.get_res_choice()
    downloader.download_vid()


def get_url_and_name():
    url = input("Please enter the url of the video to be downloaded: ")
    name = input("Please enter the new filename of the video: ")
    return url, name if name else None


if __name__ == "__main__":
    main()
