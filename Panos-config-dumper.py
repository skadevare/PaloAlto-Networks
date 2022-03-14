## PanOS config dumper!
##
##
import requests
from bs4 import BeautifulSoup as BS
import os.path
import datetime

# Firewall ip or FQDN
panfw = "192.168.1.1"
panapiport = "443"
# API username and password:
panapiuser = "apiuser"
panapipwd = ""
# Backup location Path!
path = 'x:/backup/panos/'

r = requests.get("https://" + panfw + ":" + panapiport +"/api/?type=keygen&user=" + panapiuser + "&password=" + panapipwd, verify=False)
#get the xml from http response
soup = BS(r.text,"lxml")
#get the key data from 
key = soup.find('key').text
 
#Get the config using PA expot config API
r = requests.get("https://" + panfw + "/api/?type=export&category=configuration&key={}".format(key), verify=False )
current_date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#define file name
filename = os.path.join(path, "config" + current_date + ".xml")
#Open a new file config.xml, as defined above
config = open(filename, "w")
#write the response to the config.xml, content must be in string so use r.text
config.write(r.text)
config.close()
