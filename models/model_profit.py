#! /usr/bin/env python3
# coding:utf-8


class ProfitByCombination:
    """
    Class that creates a profit object by combination
    """

    def __init__(
        self, total_share_by_combination: list, total_invest: float, total_profit: float
    ):
        self.total_share_by_combination = total_share_by_combination
        self.total_invest = total_invest
        self.total_profit = total_profit
