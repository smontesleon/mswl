
#licencia BSD

#Copyright <2011> <copyright SERGIO R. MONTES L.>. All rights reserved.

#Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

#    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

#    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

#THIS SOFTWARE IS PROVIDED BY <COPYRIGHT SERGIO R. MONTES L.> ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT SERGIO R. MONTES L.> OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#The views and conclusions contained in the software and documentation are those of the authors and should not be interpreted as representing official policies, either expressedor implied, of <copyright SERGIO R. MONTES L.>.


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

