class MP3:
    def play(self):
        print("playing MP3 audio file")

class MP4:  
    def play(self):
        print("playing MP4 vedio file")   

class VLC:
    def play(self):
        print("playing VLC media file")
def start_media(file):
    file.play()

song=MP3()
vedio=MP4()
movie=VLC()

start_media(song)
start_media(vedio)
start_media(movie)

