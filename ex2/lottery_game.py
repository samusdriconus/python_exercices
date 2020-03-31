import random

def generate_output():
    container = range(1,51)
    output = []
    for i in range(10):
        choice = random.choice(container)
        output.append(choice)
        output.sort()
    return output

