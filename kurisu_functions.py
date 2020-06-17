#!/usr/bin/python3

from functions.exchange_rate import keywords_start as exchange_start
from functions.exchange_rate import keywords_response as exchange_res
from functions.exchange_rate import dialog as exchange_dialog

from functions.sound import keywords_start as sound_start
from functions.sound import keywords_response as sound_res
from functions.sound import play_from_url as sound_play_url

from kurisu_utils import *

from threading import Thread

stay_home = False

def commander_start(record):
	global stay_home
	if not stay_home:
		addreses, names = get_near_devices()
		for name in names:
			if name == "Coconut451":
				for addr in addreses:
					if addr == "74:04:2B:4E:25:F3":
						stay_home = True
						print("С возращением дорогой.")
						thread_play = Thread(target=sound_play_url , args=((record, engine, "https://storage.lightaudio.ru/39976010/2ea34344/Michael%20McCann%20%E2%80%94%20Home.mp3")))
						thread_play.start()
			
	if get_words(record) == "курс": # exchange_start перечисление всех подходящих слов с курсом для начала диалога
		exchange_dialog(record, engine)
	elif get_words(record) == "подключи": # какие устройства есть рядом
		name, addr = get_near_devices()
		connect_to_device(name, addr)
	else:
		print(get_words(record))
		print("Я не знаю такой команды")