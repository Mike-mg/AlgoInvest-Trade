#! /usr/bin/env python3
# coding:utf-8

"""
Entry the program
"""


import algorithms
import data_base


def main():
    """
    Entry the program
    """

    # algo naive =======================

    list_shares = data_base.open_file.open_file_csv("Algorithm Naive")
    print(algorithms.algorithm_naive(list_shares, 500))

    print(f"\n\n{'#' * 50}\n\n")

    # Brute force =======================

    # top_share = algorithms.TopProfitByShare(data_base.open_file.open_file_csv("Algorithm Brute Force"))

    # print("> Objet TopShare create")
    # top_share.max_combinations()
    # print("> Task of the create of max number of combination")
    # top_share.create_object_profit_by_combination()
    # print("> Creations of objects profit by combination")
    # print("> Return of the best investment")
    # top_share.best_combination()


if __name__ == "__main__":
    main()
