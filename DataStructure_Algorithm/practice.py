def trace(func):
    def wrapper(*args, **kwargs):
        print(func.__name__, '함수 시작')
        func(*args, **kwargs)
        print(func.__name__, '함수 끝')
    return wrapper

@trace
def hello(a, b):
    print(a, b, '반갑습니다')

@trace
def world(b):
    print(b, '새로운 세상')

hello('명원님', '참')
world(b='놀라운')