#!/usr/bin/python3

from kurisu_utils import *

from urllib.request import urlopen
from pydub import AudioSegment
from pydub.playback import play

keywords_start = [
	"курс",
	"меня интересует курс",
	"скажи курс"
]

keywords_response = {
	"Ты хочешь узнать валютный курс чего?" : "Ты хочешь узнать валютный курс чего?",
	"Я вас поняла" : "Я вас поняла"
}

def play_from_url(record, engine, url):
	mp3file = urlopen(url)
	with open("./user_cache/music/" + url.split('/')[-1], 'wb') as output:
		output.write(mp3file.read())

	song = AudioSegment.from_mp3("./user_cache/music/" + url.split('/')[-1])
	play(song)