def zero_to_end(numbers):
    for number in numbers:
        if number == 0:
            index = numbers.index(number)
            numbers = numbers[:index] + numbers[index+1:] + [0]
    return numbers


def n_th_row(n):
    return n**3

