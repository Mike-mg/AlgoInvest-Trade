#! /usr/bin/env python3
# coding:utf-8

"""
Return the combinations of shares with the best profit
"""

import operator
import os
import json
# import csv
import time
from itertools import combinations
import models

os.system("clear")


class TopProfitByShare:
    """
    Return the share with the best profit
    """

    def __init__(self):
        self.shares_objects = []
        self.all_combinations = []
        self.profit_objects_by_combination = []
        self.open_file()

    def open_file(self) -> None:
        """
        Read the shares file
        """

        # csv_file_actions = csv.DictReader(open("dataset1_Python+P7.csv"))
        # for share in csv_file_actions:
        #     share["price"] = float(share["price"])
        #     share["profit"] = float(share["price"])
        #     self.shares_objects.append(
        #                 models.Action(
        #                     share["name"],
        #                     share["price"],
        #                     share["profit"]
        #                 )
        #             )

        for y, i in enumerate(self.shares_objects):
            print(f"{y+1} :: Name : {i.name} - Price : {i.price} - Profit : {i.profit}")

        with open("actions.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for share in data["actions"]:
                self.shares_objects.append(
                    models.Action(
                        str(share["name"]),
                        share["price"],
                        share["profit"],
                    )
                )

    def max_combinations(self) -> None:
        """
        Returns all possible combinations
        """

        for combination_r in range(1, len(self.shares_objects)):
            combination = combinations(self.shares_objects, combination_r)
            self.all_combinations.append(list(combination))
        print(sum(map(len, self.all_combinations)))

    def create_object_profit_by_combination(self) -> None:
        """
        Create and return list object by profit of all combinations
        """

        for select_combination in self.all_combinations:

            for combination in select_combination:

                total_invest = 0
                total_profit = 0
                total_share_by_combination = []

                for share_id in combination:
                    share_id.profit_to_years = share_id.price * share_id.profit / 100
                    total_profit += share_id.profit_to_years
                    total_invest += share_id.price
                    total_share_by_combination.append(share_id)

                self.profit_objects_by_combination.append(
                    models.ProfitByCombination(
                        total_share_by_combination, total_invest, total_profit
                    )
                )

    def best_combination(self) -> None:
        """
        Return the best combination
        """

        invest_to_500 = []

        for by_combination in self.profit_objects_by_combination:

            if by_combination.total_invest <= 500:
                invest_to_500.append(by_combination)

        profit_sorted = sorted(
            invest_to_500, key=operator.attrgetter("total_profit"), reverse=True
        )

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
