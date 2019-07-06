#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os
import json

path = os.getcwd()
def readDB():
    txt_list = []
    for i in os.listdir(os.path.join(path, "DB")):
        if i[-3:] == "txt":
            txt_list.append(i)
    message = []
    n = 1
    for j in txt_list:
        with open(os.path.join(path, "DB", j), "r+", encoding="UTF-8-sig") as f:
            line = f.readline()
            message.append(json.loads(line))
    return message

def changeDB():
    txt_list = []
    for i in os.listdir(os.path.join(path, "DB")):
        if i[-3:] == "txt":
            txt_list.append(i)
    message = []
    n = 1
    for j in txt_list:
        with open(os.path.join(path, "DB", j), "r+", encoding="UTF-8-sig") as f:
            line = f.readline()
            data = json.loads(line)
            data["id"] = n
            n += 1
        with open(os.path.join(path, "DB", j), "w+", encoding="UTF-8-sig") as f:
            json.dump(data, f, ensure_ascii="utf-8")
    return None

def writeDB(dict, now):
    with open(os.path.join(path, "DB", now + ".txt"), "w+", encoding="UTF-8") as f:
        json.dump(dict, f, ensure_ascii="utf-8")


def delDB(n):

    for i in os.listdir(os.path.join(path, "DB")):
        if i[-3:] == "txt":
            with open(os.path.join(path, "DB", i), "r+", encoding="UTF-8-sig") as f:
                line = f.readline()
                a = json.loads(line)
        if a["id"] == int(n):
            print(os.path.join(path, "DB", i))
            os.remove(os.path.join(path, "DB", i))
            return "删除成功"


if __name__ == '__main__':
    # a = readDB()
    # print(a[0])
    changeDB()
    # readDB()
    # delDB(2)