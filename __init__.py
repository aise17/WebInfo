from web_info import WebInfo
from web_info_target import WebInfoTarget

from alexa_rank import AlexaRank
from platform_analyzer import Analyzer
from search_contact import SearchContact
from search_language import SearchLanguage
from status import Status
from manager import Manager


def main():
	manager = Manager()
	manager.imports()
	count = 1
	if count >= 5:
		manager.open_book_writer()
	else:
		manager.open_book_append()
	
	for urls in manager.urls_list:
		for url in urls:
			print count
			count += 1
			manager.resultados = {'url': '','alexa': '', 'status': '', 'platform': '', 'language': '', 'mail': ['']}

		#ALEXA RANK
			alexa_rank = AlexaRank(url)
			result_alexarank = alexa_rank.get_result()
			
			print result_alexarank
			manager.resultados['alexa'] = result_alexarank

			print manager.resultados
		

		#STATUS
			status = Status(url)
			rstatus = status.get_result()
			print rstatus
			manager.resultados['url'] = status.resource_url
			manager.resultados['status'] = rstatus


			print manager.resultados



			if rstatus == 200: 

			#PLATFORM ANALYZER
				analyzer = Analyzer(url)
				result_analyzer = analyzer.analyze()
				print result_analyzer
				manager.resultados['platform'] = result_analyzer


				print manager.resultados


			#SEARCH LANGUAGE USE IN THE WEB
				search_lang = SearchLanguage(url)
				result_lang = search_lang.get_result()
				print result_lang
				try:
					manager.resultados['language'] = result_lang['lang'] 
				except KeyError:
					try:
						manager.resultados['language'] = result_lang['xml:lang'] 
					except:
						manager.resultados['language'] = result_lang					
					
				



				print manager.resultados


			# SEARCH ITEMS OF CONTACT
				search_contact = SearchContact(url)
				search_contact.get_result()
				print search_contact.resource_url
				for mail in search_contact.mail_result:
					if mail not in manager.resultados['mail']:
						manager.resultados['mail'].append(mail)
				join = ','
				manager.resultados['mail'] = join.join(manager.resultados['mail'])
				print manager.resultados
				


			manager.export()
			del manager.resultados


if __name__ == '__main__':
	main()