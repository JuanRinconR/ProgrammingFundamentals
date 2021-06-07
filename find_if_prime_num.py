def find_if_prime_num(check_prime):
    """ This function checks if any of the numbers represented are prime or not
    input: (list) check_prime
    output: (list) is_prime_number
    """
    is_prime_number = []
    for num in check_prime:
        # search for factors, iterating through numbers ranging from 2 to the number itself
        for i in range(2, num):
            # print(i)
            # number is not prime if modulo is 0
            if (num % i) == 0:
                # print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
                is_prime_number.append(False)
                break
            # otherwise keep checking until we've searched all possible factors, and then declare it prime
            if i == num - 1:
                is_prime_number.append(True)
                # print("{} IS a prime number".format(num)
    return is_prime_number


if __name__ == "__main__":
    print("Example of code with input [39, 26, 40, 10]")
    my_list_of_numbers = [7, 11, 39, 26, 40, 10, 81, 97, 71]
    isPrimeNumber = find_if_prime_num(my_list_of_numbers)
    print(isPrimeNumber)
