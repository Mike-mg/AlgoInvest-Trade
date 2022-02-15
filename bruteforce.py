#! /usr/bin/env python3
# coding:utf-8

import operator
import os
import json
import time
import models
from models import ProfitByCombination
from itertools import combinations

os.system("clear")

shares_objects = []

# Read the shares file
with open("actions.json") as f:
    data = json.load(f)
    for share in data["actions"]:
        shares_objects.append(
            models.Action(
                share["number_action"], share["price_action"], share["profit_action"]
            )
        )


def max_combinations(actions_list: list[models.Action]) -> list:
    """
    Returns all possible combinations
    """

    all_combinations = []

    for combination_r in range(1, len(actions_list)):
        combination = combinations(actions_list, combination_r)
        all_combinations.append(list(combination))

    return all_combinations


def create_object_profit_by_combination(
    all_combination: list,
) -> list[models.ProfitByCombination]:
    """
    Create and return list object by profit of all combinations
    """

    profit_objects_by_combination = []

    for select_combination in all_combination:

        for combination in select_combination:

            total_invest = 0
            total_profit = 0
            total_share_by_combination = []

            for share_id in combination:
                share_id.profit_to_years = share_id.price_action + (
                    share_id.price_action * share_id.profit_action / 100
                )
                total_profit += share_id.profit_to_years
                total_invest += share_id.price_action
                total_share_by_combination.append(share_id)

            profit_objects_by_combination.append(
                ProfitByCombination(
                    total_share_by_combination, total_invest, total_profit
                )
            )

    return profit_objects_by_combination


def best_combination(all_combinations: list) -> None:
    """
    Return the best combination
    """

    invest_to_500 = []

    sort_by_nb_combinations = sorted(
        all_combinations,
        key=operator.attrgetter("total_invest", "total_profit"),
        reverse=True,
    )

    for i in sort_by_nb_combinations:

        if i.total_invest == 500:
            invest_to_500.append(i)

    a = sorted(invest_to_500, key=operator.attrgetter("total_profit"), reverse=True)

    best = a[0]
    print(
        f"{'=' * 50}\n\n"
        f"- Total invest : {best.total_invest}\n"
        f"- Total profit : {best.total_profit}\n"
        f"- Shares : {best.total_share_by_combination}\n"
        f"\n\n{'=' * 50}\n"
    )


def main():
    """
    Execute the program
    """

    time_1 = time.time()

    all_combinations = max_combinations(shares_objects)
    profit_objects_by_combination = create_object_profit_by_combination(
        all_combinations
    )
    best_combination(profit_objects_by_combination)

    time_2 = time.time()
    time_t = time_2 - time_1
    print(f"Time to complete the task : {time_t} sec\n\n")


if __name__ == "__main__":
    main()
