#!/usr/bin/python3
"""
main function 0
"""
import sys

if __name__ == "main":
    subbreddit = sys.argv[1]
    number_of_subscribers = __import__('O-subs').number_of_subscribers
    if(len(sys.argv)<2):
        print("Please pass a name of a subbreddit as an argument😉")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))