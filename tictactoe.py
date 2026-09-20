def form_grid(grid):
    print(f''' 
| {grid[0]} | {grid[1]} | {grid[2]} |
 ---+---+---
| {grid[3]} | {grid[4]} | {grid[5]} |
 ---+---+---
| {grid[6]} | {grid[7]} | {grid[8]} |
''')

# Setting the winning combinations
win_comb = [ (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6) ]

def winner(grid1, player):
    for win in win_comb: #To verify winning combination
        if grid1[win[0]] == grid1[win[1]] == grid1[win[2]] == player:
            return True
    return False

def play_game():
    grid1 = [" "]*9
    player = "X"
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print("Grid position key:")
    print('''
        | 1 | 2 | 3 |
        ---+---+---
        | 4 | 5 | 6 |
        ---+---+---
        | 7 | 8 | 9 |
        ''')

    while not game_over:
        form_grid(grid1)

        # Input handling & validation loop
        while True:
            try:
                player_choice = int(input(f"Player {player}, pick a spot (1-9): ")) - 1
                if player_choice in range(0,9) and grid1[player_choice] == " ":
                    grid1[player_choice] = player
                    break
                else:
                    print("Spot taken or out of range. Enter a valid spot")
            except ValueError:
                print("Please enter a valid number (1-9).")  #Exception Handling

        if winner(grid1, player):
            form_grid(grid1)
            print(f"Player {player} wins!")
            game_over = True
        elif " " not in grid1: #Checking for draw
            form_grid(grid1)
            print("It's a draw!")
            game_over = True
        else:
            player = "O" if player == "X" else "X"

play_game()
