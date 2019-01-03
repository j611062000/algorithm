def number_of_subsequence(str1, str2):
    temp = [1] + [0] * (len(str1))
    for char2 in str2:
        for count, char1 in enumerate(str1):
            print("Current loop stage: Outer:{}, Inner:{}".format(char2, char1))
        	
            if char2 == char1 and temp[-1 * (count + 2)] > 0:
                temp[-1 * (count + 1)] += temp[-1 * (count + 2)]
                print(["r", "a", "b", "b", "i", "t"])
                print(temp,end = "\n\n")
    return temp[-1]


if __name__ == "__main__":
    str2 = "rabbbit"
    str1 = "rabbit"
    # nanab
    number_of_subsequence(str1[::-1], str2)
