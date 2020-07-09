import time
import tkinter as tk

sudoku = [[],[],[],[],[],[],[],[],[]]
backtracks=0
window=tk.Tk()
t=""

def isValid(row,col,n):
    for i in range(0,9):
        if sudoku[row][i]==n:
            return False
    for i in range(0,9):
        if sudoku[i][col]==n:
            return False
    sub_row=(row//3)*3
    sub_col=(col//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[sub_row+i][sub_col+j]==n:
                return False
    return True

def makeSudoku():
    matrix = input("Enter the puzzle: \n")

    #sudoku = [[],[],[],[],[],[],[],[],[]]
    for i in range(0,81):
        if i<9:
            sudoku[0].append(int(matrix[i]))
        elif i<18:
            sudoku[1].append(int(matrix[i]))
        elif i<27:
            sudoku[2].append(int(matrix[i]))
        elif i<36:
            sudoku[3].append(int(matrix[i]))
        elif i<45:
            sudoku[4].append(int(matrix[i]))
        elif i<54:
            sudoku[5].append(int(matrix[i]))
        elif i<63:
            sudoku[6].append(int(matrix[i]))
        elif i<72:
            sudoku[7].append(int(matrix[i]))
        elif i<81:
            sudoku[8].append(int(matrix[i]))

    print("\nGiven puzzle:-")
    for i in sudoku:
        print(i)




def solve():
    for x in range(9):
        for y in range(9):
            if sudoku[x][y]==0:
                for i in range(1,10):
                    if isValid(x,y,i):
                        sudoku[x][y]=i
                        solve()
                        sudoku[x][y]=0
                return

    for i in sudoku:
        print(i)

def main():
    makeSudoku()
    print("\nSolution:-")
    t1 = time.time()
    solve()
    t2 = time.time()
    print("\ntime taken - ", round(t2 - t1, 2), "s\n")


if __name__ == "__main__":
    while True:
        main()
        t = ""
        sudoku = [[], [], [], [], [], [], [], [], []]
