def find_if_odd_num(num_list):
    sorted_numbers = sorted(num_list)
    count = 0
    odd_numbers = []
    for i in sorted_numbers:
        if i % 2 != 0:
            count += 1
            odd_numbers.append(i)

        if count == 5:
            break


    return odd_numbers

if __name__ == "__main__":
    print("Example of code with input [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312,"
          "542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]")
    my_list_of_numbers = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312,
            542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
    isOddNumber = find_if_odd_num(my_list_of_numbers)
    print(("{} are the first five odd numbers of the list".format(isOddNumber)))