import random
import sys


def run(num_quotes=1):
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  for i in range(int(num_quotes)):
    print(quotes[random.randint(0, last)], end="")

if __name__== "__main__":
  run(*sys.argv[1:])
