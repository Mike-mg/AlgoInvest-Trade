#! /usr/bin/env python3
# coding:utf-8

import json
import models
from operator import attrgetter

actions = []

with open("actions.json") as f:
    data = json.load(f)
    for i in data["actions"]:
        actions.append(
            models.Action(i["number_action"], i["price_action"], i["profit_action"])
        )

for action in actions:
    nb_action_for_500_eur = 500 / action.price_action
    total_eur = nb_action_for_500_eur * action.price_action
    action.profit_to_years = total_eur + (total_eur * action.profit_action / 100)

actions_tried_by_best_profit = sorted(
    actions, key=attrgetter("profit_to_years"), reverse=True
)

for action in actions_tried_by_best_profit:
    print(
        f"Action N°{action.number_action:<5}{'-':<5}Nb action : {action.number_action:<5}{'=>':<5}\
    Profit to 2 years : {action.profit_to_years:.2f}€"
    )
