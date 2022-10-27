from bs4 import BeautifulSoup
import requests
import re
import logging
from urllib.parse import urljoin
logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class command:
    def __init__(self, urls=[]):
        self.urls = urls
    def execute(self):
        raise Exception('Overwrite this one pls')

class composite(command):
    def __init__(self,  urls=[]): 
        self.visited_urls = []
        self.urls_to_visit = urls


    def execute(self):
        print("antes"+str(self.urls_to_visit))
        self.urls_to_visit = self.urls_to_visit.rsplit(' ')
        print(self.urls_to_visit)
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:               
                crawl(url).execute()                
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                print("entre")
                print(self.visited_urls)
                print(url)
                self.visited_urls.append(url)
                print("link visitados"+str(self.visited_urls))    
        

class download_url(command):
    def execute(self):     
        print(self.urls)   
        result = requests.get(self.urls) #Enviar solicitud
        content = result.text #Obtener el texto del resultado en beautifulsoup
        return content

class get_linked_urls(command):
    def execute(self):
        print("HOLAAAA")
        content = download_url(self.urls).execute()
        soup = BeautifulSoup(content, 'html.parser')              
        for link in soup.find_all('a'):
            path = link.get('href')           
            print("HOLA"+path)
            if path and path.startswith('/'):                
                path = urljoin(self.urls, path)
                print("QUE ES"+ path)
            yield path

class add_url_to_visit(composite):
    def execute(self): 
        
        if self.urls_to_visit not in self.visited_urls and self.urls_to_visit not in self.urls_to_visit:
            print("por favor")
            print(self.urls_to_visit)

        '''
        if self.urls not in self.visited_urls and self.urls not in self.urls_to_visit:            
            self.urls_to_visit.append(self.urls)
            print("se agrego la url visit"+ str(self.urls_to_visit))
        '''
         

class crawl(command):
    def execute(self): 
        print(str(self.urls)+"Que tiene")                 
        for self.urls in get_linked_urls(self.urls).execute():
            add_url_to_visit(self.urls).execute()

if __name__ == '__main__':
    composite('https://service.uan.edu.co/mango/').execute()
