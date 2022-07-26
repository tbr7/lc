def find_averages_of_subarrays(K, arr):
    res = []
    print(arr)
    window_sum = sum(arr[0:K-1])
    window_start = 0
    for i in range(K-1, len(arr)):
        window_sum += arr[i]
        res.append(window_sum / K)
        window_sum -= arr[window_start]
        window_start += 1

    return res

# Lesson here with this one is instead of starting with K-1 or worrying about off by one
# instead do the below

def find_averages_of_subarrays_official(K, arr):
    res = []
    window_sum, window_start = 0.0, 0
    for end in range(len(arr)):
        window_sum += arr[end] # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'K'
        if end >= K - 1:
            res.append(window_sum / K)
            window_sum -= arr[window_start]
            window_start += 1
    return res


def main():
	result = find_averages_of_subarrays_official(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
	print("Averages of subarrays of size K: " + str(result))

if __name__ == "__main__":
    main()



