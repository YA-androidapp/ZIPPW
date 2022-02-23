#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.


import itertools
import os
import shutil
import sys
import zipfile


path_extract = './temp'
target_zip = './target.zip'

CHARS = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
MIN_DIGIT = 4
MAX_DIGIT = 4


def main():
    for count in range(MIN_DIGIT, MAX_DIGIT + 1):
        print(' ' * 10 + 'Number of digits: {}'.format(count))

        for pw in itertools.product(CHARS, repeat=MIN_DIGIT):
            password = ''.join(pw)
            try:
                with zipfile.ZipFile(target_zip, "r") as zp:
                    zp.extractall(
                        path=path_extract,
                        pwd=password.encode("utf-8")
                    )
            except:
                pass
                # print(' ' * 10 + 'Wrong: ' + password)
            else:
                print('Searched: ' + password)
                return

        count += 1


if __name__ == '__main__':
    if os.path.exists(path_extract):
        shutil.rmtree(path_extract)

    main()

    shutil.rmtree(path_extract)
