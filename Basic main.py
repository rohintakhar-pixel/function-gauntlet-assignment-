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


if __name__ == "__main__":
    print("is_even(6) =", is_even(6))
    print("is_even(7) =", is_even(7))

    print("count_vowels('Python') =", count_vowels("Python"))
    print("count_vowels('Hello World') =", count_vowels("Hello World"))

    print("celsius_to_fahrenheit(25) =", celsius_to_fahrenheit(25))
    print("celsius_to_fahrenheit(100) =", celsius_to_fahrenheit(100))

    print("reverse_text('Rohin') =", reverse_text("Rohin"))
    print("reverse_text('Python') =", reverse_text("Python"))

    print("larger_number(67, 21) =", larger_number(67, 21))
    print("larger_number(3, 9) =", larger_number(3, 9))

    print("average_two(67, 31) =", average_two(67, 31))
    print("average_two(10, 20) =", average_two(10, 20))

    print("can_afford(20, 10) =", can_afford(20, 10))
    print("can_afford(5, 10) =", can_afford(5, 10))

    print("repeat_text('Hi', 5) =", repeat_text("Hi", 5))
    print("repeat_text('Go!', 3) =", repeat_text("Go!", 3))

    print("contains_word(..., 'Bob') =", contains_word("Hi my name is Bob", "Bob"))
    print("contains_word(..., 'Alice') =", contains_word("Hi my name is Bob", "Alice"))

    print("calculate_tip(50, 5) =", calculate_tip(50, 5))
    print("calculate_tip(100, 10) =", calculate_tip(100, 10))

    print("make_initials('Rohin', 'Takhar') =", make_initials("Rohin", "Takhar"))
    print("make_initials('grace', 'hopper') =", make_initials("grace", "hopper"))

    print("percent_score(50, 100) =", percent_score(50, 100))
    print("percent_score(5, 0) =", percent_score(5, 0))

    print("is_between(67, 60, 70) =", is_between(67, 60, 70))
    print("is_between(90, 60, 70) =", is_between(90, 60, 70))

    print("all_different('cat', 'dog', 'bird') =", all_different("cat", "dog", "bird"))
    print("all_different('cat', 'cat', 'bird') =", all_different("cat", "cat", "bird"))

    print("average_three(67, 31, 21) =", average_three(67, 31, 21))
    print("average_three(10, 20, 30) =", average_three(10, 20, 30))

    print("describe_temperature(67, -25, 80) =", describe_temperature(67, -25, 80))
    print("describe_temperature(90, -25, 80) =", describe_temperature(90, -25, 80))
    print("describe_temperature(-30, -25, 80) =", describe_temperature(-30, -25, 80))
