'''
runes.py

ToDo:
[] data for all the Runes explanations

'''
import random

print("Welcome to Runes\n")

runes = ["Fehu","Uruz","Thurisaz","Ansuz","Raidho","Kenaz","Gebo","Wunjo","Hagalaz","Nauthiz","Isa","Jera","Ihwaz","Perthro","Algiz","Sowilo","Tiwaz","Berkano","Ehwaz","Mannaz","Laguz","Inguz"]

amount = input("How many Runes would you like to pull: ")

# make array to hold runes that get pulled
bag = []

for i in range(int(amount)):
    rune = runes[random.randrange(0,21)]
    # place rune into bag
    bag = []

for k in range(int(amount)):
    print(bag[k])