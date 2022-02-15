#! /usr/bin/env python3
# coding:utf-8

import os
import json
import time
import models
from models import Profit
from itertools import combinations


os.system('clear')

shares_objects = []

with open('actions.json') as f:
    data = json.load(f)
    for share in data["actions"]:
        shares_objects.append(
            models.Action(
                share["number_action"],
                share["price_action"],
                share["profit_action"]
            )
        )

t1 = time.time()


def max_combinations(actions_list: list[models.Action]):
    """
    return the best combination
    """

    all_combinations = []

    for combination_r in range(1, len(actions_list)):
        combination = combinations(actions_list, combination_r)
        all_combinations.append(list(combination))

    return all_combinations


def best_combination(all_combinations):
    """
    Return the best combination
    """

    sort_by_nb_combinations = sorted(all_combinations, key=lambda length: len(length), reverse=True)

    return sort_by_nb_combinations[0]


def main():
    """
    Execute the program
    """
    all_combinations = max_combinations(shares_objects)

# list_of_shares_detail = []
# for index, value in enumerate(all_combinations):
#     total_profit = 0
#     total_invest = 0
#
#     # print(f"{'=' * 50}\n\n")
#     # print(f"{index} : {value}")
#     for u in value:
#         u.profit_to_years = u.price_action + (u.price_action * u.profit_action / 100)
#         total_profit += u.profit_to_years
#         total_invest += u.price_action
#
#     list_of_shares_detail.append((value, total_invest, total_profit))
#     # print(f"\ntotal profit : {total_profit}")
#     # print(f"total invest : {total_invest}")
#     #
#     # print(f"\n\n{'=' * 50}")

if __name__ == '__main__':
    main()
