import random

def flip_coin(times):
    outcomes = {"heads": 0, "tails": 0}
    for _ in range(times):
        flip = random.choice(["heads", "tails"])
        outcomes[flip] += 1
    return outcomes

times = input("Enter the number of times to flip the coin: ")

if times.isdigit():
    outcomes = flip_coin(int(times))
    print(f"Out of {times} flips, there were {outcomes['heads']} heads and {outcomes['tails']} tails.")
else:
    print("Invalid input. Please, enter a non-negative integer.")