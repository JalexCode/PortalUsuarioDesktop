class DataEU:
    def __init__(self, id, url, descrip) -> None:
        self.__id = id
        self.__url = url
        self.__descrip = descrip
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value
        
    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self, value):
        self.__url = value
        
    @property
    def descrip(self):
        return self.__descrip
    
    @descrip.setter
    def descrip(self, value):
        self.__descrip = value