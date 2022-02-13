#! /usr/bin/env python3
# coding:utf-8

import json

with open('actions.json') as f:
    data = json.load(f)
    print(data)