
import requests
from bs4 import BeautifulSoup

class WebInfo(object):

	def __init__(self, site_url):
		'''
		this class is a constructor
		Args:
			urls_list(list) : is a list that contains all urls
			site_url(string): pure url without protocol
			resource_url(string) is a build url with protocol ethernet 
			response: it a variavle of contains the download web (metas, head, body, status, etc)
		'''
		self.urls_list = ['youtube.com', 'facebook.com', 'twiter.com', 'microsoft.com']
		self.site_url = site_url
		self.resource_url = self.get_resource_url().strip(' ')
		self.response = requests.get(self.resource_url,
			allow_redirects=True,
			verify=True,
			stream=True)
		self.soup = BeautifulSoup(self.response.text, "html.parser")
		
		self.resultados = []
		
		
	def get_resource_url(self):
		raise NotImplementedError
	def get_result(self):
		raise NotImplementedError