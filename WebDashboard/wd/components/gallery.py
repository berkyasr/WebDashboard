from ..component import Component

class gallery(Component):
    def __init__(self, instance_id="", galleryname="", photos=[]):
        Component.__init__(self, "Gallery")
        self.instance_id = instance_id
        self.name = galleryname
        self.photos = photos
        self.currentPhoto = 0
        
    def setName(self,name):
        """Sets name of the gallery"""
        self.name = name
    def getName(self):
        """Gets name of the gallery"""
        return self.name
    def addPhoto(self,photoLink):
        """Adds given photo to the gallery"""
        self.photos.append(photoLink)
    def removePhoto(self,photoLink):
        """Removes given photo from the gallery if it is there"""
        try:
            self.photos.remove(photoLink)
        except:
            pass
    def nextPhoto(self):
        if (len(self.photos) == 0):
            return "<br><p>No added photos</p>"
        elif (self.currentPhoto == len(self.photos) - 1):
            self.currentPhoto = 0
            return self.photos[self.currentPhoto]
        else:
            self.currentPhoto += 1
            return self.photos[self.currentPhoto]
            
    def prevPhoto(self):
        if (len(self.photos) == 0):
            return "<br><p>No added photos</p>"
        elif (self.currentPhoto == 0):
            self.currentPhoto = len(self.photos) - 1 # covers the case when there is only one photo
            return self.photos[self.currentPhoto]
        else:
            self.currentPhoto -= 1
            return self.photos[self.currentPhoto]
            
    def execute(self):
        result = "<p>"
        result += '<h1>Gallery: {}</h1>'.format(self.getName())
        if (len(self.photos) == 0):
            result+= "<br><p>No added photos</p><br></p>"
            return result
        result += '''<br> <img src="''' + self.photos[self.currentPhoto] + '''" alt="Pic not found" style="width:128px;height:128px;">'''
        result += '<br><form method="POST" action="/gallerymove/{}/"><button name="option" value="prevPhoto" type="submit">Prev</button></form>'.format(self.instance_id)
        result += '<form method="POST" action="/gallerymove/{}/"><button name="option" value="nextPhoto" type="submit">Next</button></form>'.format(self.instance_id)
        result += "<br></p>"
        return result