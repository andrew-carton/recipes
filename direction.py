class Direction(object):
    number = int(0)
    text = ""
    

    # The class "constructor" - It's actually an initializer 
    def __init__(self, number, text):
        self.number = number
        self.text = text

def make_direction(number, text):
    i = Direction(number, text)
    return i
    
    
    
    