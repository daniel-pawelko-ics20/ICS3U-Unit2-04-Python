#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Oct 2021
# This program calculates the price of a pizza

from constants import LABOR, RENT, CPI, HST


def main():
    # this function calculates the price of a pizza

    # input
    diameter = int(input("Enter diameter of the pizza (inch): "))

    # process
    sub_total = LABOR + RENT + (diameter * CPI)
    total = sub_total + (sub_total * HST)

    # output
    print(f"\nThe final cost of a {diameter} inch pizza is: " f"${total:,.2f}")

    print("\nDone.")


if __name__ == "__main__":
    main()
