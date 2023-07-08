from pytube import YouTube
def Download (link):
    youtube=YouTube(link)
    youtube=youtube.streams.get_highest_resolution()
    try:
        youtube.download()
    except:
        print("theres has been issue with downloading your video")
        print("your download complete thank you :) for trying my code")

link = input("put your youtube link here ")
Download (link)