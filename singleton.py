class A:
    def __init__(self, *args, **kwargs):
        # import pdb; pdb.set_trace()
        print "I am in init"

    def __new__(self, *args, **kwargs):
        print "I am in New"


a = A()
b = A()
