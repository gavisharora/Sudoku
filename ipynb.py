import itertools

arr = [[3, 0, 8, 0, 7, 4, 0, 2, 9],
       [7, 0, 0, 2, 0, 0, 0, 6, 0],
       [0, 6, 2, 0, 9, 0, 0, 0, 3],
       [0, 0, 0, 4, 0, 0, 5, 0, 7],
       [6, 0, 4, 0, 0, 0, 2, 0, 1],
       [2, 0, 5, 0, 0, 3, 0, 0, 0],
       [5, 0, 0, 0, 4, 0, 9, 1, 0],
       [0, 1, 0, 0, 0, 8, 0, 0, 4],
       [4, 2, 0, 9, 1, 0, 6, 0, 8]]

zeroes = []
possiblerows=[]
solutions=[]

def findzeroes(a):
    for j in range(0, len(a)):
        if a[j] == 0:
            zeroes.append(j)


def combinations(a):
    '''for k in range(0, 10):
        a[zeroes[0]] = k
        for l in range(0,10):
            a[zeroes[1]]=l
            for m in range(0,10):
                a[zeroes[2]] = m
                if check(a):
                    #print(a)'''
    global possiblerows
    '''ob = itertools.combinations(zeroes,len(zeroes))
    oblist = list(ob)

    oc = itertools.combinations([1,2,3,4,5,6,7,8,9],len(oblist[0]))
    oclist=list(oc)

    for i in oclist:
        print(i)'''
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for p in itertools.product(x, repeat=len(zeroes)):

        for i in range(0, len(zeroes)):
            a[zeroes[i]] = p[i]
        if checkrows(a):
            possiblerows.append(list(a))
            #print(a)


def checkrows(a):
    if (sum(a) == 45) and (len(set(a)) == 9):
        return True


def solverows(a):
    findzeroes(a)
    combinations(a)
    # print(zeroes)
    zeroes = []


if __name__ == "__main__":
    '''for i in range(0,9):
        solverows(arr[i])
        print("possible rows")
        print(possiblerows)
        zeroes=[]
        possiblerows = []'''
    print(arr[2][3])

