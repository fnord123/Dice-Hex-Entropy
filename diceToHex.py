#!/usr/bin/python3

# Use dice to generate true randomness of a desired number of bits of entropy.
# Ideally use casino dice and roll the device far enough to get the most possible
# entropy.

import argparse, math

def split(word):
  return [char for char in word]

def get_rolls(rollsNeeded):
  print("Please roll %i dice" % rollsNeeded)
  rolls = split(input())
  return rolls

parser = argparse.ArgumentParser(description='Convert dice to hex.')
parser.add_argument("--entropy", type=int, default=128,
                    help="Number of bits of entropy to roll")
args = parser.parse_args()
print("Generating %i bits of entropy" % args.entropy)
rollsNeeded = math.ceil(args.entropy / (math.log(6,10) / math.log(2,10)))
total = 0
while rollsNeeded > 0:
  rolls = get_rolls(rollsNeeded)
  while rollsNeeded > 0 and len(rolls) > 0:
    roll = int(rolls.pop(0))
    if roll < 1 or roll > 6:
      print("Invalid roll of %i skipped" % roll)
    else:
      total = total * 6 + (roll - 1)
      rollsNeeded -= 1
mask = 2**args.entropy - 1
print(hex(total & mask))
