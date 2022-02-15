#! /usr/bin/env python3
# coding:utf-8

import os
import json
import time
import models
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


def details_invest_profit_by_combination(all_combination: list):
    """
    Comparison between the amount invested and profits
    """

    for i in all_combination:

        for comb in i:

            total_invest = 0
            total_profit = 0

            for share_id in comb:
                share_id.profit_to_years = share_id.price_action + (share_id.price_action * share_id.profit_action / 100)
                total_profit += share_id.profit_to_years
                total_invest += share_id.price_action

            # print(f"\n\n{'=' * 50}")
            # print(comb)
            # print(f"invest : {total_invest}")
            # print(f"Profit : {total_profit}")
            # print(f"{'=' * 50}\n\n")
        print(len(i))



    # total_profit = 0
    # total_invest = 0
    #
    # print(f"{'=' * 50}")
    #
    # for all_shares in all_combination[0]:
    #     print(len(all_shares))
    #     for i in all_shares:
    #         print(f"{'=' * 50}")
    #         # print(i)
    #         print(f"{'=' * 50}")
    #
    #     for share_id in all_shares:
    #         share_id.profit_to_years = share_id.price_action + (share_id.price_action * share_id.profit_action / 100)
    #         total_profit += share_id.profit_to_years
    #         total_invest += share_id.price_action
    #         # print(share_id)
    #
    # print(f"For invest of {total_invest:.2f}€, the profit is : {total_profit:.2f}€")
    # print(f"{'=' * 50}")


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
    details_invest_profit_by_combination(all_combinations)


if __name__ == '__main__':
    main()
