import numpy as np
from models.coordinate import Coordinate


def _get_left_move(x, y):
    return Coordinate(x - 2, y)


def _get_up_move(x, y):
    return Coordinate(x, y - 2)


def _get_right_move(x, y):
    return Coordinate(x + 2, y)


def _get_down_move(x, y):
    return Coordinate(x, y + 2)


def get_clean_board():
    return np.array([[-1, -1, 0, 1, 1, -1, -1],
                     [-1, 1, 1, 1, 1, 1, -1],
                     [1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1],
                     [-1, 1, 1, 1, 1, 1, -1],
                     [-1, -1, 1, 1, 1, -1, -1]])


def get_all_legal_moves(board):
    legal_moves = []
    for x in range(0, 7):
        for y in range(0, 7):
            start_position = Coordinate(x, y)
            left_move = _get_left_move(x, y)
            if is_legal_move(board, start_position, left_move):
                legal_moves.append((start_position, left_move))
            right_move = _get_right_move(x, y)
            if is_legal_move(board, start_position, right_move):
                legal_moves.append((start_position, right_move))
            up_move = _get_up_move(x, y)
            if is_legal_move(board, start_position, up_move):
                legal_moves.append((start_position, up_move))
            down_move = _get_down_move(x, y)
            if is_legal_move(board, start_position, down_move):
                legal_moves.append((start_position, down_move))
    return legal_moves


def is_solved(board):
    ones_count = 0
    for x in range(0, 7):
        for y in range(0, 7):
            ones_count += 1 if board[x, y] == 1 else 0
            if ones_count > 1:
                return False
    return ones_count == 1


def perform_move(board, move):
    new_board = board.copy()
    start_position = move[0]
    end_position = move[1]
    new_board[start_position.x, start_position.y] = 0
    new_board[end_position.x, end_position.y] = 1
    jumped_x = int(np.mean([start_position.x, end_position.x]))
    jumped_y = int(np.mean([start_position.y, end_position.y]))
    new_board[jumped_x, jumped_y] = 0
    return new_board


def is_legal_move(board, start_position, end_position):
    # I don't know if there is a better way to prevent wrap around indexing for the positions
    if end_position.x < 0 or end_position.x > 6 or end_position.y < 0 or end_position.y > 6:
        return False
    # We must be landing on an empty square
    if board[end_position.x, end_position.y] != 0:
        return False
    # We must be starting on a populated square
    if board[start_position.x, start_position.y] != 1:
        return False
    # We must only be jumping in one direction
    change_in_x = start_position.x - end_position.x
    change_in_y = start_position.y - end_position.y
    moving_in_x = change_in_y == 0 and abs(change_in_x) == 2
    moving_in_y = change_in_x == 0 and abs(change_in_y) == 2
    # The position we are jumping over must be populated
    if moving_in_x:
        intermediary_position = int(np.mean([start_position.x, end_position.x]))
        return board[intermediary_position, start_position.y] == 1
    if moving_in_y:
        intermediary_position = int(np.mean([start_position.y, end_position.y]))
        return board[start_position.x, intermediary_position]

    return False
