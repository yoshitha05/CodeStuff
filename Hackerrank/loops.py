if __name__ == '__main__':
    n = int(input())
    
# n can taken as input 5
squares_list = []

# add numbers less than 5 to the list
for i in range(0, n):
    squares_list.append(i**2)
    
# print individual numbers in list after squaring
for i in squares_list:
    print(i)
