play_again = True

while play_again:    
    print("Welcome to my text-based RPG!")
    name = input("Enter your name: ")
    print(f"Greetings {name}! Welcome to your adventure.")

    start = input("Would you rather play the game or perish? ")
    if start.lower() == "play":
        print("Great! Let's play the game!")
        setting = input("Would you like to go to the jungle(1), the desert(2), or the mysterious third place(3) ? ")

        if setting.lower() == "1":
            print("Welcome to the mighty Amazon rainforest! Your tour guide told you to wait here...")
            response = input("He has been gone a long time. Do you follow him or wait here? ")

            if response.lower() == "follow":
                print("You follow him into the trees...")
                transport = input("You see a canoe nearby. Walk or take the canoe down the river? ")

                if transport.lower() == "walk":
                    print("After walking for a few minutes, you get eaten by a giant snake and die. (Ending 3)")
                elif transport.lower() == "canoe":
                    print("You take the canoe down the river and eventually fall down a huge waterfall and die. (Ending 4)")

            elif response.lower() == 'wait':
                print("You wait another ten minutes, and he still isn't here!")
                decision = input("Do you wait some more or go find him? ")

                if decision.lower() == "wait more":
                    print("You waited a little longer, your tour guide returns, and you both go home safe. (Ending 5)")
                elif decision.lower() == "find him":
                    print("You follow him into the trees...")
                    transport = input("You see a canoe nearby. Walk or take the canoe down the river? ")

                    if transport.lower() == "walk":
                        print("After walking for a few minutes, you get eaten by a giant snake and die. (Ending 3)")
                    elif transport.lower() == "canoe":
                        print("You take the canoe down the river and eventually fall down a huge waterfall and die. (Ending 4)")
                    else:
                        print("Invalid response! You lose!")

        elif setting.lower() == "2":
            print("Welcome to the mighty Sahara Desert! Your tour guide told you to wait here...")
            response = input("He has been gone a long time. Do you follow him or wait here? ")

            if response.lower() == "follow":
                print("You follow him into the dunes...")
                transport = input("You follow him into the dunes and you see a tree and water in the distance... Do you go to the oasis, or go in the opposite direction? ")

                if transport.lower() == "oasis":
                    print("You walk to the oasis, and it turns out it was an illusion... You pass out due to the heat and die. (Ending 6)")
                elif transport.lower() == "opposite direction":
                    print("You end up walking in the opposite direction and finding a village. They give you water and food, and you survive! (Ending 7)")

            elif response.lower() == 'wait':
                print("You wait another ten minutes, and he still isn't here!")
                decision = input("Do you want to wait again or go find him? ")

                if decision.lower() == "wait again":
                    print("Your tour guide comes back and says it is too hot today to go out. You go home safe. (Ending 8)")
                elif decision.lower() == "find him":
                    print("You follow him into the dunes...")
                    transport = input("You follow him into the dunes and you see a tree and water in the distance... Do you go to the oasis, or go in the opposite direction? ")

                    if transport.lower() == "oasis":
                        print("You walk to the oasis, and it turns out it was an illusion... You pass out due to the heat and die. (Ending 6)")
                    elif transport.lower() == "opposite direction":
                        print("You end up walking in the opposite direction and finding a village. They give you water and food, and you survive! (Ending 7)")
                    else:
                        print("Invalid response! You lose!")

        elif setting.lower() == "3":
            print("You have chosen the mysterious third place...")
            print("Welcome to Bikini Bottom! Your guide, Spongebob told you to wait here while he goes into the goo lagon to check things out...")
            response = input("He has been gone a long time. Do you follow him or wait here? ")

            if response.lower() == "follow":
                print("You follow him into the goo lagon...")
                transport = input("You follow him into the goo lagon and you see a crazed fish in the distance! Do you run or stand your ground? ")

                if transport.lower() == "run":
                    print("As you run away, you realize it was the hash slinging slasher coming to get you... He gets you and eats you... You perished! (Ending 9) ")
                elif transport.lower() == "stand ground":
                    print("You end up standing your ground, and once the hash slinging slasher gets to you... It gets intimidated and swims off! You survived! (Ending 10)")

            elif response.lower() == 'wait':
                print("You wait another ten minutes, and Spongebob still isn't here!")
                transport = input("Do you want to wait again or go find him? ")

                if transport.lower() == "wait again":
                    print("Spongebob comes back and says it is too hot today to go out to swim today. You go home safe. (Ending 11)")
                elif transport.lower() == "find him":
                    print("You follow him into the goo lagon...")
                    transport = input("You follow him into the goo lagon and you see a crazed fish in the distance! Do you run or stand your ground? ")

                    if transport.lower() == "run":
                        print("As you run away, you realize it was the hash slinging slasher coming to get you... He gets you and eats you... You perished! (Ending 9) ")
                    elif transport.lower() == "stand ground":
                        print("You end up standing your ground, and once the hash slinging slasher gets to you... It gets intimidated and swims off! You survived! (Ending 10)")

                    else:
                        print("Invalid response! You lose!")

        else:
            print("Invalid response! You lose! (Ending 2) ")

    else:
        print("Lame. Okay, you are dead now... (Ending 1)")

    play_again_input = input("Do you want to play again? (yes/no): ")
    if play_again_input.lower() != "yes":
          play_again = False