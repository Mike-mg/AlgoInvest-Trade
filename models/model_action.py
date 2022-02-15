#! /usr/bin/env python3
# coding:utf-8


class Action:
    """
    Class that creates an action object
    """

    def __init__(
        self,
        number_action: str,
        price_action: int,
        profit_action: int,
        profit_to_years: int = 0
    ):
        self.number_action = number_action
        self.price_action = price_action
        self.profit_action = profit_action
        self.profit_to_years = profit_to_years
