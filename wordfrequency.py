import requests
from bs4 import BeautifulSoup
import operator


def create_dict(words):
    dictionary = dict()

    for word in words:
        value = dictionary.get(word)
        if type(value) is int:
            value += 1
        else:
            value = 1
        dictionary.update({word: value})

    return dictionary


r = requests.get("https://tr.wikipedia.org/wiki/Aziz_Sancar")
content = BeautifulSoup(r.content, "html.parser")
paragraphs = content.find_all("p")

words = list()
for p in paragraphs:
    words.extend(p.text.lower().replace(".", "").replace(",", "").replace('"', '').split())

dict = create_dict(words)

for key, value in sorted(dict.items(), key=operator.itemgetter(0)):
    print(key, value)
