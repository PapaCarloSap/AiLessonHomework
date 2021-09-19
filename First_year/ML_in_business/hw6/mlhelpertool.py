

class AttributeNamesManager:

    def __init__(self, numeric:list, category:list, target:str):
        self.__numeric = numeric
        self.__category = category
        self.__target = target

    @property
    def Numerics(self)->list:
        return self.__numeric

    @property
    def Categories(self)->list:
        return self.__category

    @property
    def Features(self)->list:
        return self.__category + self.__numeric

    @property
    def Target(self)->str:
        return self.__target