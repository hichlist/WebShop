
import pytest_django

def count(x):
    return x + 5

def test_count():
    assert count(4) == 9

# def test_site(cli):
#     assert
# import http.client
#
# host1 = http.client.HTTPConnection("ya.ru")
# host1.set_tunnel('ya.ru')
# print(host1.request("HEAD", '/index.html'))
# print(host1)
