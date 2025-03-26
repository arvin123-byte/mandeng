class Calculator:
    def __init__(self, initial_value=0):
        self.value = initial_value
    
    def add(self, x):
        return self.value + x

    def is_positive(self):
        if self.value > 0:
            return True
        elif self.value == 0:
            return None
        else:
            return False
            
    def compare_with(self, other):
        
        if other is None:
            pass  
        return self.value > other