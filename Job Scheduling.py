def printJobScheduling(arr, t): 
 
    n = len(arr) 
 
    # Sort all jobs according to 
    # decreasing order of profit 
    for i in range(n): 
        for j in range(n - 1 - i): 
            if arr[j][2] < arr[j + 1][2]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
 
    # To keep track of free time slots 
    result = [False] * t 
 
    # To store result (Sequence of jobs) 
    job = ['-1'] * t 
 
    # Iterate through all given jobs 
    for i in range(len(arr)): 
 
        # Find a free slot for this job 
        # (Note that we start from the 
        # last possible slot) 
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1): 
 
            # Free slot found 
            if result[j] is False: 
                result[j] = True 
                job[j] = arr[i][0] 
                break 
    profit = 0 
    for i in range(n): 
        for j in range(4): 
            if arr[i][0] == job[j]: 
                profit = profit + arr[i][2] 
    # print the sequence 
    print("\n Maximum profit sequence of jobs : ",job) 
 
    print("\nMaximum profit of jobs : ",profit) 
     
 
# Driver's Code 
if __name__ == '__main__': 
    arr = [['J1', 1, 3], # Job Array 
            ['J2', 3, 5], 
            ['J3', 4, 20], 
            ['J4', 3, 18], 
            ['J5', 2, 0], 
            ['J6', 1, 6], 
            ['J7', 2, 30]] 
     
    n = len(arr) 
    print("\nJobs are\n") 
    for i in range(n): 
        print(arr[i]) 
 
    # Function Call 
    printJobScheduling(arr, 4)