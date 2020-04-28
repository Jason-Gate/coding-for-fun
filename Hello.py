# ---------- Global variable: ----------

# Initialize variables & list:
field_list = ["_", "_", "_",

              "_", "_", "_",
              "_", "_", "_"]


# ---------- Functions: ----------


# Initialize and show Tic-Tac-Toe field:
def show_field():
    field_design = f"""---------
| {field_list[0]} {field_list[1]} {field_list[2]} |
| {field_list[3]} {field_list[4]} {field_list[5]} |
| {field_list[6]} {field_list[7]} {field_list[8]} |
---------"""
    return field_design


# Check if there is a winner:
def check_state():
    row_1 = field_list[0] == field_list[1] == field_list[2] != "_"
    row_2 = field_list[3] == field_list[4] == field_list[5] != "_"
    row_3 = field_list[6] == field_list[7] == field_list[8] != "_"
    col_1 = field_list[0] == field_list[3] == field_list[6] != "_"
    col_2 = field_list[1] == field_list[4] == field_list[7] != "_"
    col_3 = field_list[2] == field_list[5] == field_list[8] != "_"
    dia_1 = field_list[0] == field_list[4] == field_list[8] != "_"
    dia_2 = field_list[6] == field_list[4] == field_list[2] != "_"
    return row_1, row_2, row_3, col_1, col_2, col_3, dia_1, dia_2


# Iterate field states and print the current field state
def decide_field_state(state):
    bool_value = state
    if bool_value.count(True) > 1:
        print("Impossible")
    elif field_list.count("X") > field_list.count("O") + 1:
        print("Impossible")
    elif field_list.count("O") > field_list.count("X") + 1:
        print("Impossible")
    elif bool_value.count(True) == 0 and field_list.count("_") != 0:
        print("Game not finished")
    elif bool_value.count(True) == 0 and field_list.count("_") == 0:
        print("Draw")
    elif bool_value.count(True) == 1:
        bool_reference = {1: field_list[0],
                          2: field_list[3],
                          3: field_list[6],
                          4: field_list[0],
                          5: field_list[1],
                          6: field_list[2],
                          7: field_list[0],
                          8: field_list[6]}
        print(bool_reference.get(bool_value.index(True) + 1), "wins")


def start_the_game():
    field_incrementer = 0

    user_input = list(input("Enter cells: ").upper())
    user_input = user_input[:9]

    for field in user_input:
        field_list[field_incrementer] = field
        field_incrementer += 1


def player_move():
    while True:
        move = input("Enter the coordinates: ").split()

        try:
            string_to_int_converter = [int(string) for string in move]
        except ValueError:
            print("You should enter numbers!")
        else:
            if string_to_int_converter[0] not in [1, 2, 3] or string_to_int_converter[1] not in [1, 2, 3]:
                print("Coordinates should be from 1 to 3!")
            else:
                return move


def field_list_check(index):
    if field_list[index] != "_":
        print("This cell is occupied! Choose another one!")
        index_to_coordinate_converter(player_move())
    else:
        field_list[index] = "X"


def index_to_coordinate_converter(move):
    if move == ["1", "1"]:
        field_list_check(6)
    elif move == ["1", "2"]:
        field_list_check(3)
    elif move == ["1", "3"]:
        field_list_check(0)
    elif move == ["2", "1"]:
        field_list_check(7)
    elif move == ["2", "2"]:
        field_list_check(4)
    elif move == ["2", "3"]:
        field_list_check(1)
    elif move == ["3", "1"]:
        field_list_check(8)
    elif move == ["3", "2"]:
        field_list_check(5)
    elif move == ["3", "3"]:
        field_list_check(2)


start_the_game()
print(show_field())
index_to_coordinate_converter(player_move())
print(show_field())
# decide_field_state(check_state())
