import requests,jsonify
from assertpy import assert_that
s = requests.session()


class hello:
    def __int__(self):
        super().__init__()

    def test_hello_world(self):
        header = {}
        payload = {}
        url = "http://127.0.0.1:5000/"
        response = s.get(url,headers=header,data=payload)
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
        assert_that(response.text).contains("Hello world")
        print(response.status_code)
        print(response.text)


if __name__ == '__main__':
    hello_world = hello()
    new = hello_world.test_hello_world()

'''super() lets you avoid referring to the base class explicitly, which can be nice. 
But the main advantage comes with multiple inheritance, where all sorts of fun stuff can happen. 
See the standard docs on super if you haven't already.

Note that the syntax changed in Python 3.0: 
you can just say super().__init__() instead of super(ChildB, self).__init__() which IMO is quite a bit nicer. 
The standard docs also refer to a guide to using super() which is quite explanatory.'''
