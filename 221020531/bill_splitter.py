import random
print("Enter the number of people joining (including yourself):");
numofpeople = int(input())
if numofpeople > 0:
guests = {}
print("")
print("Enter the name of every friend (including you), each on a new line:")
for i in range(numofpeople):
name = input()
guests[name] = 0
print("")
final_bill = float(input("Enter the total bill value:\n"))
split_value = round(final_bill / numofpeople, 2)
for guest in guests:
guests[guest] = split_value
print("")
print("Do you want to use the 'Who is lucky?' feature? (Yes/No):")
use_lucky_feature = input()
if use_lucky_feature.lower() == "yes":
lucky_person = random.choice(list(guests.keys()))
print("")
print(f"{lucky_person} is the lucky one!");
else:
print("")
print("No one is going to be lucky")
# print(guests)
else:
print("No one is joining for the party")
