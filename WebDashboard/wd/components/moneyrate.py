from ..component import Component
import requests
import json
import pprint
class moneyrate(Component):
    def __init__(self,instance_id=""):
        Component.__init__(self)
        self.base = 'TRY'
        self.date = 'latest'
        self.istance_id = instance_id

    def setBase(self, base):
        """Set the base currency that you want to get the rates of.'TRY' by default"""
        self.base = base

    def _getrates(self):
        """Gets rates of the base currency"""
        r = requests.get('http://api.fixer.io/{}?base={}'.format(self.date, self.base))
        #pprint.pprint(json.loads(r.text))
        return json.loads(r.text)

    def change(self, first, second, amount):
        """Converts given amount of currency to another"""
        r = requests.get('http://api.fixer.io/{}?base={}'.format(self.date, first))
        x = json.loads(r.text)
        return x['rates'][second]*amount

    def execute(self):
        """Basic behaviour of components"""
        x = self._getrates()
        result ="<br><p>"
        result += '<br>Exchange rates for ' + str(x['base']) + ':'
        for key in x['rates']:
            result += "<br>&nbsp;    " + str(key) + ": " + str(x['rates'][key])
        return result + "<br></p>"
