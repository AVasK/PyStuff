class ListInstance:
    def __str__(self):
        return f'<Instance of {self.__class__.__name__}, address: {id(self)}>\n{self.__attrnames()}'
    
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += f'\tattr: {attr} = {self.__dict__[attr]}\n'
        return result
    
class Spam(ListInstance):
    def __init__(self):
        self.data1 = 'food'
        self.data2 = True
        
    def __str__(self):
        return ListInstance.__str__(self) + "\nOVERLOADED..."
        
        
x = Spam()
print(x)