a = 10
print(a)

def func():
    global a
    a = 20
func()
print(a)

def upperFunc():
    b = 10
    def lowerFunc():
        nonlocal b
        b = 20
    lowerFunc()
        
upperFunc()
print(a)
