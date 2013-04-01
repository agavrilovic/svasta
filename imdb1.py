import httplib
import json
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    marker=0
    projects=0
    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.marker=1
        if tag == "script":
            self.marker=0
    def handle_endtag(self, tag):
        if tag == "script":
            self.marker=1
    def handle_data(self, data):
        info = data.strip()
        if self.marker == 1:
            if "Details only on" in info:
                self.projects = 0
            if self.projects == 1 and info is not "":
                try:
                    val = float(info)
                except ValueError:
                    print info+",", 
            if "Projects In Development" in info:
                print "Nadolazeæi projekti:"
                self.projects = 1

print "Upisi ime glumca:"
name = raw_input().replace(' ', '+')
conn = httplib.HTTPConnection("www.imdb.com")
conn.request("GET","/xml/find?json=1&q="+name)
data = conn.getresponse().read()
conn.close()
info = json.JSONDecoder().decode(data).iteritems()
for key,val in info:
    if key == "name_popular":
        popular = val
IMDBaddress = popular[0]['id']
print IMDBaddress
conn = httplib.HTTPConnection("www.imdb.com")
conn.request("GET","/name/"+IMDBaddress+"/")
data = conn.getresponse().read()
conn.close()
parser = MyHTMLParser()
parser.feed(data)
print "i to je to."