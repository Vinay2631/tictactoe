from random import randint
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
positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
turn = 1
turns = 0
game_over = False


# functions
def check_gameover(pos):
    global game_over
    if pos[0] + pos[1] + pos[2] == 'XXX' or \
            pos[3] + pos[4] + pos[5] == 'XXX' or \
            pos[6] + pos[7] + pos[8] == 'XXX' or \
            pos[0] + pos[3] + pos[6] == 'XXX' or \
            pos[1] + pos[4] + pos[7] == 'XXX' or \
            pos[2] + pos[5] + pos[8] == 'XXX' or \
            pos[0] + pos[4] + pos[8] == 'XXX' or \
            pos[6] + pos[4] + pos[2] == 'XXX':
        game_over = True
        if player_character=="X":
            play_song()
            win_message = messagebox.showinfo("Tic Tac Toe", "YOU WON, If you want to play again select a character and hit start!")
        else:
            draw_song()
            win_message = messagebox.showinfo("Tic Tac Toe",
                                              "AI WON, If you want to play again select a character and hit start!")
        root.destroy()
    elif pos[0] + pos[1] + pos[2] == 'OOO' or \
            pos[3] + pos[4] + pos[5] == 'OOO' or \
            pos[6] + pos[7] + pos[8] == 'OOO' or \
            pos[0] + pos[3] + pos[6] == 'OOO' or \
            pos[1] + pos[4] + pos[7] == 'OOO' or \
            pos[2] + pos[5] + pos[8] == 'OOO' or \
            pos[0] + pos[4] + pos[8] == 'OOO' or \
            pos[6] + pos[4] + pos[2] == 'OOO':
        game_over = True
        if player_character=="O":
            play_song()
            win_message = messagebox.showinfo("Tic Tac Toe", "YOU WON, If you want to play again select a character and hit start!")
        else:
            draw_song()
            win_message = messagebox.showinfo("Tic Tac Toe",
                                              "AI WON, If you want to play again select a character and hit start!")
        root.destroy()
    elif turns == 8 and game_over == False:
        draw_song()
        tie_message = messagebox.showinfo("Tic Tac Toe",
                                          " TIE GAME, If you want to play again select a character and hit start!")
        root.destroy()


    return game_over


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


def ai_turn():
    global turns, turn, positions, game_over, ai_character

    while turn == 0 and turns < 9 and game_over == False:
        ai_select = randint(0, 8)
        if positions[ai_select] == " ":
            positions[ai_select] = ai_character
            if 0 <= ai_select and ai_select <= 2:
                r = 0
            elif 3 <= ai_select and ai_select <= 5:
                r = 1
            elif 6 <= ai_select and ai_select <= 8:
                r = 2

            if ai_select == 0 or ai_select == 3 or ai_select == 6:
                c = 0
            elif ai_select == 1 or ai_select == 4 or ai_select == 7:
                c = 1
            elif ai_select == 2 or ai_select == 5 or ai_select == 8:
                c = 2
            new_button = Button(frame_bottom, text=positions[ai_select], height=4, width=8).grid(row=r, column=c)
            game_over = check_gameover(positions)
            turn = 1
            turns += 1


def player_pos(pos):
    global turn, turns, game_over, player_character

    if turn == 1 and turns < 9 and game_over == False:
        if positions[pos] == " ":
            if 0 <= pos and pos <= 2:
                r = 0
            elif 3 <= pos and pos <= 5:
                r = 1
            elif 6 <= pos and pos <= 8:
                r = 2

            if pos == 0 or pos == 3 or pos == 6:
                c = 0
            elif pos == 1 or pos == 4 or pos == 7:
                c = 1
            elif pos == 2 or pos == 5 or pos == 8:
                c = 2

            positions[pos] = player_character
            new_button = Button(frame_bottom, text=positions[pos], height=4, width=8).grid(row=r, column=c)
            game_over = check_gameover(positions)
            turn = 0
            turns += 1
            ai_turn()


# Top frame setup
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
    global positions
    global turn
    global turns, game_over
    turn = 1
    turns = 0
    game_over = False

    positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    b1 = Button(frame_bottom, text=positions[0], height=8, width=18, command=lambda: player_pos(0)).grid(row=0,column=0)
    b2 = Button(frame_bottom, text=positions[1], height=8, width=18, command=lambda: player_pos(1)).grid(row=0,column=1)
    b4 = Button(frame_bottom, text=positions[2], height=8, width=18, command=lambda: player_pos(2)).grid(row=0,column=2)

    b4 = Button(frame_bottom, text=positions[3], height=8, width=18, command=lambda: player_pos(3)).grid(row=1,column=0)
    b5 = Button(frame_bottom, text=positions[4], height=8, width=18, command=lambda: player_pos(4)).grid(row=1,column=1)
    b8 = Button(frame_bottom, text=positions[5], height=8, width=18, command=lambda: player_pos(5)).grid(row=1,column=2)

    b7 = Button(frame_bottom, text=positions[6], height=8, width=18, command=lambda: player_pos(6)).grid(row=2,column=0)
    b8 = Button(frame_bottom, text=positions[7], height=8, width=18, command=lambda: player_pos(7)).grid(row=2,column=1)
    b9 = Button(frame_bottom, text=positions[8], height=8, width=18, command=lambda: player_pos(8)).grid(row=2,column=2)


root.mainloop()