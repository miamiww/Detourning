import sys
import argparse

def insult_me(name, insult):
    full_insult= name + " is " + insult
    print full_insult

parser = argparse.ArgumentParser(description = "Insults people")
parser.add_argument("--name", dest="name", help="The person to be insulted", default="Nobody")
parser.add_argument("--insult", dest="insult", help="The insult to use")

args = parser.parse_args()

insult_me(args.name, args.insult)
# print(args)
