def falsecount(arr, row, column):

    count = 0;

    for i in range(8):
        if arr[i][column] == 1:
            count += 1

    for i,j in zip(range(row-1,-1,-1), range(column-1,-1,-1)):
        if arr[i][j] == 1:
            count += 1

    for i,j in zip(range(row+1, 8), range(column+1,8)):
        if arr[i][j] == 1:
            count += 1

    for i,j in zip(range(row-1,-1,-1), range(column+1,8)):
        if arr[i][j] == 1:
            count += 1

    for i,j in zip(range(row+1,8), range(column-1,-1,-1)):
        if arr[i][j] == 1:
            count += 1

    return count


def print_(arr):
    for i in range(8):
        for j in range(8):
            print(arr[i][j], end=" ")

        print()



def Queen_Hue(arr):
    row,count,column,count1 = (0,8,0,0)

    for i in range(8):
        count = 8
        for j in range(8):
            arr[i][j] = 0
            count1 = falsecount(arr, i, j)

            if count > count1:
                count = count1
                row = i
                column = j

        arr[row][column] = 1
        row = i+1
        column = 0

    print_(arr)


if __name__ == "__main__":

    arr = [ 8*[0] for i in range(8)]

    for i in range(8):
        arr[i][0] = 1

    Queen_Hue(arr)
