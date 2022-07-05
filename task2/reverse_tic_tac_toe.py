from tkinter import *
import random


def who_first_play(value):
    global person_play
    global computer_play
    if value == 'X':
        person_play = 'X'
        computer_play = 'O'
    else:
        person_play = 'O'
        computer_play = 'X'


def start_window(window):
    window.title("Игра 'Крестики нолики'")
    i_first = Button(window, text='Я хочу начать первым', bg='#fafad2', activebackground='#d2b48c',
                     command=lambda: [who_first_play('X'), change_window_start_on_window_game()])
    i_no_first = Button(window, text='Пусть компьютер начнет первым', bg='#fafad2', activebackground='#d2b48c',
                        command=lambda: [who_first_play('O'), change_window_start_on_window_game()])
    i_first.grid(row=0, column=1, columnspan=2, sticky=N + S + W + E, padx=5, pady=5, ipadx=5, ipady=5)
    i_no_first.grid(row=0, column=7, columnspan=2, sticky=N + S + W + E, padx=5, pady=5, ipadx=5, ipady=5)
    window_center(window)
    window.mainloop()


def change_window_start_on_window_game():
    global window_game
    window_game = Toplevel()
    window_game['background'] = '#f0e68c'
    window_game.iconbitmap('logo.ico')
    game_window(window_game)


def game_window(window):
    global field
    window.title("Игра 'Крестики нолики'")
    for row in range(10):
        line = []
        for col in range(10):
            button = Button(window, text=' ', width=2, height=1,
                            font='bold',
                            background='lavender',
                            command=lambda row=row, col=col: [click_person(row, col), check_win(), play_computer()])
            button.grid(row=row, column=col, sticky=N + S + W + E, padx=2, pady=2, ipadx=2, ipady=2)
            line.append(button)
        field.append(line)
    window_center(window)
    new_game()
    window.mainloop()


def question_about_continuation():
    window_question = Toplevel()
    window_question['background'] = '#f0e68c'
    window_question.iconbitmap('logo.ico')
    button_question_yes = Button(window_question, text='Да', bg='#fafad2', activebackground='#d2b48c',
                                 command=lambda: [window_question.destroy(), new_game()])
    button_question_no = Button(window_question, text='Нет', bg='#fafad2', activebackground='#d2b48c',
                                command=lambda: [window_question.destroy(), window_game.destroy(), root.destroy()])
    Label(window_question, text='Ещё?)', bg='#f0e68c').grid(row=0, column=2, sticky=N + S + W + E, padx=5,
                                                            pady=5, ipadx=5,
                                                            ipady=5)
    button_question_yes.grid(row=1, column=1, sticky=N + S + W + E, padx=5, pady=5, ipadx=5, ipady=5)
    button_question_no.grid(row=1, column=3, columnspan=2, sticky=N + S + W + E, padx=5, pady=5, ipadx=5, ipady=5)
    window_center(window_question)


def window_center(window):
    window.update_idletasks()
    w, h = window.winfo_width(), window.winfo_height()
    window.geometry(f'+{(window.winfo_screenwidth() - w) // 2}+{(window.winfo_screenheight() - h) // 2}')


def new_game():
    global game_run
    global weight_charts
    global end_game
    global list_of_movies
    global next_move
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = '#fafad2'
            field[row][col]['activebackground'] = '#d2b48c'
            field[row][col]['fg'] = '#4b0082'
    game_run = True
    weight_charts = map_creation()
    end_game = False
    list_of_movies = []
    next_move = [5, 5]
    if computer_play == 'X':
        field[5][5]['text'] = 'X'


def click_person(row, col):
    global game_run
    global end_game
    global person_play
    global field
    game_run = True
    if field[row][col]['text'] == ' ' and not end_game:
        field[row][col]['text'] = person_play
    else:
        game_run = False


