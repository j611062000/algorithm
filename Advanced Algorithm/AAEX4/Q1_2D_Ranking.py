import pdb
import matplotlib.pyplot as plt


class point():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rank = 0


def raw_data_to_class_type(raw_data):
    temp = list()
    for element in raw_data:
        temp.append(point(element[0], element[1]))
    return temp


def L_finding(length_of_array):
    if length_of_array % 2 == 1:
        return (length_of_array - 1) / 2
    else:
        return ((length_of_array) / 2) - 1


def print_element(array):
    for element in array:
        print("(x,y) = ({},{}), rank = {}".format(
            element.x, element.y, element.rank))

# update the attribute, rank


def find_rank(array):

    if len(array) == 1:
        array[0].rank = 0

        return array

    else:
        # the median position in the array
        L = int(L_finding(len(array)))

        left = sorted(find_rank(array[:L + 1]), key=lambda x: x.y)
        right = sorted(find_rank(array[L + 1:]), key=lambda x: x.y)

        left_y = 0
        for right_element in right:
            if left_y <= L:
                while right_element.y > left[left_y].y:
                    left_y += 1
                    if left_y > L:
                        break
            right_element.rank += (left_y)

        return left + right


if __name__ == "__main__":
    # array: The elements are coordinate !
    unsorted_x_input = [(1, 2), (3, 4), (5, 6), (7, 9),(1,1)]
    sorted_x_input = sorted(unsorted_x_input, key=lambda x: x[0])
    processed_data = raw_data_to_class_type(sorted_x_input)
    print_element(find_rank(processed_data))
