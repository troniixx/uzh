#!/usr/bin/env python3

def pack_and_bill(order, prices):
    allBalls = sum(order)
    # calculate necessary boxes
    largeBoxes = allBalls // 500
    remainder = allBalls % 500
    if (remainder > 100):
        smallBoxes = 0
        largeBoxes += 1
    elif remainder:
        smallBoxes = 1
    else:
        smallBoxes = 0
    # calculate price
    price = round(prices["ball"] * allBalls +
                  prices["smallbox"] * smallBoxes +
                  prices["largebox"] * largeBoxes,
                  2)
    return (largeBoxes, smallBoxes, price)

