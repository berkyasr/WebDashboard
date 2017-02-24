from ..component import Component

class clock(Component):
    def __init__(self, instance_id=""):
        Component.__init__(self, "Clock")
        self.instance_id = instance_id
            
    def execute(self):
        result = '<p><a href="/clock">---->>>>Go to clock<<<<---</a></p>'
        return result