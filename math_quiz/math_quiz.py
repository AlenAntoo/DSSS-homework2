import random

def get_random_integer(min_value, max_value):
    """
    Generates a random integer within a specified range.

    Parameters:
        min_value (int): The minimum value of the range.
        max_value (int): The maximum value of the range.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def get_random_operator():
    """
    Selects a random arithmetic operator.

    Returns:
        str: A random operator ('+', '-', '*').
    """
    return random.choice(['+', '-', '*'])

def generate_problem(num1, num2, operator):
    """
    Creates a math problem as a string and calculates the correct answer based on the operator.

    Parameters:
        num1 (int): The first number in the problem.
        num2 (int): The second number in the problem.
        operator (str): The operator for the problem ('+', '-', '*').

    Returns:
        tuple: A tuple containing the problem as a string and the correct answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator
        num1 = get_random_integer(1, 10)
        num2 = get_random_integer(1, 5)  # Fixed the second argument to be an integer
        operator = get_random_operator()

    
        problem, correct_answer = generate_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print( 'Please enter an integer.')
            continue  # Skip to the next question

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
