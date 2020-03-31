import requests
from bs4 import BeautifulSoup

class TwitterFolowers(object):
    def __init__(self,url):
        self.url = url
    
    def check_response_status(self):
        """ check if the http response """
        r = requests.get(self.url)
        if r.status_code == 200:
            return True
        else :
            return False
    
    def get_html_content(self):
        """ get the html content from url"""
        if self.check_response_status():
            content = requests.get(self.url).content
            return content
        else:
            raise Exception("Problem in connection to the endpoint")
    
    def get_folowers(self):
        content = self.get_html_content()
        soup = BeautifulSoup(content, 'html.parser')
        href = "/" + self.url.split("/")[-1] + "/followers"
        link = soup.findAll("a", {"href" : href})
        output = link[0]['title']
        return output

if __name__ == '__main__' :
    t = TwitterFolowers("https://twitter.com/KMbappe")
    print(t.get_folowers())


    