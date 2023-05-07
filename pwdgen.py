#!/usr/bin/env python3

import os
import re
import random
import argparse

SOURCE = "/usr/share/dict/words"
INITIAL_SAMPLE = 10000
REGEX = r"^[^aqwzmAZQWM]*$"
PASSWORD_NUMBER = 5
WORDS_IN_PASS = 3
WORD_LEN_MIN = 4
SPECIAL_CHARS = list("1234567890-_!@$;")

def main():
    with open(SOURCE) as fd:
        data = fd.read().split("\n")
    data = random.sample(data, INITIAL_SAMPLE) 
    filtered_data = list(filter(lambda x: re.search(REGEX, x), data))
    filtered_data = [word.lower() for word in filtered_data] 
    for i in range(PASSWORD_NUMBER):
        password = ""
        for j in range(WORDS_IN_PASS):
            word = random.choice(filtered_data).split("'")[0]
            if len(word) > WORD_LEN_MIN:
                word_length = random.randrange(WORD_LEN_MIN, len(word))
                password += word[:word_length]
            else:
                password += word
            special_chars = random.randrange(0,3)
            for k in range(special_chars):
                password += random.choice(SPECIAL_CHARS)
        print(password)

if __name__ == "__main__":
    main()

