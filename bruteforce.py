#! /usr/bin/env python3
# coding:utf-8

import os
import json
import time
import models
from itertools import combinations

os.system('clear')

shares_objects = []
profit_objects_by_combination = []

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


def details_invest_profit_by_combination(all_combination: list):
    """
    Comparison between the amount invested and profits
    """



    for select_combination in all_combination:

        for combination in select_combination:

            total_invest = 0
            total_profit = 0
            total_share_by_combination = []

            for share_id in combination:
                share_id.profit_to_years = share_id.price_action + (share_id.price_action * share_id.profit_action / 100)
                total_profit += share_id.profit_to_years
                total_invest += share_id.price_action
                total_share_by_combination.append(share_id)

            profit_objects_by_combination.append((total_share_by_combination, total_invest, total_profit))

    for index, value in enumerate(profit_objects_by_combination):
        print(f"{index} : {value[1]} - {value[2]}")

        # print(f"\n\n{'=' * 50}")
        # print(comb)
        # print(f"invest : {total_invest}")
        # print(f"Profit : {total_profit}")
        # print(f"{'=' * 50}\n\n")


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

    time_1 = time.time()
    all_combinations = max_combinations(shares_objects)
    details_invest_profit_by_combination(all_combinations)
    time_2 = time.time()
    time_t = time_2 - time_1
    print(f"Time to complete the task : {time_t} sec")


if __name__ == '__main__':
    main()
