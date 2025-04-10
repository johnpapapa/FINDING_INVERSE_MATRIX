import sys
import pprint
import copy
import re

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
            for j in range(len(B)):
                z += A[i][j] * B[j][k]
            line.append(z)
        C.append(line)
    return C


# ユーザー入力の受け取り
def input_row() -> str:
    row_str = input(">> ")
    if row_str == "":
        return ""
    if not re.fullmatch(r"^\d+(\s+\d+)*$", row_str):
        raise ValueError("Invalid input. Please enter numbers separated by spaces.")
    return row_str

# ユーザー入力をリストに整形
def format_row(row_str:str) -> list:
    row_list = row_str.split()
    row_list = [int(val) for val in row_list if val != ""]
    return row_list

# ユーザー入力の検証
def validate_input(matrix, row) -> bool:
    last_matrix_row_length = len(matrix[-1]) if matrix != [] else -1
    input_row_length = len(row)

    # 既に行列が存在する場合要素数が一致するかの判定
    if(last_matrix_row_length > 0 and last_matrix_row_length != input_row_length):
        raise ValueError("The number of elements in the rows does not match.")
    
    # 列の大きさが要素数以下かの判定
    last_matrix_column_length = len(matrix)
    if last_matrix_column_length >= input_row_length:
        raise ValueError("The number of elements in the columns does not match.")
    
    return True

#正方行列であるかの検証
def validate_square_matrix(matrix) -> bool:
    return all([True if len(i) == len(matrix) else False for i in matrix])

# 行列の入力部
def input_matrix() -> list:
    print("Please input matrix.")
    print("Enter a number with a space between the numbers.")
    print("To finish typing, press enter twice.")

    input_matrix = []
    while True:
        try:
            row_str = input_row()

            if row_str == "": #入力値が空の場合入力を終了
                break

            row_list = format_row(row_str)
            validate_input(input_matrix, row_list)
            
            input_matrix.append(row_list)
        except Exception as E:
            print(E)
            input_matrix = []
            break
    return input_matrix

# メインループ
def main() -> None:
    #初期化処理
    matrix = input_matrix()
    if matrix == []:
        print("Invalid input.")
        return

    result = validate_square_matrix(matrix)
    if not result:
        print("This matrix is not a square matrix.")
        return
    
    print("[ input matrix ]")
    disp_matrix(matrix)

    try:
        matrix_cp = copy.deepcopy(matrix)
        matrix_inv = inverse_matrix(matrix_cp)
        identity_matrix = multiply_matrix(matrix, matrix_cp)
    except ZeroDivisionError:#正則行列でない場合
        print("is this This matrix is not a regular matrix")
        print("Unable to find inverse matrix.")
        return
    
    print("[ inverse matrix ]")
    disp_matrix(matrix_inv)

    print("[ identity matrix ]")
    disp_matrix(identity_matrix)
    
    

if __name__ == "__main__":
    main()
