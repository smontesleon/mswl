
import urllib2
user_agent = " Mozilla /5.0 ( X11; U; Linux x86_64 ; en -US) AppleWebKit /534.7 (KHTML , like Gecko ) Chrome/7.0.517.41 Safari /534.7"
_opener = urllib2 . build_opener ()
_opener . addheaders = [( 'User - agent', user_agent )]
url="http://www.evernote.com"
raw_code = _opener . open ( url). read ()

from BeautifulSoup import BeautifulSoup as Soup
soup_code = Soup ( raw_code )
links = [ link ['href'] for link
 in soup_code . findAll ('a')
 if link . has_key ('href')]

for link in links:
 print link