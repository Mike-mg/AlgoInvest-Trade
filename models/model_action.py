#! /usr/bin/env python3
# coding:utf-8


class Action:
    """
    Class that creates an action object
    """

    def __init__(
        self,
        name: str,
        price: float,
        profit: float,
        profit_to_years: float = 0,
    ):
        self.name = name
        self.price = price
        self.profit = profit
        self.profit_to_years = profit_to_years

    def __repr__(self):
        return self.name
