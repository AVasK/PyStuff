class we:
    count = 0
    
    def __init__(self):
        we.count += 1
        
    def __del__(self):
        we.count -= 1
        
    