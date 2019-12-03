arr = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0]

def main(arr):
    # split arrays in groups of 4
    for i in range(0,len(arr), 4):
        temp = arr[i:i+4]
        
        if temp[0] == 1:
            a, b = arr[temp[1]], arr[temp[2]]
            sumIt = a + b
            arr[temp[3]] = sumIt

        # check for opcode multiplication
        elif temp[0] == 2:
            c, d = arr[temp[1]], arr[temp[2]]
            mult = c * d
            arr[temp[3]] = mult
            
        elif temp[0] == 99:
            return arr[0]
    
    
if __name__ == "__main__":
    print(main(arr))


