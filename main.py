#! /usr/bin/env python3
# coding:utf-8
"""
Docstring
"""


import algorithms


def main():
    """
    Entry the program
    """

    # Mon force brute =======================

    top_share = algorithms.TopProfitByShare()

    print("> Objet TopShare create ... Finish")
    top_share.max_combinations()
    print("> Task of the create of max number of combination ... Finish")
    top_share.create_object_profit_by_combination()
    print("> Creations of objects profit by combination ... Finish")
    print("> Return of the best investment ... Finish")
    top_share.best_combination()

    print(f"\n{'#' * 25}\n")

    # algomius naif =======================

    all_shares = algorithms.list_of_dict_shares()

    print(f"Algo naive algomius\n{'-' * 25}")
    print(algorithms.algorithm_naive(500, all_shares))

    print(f"\n{'#' * 25}\n")

    # algomius force brute =======================

    all_shares = algorithms.list_of_dict_shares()

    print(f"Algo brute force algomius\n{'-' * 25}")
    print(algorithms.algorithm_brute_force(500, all_shares))

    print(f"\n{'#' * 25}\n")


if __name__ == "__main__":
    main()
