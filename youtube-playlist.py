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

url = "PUT_YOUR_YOUTUBE_PLAYLIST_URL_HERE"

def detect_key():
    global key
    while True:
        try:
            key = keyboard.read_key() # Detects the pressed key
        except(BaseException):
            break


t = threading.Thread(target=detect_key)
t.start()


def playlist_(playlist):
    global key
    d = 1
    try:
        keyboard.read_key()
    except(BaseException):
        d=0

    print(f'{bg_y}{black} Playlist {res}')
    for music in playlist['items']:
        
        url_video = music['playlist_meta']['encrypted_id'] # Extracts the url from the videos
        try:
            video = pafy.new(url_video)
        except(IOError):
            print('There was an error playing this song')
            print(f'{cyan}-next         {res}') 
            continue

        audio = video.getbestaudio() # Extracts only the audio from the videos
        playurl = audio.url

        print('\r'+video.title + f' - {red}' + video.duration + f'{res}')

        # Below is the standard media reproduction of the python-vlc library
        opt = "--quiet"
        Instance = vlc.Instance(opt)
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        timer = 5
        key = ''
        if d == 1:
            for s in range(5):   
                print('\r'+str(timedelta(seconds=s)), end='')
                if key == 'page up':
                    break
                sleep(1)

            if key == 'page up':
                print(f'\r{cyan}-next         {res}')
                player.stop()
                continue
                
        else:
            sleep(3)
        
        
        while player.is_playing() and timer < video.length:
            if d == 1:
                print('\r'+str(timedelta(seconds=timer)), end='')
            timer +=1
            sleep(1)
 
            if key == 'page up':
                print(f'\r{cyan}-next         {res}')
                break
            if d == 0:
                input('Please press Enter to next song')
                print(f'\r{cyan}-next         {res}')  
                break
        player.stop()


def only_one(url_video):
    video = pafy.new(url_video)
    audio = video.getbestaudio() # Extracts only the audio from the videos
    playurl = audio.url
    print(f'{bg_y}{black} Single {res}')

    print('\n\r'+video.title + f' - {red}' + video.duration + f'{res}')

    # Below is the standard media reproduction of the python-vlc library
    opt = "--quiet"
    Instance = vlc.Instance(opt)
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()

    timer = 5
    
    for s in range(5):   
        print('\r'+str(timedelta(seconds=s)), end='')
        sleep(1)
    
    while player.is_playing():
        print('\r'+str(timedelta(seconds=timer)), end='')
        timer +=1
        sleep(1)
    player.stop()

if 'list' in url:
    try:
        playlist_(pafy.get_playlist(url)) # Extracts playlist information and call the playlist function
    except(ValueError):
        print('The url is not right')
else:
    try:
        only_one(url)  # Call the one song function
    except(ValueError):
        print('The url is not right')
    
