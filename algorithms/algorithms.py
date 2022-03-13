#! /usr/bin/env python3
# coding:utf-8

"""
Solutions algorithms
"""

import operator


def algorithm_naive(list_shares: list, max_invest: float):
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
