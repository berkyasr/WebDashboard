from ..component import Component


class note(Component):
    def __init__(self, instance_id="", name=""):
        Component.__init__(self, "Gallery")
        self.instance_id = instance_id
        self.name = name
        self.list = []

    def setName(self, name):
        """Sets name of the note"""
        self.name = name

    def getName(self):
        """Gets name of the note"""
        return self.name

    def addElement(self,element):
        self.list += [element]

    def deleteElement(self,elementNo):
        del self.list[elementNo]
    #&#164;
    def execute(self):
        result = "<p>"
        result += '<h1>Note: {}</h1>'.format(self.getName())
        result += '<table>'
        for i,j in enumerate(self.list):
            result += '<tr><th>&nbsp;&nbsp;&nbsp;&nbsp;&#164;{}</th>'.format(j)
            result += '<th><form method="POST" action="/deleteelement/{}/{}/"><button name="option" type="submit">Delete</button></form></th></tr>'.format(self.instance_id,i)
        result += '</table>'
        return result