def check_win():
    global end_game
    global game_run
    global field

    def check_win_horizontal():
        win_check = False
        finish_comb = []
        for row in range(10):
            for col in range(6):
                if field[row][col]['text'] != ' ':
                    x = field[row][col]['text']
                    if all((
                            field[row][col + 1]['text'] == x,
                            field[row][col + 2]['text'] == x,
                            field[row][col + 3]['text'] == x,
                            field[row][col + 4]['text'] == x
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row, col + i])
                        finish_comb.append(win_check)
                        return finish_comb
        return win_check

    def check_win_vertical():
        win_check = False
        finish_comb = []
        for col in range(10):
            for row in range(6):
                if field[row][col]['text'] != ' ':
                    x = field[row][col]['text']
                    if all((
                            field[row + 1][col]['text'] == x,
                            field[row + 2][col]['text'] == x,
                            field[row + 3][col]['text'] == x,
                            field[row + 4][col]['text'] == x
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row + i, col])
                        finish_comb.append(win_check)
                        return finish_comb
        return win_check

    def check_win_diagonal_right():
        win_check = False
        finish_comb = []
        for row in range(6):
            for col in range(6):
                if field[row][col]['text'] != ' ':
                    x = field[row][col]['text']
                    if all((
                            field[row + 1][col + 1]['text'] == x,
                            field[row + 2][col + 2]['text'] == x,
                            field[row + 3][col + 3]['text'] == x,
                            field[row + 4][col + 4]['text'] == x
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row + i, col + i])
                        finish_comb.append(win_check)
                        return finish_comb
        return win_check

    def check_win_diagonal_left():
        win_check = False
        finish_comb = []
        for row in range(6):
            for col in range(9, 3, -1):
                if field[row][col]['text'] != ' ':
                    x = field[row][col]['text']
                    if all((
                            field[row + 1][col - 1]['text'] == x,
                            field[row + 2][col - 2]['text'] == x,
                            field[row + 3][col - 3]['text'] == x,
                            field[row + 4][col - 4]['text'] == x
                    )):
                        win_check = True
                        for i in range(5):
                            finish_comb.append([row + i, col - i])
                        finish_comb.append(win_check)
                        return finish_comb
        return win_check

    def display_win(end_comb):
        if end_game:
            for i in range(5):
                row = end_comb[i][0]
                col = end_comb[i][1]
                if person_play == 'X' and field[row][col]['text'] == 'X':
                    field[row][col]['fg'] = 'red'
                elif person_play == 'O' and field[row][col]['text'] == 'O':
                    field[row][col]['fg'] = 'red'
                else:
                    field[row][col]['fg'] = 'green'

    def end_play(end_comb):
        global game_run
        global end_game
        end_game = end_comb[-1]
        display_win(end_comb)
        if game_run:
            question_about_continuation()
        game_run = False

    if (end_comb := check_win_diagonal_right()) != False:
        end_play(end_comb)
    elif (end_comb := check_win_diagonal_left()) != False:
        end_play(end_comb)
    elif (end_comb := check_win_horizontal()) != False:
        end_play(end_comb)
    elif (end_comb := check_win_vertical()) != False:
        end_play(end_comb)
    else:
        end_game = False


def play_computer():
    global field
    global computer_play
    global weight_charts
    global list_of_movies
    global next_move
    global game_run
    global end_game

    def occupied_cells():
        global weight_charts
        for row in range(10):
            for col in range(10):
                if field[row][col]['text'] != ' ':
                    weight_charts[row][col] = -1

    def cell_selection_protection(amount, start_weight, end_weight):
        global weight_charts
        global computer_play
        global field
        x = computer_play

        def check_four_horizontal(row, col, x):
            global weight_charts
            check = False
            kol = 0
            for i in creating_range(amount):
                try:
                    if field[row][col + i]['text'] == x and (col + i >= 0):
                        kol += 1
                except IndexError:
                    continue
            if kol == amount:
                check = True
            return check

        def check_four_vertical(row, col, x):
            global weight_charts
            check = False
            kol = 0
            for i in creating_range(amount):
                try:
                    if field[row + i][col]['text'] == x and (row + i >= 0):
                        kol += 1
                except IndexError:
                    continue
            if kol == amount:
                check = True
            return check

        def check_four_diagonal_right(row, col, x):
            global weight_charts
            check = False
            kol = 0
            for i in creating_range(amount):
                try:
                    if field[row + i][col + i]['text'] == x and (row + i >= 0) and (col + i >= 0):
                        kol += 1
                except IndexError:
                    continue
            if kol == amount:
                check = True
            return check

        def check_four_diagonal_left(row, col, x):
            global weight_charts
            check = False
            kol = 0
            for i in creating_range(amount):
                try:
                    if field[row - i][col + i]['text'] == x and (row - i >= 0) and (col + i >= 0):
                        kol += 1
                except IndexError:
                    continue
            if kol == amount:
                check = True
            return check

        for row in range(10):
            for col in range(10):
                if weight_charts[row][col] == start_weight:
                    if (check_four_horizontal(row, col, x)) or (check_four_vertical(row, col, x)) or (
                            check_four_diagonal_right(row, col, x)) or (
                            check_four_diagonal_left(row, col, x)):
                        weight_charts[row][col] = end_weight

    def choice_of_possible_move():
        global weight_charts
        global list_of_movies
        global next_move
        global person_play
        list_of_movies = []
        for row in range(10):
            for col in range(10):
                if weight_charts[row][col] == 0:
                    list_of_movies.append([row, col])
        random_index = random.randint(0, len(list_of_movies) - 1)
        next_move = list_of_movies[random_index]
        if person_play == 'X':
            field[next_move[0]][next_move[1]]['text'] = 'O'
        else:
            field[next_move[0]][next_move[1]]['text'] = 'X'

    if game_run and not end_game:
        occupied_cells()
        cell_selection_protection(4, 0, -1)
        choice_of_possible_move()
        check_win()
        weight_charts = map_creation()
        list_of_movies = []
        next_move = []


def map_creation():
    map_i = []
    for row in range(10):
        row_i = []
        for col in range(10):
            row_i.append(0)
        map_i.append(row_i)
    return map_i


def creating_range(amount):
    diapason = []
    for i in range(-amount, amount + 1):
        if i != 0:
            diapason.append(i)
    return diapason


person_play = ''
computer_play = ''
game_run = True
field = []
end_game = False
weight_charts = map_creation()
list_of_movies = []
next_move = [5, 5]
root = Tk()
root['background'] = '#f0e68c'
root.iconbitmap('logo.ico')
start_window(root)
