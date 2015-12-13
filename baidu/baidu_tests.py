# coding: utf-8
import baidu
import pytest


def test_get_response():
    word = "hello"
    response = baidu.get_response(word)
    assert response.status_code == 200, \
        "baidu.get_response should get translate result"


def test_has_main():
    assert hasattr(baidu, "main"), \
        "baidu module should have main function"
