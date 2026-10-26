def is_even(number: int) -> bool:
    """Return True if number is even, False if odd.

    :param number: 6
    :return: True if number is even, False otherwise
    """
    return number % 2 == 0


def count_vowels(text: str) -> int:
    """Count the vowels in text.

    :param text: Python
    :return: how many vowels appear in text
    """
    count = 0
    for letter in text.lower():
        if letter in "aeiou":
            count += 1
    return count


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit.

    :param celsius: 25
    :return: the temperature in Fahrenheit
    """
    return celsius * 9 / 5 + 32


def reverse_text(text: str) -> str:
    """Reverse the characters in text.

    :param text: Rohin
    :return: text reversed
    """
    return text[::-1]


def larger_number(a: int, b: int) -> int:
    """Return the larger of two integers.

    :param a: 67
    :param b: 21
    :return: the larger value
    """
    if a >= b:
        return a
    return b


def average_two(a: int, b: int) -> float:
    """Average two integers.

    :param a: 67
    :param b: 31
    :return: the average of a and b
    """
    return (a + b) / 2


def can_afford(balance: float, cost: float) -> bool:
    """Check if balance covers cost.

    :param balance: 20
    :param cost: 10
    :return: True if balance >= cost, False otherwise
    """
    return balance >= cost


def repeat_text(text: str, times: int) -> str:
    """Repeat text a number of times.

    :param text: Hi
    :param times: 5
    :return: text repeated times times
    """
    return text * times


def contains_word(sentence: str, word: str) -> bool:
    """Check if word is inside sentence.

    :param sentence: Hi my name is Bob
    :param word: Bob
    :return: True if word is found, False otherwise
    """
    return word in sentence


def calculate_tip(cost: float, percent: float) -> float:
    """Calculate a tip amount.

    :param cost: 50
    :param percent: 5
    :return: the tip amount
    """
    return cost * percent / 100


def make_initials(first_name: str, last_name: str) -> str:
    """Get uppercase initials from two names.

    :param first_name: Rohin
    :param last_name: Takhar
    :return: the uppercase initials
    """
    return first_name[0].upper() + last_name[0].upper()


def percent_score(points: int, possible: int) -> float | None:
    """Calculate percent of points earned.

    :param points: 50
    :param possible: 100
    :return: percent earned, or None if possible < 1
    """
    if possible < 1:
        return None
    return points / possible * 100


def is_between(number: int, minimum: int, maximum: int) -> bool:
    """Check if number is within an inclusive range.

    :param number: 67
    :param minimum: 60
    :param maximum: 70
    :return: True if in range, False otherwise
    """
    return minimum <= number <= maximum


def all_different(a: str, b: str, c: str) -> bool:
    """Check if three strings are all different.

    :param a: cat
    :param b: dog
    :param c: bird
    :return: True if all different, False otherwise
    """
    return a != b and b != c and a != c


def average_three(a: int, b: int, c: int) -> float:
    """Average three integers.

    :param a: 67
    :param b: 31
    :param c: 21
    :return: the average of a, b, and c
    """
    return (a + b + c) / 3


def describe_temperature(temperature: float, cold_limit: float, hot_limit: float) -> str:
    """Describe a temperature as cold, hot, or comfortable.

    :param temperature: 67
    :param cold_limit: -25
    :param hot_limit: 80
    :return: "cold", "hot", or "comfortable"
    """
    if temperature < cold_limit:
        return "cold"
    if temperature > hot_limit:
        return "hot"
    return "comfortable"


def temperature_in_safe_range(celsius: float, minimum_f: float, maximum_f: float) -> bool:
    """Convert celsius to Fahrenheit and check it against safe Fahrenheit limits.

    :param celsius: 20
    :param minimum_f: 60
    :param maximum_f: 75
    :return: True if the converted temperature is within range, False otherwise
    """
    fahrenheit = celsius_to_fahrenheit(celsius)
    return is_between(fahrenheit, minimum_f, maximum_f)


def can_afford_with_tip(balance: float, cost: float, tip_percent: float) -> bool:
    """Calculate a tip, add it to cost, and check the total against balance.

    :param balance: 50
    :param cost: 40
    :param tip_percent: 15
    :return: True if balance covers cost plus the tip, False otherwise
    """
    tip = calculate_tip(cost, tip_percent)
    total = cost + tip
    return can_afford(balance, total)


def meets_average(score1: int, score2: int, score3: int, required_average: float) -> bool:
    """Average three scores and check the average against a required value.

    :param score1: 80
    :param score2: 90
    :param score3: 70
    :param required_average: 75
    :return: True if the average is >= required_average, False otherwise
    """
    average = average_three(score1, score2, score3)
    return average >= required_average


def initials_match(first_name: str, last_name: str, expected_initials: str) -> bool:
    """Build initials from a name and compare them to expected_initials.

    :param first_name: Rohin
    :param last_name: Takhar
    :param expected_initials: RT
    :return: True if the initials match expected_initials, False otherwise
    """
    initials = make_initials(first_name, last_name)
    return initials == expected_initials.upper()


if __name__ == "__main__":
    print("temperature_in_safe_range(20, 60, 75) =", temperature_in_safe_range(20, 60, 75))
    print("temperature_in_safe_range(0, 60, 75) =", temperature_in_safe_range(0, 60, 75))

    print("can_afford_with_tip(50, 40, 15) =", can_afford_with_tip(50, 40, 15))
    print("can_afford_with_tip(30, 40, 15) =", can_afford_with_tip(30, 40, 15))

    print("meets_average(80, 90, 70, 75) =", meets_average(80, 90, 70, 75))
    print("meets_average(60, 65, 70, 75) =", meets_average(60, 65, 70, 75))

    print("initials_match('Rohin', 'Takhar', 'RT') =", initials_match("Rohin", "Takhar", "RT"))
    print("initials_match('rohin', 'takhar', 'xy') =", initials_match("rohin", "takhar", "xy"))

    try:
        celsius_input = float(input("Enter a Celsius reading: "))
        minimum_input = float(input("Enter the safe minimum (F): "))
        maximum_input = float(input("Enter the safe maximum (F): "))
        print("temperature_in_safe_range result =", temperature_in_safe_range(celsius_input, minimum_input, maximum_input))
    except ValueError:
        print("Please enter numbers only.")

    try:
        balance_input = float(input("Enter your balance: "))
        cost_input = float(input("Enter the cost: "))
        tip_input = float(input("Enter the tip percent: "))
        print("can_afford_with_tip result =", can_afford_with_tip(balance_input, cost_input, tip_input))
    except ValueError:
        print("Please enter numbers only.")
