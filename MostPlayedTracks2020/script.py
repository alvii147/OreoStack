import os
import json

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
MAIN_LOGO_PATH = '../img/oreostacklogo.png'
MAIN_TITLE = 'My Most Played Tracks'
JSON_FILENAME = 'tracks.json'
MD_FILENAME = 'index.md'
LOGO_WIDTH = 60
SHIELDS = {
    'youtube': 'https://img.shields.io/badge/YouTube-ff0000?style=flat&logo=youtube',
    'spotify': 'https://img.shields.io/badge/Spotify-000000?style=flat&logo=spotify',
}
COVER_WIDTH = 400

def generate_img(src, width=None):
    tag = f'<img src="{src}" '
    if width is not None:
        tag += f'width="{width}" '

    tag += '/>'

    return tag

def generate_md(year):
    with open(f'{SCRIPT_PATH}/{JSON_FILENAME}', 'r') as jsonfile:
        tracks = json.load(jsonfile)

    with open(f'{SCRIPT_PATH}/{MD_FILENAME}', 'w') as mdfile:
        mdfile.write(f'# {generate_img(MAIN_LOGO_PATH, width=LOGO_WIDTH)} {MAIN_TITLE} {str(year)} \n\n')

        for i, track in enumerate(tracks):
            rank = i + 1
            title = track['title']
            artist = track['artist']
            album_cover = track['album_cover']
            links = track['links']

            mdfile.write(f'## {rank}. {title}\n\n')
            mdfile.write(f'**{artist}**\n\n')
            mdfile.write(generate_img(album_cover, width=COVER_WIDTH) + '\n\n')

            for (platform, link) in links.items():
                shield = SHIELDS[platform]
                mdfile.write(f'[![]({shield})]({link})\n')

            if i < len(tracks) - 1:
                mdfile.write('\n---\n\n')

if __name__ == '__main__':
    generate_md(2020)
