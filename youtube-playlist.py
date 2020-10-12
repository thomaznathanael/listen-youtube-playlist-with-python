import pafy
import vlc
from time import sleep
from pynput import keyboard
from datetime import timedelta
import threading
from colored import attr, fg, bg

cyan = fg('cyan')
red = fg('red')
res = attr('reset')
black = fg('black')
bg_y = bg('yellow')

url = "PUT_YOUR_YOUTUBE_PLAYLIST_URL_HERE"

def on_press(k):
    global key
    key = str(k)


def listen_key():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


t = threading.Thread(target=listen_key)
t.start()


def playlist_(playlist):
    global key

    print(f'{bg_y}{black} Playlist {res}')
    v=0
    while True:     
        url_video = playlist['items'][v]['playlist_meta']['encrypted_id'] # Extracts the url from the videos
        try:
            video = pafy.new(url_video)
        except(IOError):
            print('There was an error playing this song (Youtube Error)')
            print(f'{cyan}-next         {res}')
            v+=1 
            continue

        audio = video.getbestaudio() # Extracts only the audio from the videos
        playurl = audio.url

        print('\r'+video.title + f' - {red}' + video.duration + f'{res}')

        # Below is the standard media reproduction of the python-vlc library
        Instance = vlc.Instance("--quiet")
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        timer = 5
        key = ''

        for s in range(5):   
            print('\r'+str(timedelta(seconds=s)), end='')
            if key == 'Key.page_up' or key == 'Key.page_down':
                break
            sleep(1)

        if key == 'Key.page_up':
            print(f'\r{cyan}-next         {res}')
            v+=1
            player.stop()
            continue

        if key == 'Key.page_down':
            print(f'\r{cyan}-prev         {res}')
            v-=1
            player.stop()
            continue
        
        while player.is_playing() and timer < video.length:
            print('\r'+str(timedelta(seconds=timer)), end='')
            timer +=1
            sleep(1)
 
            if key == 'Key.page_up':
                print(f'\r{cyan}-next         {res}')
                break
            if key == 'Key.page_down':
                print(f'\r{cyan}-prev         {res}')
                v-=2
                break
        v+=1
        player.stop()


def only_one(url_video):
    video = pafy.new(url_video)
    audio = video.getbestaudio() # Extracts only the audio from the videos
    playurl = audio.url
    print(f'{bg_y}{black} Single {res}')

    print('\n\r'+video.title + f' - {red}' + video.duration + f'{res}')

    # Below is the standard media reproduction of the python-vlc library
    Instance = vlc.Instance("--quiet")
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
    
