
def tester(start):
    state = start  # В каждом вызове сохраняется свое значение state
    def nested(label):        
        print(label, state) # в объемлющей области видимости
    return nested

f = tester(0)

f(1)
f(2)
f(3)




def tester1(start):
    state = start  # В каждом вызове сохраняется свое значение state
    def nested(label):
        nonlocal state      # Объект state находится 

        print(label, state) # в объемлющей области видимости
        state += 1 # Изменит значение переменной, объявленной как nonlocal
    return nested

f = tester1(0)
f(1)
f(2)
f(3)