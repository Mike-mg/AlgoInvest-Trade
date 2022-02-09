#! /usr/bin/env python3
# coding:utf-8

import models
import json

actions = []

with open("actions.json") as f:
    data = json.load(f)
    for i in data["actions"]:
        actions.append(models.Action(i["number_action"], i["price_action"], i["profit_action"]))

for action in actions:

    print("----------------")
    nb_action_for_500_eur = 500 * 1 / action.price_action
    print(f"{nb_action_for_500_eur:.2f}")
    total = nb_action_for_500_eur * action.price_action
    print(total)
    action.profit_to_years = total + (total * action.profit_action / 100)
    # price_init[3] = total + (total * action[N_action].profit_action / 100)
    print(action.profit_to_years)
