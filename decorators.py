def greet(fx):
    def mfx(*args, **kwargs):
        print("What's up ")
        fx(*args, **kwargs)
        print("So long Sucker")
    return mfx

@greet
def hello():
    print("bla bla")

@greet
def add(a, b):
    print(a-b)

hello()

add(171, 102)