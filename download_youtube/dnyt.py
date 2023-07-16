from pytube import YouTube 
import sys
import os 

Print ("Hope you used the format 'yt video link' 'current folder' ")
n = len(sys.argv)

if n<2:
    print("Not enought arguments given")
    exit()

if sys.argv[1] == '.':
    sys.argv[1] = os.path.dirname(os.path.realpath(__file__))
    print(sys.argv[1])

def download_video_from_youtube(link, path): 
    yt = YouTube(link,use_oauth=True, allow_oauth_cache=True) 
    video = yt.streams.get_highest_resolution() 
    # download the video 
    video.download(path) 

download_video_from_youtube(sys.argv[0],sys.argv[1])
