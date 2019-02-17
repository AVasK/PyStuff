def toint(f):
    def newf(*a):
        a = list(map(lambda x: x if type(x) != float else int(x), a))
        res = f(*a)
        if type(res) == float:
            res = int(res)
        return res
    return newf

if __name__ == '__main__':
    @toint
    def root(x, y, z):
        return x**0.5
    
    print(root(11.8, 33, 11.8))