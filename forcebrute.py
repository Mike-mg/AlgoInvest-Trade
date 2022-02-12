#! /usr/bin/env python3
# coding:utf-8

import os
import json
import models
from operator import attrgetter

os.system("clear")


def shares_sorted_by_price():
    """
    Returns stocks sorted by price
    """

    with open("actions.json") as f:
        data = json.load(f)

        actions_objects = []

        for action_id in data["actions"]:
            actions_objects.append(
                models.Action(
                    action_id["number_action"],
                    action_id["price_action"],
                    action_id["profit_action"],
                )
            )

    sorted_shares_by_price = sorted(
        actions_objects, key=attrgetter("price_action"), reverse=True
    )

    for id_action in sorted_shares_by_price:
        id_action.profit_to_years = id_action.price_action + (
            id_action.price_action * id_action.profit_action / 100
        )

    return sorted_shares_by_price


all_actions = shares_sorted_by_price()
shares_preference = []
max_invest = 500
total_invest = 0

while True:
    if total_invest <= max_invest:
        for action in all_actions:
            if total_invest + action.profit_to_years <= max_invest:
                total_invest += action.profit_to_years
                shares_preference.append(action)
                print(action.number_action)
    else:
        for i in shares_preference:
            print(i.number_action)
        break



for action_id in all_actions:
    print(
        f"N°: {action_id.number_action} - Price : {action_id.price_action} - Years % : {action_id.profit_action}% - Profit total :{action_id.profit_to_years}"
    )
#
# profit_total = 0
# for profit in shares_preference:
#     profit_total += profit.profit_to_years
# print(profit_total)
