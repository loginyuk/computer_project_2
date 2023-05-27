def my(algo):
    print(globals())
    algo = globals()[algo]
    algo('hello')

def anoth(a):
    print(a)

def hellom(a):
    print(a)

my('hellom')