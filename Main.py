from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("7x6 Button Grid")

# Initialize variables
clicked = True
count = 0
my_red_list = []
my_blue_list = []
# Create a 2D list (array) of buttons
buttons = [[None for _ in range(6)] for _ in range(7)]

def b_click(r, c):
    global clicked, count

    b = buttons[r][c]  # the clicked button
    columns = c
    if b["bg"] == "SystemButtonFace" and clicked == True:
        b["bg"] = "red"
        clicked = False
        count += 1
        print(f"Clicked at row={r}, col={c}")
        my_red_list.append([r,c])
    elif b["bg"] == "SystemButtonFace" and clicked == False:
        b["bg"] = "blue"
        clicked = True
        count += 1
        print(f"Clicked at row={r}, col={c}")
        my_blue_list.append([r,c])
    else:
        messagebox.showerror("Error", f"Already clicked at row={r}, col={c}")

    disableRunner()
    checkForWin()

def disableRunner():
    for r in range(7):
        for c in range(6):
            but = buttons[r][c]
            flag = True
            if (r == 6):
                but["text"] = "enable"
                but["state"] = "normal"
            else:
                for t in range(r+1, 7):
                    if buttons[t][c]["bg"] == "SystemButtonFace":
                        flag = False
                if flag:
                    but["text"] = "enable"
                    but["state"] = "normal"
                else:
                    but["text"] = "disable"
                    but["state"] = "disable"


def checkForWin():
    draw = True
    for r in range(7):
        for c in range(6):
            but = buttons[r][c]
            if (but["bg"] == "SystemButtonFace"):
                draw = False
                break
    if (draw):
        messagebox.showinfo("Game Over", "Game Ends in Tie. Click OK to reset.")
        reset()


    for r in range(7):
        for c in range(6):
            but = buttons[r][c]
            if (but["bg"] == "red"):
                if not([r,c] in my_red_list):
                    my_red_list.append([r,c])
    print(my_red_list)

    for r in range(7):
        for c in range(6):
            but = buttons[r][c]
            if (but["bg"] == "blue"):
                if not([r,c] in my_blue_list):
                    my_blue_list.append([r,c])
    print(my_blue_list)

    z = 1

    foundRedWinner = False
    for x in my_red_list:
        up = 1
        up = checkUp(up, x[0], x[1], my_red_list)
        print(up)
        if (up == 4):

            foundRedWinner = True
            break
        right = 1
        right = checkRight(right ,x[0], x[1], my_red_list)
        if (right == 4):
            foundRedWinner = True
            break
        diag = 1
        diag = checkUpRight(diag, x[0], x[1], my_red_list)
        if (diag == 4):
            foundRedWinner = True
            break

        Otherdiag = 1
        Otherdiag = checkDownRight(Otherdiag, x[0], x[1], my_red_list)
        if (Otherdiag == 4):
            foundRedWinner = True
            break
    foundBlueWinner = False
    for x in my_blue_list:
        up = 1
        up = checkUp(up, x[0], x[1], my_blue_list)
        print(up)
        if (up == 4):

            foundBlueWinner = True
            break
        right = 1
        right = checkRight(right ,x[0], x[1], my_blue_list)
        if (right == 4):
            foundBlueWinner = True
            break
        diag = 1
        diag = checkUpRight(diag, x[0], x[1], my_blue_list)
        if (diag == 4):
            foundBlueWinner = True
            break

        Otherdiag = 1
        Otherdiag = checkDownRight(Otherdiag, x[0], x[1], my_blue_list)
        if (Otherdiag == 4):
            foundBlueWinner = True
            break

    # print("do we win through up" , up)
    # print("do we win through right" , right)
    # print("do we win through diag", diag)
    # print("do we win through otherdiag", Otherdiag)

    if (foundRedWinner):
        messagebox.showinfo("Game Over", "Red wins. Click OK to reset.")
        reset()
        foundRedWinner = False
    if (foundBlueWinner):
        messagebox.showinfo("Game Over", "Blue wins. Click OK to reset.")
        reset()
        foundBlueWinner = False

def reset():
    clicked = True
    count = 0
    my_red_list.clear()
    my_blue_list.clear()
    for r in range(7):
        for c in range(6):
             but = buttons[r][c]
             but["bg"] = "SystemButtonFace"
             but["state"] = "normal"
             but["text"] = "normal"

    disableRunner()

    pass
def checkUp(up, a, b, my_list):
    if (a==-1):
        print("escsaping the out of bounds")
        return up
    if (up == 4):
        print("reached the four")
        return up
    if [a-1, b] in my_list:
        print("we should be incrementing")
        up = up +1
        return checkUp(up, a -1, b, my_list)
    return up

def checkRight(right, a, b, my_list):
    if (b == 6):
        print("escsaping the out of bounds")
        return right
    if (right == 4):
        print("reached the four")
        return right
    if [a, b+1] in my_list:
        print("we should be incrementing")

        right = right +1
        print(right)
        return checkRight(right,a, b+1, my_list)
    return right
def checkUpRight(diag, a, b, my_list):
    if (a==-1 or b == 6):
        print("escsaping the out of bounds")
        return diag
    if (diag == 4):
        print("reached the four")
        return diag
    if [a-1, b+1] in my_list:
        print("we should be incrementing")

        diag = diag +1
        print(diag)
        return checkUpRight(diag, a-1, b+1, my_list)
        
def checkDownRight(Otherdiag, a, b, my_list):
    if (a==7 or b == 6):
        print("escsaping the out of bounds")
        return Otherdiag
    if (Otherdiag == 4):
        print("reached the four")
        return Otherdiag
    if [a+1, b+1] in my_list:
        print("we should be incrementing")

        Otherdiag = Otherdiag +1
        print(Otherdiag)
        return checkDownRight(Otherdiag, a+1, b+1, my_list)


# Create 7x6 grid of buttons
for r in range(7):
    for c in range(6):
        buttons[r][c] = Button(
            root,
            text=" ",
            font=("Helvetica", 20),
            height=2,
            width=4,
            bg="SystemButtonFace",
            command=lambda r=r, c=c: b_click(r, c)   # capture row, col
        )
        buttons[r][c].grid(row=r, column=c)

disableRunner()


root.mainloop()
