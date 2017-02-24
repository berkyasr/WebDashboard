from ..component import Component

class poll(Component):
    def __init__(self, instance_id="", pollName="", creatorName="", options={}):
        Component.__init__(self,"Poll")
        self.instance_id = instance_id
        self.name = pollName
        self.creator = creatorName
        self.options = options

    def setCreator(self, creator):
        """Sets creator of the poll"""
        self.creator = creator

    def getCreator(self):
        """Returns creator of the poll"""
        return self.creator

    def setName(self,name):
        """Sets name of the poll"""
        self.name = name

    def getName(self):
        """Returns name of the poll"""
        return self.name

    def addOption(self, option):
        """Adds a new option to the poll"""
        if option.endswith("/r"):
            option = option[:-2]
        self.options[option] = 0

    def deleteOption(self, option):
        """Deletes an option from the poll"""
        del self.options[option]

    def vote(self, option):
        """Gives a vote for an option"""
        self.options[option] += 1


    def execute(self):
        result = ""
        result += "<br>Votes for poll '{}' created by {}:".format(self.name,self.creator) + "<table>"
        for i, key in enumerate(sorted(self.options, key=self.options.get, reverse=True)):
            result += "<br><tr><th>" + str(i+1) + ': ' + str(key) + ' --> ' + str(self.options[key]) +'</th><th><form method="POST" action="/votepoll/{}/{}/"><button type="submit">Vote</button></form>'.format(self.instance_id,key) + '</th></tr>'
        result += "</table>"
        return result
