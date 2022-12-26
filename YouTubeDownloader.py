from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There has been error while Dowloading Video")
    print("Your video has been downloaded! Yahoooo")
    
link = input("Put Your YouTube Link Here! URl: ")
Download(link)