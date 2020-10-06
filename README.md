# Listen Youtube Playlist With Python
This is an example of how to listen music from a youtube playlist.

## Installation

Install the all dependencies:
```bash
pip install -r requirements.txt
```
ou:
```bash
pip3 install -r requirements.txt
```

intale o aplicativo VLC no seu sistema também

## Usage

You just need to replace the playlist url and open.

```python

...

url = "PUT_YOUR_YOUTUBE_PLAYLIST_URL_HERE"
playlist = pafy.get_playlist(url) # Extracts the playlist information

...

```
For the next song press the "Page Up" key on your keyboard ou em caso de falha da biblioteca você terá que apertar enter no terminal.(geralmente acontece no linux)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
