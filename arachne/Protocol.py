import requests,json

import Arachne,Config

class Gateway(object):
	def __init__(self):
		pass

	@staticmethod
	def Send(searchRequest = Config.SearchRequest()):
		response = requests.post(Arachne.Arachne.SearchInterface, data = searchRequest.toJson(), headers = {'Content-type' : 'application/json'})

		return Config.SearchResponse(json.loads(response.text))

	def __del__(self):
		pass