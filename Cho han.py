import random
import time


def get_dices() -> list:
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    return [first_dice, second_dice]


def cho_han():
    players_money = 500
    japanese_numbers = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

    while True:
        if players_money > 0:
            print(f"You have {players_money} mon")
            user_input = input("How much money do you want to bet (or QUIT)?: ")

            if user_input == 'QUIT' or user_input == 'quit':
                break
            try:
                user_input = int(user_input)
            except ValueError:
                print("Please enter a valid number.")
            else:
                if user_input > players_money or user_input < 1:
                    print("Please enter a valid bet.")
                    continue

                random_pair_of_dice = get_dices()
                time.sleep(0.5)
                print("The dealer swirls the cup and you hear the rattle of dice.\n"
                      "The dealer slams the cup on the floor,"
                      "still covering the dice and asks for your bet.")
                time.sleep(1)

                while True:
                    user_choice = input("CHO (even) or HAN (odd)?: ").lower()

                    if user_choice == 'cho' or user_choice == 'han':
                        print("The dealer lifts the cup to reveal:")
                        time.sleep(0.5)
                        print(f"{japanese_numbers[random_pair_of_dice[0]]} "
                              f"- {japanese_numbers[random_pair_of_dice[1]]}")
                        print(f"{random_pair_of_dice[0]} - {random_pair_of_dice[1]}")

                        if ((user_choice == 'han' and sum(random_pair_of_dice) % 2 == 1)
                                or (user_choice == 'cho' and sum(random_pair_of_dice) % 2 == 0)):
                            print(f"You won! You take {user_input} mon. The house collects a 40 mon fee.")
                            players_money = players_money + user_input - 40

                        else:
                            print(f"You lost! You lost {user_input} mon.")
                            players_money = players_money - user_input
                        break
                    else:
                        print("Please enter a valid choice.")
                        continue
        else:
            print("Game over")
            break


if __name__ == '__main__':
    cho_han()
