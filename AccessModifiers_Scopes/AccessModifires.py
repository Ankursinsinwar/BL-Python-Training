class Public_class:

    static_Variable = 20

    def __init__(self, Public_Variable, WeakPrivate_Variable, Private_Variable):
        self.Public_Variable = Public_Variable
        self._WeakPrivate_Variable = WeakPrivate_Variable
        self.__Private_Variable = Private_Variable


    def public_Func(self):
        return self.__Private_Variable

    def _WeakPrivate_Func(self):
        return self._WeakPrivate_Variable



pc = Public_class(1,2,3)
print(Public_class.static_Variable)
print(pc.Public_Variable)
print(pc.public_Func())
print(pc._WeakPrivate_Func())
