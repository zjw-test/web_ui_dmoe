# -*- coding: UTF-8 -*-
import json
import os

from global_config import FILE_LOCATION


def read_json(filename, key):
    file = FILE_LOCATION + os.sep + "data" + os.sep + filename
    new = []
    with open(file, "r", encoding="utf-8") as f:
        for data in json.load(f).get(key):
            new.append(tuple(data.values())[1:])
        return new


def read_json_title(filename, key):
    file = FILE_LOCATION + os.sep + "data" + os.sep + filename
    new = []
    with open(file, "r", encoding="utf-8") as f:
        for data in json.load(f).get(key):
            a = list(data.values())
            b = a[0]
            new.append(b)
        return new
