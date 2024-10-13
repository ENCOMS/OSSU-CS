from hello import hello

'''
def test_hello():
    assert hello("Richard") == "hello, Richard"
    assert hello() == "hello, world"
'''

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"