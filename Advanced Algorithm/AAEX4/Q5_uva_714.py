def min_max(data, k):
    lb, ub = max(data), sum(data)
    mid = (lb + ub) // 2
    c = 0
    result = dict()

    while lb < ub:
        # if mid is the min_max, can we find out way that the number of the
        # partition is <= k ?
        k_is_to_small = False
        capacity_of_partition, accumulated_k = 0, 0

        for element in data:

            if (element + capacity_of_partition) <= mid and accumulated_k < k:
                capacity_of_partition += element

            elif accumulated_k < k:
                accumulated_k += 1
                capacity_of_partition = element
            else:
                k_is_to_small = True

        if mid in result:
            break

        result[mid] = k_is_to_small    
        if k_is_to_small:
            mid = (ub + lb) // 2

        else:
            ub = mid
            mid = (ub + lb) // 2
    return min(result.keys())

if __name__ == '__main__':
    data = [1, 2, 4, 1, 5, 2, 1,10,4,9,8]
    k = 3
    print(min_max(data, k))
