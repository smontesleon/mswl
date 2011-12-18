
import urllib2
user_agent = " Mozilla /5.0 ( X11; U; Linux x86_64 ; en -US) AppleWebKit /534.7 (KHTML , like Gecko ) Chrome/7.0.517.41 Safari /534.7"
_opener = urllib2 . build_opener ()
_opener . addheaders = [( 'User - agent', user_agent )]
#url="http://www.evernote.com"

from BeautifulSoup import BeautifulSoup as Soup
import argparse

def leerymostrarURl(url_actual, nivel_actual, espacios):   
 while nivel_actual <= niveles_a_leer:
  nivel_actual=nivel_actual+1
  raw_code = _opener . open ( url_actual). read ()
  soup_code = Soup ( raw_code )
  todos_los_links = [ link ['href'] for link in soup_code . findAll ('a')
   if link . has_key ('href')]
  for un_link in todos_los_links:
   print espacios+" "+un_link
   if un_link.startswith("http") | un_link.startswith("https"): 
    leerymostrarURl(un_link, nivel_actual, espacios+" ")

        
parser = argparse . ArgumentParser ( description = "Argumentos de mi crawler" )
parser . add_argument ( 'url' , nargs =1 ,help = 'URL de la que desea leer los links')
parser . add_argument ( '-n' ,'--numero-de-niveles' , type = int , default =1 , help = 'Niveles que el crawler debe leer')
argumentos = parser . parse_args()
url_a_leer = argumentos.url.pop()
niveles_a_leer=argumentos.numero_de_niveles

leerymostrarURl(url_a_leer,1," ")

"""
  
raw_code = _opener . open ( url_a_leer). read ()

soup_code = Soup ( raw_code )
links = [ link ['href'] for link
 in soup_code . findAll ('a')
 if link . has_key ('href')]

for link in links:
 print link
"""

