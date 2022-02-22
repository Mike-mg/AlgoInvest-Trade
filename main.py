#! /usr/bin/env python3
# coding:utf-8
"""
Docstring
"""


import algorithms


def main():
    """
    Docstring
    """

    shares = algorithms.list_of_dict_shares()
    print(algorithms.algorithm_brute_force(500, shares))


if __name__ == "__main__":
    main()
