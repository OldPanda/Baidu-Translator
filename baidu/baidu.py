# !/usr/bin/env python
# coding: utf-8

import sys
import getopt
import requests
import json

# to print non-ascii string
reload(sys)
sys.setdefaultencoding('utf-8')

API_KEY = "h8VzXEBGrbBB06YFtVsdSKGG"
URL = "http://openapi.baidu.com/public/2.0/translate/dict/simple"


def get_response(word):
    """ Fetch translate result from baidu api
    Args:
        word(str): query word
    Returns:
        (requests.models.Response): response object
    """
    url = URL + "?client_id=" + API_KEY + "&q=" + word + "&from=en&to=zh"
    return requests.get(url)


def print_res(data):
    """ Print translate result in a better format
    Args:
        data(str): result
    """
    print '==================================='
    main_part = data['data']
    print main_part['word_name']
    symbols = main_part['symbols'][0]
    print "美式音标：[" + symbols['ph_am'] + "]"
    print "英式音标：[" + symbols['ph_en'] + "]"
    print '-----------------------------------'
    parts = symbols['parts']
    for part in parts:
        print part['part']
        for mean in part['means']:
            print "    ", mean
    print '==================================='


def main():
    print "Translating..."
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)

    if len(args) == 0:
        print "Need a word to be translated. "
        sys.exit(2)

    word = " ".join(args).lower()
    data = json.loads(get_response(word).text)
    if len(data['data']) == 0:
        # if word doesn't exist
        print "Not a valid word. "
        sys.exit(2)
    print_res(data)

if __name__ == "__main__":
    main()
