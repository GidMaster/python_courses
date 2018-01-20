from functools import partial



def log_params(f):
    def wrapper(a, b):
        print(f'a = {a}, b = {b}')
        return f(a,b)
    return wrapper

@log_params
def plus(a, b):
    return(a + b)

def main():
    
    p = plus(1, 2)
    print(p)

if __name__ == '__main__':
    main()