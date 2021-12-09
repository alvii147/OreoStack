import os
import sys
import re
import json

OREOSTACK_LOGO_PATH = '../../img/oreostacklogo.png'

SERIES_TITLE = 'Selected Chords'
MD_FILENAME = 'SelectedChords.md'
LOGO_WIDTH = 60
SHIELDS = {
    'youtube': 'https://img.shields.io/badge/YouTube-ff0000?style=flat&logo=youtube',
    'spotify': 'https://img.shields.io/badge/Spotify-000000?style=flat&logo=spotify',
}
COVER_WIDTH = 400
NUMS_TO_WORDS = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'keycap_ten',
}

def readJSON(filename):
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)

    return data

def generateHTML_img(src, width=None):
    tag = f'<img src="{src}" '
    if width is not None:
        tag += f'width="{width}" '

    tag += '/>'

    return tag

def processArticle(dirname, year):
    tunes = readJSON(dirname + '/tunes.json')

    with open(dirname + '/' + MD_FILENAME, 'w') as mdfile:
        mdfile.write('# ' + generateHTML_img(OREOSTACK_LOGO_PATH, width=LOGO_WIDTH) + SERIES_TITLE + ' ' + year + '\n\n')

        tunes = sorted(tunes, key=lambda tune: int(tune['rank']))

        for i, tune in enumerate(tunes):
            rank = NUMS_TO_WORDS[tune['rank']]
            title = tune['title']
            artist = tune['artist']
            album_cover = tune['album_cover']
            links = tune['links']

            mdfile.write(f'## :{rank}: {title}\n\n')
            mdfile.write(f'**{artist}**\n\n')
            mdfile.write(generateHTML_img(album_cover, width=COVER_WIDTH) + '\n\n')

            for (platform, link) in links.items():
                shield = SHIELDS[platform]
                mdfile.write(f'[![]({shield})]({link})\n')

            if i < len(tunes) - 1:
                mdfile.write('\n---\n\n')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError('Expected at least one command-line argument')

    if sys.argv[1] == '__all__':
        for dirname in filter(os.path.isdir, os.listdir('.')):
            year = re.match(r'^[A-Za-z]+([0-9]+)\S*$', dirname).group(1)
            processArticle(dirname, year)
    else:
        dirname = sys.argv[1]
        year = re.match(r'^[A-Za-z]+([0-9]+)\S*$', dirname).group(1)
        processArticle(dirname, year)