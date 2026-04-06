import random
import time
import winsound


def end(usr_cnt,sys_cnt):
    print(f"{usr_cnt} - {sys_cnt}")
    if usr_cnt == sys_cnt:
        print("This match is a draw!!!!!!")
    elif usr_cnt > sys_cnt:
        print("you have won the game!")
    elif usr_cnt < sys_cnt:
        print("You have lost the game!")
    print("Thank your for playing this game ^_^ ")
    exit()


# noinspection DuplicatedCode
def batting(number,sys_cnt=0):
    usr_cnt = 0
    print("You are going to bat!")
    while True:
        sys_val = random.randint(1,10)
        while True:
            try:
                usr_val = int(input("Enter a number to bat: "))
                if usr_val in range(1,11):
                    break
                else:
                    print("Please enter the values in the given range of 1 - 10")
                    continue
            except ValueError:
                print("Please enter a valid input")
        for i in range(3,0,-1):
            print(f"{i}{"."*i}")
            time.sleep(0.25)
        print(f"{usr_val} - {sys_val}")
        if usr_val == sys_val:
            winsound.Beep(2500,600)
            print("You lose!")
            print("Your total points: ", usr_cnt)
            if number == 0 and sys_cnt == 0:
                print("Now",end=" ")
                bowling(1,usr_cnt)
            if number == 1:
                end(usr_cnt,sys_cnt)
        else:
            usr_cnt = usr_cnt + usr_val
            print(f"Your points: {usr_cnt}")


# noinspection DuplicatedCode
def bowling(number,usr_cnt=0):
    sys_cnt = 0
    print("You are going to bowl!")
    while True:
        if number == 1:
            if usr_cnt<sys_cnt:
                print("Since the system scored more than you; this match is coming to an end")
                end(usr_cnt,sys_cnt)
        sys_val = random.randint(1,10)
        while True:
            try:
                usr_val = int(input("Enter a number to bowl: "))
                if usr_val in range(1,11):
                    break
                else:
                    print("Please enter the values in the given range of 1 - 10")
                    continue
            except ValueError:
                print("Please enter a valid input")

        for i in range(3,0,-1):
            print(f"{i}{"."*i}")
            time.sleep(0.25)
        print(f"{usr_val} - {sys_val}")
        if usr_val == sys_val:
            winsound.Beep(2500,600)
            print("You win!")
            print("system's total points: ", sys_cnt)
            if number == 0 and usr_cnt == 0:
                print("Now",end=" ")
                batting(1,sys_cnt)
            if number == 1:
                end(usr_cnt,sys_cnt)
        else:
            sys_cnt = sys_cnt + sys_val
            print(f"System's points : {sys_cnt}")


# If the user has won the odd or even the odd_even function will return 0 or 1 based on the selection will be done
def bat_bowl(val):
    if val == 1:
        while True:
            try:
                choo = int(input("1.To Bat\n2.To bowl\n"))
                if choo in [1,2]:
                    break
                else:
                    print("Please enter 1 or 2")
                    continue
            except ValueError:
                print("Please enter a valid input")
        if choo == 1:
            batting(0)
        elif choo == 2:
            bowling(0)
    elif val == 0:
        sys = random.randint(0,1)
        if sys == 1:
            bowling(0)
        elif sys == 0:
            batting(0)


# Works in addition to the odd_even to find the winner in odd or even
def win_finder(num):
    sys_num = random.randint(1,10)
    summing = sys_num+num
    print(f"{num} - {sys_num}")
    if summing %2 == 0:
        print(f"{summing} is even!!")
        return "even"
    else:
        print(f"{summing} is odd!!")
        return "odd"


# this program checks whether the user has won the odd or even thing or not by calling win_finder
def odd_even():
    while True:
        choice = input("Enter Odd or Even: ").lower().replace(" ","").strip()
        if choice.isalpha() and choice in ["odd","even"]:
            break
        else:
            print("Please enter a valid input")
            continue
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a number")
    winner = win_finder(num)
    if winner == choice:
        print("You win!")
        return 1
    else:
        print("You lose!")
        return 0


def main():
    print("!===WELCOME TO HAND CRICKET ===!")
    bat_bowl(odd_even())


main()
