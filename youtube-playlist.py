import pafy
import vlc
from time import sleep
import keyboard
from datetime import timedelta
import threading
from colored import attr, fg, bg

cyan = fg('cyan')
red = fg('red')
res = attr('reset')
black = fg('black')
bg_y = bg('yellow')
d = 0

url = "PUT_YOUR_YOUTUBE_PLAYLIST_URL_HERE"

def contador():
    global key
    global d

    while True:
        d = 1
        key = keyboard.read_key() # Detects the pressed key
        

t = threading.Thread(target=contador)
t.start()


def playlist_(playlist):
    global key
    global d
    print(f'{bg_y}{black} Playlist {res}')
    for music in playlist['items']:
        
        url_video = music['playlist_meta']['encrypted_id'] # Extracts the url from the videos
        video = pafy.new(url_video)
        audio = video.getbestaudio() # Extracts only the audio from the videos
        playurl = audio.url

        print(video.title + f' - {red}' + video.duration + f'{res}')

        # Below is the standard media reproduction of the python-vlc library
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        timer = 3
        if d == 1:   
            print(str(timedelta(seconds=0)))
            sleep(1)
            print(str(timedelta(seconds=1)))
            sleep(1)
            print(str(timedelta(seconds=2)))
            sleep(1)
        else:
            sleep(3)
        
        key = ''
        while player.is_playing() and timer < video.length:
            if d == 1:
                print(str(timedelta(seconds=timer)))
            timer +=1
            sleep(1)
 
            if key == 'page up':
                print(f'{cyan}-next{res}')
                break
            if d == 0:
                input('Please press Enter to next song')
                print(f'{cyan}-next{res}')  
                break
        player.stop()


def only_one(url_video):
    video = pafy.new(url_video)
    audio = video.getbestaudio() # Extracts only the audio from the videos
    playurl = audio.url
    print(f'{bg_y}{black} Single {res}')

    print(video.title + f' - {red}' + video.duration + f'{res}')

    # Below is the standard media reproduction of the python-vlc library
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()

    timer = 3
    print(str(timedelta(seconds=0)))
    sleep(1)
    print(str(timedelta(seconds=1)))
    sleep(1)
    print(str(timedelta(seconds=2)))
    sleep(1)
    
    while player.is_playing():
        print(str(timedelta(seconds=timer)))
        timer +=1
        sleep(1)
    player.stop()

if 'list' in url:
    try:
        playlist_(pafy.get_playlist(url)) # Extracts playlist information and call the playlist function
    except:
        print('The url is not right')
else:
    try:
        only_one(url)  # Call the one song function
    except:
        print('The url is not right')
    
