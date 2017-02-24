from ..component import Component
import time


class mblog(Component):
    def __init__(self, instance_id="", name="", topic=""):
        Component.__init__(self, "Micro Blog Component")
        self.topic = topic
        self.instance_id = instance_id
        self.owner = name
        self.entries = []

    def getWriterName(self):
        """Returns writer of the Micro Blog"""
        return self.owner

    def setWriterName(self, name):
        """Sets writer name as parameter"""
        self.owner = name

    def getTopic(self):
        """Returns writer of the Micro Blog"""
        return self.topic

    def setTopic(self, name):
        """Sets writer name as parameter"""
        self.topic = name
    def getInstanceId(self):
        """Returns InstanceId"""
        return self.instance_id

    def getEntries(self):
        """Returns entries in Micro Blog"""
        return [x.getText() for x in self.entries]

    def saveEntry(self, writer, text):
        """Saves entry written by Micro Blog writer"""
        self.entries.append(Entry(writer,text))

    def like(self, entryid):
        """Increases like count of entry by one"""
        self.entries[entryid].like()

    def dislike(self, entryid):
        """Increases dislike count by one"""
        self.entries[entryid].dislike()

    def execute(self):
        """Basic behaviour of components"""

        result = "<p><table>"
        len = self.entries.__len__()
        result += '<h1>{} by {}</h1>'.format(self.getTopic(), self.getWriterName())
        for j,i in enumerate(self.entries):
            result += '<tr><th rowspan="2">{}</th><td>{}</td></tr><tr><td>{}&nbsp;&nbsp;&nbsp;&nbsp;Likes:{}&nbsp;&nbsp;Dislikes:{}</td></tr>'.format(i.getWriter(), i.getText(), i.getPosttime(), i.getLikes(), i.getDislikes())
            result += '<tr><th><form method="POST" action="/likedislike/{}/{}/"><button name="option" value="like" type="submit">Like</button></form></th><th><form method="POST" action="/likedislike/{}/{}/"><button name="option" value="dislike" type="submit">Dislike</button></form></th></tr>'.format(self.instance_id,j,self.instance_id,j)
        return result + '</table>'


class Entry(object):
    def __init__(self, writer,text):
        self.writer = writer
        self.txt = text
        self.likes = 0
        self.dislikes = 0
        self.time = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

    def getText(self):
        return self.txt

    def setWriter(self, writer):
        self.writer = writer

    def getWriter(self):
        return self.writer

    def getLikes(self):
        return self.likes

    def getDislikes(self):
        return self.dislikes

    def getPosttime(self):
        return self.time

    def like(self):
        self.likes += 1

    def dislike(self):
        self.dislikes += 1
