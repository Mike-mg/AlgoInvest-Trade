#! /usr/bin/env python3
# coding:utf-8
"""
Docstring
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


def algorithm_naif(max_invest, list_shares):
    """
    Description
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


def algorithm_brute_force(invest_max, list_shares, shares_select: list =[]):
    """
    Docstring
    """

    if list_shares:
        liste_1, liste_2 = algorithm_brute_force(
            invest_max, list_shares[1:], shares_select
        )
        share_0 = list_shares[0]
        if share_0[1] <= invest_max:
            liste_3, liste_4 = algorithm_brute_force(
                invest_max - share_0[1], list_shares[1:], shares_select + [share_0]
            )
            if liste_1 < liste_3:
                return liste_3, liste_4

        return liste_1, liste_2
    else:
        return sum([i[2] for i in shares_select]), shares_select
