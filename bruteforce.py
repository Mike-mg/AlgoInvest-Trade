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


class TopProfitByShare:
    """
    Return the share with the best profit
    """

    def __init__(self):
        self.shares_objects = self.open_file()
        self.all_combinations = []
        self.profit_objects_by_combination = []

    def open_file(self):
        """
        Read the shares file
        """

        shares_objects = []

        with open("actions.json") as f:
            data = json.load(f)
            for share in data["actions"]:
                shares_objects.append(
                    models.Action(
                        share["number_action"], share["price_action"], share["profit_action"]
                    )
                )

        return shares_objects

    def max_combinations(self):
        """
        Returns all possible combinations
        """

        for combination_r in range(1, len(self.shares_objects)):
            combination = combinations(self.shares_objects, combination_r)
            self.all_combinations.append(list(combination))

    def create_object_profit_by_combination(self):
        """
        Create and return list object by profit of all combinations
        """

        for select_combination in self.all_combinations:

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

                self.profit_objects_by_combination.append(
                    ProfitByCombination(
                        total_share_by_combination, total_invest, total_profit
                    )
                )

    def best_combination(self) -> None:
        """
        Return the best combination
        """

        invest_to_500 = []

        sort_by_nb_combinations = sorted(
            self.profit_objects_by_combination,
            key=operator.attrgetter("total_invest", "total_profit"),
            reverse=True,
        )

        for by_combination in sort_by_nb_combinations:

            if by_combination.total_invest == 500:
                invest_to_500.append(by_combination)

        profit_sorted = sorted(invest_to_500, key=operator.attrgetter("total_profit"), reverse=True)

        best_profit = profit_sorted[0]
        print(
            f"\n\n{'=' * 50}\n\n"
            f"- Total invest : {best_profit.total_invest}\n"
            f"- Total profit : {best_profit.total_profit}\n"
            f"- Shares : {best_profit.total_share_by_combination}\n"
            f"\n\n{'=' * 50}\n"
        )


def main():
    """
    Execute the program
    """

    time_1 = time.time()

    top_share = TopProfitByShare()
    print("> Objet TopShare create ... Finish")
    top_share.max_combinations()
    print("> Task of the create of max number of combination ... Finish")
    top_share.create_object_profit_by_combination()
    print("> Creations of objects profit by combination ... Finish")
    print("> Return of the best investment ... Finish")
    top_share.best_combination()

    time_2 = time.time()
    time_t = time_2 - time_1
    print(f"\nTime to complete the task : {time_t} sec\n\n")


if __name__ == "__main__":
    main()
