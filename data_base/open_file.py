#! /usr/bin/env python3
# coding:utf-8

"""
open file csv selected
"""

import os
import csv


def open_file_csv(type_algo) -> list:
    """
    Read the shares file
    """
    print(f"\n\n{'#' * 50}\n\n")

    files = []
    folders = os.listdir("data_base")
    list_shares = []

    for folder in folders:
        if ".csv" in folder:
            files.append(folder)

    print(f"Selected folders for get shares ({type_algo}):\n{'-' * 50}\n")

    for index, path in enumerate(files):
        print(f"[ {index} ] {path}")

    select_path = int(input("\nSelected folders for iterate the combinations : "))

    folder_selected = f"data_base/{folders[select_path]}"

    with open(folder_selected, "r", encoding="utf-8") as file:
        data = csv.reader(file)

        next(data)

        for share in data:
            share[1] = float(share[1])
            share[2] = float(share[2])
            list_shares.append((share[0], share[1], share[2]))

    print(f"\n\n{'°' * 50}\n\n")

    return list_shares
