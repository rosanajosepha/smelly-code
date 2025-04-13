def calculate_total(fruits):
    totalPrice = 0
    for fruit in fruits:
        if fruit == "apple":
            totalPrice += 1.0
        elif fruit == "banana":
            totalPrice += 0.5
        elif fruit == "cherry":
            totalPrice += 0.75
        elif fruit == "mango":
            totalPrice += 1.00
        elif fruit == "pineapple":
            totalPrice += 1.50
        elif fruit == "dragonfruit":
            totalPrice += 2.00
        elif fruit == "durian":
            totalPrice += 2.75
        else:
            print("Unknown fruit: " + fruit)
    if totalPrice >= 10:
        totalPrice *= 0.9
    return totalPrice


if __name__ == "__main__":
    print("run `pytest tests/smells1_test.py` instead.")
