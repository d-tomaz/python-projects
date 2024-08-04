def luhn_algorithm(card_number):
    digits = [int(d) for d in card_number]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total = sum(digits)
    return total % 10 == 0

def validate_credit_card(card_number):
    if not card_number.isdigit():
        return False
    return luhn_algorithm(card_number)

card_number = input("Enter your credit card number: ")

if validate_credit_card(card_number):
    print("Valid credit card number.")
else:
    print("Invalid credit card number.")