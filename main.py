import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    consent = input("\n🎲 Do you want to play a game of Blackjack? Type 'Y' or 'N': ").upper()
    if consent == 'Y':
        print(art.logo)

        users_hand = random.sample(cards, 2)
        comps_hand = random.sample(cards, 2)
        sum_uh = sum(users_hand)
        sum_ch = sum(comps_hand)

        def display():
            print(f"\n\tYour Cards: {users_hand}\tCurrent Total: {sum_uh}")
            print(f"\tComputers First Card: {comps_hand[0]}")
            if sum_uh == 21:
                print("\n🎊BLACK JACK, You Win!!!!!🎊")
                return "EXIT"  # ✅ Replace `break` with `return`
            move = input("Press 'H' to hit or 'S' to stand: ").upper()
            return move

        def mid_display():
            print(f"\n\tYour final hand: {users_hand}, final score: {sum_uh}")
            print(f"\tComputer's final hand: {comps_hand}, final score: {sum_ch}")

        def final_display():
            global sum_ch # ✅ Ensure sum_ch updates globally

            while sum_ch <= 17:
                comps_hand.append(random.choice(cards))
                sum_ch = sum(comps_hand) # ✅ Update sum dynamically after each hit
            print(f"\n\tYour final hand: {users_hand}, final score: {sum_uh}")
            print(f"\tComputer's final hand: {comps_hand}, final score: {sum_ch}")
            if sum_ch > 21:
                print("\nOpponent went over. You win 😁")
            elif sum_uh > sum_ch:
                print("\nYou win 😃")
            elif sum_uh == sum_ch:
                print("\nIt's a tie! 🤝")
            else:
                print("\n🕹️ Computer Won!!!")

        move = display()

        while move == 'H':
            users_hand.append(random.choice(cards))
            sum_uh = sum(users_hand)
            if sum_uh == 21:
                mid_display()
                print("\n🎊BLACK JACK, You Win!!!!!🎊")
                break
            elif sum_uh > 21:
                mid_display()
                print("\nYou Went Over, You Lose 😤")
                break
            else:
                move = display()

        if sum_uh < 21:
            final_display()

    else:
        break