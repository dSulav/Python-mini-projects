'''
 Using this CLI python app, we can download youtube videos in different 
 formats and video quality.
'''
from pytube import YouTube

link = input("Enter the youtube url link of a video to be downloaded: ")
yt = YouTube(link)

videos = yt.streams.all()
i=1
for stream in videos:
    print(str(i)+" "+str(stream))
    i+=1
stream_num = int(input("Enter number (according to above format s.n.) : "))
video = videos[stream_num-1]
video.download("/Users/Desktop")
print("Downloaded")



