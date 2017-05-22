from bs4 import BeautifulSoup
import requests
from web_info_target import WebInfoTarget

class Status(WebInfoTarget):
	''' information of web status  '''
	def __init__(self , site_url):
		super(Status,self).__init__(site_url)

	

	def get_result(self):
		'''
		this fuction , show to status code of the get web 

		Args:
			status(int): this variable stores the state of the web
		'''
		status = self.response.status_code

		return status


	
'''
p = Status("comprarseguridad.es")
print p.get_result()

'''