import random


class chip:

    def __init__(self, real_identity, number):
        self.number = number
        self.real_identity = real_identity

    def __str__(self):
        return "Number:{}, real_identity:{}".format(self.number, self.real_identity)


def print_chip(data_set):
    for element in data_set:
        print(element)


def abandon_1_or_2(chip1, chip2):
    if (chip1 and chip2):
        return 1
    else:
        return 2


def test_result(chip1, chip2):
    if (chip1 and chip2) or (not chip1 and not chip2):
        return True, True
    else:
        return random.choice([(False, False), (True, False)])


def pair_test(data_set):
    if len(data_set) == 1:
        return "The chip ({}) is good!".format(data_set[0])

   
    else:
        remaining_chips = list()
        if len(data_set) % 2 == 0:
            length = len(data_set)
        else:
            length = len(data_set) - 1
            remaining_chips.append(data_set[-1])

        for i in range(0, length, 2):

            chip1, chip2 = test_result(
                data_set[i].real_identity, data_set[i + 1].real_identity)

            if abandon_1_or_2(chip1, chip2) == 1:
                remaining_chips.append(data_set[i])
        
        if len(remaining_chips) == 2:
            return remaining_chips[-1]


    return pair_test(remaining_chips)


if __name__ == "__main__":
    data = [[0,1,1],[1,0,0],[1,0,1],[1,1,0]]
    data_set = list()
    for count, element in enumerate(data[-1]):
        data_set.append(chip(element, count + 1))
    print(pair_test(data_set))
