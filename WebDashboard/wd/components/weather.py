import requests
import json
import pprint
import time

from ..component import Component

class weather(Component):
    def __init__(self,instance_id = "",  loc = ""):
        Component.__init__(self,"Weather Component")
        """self.API_KEY = 'd9cecb4627cc68580722428e741356ec'
        self.loc = loc or self._getLocation()['city']
        self.instance_id = instance_id
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}'.format(self.loc, self.API_KEY))

        try:
            json.loads(r.text)
        except ValueError:
            raise KeyError("Invalid Location Parameter")"""

    def _getLocation(self):
        """send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        return json.loads(r.text)"""
        
    def setLocation(self,loc):
        """Sets location"""
        """self.loc = loc
        
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}'.format(self.loc, self.API_KEY))

        try:
            json.loads(r.text)
        except ValueError:
            raise KeyError("Invalid Location Parameter")"""

    def weatherNow(self):
        """Returns weather information of current weather for location"""
        """result = ""
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}'.format(self.loc,self.API_KEY))
        x = json.loads(r.text)
        result += "<br>Weather information for " + x['name'] + ", " + x['sys']['country'] + ":"
        result += "<br>&nbsp;    State: " + x['weather'][0]['description'].capitalize()
        result += "<br>&nbsp;    Temperature: " + str(x['main']['temp'])
        return result"""

    def weatherForecast(self, n = 7):
        """Returns weather forecasts for location"""
        """r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?q={}&units=metric&APPID={}'.format(self.loc,self.API_KEY))
        x = json.loads(r.text)
        a = x['list']
        result = ""
        result += "<br>Weather information for " + x['city']['name'] + ", " + x['city']['country'] + " for next {} days:".format(n)

        for i in range(0,n,1):
            result += "<br>" + str(time.strftime("%a, %d %b %Y", time.gmtime(a[i]['dt'])))
            result += "<br>&nbsp;    State: " + a[i]['weather'][0]['description'].capitalize()
            result += "<br>&nbsp;    Day Temperature: " + str(a[i]['temp']['day'])
            result += "<br>&nbsp;    Night Temperature: " + str(a[i]['temp']['night'])
        return result"""


    def execute(self):
        """Basic behaviour of components"""
        """result =""
        result += "<br>" + self.weatherNow() + "<br>"
        result += "<br>" + self.weatherForecast()
        return str(result)"""
