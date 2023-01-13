def greetings():
    print("Welcome to the game 'Naughts and crosses'")
    print("You need to enter two numbers, x and y")
    print("x - it is line's number, y -it is column's number")

field = [
     [" ",  " ", " "],
     [" ",  " ", " "],
     [" ",  " ", " "]
]

def view():
    print(f"  0 1 2")
    print(f"0 {field[0][0]} {field[0][1]} {field[0][2]}")
    print(f"1 {field[1][0]} {field[1][1]} {field[1][2]}")
    print(f"2 {field[2][0]} {field[2][1]} {field[2][2]}")

def inquiry():
    count = 0
    while True and count < 10:
        x = int(input("Enter the coordinate of your turn line: "))
        y = int(input("Enter the coordinate of your turn column: "))
        if 0 <= x <= 2 and 0 <= y <= 2:
            count += 1
            if field[x][y] == " ":
                return x,y
            else:
                print("Sorry, this place is busy")
        else:
            print("Your coordinates are out of the field")

def who_win():
    win = (((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)), ((0,2), (1,2), (2,2)), ((0,0), (1,0), (2,0)), ((0,1), (1,1), (2,1)), ((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0)))
    for move in win:
        symbols = []
        for b in move:
            symbols.append(field[b[0]][b[1]])
        if symbols == ["X", "X", "X"]:
            print("X - win")
            return True
        elif symbols == ["0", "0", "0"]:
            print("0 - win")
            return True
        return False

greetings()
count = 0
while True:
    count += 1
    view()
    if count % 2 == 1:
        print ("X - your turn")
    else:
        print("0 - your turn")
    x, y = inquiry()
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if who_win():
        break
    if count == 9:
        print("Run out, draw")
        break

