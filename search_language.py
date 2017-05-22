from web_info_target import WebInfoTarget
from bs4 import BeautifulSoup


class SearchLanguage(WebInfoTarget):
	def __init__(self, site_url):
		super(SearchLanguage,self).__init__(site_url)



	def get_result(self):
		'''
		scraping a web for extraction a lang
		Args:
			soup(string): this variable contains the organized mark language
		'''
		for lang in self.soup.findAll('html'):
			return lang.attrs 
		
'''
search = SearchLanguage('comprarseguridad.es')

res = search.get_result()

print res'''