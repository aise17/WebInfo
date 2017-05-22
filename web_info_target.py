from web_info import WebInfo 


class WebInfoTarget(WebInfo):
	def __init__(self, site_url):
		super(WebInfoTarget,self).__init__(site_url)


	def get_resource_url(self):
		'''
		in  this fuction, become the url without protocol in a url with protocol 

		Args :
			site_url(string): pure url without protocol
			resource_url(string) is a build url with ethernet protocol  
		'''
		if (self.site_url[:7]) == 'http://':

			print('URL corecta')    
			return self.site_url                    # comprobamos que las primeras letras de la url del 0 - 7 sea igual a " 'http:// "

		else:
			print (' URL corregida')
			self.resource_url = ('http://'+ self.site_url)

			return self.resource_url
	









