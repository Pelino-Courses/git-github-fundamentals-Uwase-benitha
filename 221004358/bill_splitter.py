import random

num_people = int(input("Enter the number of people joining (including yourself): \n"))

if num_people <= 0:

    print("No one is joining for the party")

else:

    participants = {}

    print("")

    print('Enter the name of person ')

    for i in range(num_people):

        name = input("")

        participants[name] = 0

    print("")

    print("Enter the total bill amount: ")

    final_bill = float(input())

    split_value = round(final_bill / num_people+num_people, 2)

    for guest in participants:

        participants[guest] =  split_value

    print("")

    print("Do you want to use the 'Who is lucky?' feature? (Yes/No): ")

    use_lucky_feature = input()

    if use_lucky_feature.lower() == "yes":

        lucky_person = random.choice(list(participants.keys()))
        
        print("")

        print(f"{lucky_person} is the lucky one!")

        # split_value = round(final_bill / num_people, 2)

        for guest in participants:

          if guest == lucky_person:

            split_value = 0

            participants[guest]=split_value

        print(participants)    

    else:

        print("")

        print("No one is going to be lucky")

        for guest in participants:

          # if guest == lucky_person:

            split_value = round(final_bill / num_people, 2)

            participants[guest]=split_value

        print(participants)
