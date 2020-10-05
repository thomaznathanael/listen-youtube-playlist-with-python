import pafy # o pafy depende da biblioteca youtube_dl
import vlc  # python-vlc
from time import sleep
import keyboard
from colored import attr, fg
cyan = fg('cyan')
red = fg('red')
res = attr('reset')

url = "https://www.youtube.com/watch?v=duZR6GLM8Es&list=RDVFp_Y0kz6CY&index=7"
playlist = pafy.get_playlist(url) # Extrai as informações da playlist em formato de dicionário

for musica in playlist['items']:
    url_video = "https://www.youtube.com/watch?v=" + musica['playlist_meta']['encrypted_id'] # Extrai o link de cada vídeo da playlist
    video = pafy.new(url_video)
    audio = video.getbestaudio() # Extrai apenas o áudio de cada vídeo
    playurl = audio.url

    print(musica['playlist_meta']['title'] + f' - {red}' + musica['playlist_meta']['duration'] + f'{res}')

    # Abaixo temos a reprodução de mídia padrão da biblioteca python-vlc
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    sleep(3)
    while player.is_playing():
        key = keyboard.read_key() # Detecta a tecla pressionada
        if key == 'page up':
            print(f'{cyan}-next{res}')
            break
    player.stop()
    