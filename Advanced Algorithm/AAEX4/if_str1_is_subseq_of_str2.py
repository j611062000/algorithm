# str1 is shorter than str2
def str1_is_subseq_of_str2(str1, str2, start_of_str1=0):
    for char in str2:
        if char == str1[start_of_str1]:
            start_of_str1 += 1
    if start_of_str1 == len(str1):
    	return True
    else:
    	return False

if __name__ == "__main__":
    str2 = "Apple"
    str1 = "pke"
    print(str1_is_subseq_of_str2(str1, str2))
