#! /usr/bin/env python3
# coding:utf-8

import operator
import os
import json

# osystem("clear")


def list_of_dict_shares():
    """
    Returns list od dict od shares sort by % profit
    """

    shares_objects = []

    with open("actions.json") as f:
        data = json.load(f)

        for share in data["actions"]:
            shares_objects.append((share["name"], share["price"], share["profit"]))

    shares_objects.sort(key=lambda index: index[2])

    return shares_objects


def algo_naif(max_invest, list_shares):
    share_select = []
    total_invest = 0

    while list_shares:
        share = list_shares.pop()
        if share[1] + total_invest <= max_invest:
            share_select.append(share)
            total_invest += share[1]

    return f"- Total invest : {sum([i[1] for i in share_select])}\n- Total profit : {sum([i[2] for i in share_select])}\n- Shares : {[i[0] for i in share_select]}"


def profit_max_algo_force_brute(max_invest, list_shares):
    pass






print(f"\nAlgo naîf :\n{'-' * 11}\n{profit_max_algo_naif(500, list_of_dict_shares())}\n")
