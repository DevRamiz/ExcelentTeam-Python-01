from collections import Counter
import re

def long_cat_is_long(text):
    words = re.findall(r"[a-zA-Z]+", text.lower())
    return Counter({word: len(word) for word in words})
