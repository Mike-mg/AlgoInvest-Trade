#! /usr/bin/env python3
# coding:utf-8
"""
Solutions algorithms
"""

import operator


def algorithm_naive(list_shares: list, max_invest: int):
    """
    Return the best invest with a naif
    """

    share_select = []
    total_invest = 0

    for share in sorted(list_shares, key=operator.itemgetter(2), reverse=True):
        if share[1] + total_invest <= max_invest:
            share_select.append(share)
            total_invest += share[1]

    return (
        f"- Total invest : {sum([i[1] for i in share_select])}\n"
        f"- Total profit : {sum([i[1] * i[2] / 100 for i in share_select])}\n"
        f"- Shares : {[i[0] for i in share_select]}"
        )

def algorithm_dynamic(list_shares: list, invest_max: int):
    matrice = [[0 for x in range(invest_max + 1)] for x in range(len(list_shares) + 1)]

    for i in range(1, len(list_shares) + 1):
        for w in range(1, invest_max + 1):
            if list_shares[i-1][1] <= w:
                w = int(w)
                matrice[i][w] = max(list_shares[i-1][2] + matrice[i-1][w-list_shares[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # Retrouver les éléments en fonction de la somme
    w = invest_max
    n = len(list_shares)
    select_shares = []

    while w >= 0 and n >= 0:
        e = list_shares[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            select_shares.append(e)
            w -= e[1]

        n -= 1

    return matrice[-1][-1], select_shares