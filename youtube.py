userSelection = int(input("""Enter 1 for downloading single video.\n
Enter 2 for downloading complete playlist.\n"""))

if (userSelection == 1):
    from pytube import YouTube

    link= input("Enter the link of youtube video: ")
    yt = YouTube(link)

    # print(yt.title)

    videos = yt.streams.all()
    vid = list(enumerate(videos))

    for i in vid:
        print(i)

    print()
    strm = int(input("Enter: "))

    print(f'Downloading: {yt.title}')
    videos[strm].download()

elif (userSelection == 2):
    from pytube import Playlist

    link = input("Enter the link of youtube playlist: ")
    py = Playlist(link)

    vid = list(enumerate(py.videos))

    print(f'Downloading: {py.title}')
    for video in py.videos:
        video.streams.first().download()


print("Task completed")

# https://youtube.com/playlist?list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA