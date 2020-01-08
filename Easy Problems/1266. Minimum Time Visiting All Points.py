def minTimeToVisitAllPoints(points):
    sum = 0
    for i in range(len(points)-1):
        if (points[i] == points[i+1]):
            continue
        elif (points[i][0] == points[i+1][0] and points[i][1] != points[i+1][1]):
            sum = sum + 1
        elif (points[i][1] == points[i+1][1] and points[i][0] != points[i+1][0]):
            sum = sum + 1
        else:
            print("exec")
            if (abs(points[i][0] - points[i+1][0]) < abs(points[i][1]-points[i+1][1])):
                sum = sum + abs(points[i][0] - points[i+1][0])
            else:
                sum = sum + abs(points[i][1]-points[i+1][1])
        print(sum)
    return sum
print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))