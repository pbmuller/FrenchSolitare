# This is a sample Python script.f
from models.board import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def map_moves_with_board(board, moves):
    return list(map(lambda move: (board, move), moves))


def get_hashable_move(move):
    return hash((str(move[0]), move[1]))


def main():
    board = get_clean_board()
    moves = get_all_legal_moves(board)
    potential_moves_list = map_moves_with_board(board, moves)
    unsolvable_boards = []
    while len(potential_moves_list) != 0:
        move = potential_moves_list.pop(0)
        move_board = move[0]
        move_coordinates = move[1]
        if str(move_board) in unsolvable_boards:
            print("We already know this board is unsolvable")
            continue
        new_board = perform_move(move_board, move_coordinates)
        next_moves = get_all_legal_moves(new_board)
        if is_solved(new_board):
            print("I've beaten the French!")
            return
        if str(new_board) in unsolvable_boards:
            print("The new board will be unsolvable")
            continue
        if not next_moves:
            unsolvable_boards.append(str(new_board))
            print("This board is unsolvable")
            continue
        clean_next_moves = []
        for next_move in next_moves:
            next_new_board = perform_move(new_board, next_move)
            next_next_legal_moves = get_all_legal_moves(next_new_board)
            if next_next_legal_moves:
                clean_next_moves.append(next_move)
            else:
                unsolvable_boards.append(str(next_new_board))
        if not clean_next_moves:
            print('The next moves are unsolvable')
            unsolvable_boards.append(str(new_board))
            continue
        next_move_list = map_moves_with_board(new_board, clean_next_moves)
        next_move_list.extend(potential_moves_list)
        potential_moves_list = next_move_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
