"""
Tic-Tac-toe judge
"""

data = [
    "OOX",
    "XXO",
    "OXX"
 ]
result = ''
length = len(data)

while not result:
    result = f'-> D'
    #1st diagonal
    if data[0][0] == data[1][1] == data[2][2]:
        #print(f'-> {data[0][0]} 1st diagonal')
        result = f'-> {data[0][0]} 1st diagonal'
    #2st diagonal
    if data[2][0] == data[1][1] == data[0][2]:
        #print(f'-> {data[2][0]} 2st diagonal')
        result = f'-> {data[2][0]} 2st diagonal'
    #horizontal&vertical
    for i in range(length):
        #horizontal
        if data[i][0] == data[i][1] == data[i][2]:
            #print(f'-> {data[i][0]} horizontal')
            result = f'-> {data[i][0]} horizontal'
            break
        #vertical
        elif data[0][i] == data[1][i] == data[2][i]:
            #print(f'-> {data[0][i]} vertical')
            result = f'-> {data[0][i]} vertical'
            break    
print(result)
