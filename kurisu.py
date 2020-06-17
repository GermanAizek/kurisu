#!/usr/bin/python3

import os

if not os.path.exists("models/model-ru"):
	print ("Please download the model from https://github.com/alphacep/kaldi-android-demo/releases and unpack as 'model-ru' in the current folder.")
	exit (1)
from kurisu_functions import *
from vosk import Model, KaldiRecognizer
import requests
import pyaudio
import sys
import wave

	#elif 'курс биткоин' in zadanie:
		#response = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/")
		#response_json = response.json()
		#talk(response_json[0]['price_usd'].split('.')[0] + " долларов")
	#elif 'погода питер' in zadanie:
		#res = requests.get("http://api.openweathermap.org/data/2.5/find?q=Petersburg,RU&type=like&APPID=f98abe5235a919f50fc6536fbaa383ca")
		#data = res.json()
		#cities = ["{} ({})".format(d['name'], d['sys']['country'])
		#		for d in data['list']]
		#print( "city:", cities )
	#elif 'имя' in zadanie:
		#talk("Меня зовут Курису.")

if __name__ == "__main__":
	model = Model("models/model-ru")
	rec = KaldiRecognizer(model, 16000)
	
	p = pyaudio.PyAudio()
	stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
	stream.start_stream()

	while True:
		data = stream.read(4000)
		if len(data) == 0:
			break
		if rec.AcceptWaveform(data):
			commander_start(rec)
		#else:
			#print(rec.PartialResult())

	#print(rec.FinalResult())