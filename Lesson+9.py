"""
lesson-9
"""

x = 10

def func():
    x = 2
    print('x =', x)
    
    def func_inner(): 
        def super_inner():
            nonlocal x
            x = 8
        super_inner()
        print('inner print', x)
        
    func_inner()
    print('Replace x to', x)
    
func()
print(x)