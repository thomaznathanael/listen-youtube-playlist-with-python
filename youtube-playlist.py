import pafy
import vlc
from time import sleep
import keyboard
from colored import attr, fg, bg
cyan = fg('cyan')
red = fg('red')
res = attr('reset')
black = fg('black')
bg_y = bg('yellow')

url = "PUT_YOUR_YOUTUBE_PLAYLIST_URL_HERE"

def playlist_(playlist):
    print(f'{bg_y}{black} Playlist {res}')
    for music in playlist['items']:
        url_video = music['playlist_meta']['encrypted_id'] # Extracts the url from the videos
        video = pafy.new(url_video)
        audio = video.getbestaudio() # Extracts only the audio from the videos
        playurl = audio.url

        print(music['playlist_meta']['title'] + f' - {red}' + music['playlist_meta']['duration'] + f'{res}')

        # Below is the standard media reproduction of the python-vlc library
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()
        sleep(3)
        while player.is_playing():
            key = keyboard.read_key() # Detects the pressed key
            if key == 'page up':
                print(f'{cyan}-next{res}')
                break
        player.stop()


def only_one(url_video):
    video = pafy.new(url_video)
    audio = video.getbestaudio() # Extracts only the audio from the videos
    playurl = audio.url
    print(f'{bg_y}{black} Single {res}')

    #print(music['playlist_meta']['title'] + f' - {red}' + music['playlist_meta']['duration'] + f'{res}')

    # Below is the standard media reproduction of the python-vlc library
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    sleep(3)
    while player.is_playing():
        pass
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

    
