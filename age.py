import random


def main():
    print("Hello, I am going to guess your age.")
    name = input("What is your name?: ")
    age = 0
    past_ages = []
    while True:
        age = random.randint(15,40)
        while age in past_ages:
            age = random.randint(15,40)
            if len(past_ages) >= 26:
                print("You are either too old or too young :(")
                return
        answer = input(f"Is your age {age}?: ")
        if answer == 'y':
            break;
        print("Rats.")
        past_ages.append(age)
    print(f"Your name is {name} and your age is {age}!")
    return


if __name__ == "__main__":
    main()
