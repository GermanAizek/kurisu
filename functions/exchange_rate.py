#!/usr/bin/python3

from kurisu_utils import *

keywords_start = [
	"курс",
	"меня интересует курс",
	"скажи курс"
]

keywords_response = {
	"Ты хочешь узнать валютный курс чего?" : "Ты хочешь узнать валютный курс чего?",
	"Я вас поняла" : "Я вас поняла"
}

def dialog(record, engine):
	print(keywords_response["Ты хочешь узнать валютный курс чего?"])
	#engine.say(exchange_res["Ты хочешь узнать валютный курс чего?"])
	if get_words(record) == keywords_request["курс"]:
		#continue
		print(keywords_response["Я вас поняла"])
	elif get_words(record) == keywords_request["проехали"]:
		print(keywords_response["Я вас поняла"])