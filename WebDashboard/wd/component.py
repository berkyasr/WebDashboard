class Component(object):
    def __init__(self, descript=""):
        self.descript = descript
    
    def description(self):
        """Returns description of the component"""
        return self.descript
        
    def attributes(self):
        """Returns attributes of the component"""
        dirlist = self.__dict__
        mydict = {}
        for i in dirlist.keys():
            mydict[i] = type(dirlist[i]).__name__
            
        return mydict
        
    def __getitem__(self, key):
        if self.__dict__.has_key(key):
            return self.__dict__[key]
        else:
            raise KeyError(key)
        
    def __setitem__(self, key, value):
        if self.__dict__.has_key(key):
            self.__dict__[key] = value
        else:
            raise KeyError(key)
            
    
    def methods(self):
        """Returns methods of components"""
        return  [(func,getattr(self, func).__doc__) for func in dir(self) if callable(getattr(self, func)) and func[0]!='_']

    def execute(self):
        """Basic behaviour of components"""
        raise NotImplementedError
