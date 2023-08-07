from tkinter import *
from tkinter import messagebox
import pygame

pygame.mixer.init()

def play_song():
    pygame.mixer.music.load("success-fanfare-trumpets-6185.mp3")
    pygame.mixer.music.play(loops=0)

def draw_song():
    pygame.mixer.music.load("game-over-arcade-6435.mp3")
    pygame.mixer.music.play(loops=0)

root = Tk()
root.title("Tic Tac Toe by Vinay")
root.geometry("800x800")

# global variables
player_character = ''
ai_character = ''
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
turn = 1
turns = 0
game_over = False


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        if board[position] == " ":
            if 0 <= position and position <= 2:
                r = 0
            elif 3 <= position and position <= 5:
                r = 1
            elif 6 <= position and position <= 8:
                r = 2

            if position == 0 or position == 3 or position == 6:
                c = 0
            elif position == 1 or position == 4 or position == 7:
                c = 1
            elif position == 2 or position == 5 or position == 8:
                c = 2

            board[position] =letter
            new_button = Button(frame_bottom, text=board[position], height=4, width=8).grid(row=r, column=c)

        if (checkDraw()):
            draw_song()
            win_message = messagebox.showinfo("Tic Tac Toe",
                                              "DRAW , If you want to play again select a character and hit start!")
            root.destroy()

        if checkForWin():
            if letter == 'X' and player_character=='X':
                play_song()
                win_message = messagebox.showinfo("Tic Tac Toe",
                                                  "YOU WON, If you want to play again select a character and hit start!")
            elif letter == 'O' and player_character=='O':
                play_song()
                win_message = messagebox.showinfo("Tic Tac Toe",
                                                  "YOU WON, If you want to play again select a character and hit start!")
            else:
                draw_song()
                win_message = messagebox.showinfo("Tic Tac Toe",
                                                  "AI WON, If you want to play again select a character and hit start!")
            root.destroy()


def checkForWin():
    if (board[0] == board[1] and board[0] == board[2] and board[0] != ' '):
        return True
    elif (board[3] == board[4] and board[3] == board[5] and board[3] != ' '):
        return True
    elif (board[6] == board[7] and board[6] == board[8] and board[6] != ' '):
        return True
    elif (board[0] == board[3] and board[0] == board[6] and board[0] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[0] == board[4] and board[0] == board[8] and board[0] != ' '):
        return True
    elif (board[6] == board[4] and board[6] == board[2] and board[6] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if board[0] == board[1] and board[0] == board[2] and board[0] == mark:
        return True
    elif (board[3] == board[4] and board[3] == board[5] and board[3] == mark):
        return True
    elif (board[6] == board[7] and board[6] == board[8] and board[6] == mark):
        return True
    elif (board[0] == board[3] and board[0] == board[6] and board[0] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[0] == board[4] and board[0] == board[8] and board[0] == mark):
        return True
    elif (board[6] == board[4] and board[6] == board[2] and board[6] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in range(9):
        if (board[key] == ' '):
            return False
    return True


def playerMove(position):
    if board[position]==" ":
        insertLetter(player_character, position)
        compMove()


def compMove():
    bestScore = -10
    bestMove = 0
    for key in range(9):
        if (board[key] == ' '):
            board[key] = ai_character
            score = minimax(board, False,-10,10)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(ai_character, bestMove)


def minimax(board,isMaximizing,alpha,beta):
    if (checkWhichMarkWon(ai_character)):
        return 1
    elif (checkWhichMarkWon(player_character)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -10
        for key in range(9):
            if (board[key] == ' '):
                board[key] = ai_character
                score = minimax(board,  False,alpha,beta)
                board[key] = ' '
                bestScore=max(score,bestScore)
                alpha=max(alpha,score)
                if beta<=alpha:
                    break
        return bestScore

    else:
        bestScore = 10
        for key in range(9):
            if (board[key] == ' '):
                board[key] = player_character
                score = minimax(board, True,alpha,beta)
                board[key] = ' '
                bestScore=min(score,bestScore)
                beta=min(beta,score)
                if beta<=alpha:
                    break
        return bestScore


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def selected_x():
    global player_character
    global ai_character
    player_character = 'X'
    ai_character = 'O'
    player_label = Label(frame_top, text="Your character  " + player_character, padx=10, pady=20).grid(row=2, column=0)
    start_button = Button(frame_top, text="Start!", height=2, width=8, command=create_board).grid(row=4, column=0)


def selected_o():
    global player_character
    global ai_character
    player_character = 'O'
    ai_character = 'X'
    player_label = Label(frame_top, text="Your character  " + player_character, padx=10, pady=20).grid(row=2, column=0)
    start_button = Button(frame_top, text="Start!", height=2, width=8, command=create_board).grid(row=4, column=0)



frame_top = LabelFrame(root, padx=40, pady=40)
frame_top.pack(padx=10, pady=10)

# label of top frame
label = Label(frame_top, text="Select Player.").grid(row=0, column=0)


# Player Select Button creation
player_button_1 = Button(frame_top, text="X", height=3, width=6, command=selected_x).grid(row=1, column=0)
player_button_2 = Button(frame_top, text="O", height=3, width=6, command=selected_o).grid(row=1, column=4)


# Bottom frame setup
frame_bottom = LabelFrame(root, padx=40, pady=40)
frame_bottom.pack(padx=10, pady=10)


# Game buttons creation
def create_board():
    global board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    b1 = Button(frame_bottom, text=board[0], height=8, width=18, command=lambda: playerMove(0)).grid(row=0, column=0)
    b2 = Button(frame_bottom, text=board[1], height=8, width=18, command=lambda: playerMove(1)).grid(row=0, column=1)
    b4 = Button(frame_bottom, text=board[2], height=8, width=18, command=lambda: playerMove(2)).grid(row=0, column=2)

    b4 = Button(frame_bottom, text=board[3], height=8, width=18, command=lambda: playerMove(3)).grid(row=1, column=0)
    b5 = Button(frame_bottom, text=board[4], height=8, width=18, command=lambda: playerMove(4)).grid(row=1, column=1)
    b8 = Button(frame_bottom, text=board[5], height=8, width=18, command=lambda: playerMove(5)).grid(row=1, column=2)

    b7 = Button(frame_bottom, text=board[6], height=8, width=18, command=lambda: playerMove(6)).grid(row=2, column=0)
    b8 = Button(frame_bottom, text=board[7], height=8, width=18, command=lambda: playerMove(7)).grid(row=2, column=1)
    b9 = Button(frame_bottom, text=board[8], height=8, width=18, command=lambda: playerMove(8)).grid(row=2, column=2)
    compMove()

root.mainloop()