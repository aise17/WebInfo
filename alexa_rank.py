from bs4 import BeautifulSoup
from web_info import WebInfo

class AlexaRank(WebInfo):
	''' information of number of alexa ranck  '''
	def __init__(self, site_url):
		super(AlexaRank,self).__init__(site_url)
		self.soup = BeautifulSoup(self.response.text, "html.parser")

	def get_resource_url(self):
		'''
		allow build a url whit alexa rank search uri
		Args:
			baseUrl(string): contains alexa perfix for search 
			finalUrl(string): contains alexa suffix for search 
		'''
		baseUrl = 'http://www.alexa.com/siteinfo/'
		finalUrl = '#linksin'

		url_alexa = baseUrl + self.site_url + finalUrl
		return url_alexa

	def get_result(self):
		'''
		scraping a web for extraction a number of alexa rank
		Args:
			soup(string): this variable contains the organized mark language
			result_AlexaRank(int): in the alexaranking number
		'''
		
		for span in self.soup.find_all('span',{'class':'globleRank'}):  
			for strong in span.find_all('strong', {'class': 'metrics-data align-vmiddle'}):  

				result_AlexaRank = strong.text
				result_AlexaRank = result_AlexaRank.strip(' ')
				result_AlexaRank = result_AlexaRank.strip('\n')
				return result_AlexaRank    





alexa_rank = AlexaRank('disfraces.tienda')

result_alexarank = alexa_rank.get_result()

print result_alexarank