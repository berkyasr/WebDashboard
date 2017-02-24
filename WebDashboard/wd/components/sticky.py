from ..component import Component

class sticky(Component):
    def __init__(self, instance_id="", stickyname=""):
        Component.__init__(self, "Gallery")
        self.instance_id = instance_id
        self.name = stickyname
        self.notes=[]
        
    def setName(self,name):
        """Sets name of the gallery"""
        self.name = name
    def getName(self):
        """Gets name of the gallery"""
        return self.name
    
    def addNote(self,text):
        """Adds a note"""
        self.notes.append(text)
    def getNotes(self):
        return self.notes
            
    def execute(self):
        result = '<p><a href="/' + self.instance_id + '">---->>>>Go to related stickies:' + self.name +'<<<<---</a></p>'
        return result