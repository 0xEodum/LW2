import random
from colorama import Style, Fore

colors = [Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.MAGENTA, Fore.LIGHTBLUE_EX]


def game(max_number):
    potential_nums = []
    imagined_num = random.randint(1, max_number)
    msg = input()
    while msg:

        if msg == "HELP":
            print(potential_nums)

        elif len(msg.split()) == 1 and int(msg) == imagined_num:
            print(f"{colors[3]}success{Style.RESET_ALL}")
            quit()

        elif msg != "HELP":
            user_list = msg.split()
            for i in range(len(user_list)):
                user_list[i] = int(user_list[i])
            if imagined_num in user_list:
                print(f"{colors[1]}YES{Style.RESET_ALL}")
                potential_set = set(potential_nums)
                new_set = set(user_list)

                if new_set.issubset(potential_set):
                    potential_nums = list(new_set)
                else:
                    for num in user_list:
                        if num not in potential_nums:
                            potential_nums.append(num)
            else:
                print(f"{colors[0]}NO{Style.RESET_ALL}")
                for num in user_list:
                    if num in potential_nums:
                        potential_nums.remove(num)
        msg = input()


if __name__ == '__main__':
    max_number = int(input(f"{colors[2]} Введите максимальное загадываемое число: {Style.RESET_ALL}"))
    game(max_number)

