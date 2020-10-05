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

And you just need to replace the playlist url and open.

```python
...
url = "https://www.youtube.com/watch?v=EiXFGW75D-8&list=PL0GC85adzsKqVFXGKntt-KB5dHskW5Gp7"
playlist = pafy.get_playlist(url) # Extrai as informações da playlist em formato de dicionário
...
```
To next the music press the key "Page Up" from your keyboard.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
