import random


def main():
    print("I think I know your age. I am going to guess your age.")
    name = input("Tell me, what is your name?: ")
    age = 0
    past_ages = []
    while True:
        age = random.randint(15,50)
        while age in past_ages:
            age = random.randint(15,50)
            if len(past_ages) >= 36:
                print("You are either too old or too young to be here :(")
                return
        answer = input(f"Is your age {age}?: ")
        while answer != 'y' and answer != 'n':
            answer = input(f"Well? Is {age} your age or not? ")
        if answer == 'y':
            break;
        elif answer == 'n':
            past_ages.append(age)
            print("Rats.")
                
    print(f"Alas! I have figured it out! \nYour name is {name} and your age is {age}!")
    return


if __name__ == "__main__":
    main()
