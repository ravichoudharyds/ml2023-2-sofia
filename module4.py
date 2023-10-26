import sys
def input_validation(N):
    try:
        N = int(N)
        return N
    except ValueError:
        raise ValueError("Error! Please restart the script and enter a number")

if __name__ == "__main__":

    N = input("Please input a positive number N:")
    N = input_validation(N)

    if N > 0:
        dict_num = {}
        for i in range(N):
            num_input = input("Please input a number:")
            input_validation(num_input)
            dict_num[num_input] = i
        search_num = input("Please input number to be searched X:")
        print(dict_num.get(search_num,-2)+1)
