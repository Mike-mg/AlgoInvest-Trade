#! /usr/bin/env python3
# coding:utf-8
"""
Solutions algorithms
"""

import json


def list_of_dict_shares():
    """
    Returns list od dict od shares sort by % profit
    """

    shares_objects = []

    with open("data_base/actions.json", "r", encoding="utf-8") as file:
        data = json.load(file)

        for share in data["actions"]:
            shares_objects.append((share["name"], share["price"], share["profit"]))

    shares_objects.sort(key=lambda index: index[2])

    return shares_objects


def algorithm_naive(max_invest, list_shares):
    """
    Return the best invest with a naif
    """

    share_select = []
    total_invest = 0

    while list_shares:
        share = list_shares.pop()
        if share[1] + total_invest <= max_invest:
            share_select.append(share)
            total_invest += share[1]

    return (
        f"- Total invest : {sum([i[1] for i in share_select])}\n"
        f"- Total profit : {sum([i[2] for i in share_select])}\n"
        f"- Shares : {[i[0] for i in share_select]}"
    )


def algorithm_brute_force(invest_max, list_shares, shares_select: list = []):
    """
    Return the best invest with a brute force
    """

    if list_shares:

        val1, lstVal1 = algorithm_brute_force(
            invest_max, list_shares[1:], shares_select
        )
        val = list_shares[0]
        if val[1] <= invest_max:
            val2, lstVal2 = algorithm_brute_force(
                invest_max - val[1], list_shares[1:], shares_select + [val]
            )
            if val1 < val2:
                return val2, lstVal2

        return val1, lstVal1
    else:
        return sum([i[2] for i in shares_select]), shares_select
