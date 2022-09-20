# pip install pytube

from pytube import YouTube

video_link = "https://www.youtube.com/watch?v=35EQXmHKZYs"

video = YouTube(video_link)

video.streams.filter(res='720p').first().download('E:\\videos')