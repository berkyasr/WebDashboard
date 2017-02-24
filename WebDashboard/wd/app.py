import pkgutil
import importlib
import dill
import os

import components


class Application(object):
    def __init__(self, grid_size = 20):
        self.components_package = components
        self.loaded_comps = {}
        self.id_counter = 1
        self.grid = [[0]*grid_size for i in range(grid_size)]
        self.current_instances = {}

    def available(self):
        return [name for _, name, _ in pkgutil.iter_modules(self.components_package.__path__)]

    def loaded(self):
        return self.loaded_comps

    def load(self,module_name):
        if module_name not in self.available() :
            raise Exception("Module you're trying to import is not available")

        if (self.loaded_comps.has_key(module_name)) :
            return
        else :
            mymodule = importlib.import_module(".components." + module_name, 'wd')
            myclass = getattr(mymodule,module_name)
            myinstance = myclass()
            self.loaded_comps[module_name] = myinstance.description()

    def loadDesign(self, filename):
        with open("wd/saveddesigns/" + filename +".pkl", "rb") as myfile:
            temp = dill.load(myfile)
            self.__dict__.update(temp.__dict__)
            
    def loadableDesigns(self):
        result = []
        for _,_,files in os.walk("./wd/saveddesigns"):
            for afile in files:
                if afile[-4:] == ".pkl":
                    result.append(afile[:-4])
        return result

    def saveDesign(self, filename):
        with open("wd/saveddesigns/" + filename + ".pkl", "wb") as myfile:
            dill.dump(self,myfile)
            
    def addInstance(self,componentname,x,y):
        instance_id = componentname + str(self.id_counter)

        if self.loaded_comps.has_key(componentname):
            mymodule = importlib.import_module(".components." + componentname, 'wd')
            myclass = getattr(mymodule , componentname)
            myinstance = myclass(instance_id)
            if self.grid[y][x] == 0:
                self.grid[y][x] = myinstance
                self.current_instances[instance_id] = (componentname,x,y)
                self.id_counter += 1
                return instance_id
            else:
                raise Exception("The position you are trying to insert a component to is already occupied")

        else:
            raise Exception("There doesn't exist such a component")
        

    def instances(self):
        return self.current_instances

    def removeInstance(self, instance_id):
        if self.current_instances.has_key(instance_id):
            instance = self.current_instances[instance_id]
            x_value, y_value = instance[1], instance[2]
            self.grid[y_value][x_value] = 0
            del self.current_instances[instance_id]
        else :
            raise Exception("You can't remove a non-existing instance")

    def callMethod(self,instance_id,methodname,params=[]):
        instance = self.current_instances[instance_id]
        instance_x, instance_y = instance[1], instance[2]
        myinstance = self.grid[instance_y][instance_x]
        return getattr(myinstance,methodname)(*params)
        
    def execute(self):
        result =""
        result += "\n-------------------------------"
        for key, _ in self.current_instances.iteritems():
            result += "\n" + self.callMethod(key,"execute",[])
            result += "\n\n-------------------------------"
        return result
