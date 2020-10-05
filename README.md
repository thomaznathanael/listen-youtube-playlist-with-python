# Listen-youtube-playlist-with-python
This is an example of how to listen music from a youtube playlist.

## Installation

Install the all dependencies

The dependency of pafy:
```bash
pip install youtube_dl
```
The pafy module:
```bash
pip install pafy
```
The vlc module:
```bash
pip install python-vlc
```
The keyboard module for keys detection:
```bash
pip install keyboard
```
The colored module:
```bash
pip install colored
```

## Usage

You just need to replace the playlist url and open.

```python

...

url = "PUT_YOUR_YOUTUBE_PLAYLIST_URL_HERE"
playlist = pafy.get_playlist(url) # Extracts the playlist information

...

```
For the next song press the "Page Up" key on your keyboard.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
