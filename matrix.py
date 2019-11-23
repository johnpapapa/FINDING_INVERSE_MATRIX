import sys
import pprint
import copy

def disp_matrix(matrix):
    for y in matrix:
        print("|",end="")
        for x in y:
            print("{:^3,.0f}".format(x),end="")
        print("|")
    print("")
    
def inverse_matrix(before_matrix):
    n = len(before_matrix)
    after_matrix = []

    for i in range(n):
        x = []
        for j in range(n):
            if i == j:
                x.append(1)
            else:
                x.append(0)
        after_matrix.append(x)
        
    tmp = 0
    for i in range(n):#vertical
        tmp = 1 / before_matrix[i][i] #Derive the reciprocal
        
        for j in range(n):#row
            before_matrix[i][j] *= tmp
            after_matrix[i][j] *= tmp

        for j in range(n):#vertical
            if(i != j):
                tmp = before_matrix[j][i]
                for k in range(n):
                    before_matrix[j][k] -= before_matrix[i][k] * tmp
                    after_matrix[j][k] -= after_matrix[i][k] * tmp
    return after_matrix

def multiply_matrix(A, B):
    C = []
    for k in range(len(A)):
        line = []
        for i in range(len(A[0])):
            z = 0
            s = ""
            for j in range(len(B)):
                z += A[i][j] * B[j][k]
            line.append(z)
        C.append(line)
    return C

if __name__ == "__main__":
    print("Please input matrix.")
    print("Enter a number with a space between the numbers.")
    print("To finish typing, press enter twice.")
    input_matrix = []
    while True:
        s = input(">> ")
        if(s == ""):
            break
        else:
            s = s.split()
            input_matrix.append([int(S) for S in s])
    
    print("input matrix")
    disp_matrix(input_matrix)

    if(all([True if len(i) == len(input_matrix) else False for i in input_matrix])):
        try:
            matrix = copy.deepcopy(input_matrix)
            inv_matrix = inverse_matrix(matrix)
            identity_matrix = multiply_matrix(input_matrix, inv_matrix)
        except ZeroDivisionError:#正則行列でない場合
            print("is this This matrix is not a regular matrix")
            print("Unable to find inverse matrix.")
    
        print("inverse matrix")
        disp_matrix(inv_matrix)

        print("identity matrix")
        disp_matrix(identity_matrix)
    else:#正方行列でない場合
        print("This matrix is not a square matrix.")
        print("Unable to find inverse matrix.")
        

    

    
