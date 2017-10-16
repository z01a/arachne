import json

class SearchRequest(object):
	def __init__(self, settings = None, params = None):
		self.searchSettings = {
			"MainTypeGroup":"1",
			"Category":"1",
			"AdvancedSearchOpen":"false",
			"MailID":"",
			"PayType":"1",
			"Type":"1",
			"RoomsMin":"0",
			"RoomsMax":"0",
			"PriceMin":"0",
			"PriceMax":"0",
			"Regions":[],
			"SubTypes":["0"],
			"SizeMin":"0",
			"SizeMax":"0",
			"Available":"",
			"NoAgreement":"false",
			"FloorRange":"0",
			"RentalPeriod":"0",
			"equipmentgroups":[],
			"Email":"",
			"Interval":"0",
			"SubscriptionType1":"true",
			"SubscriptionType2":"true",
			"SubscriptionType4":"true",
			"SubscriptionType8":"true",
			"SubscriptionType128":"true",
			"SubscriptionType512":"true",
			"Sort":"0"
		}

		self.searchParams = {
			"manual":False,
			"skip":0,
			"reset":True,
			"position":0,
			"iframe":0,
			"defaultTitle":True,
			"saveSettings":True
		}

		self.searchRequest = None

		if settings is not None:
			for key in settings:
				if key in self.searchSettings:
					self.searchSettings[key] = settings[key]

		if params is not None:
			for key in params:
				if key in self.searchParams:
					self.searchParams[key] = params[key]

		self.searchRequest = self.searchParams
		self.searchRequest.update( { "settings" : self.searchSettings } )

	def toJson(self):
		return json.dumps(self.searchRequest)

	def format(self, _format = "dict"):

		returnData = {
			'dict' : self.searchRequest,
			'json' : json.dumps(self.searchRequest)
		}

		if _format in returnData:
			return returnData[_format]
		else:
			return None


	def __del__(self):
		pass

class SearchResponse(object):
	def __init__(self, response):
		self.searchResponse = response

	def format(self, _format = "dict"):

		returnData = {
			'dict' : self.searchResponse,
			'json' : json.dumps(self.searchResponse)
		}

		if _format in returnData:
			return returnData[_format]
		else:
			return None

	def __del__(self):
		pass