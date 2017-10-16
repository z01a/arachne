import Config,Protocol

class Arachne(object):
	Name = "Arachne"
	Version = "v1.0.0"
	Author = "5a6f4c41"

	SearchInterface = "http://www.urbanhome.ch/Search/DoSearch"

	@staticmethod
	def Main():
		print("Welcome to Arachne!!!")
		myConfig = Config.SearchRequest(settings = {"regions" : ["188542"]}, params = {"skip" : 0, "position" : 200})

		myResponse = Protocol.Gateway.Send(myConfig)
		print(myResponse.format('dict')['Rows']) # I just need to parse this and fill JSON structure