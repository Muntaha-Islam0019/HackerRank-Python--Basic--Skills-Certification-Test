#!/bin/python3

import os


class VendingMachine:
    def __init__(self, total_number_of_items, price_of_single_item):
        self.total_number_of_items = total_number_of_items
        self.price_of_single_item = price_of_single_item

    def buy(self, requested_number_of_items, amount_customer_put_into):
        if requested_number_of_items <= self.total_number_of_items and amount_customer_put_into >= (requested_number_of_items * self.price_of_single_item):
            self.total_number_of_items -= requested_number_of_items
            return amount_customer_put_into - (requested_number_of_items * self.price_of_single_item)
        elif requested_number_of_items > self.total_number_of_items:
            raise ValueError('Not enough items in the machine')
        else:
            raise ValueError('Not enough coins')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
