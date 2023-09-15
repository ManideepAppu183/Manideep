"""
We are developing a Snakes and Ladders game
For this game the entities are :
1.Board

<--

The Board class will be informing us the size of the Snake and Ladder Board

-->
2.Dice

<--

The Dice class will be informing us the no of sides of Dice used to play the game

-->

3.Snake
<--

The Snake class will be informing us the start and end positions of a Snake

-->
4.Ladder
<--

The Ladder class will be informing us the start and end positions of a Ladder

-->
"""
# First we need to import random numbers for the generation of numbers on a dice
import random


class Board:
    def __init__(self, size):
        self.size = size
        self.snakes = {}
        self.ladders = {}

    # We will define a Constructor for Board class for initializing the size of the board and the snakes and ladders on the board
    # We assume the Snakes and ladders as Dictionaries so that the Key of particular Snake
    # defines the Start position and Value of that particular key defines the End position of that Snake
    # For Snake Start position is greater than End position
    # Key of particular Ladder defines the Start position and Value of that particular key defines the End position of that Ladder
    # For Ladder Start position is lesser than End position

    def add_snake(self, start, end):
        self.snakes[start] = end

    def add_ladder(self, start, end):
        self.ladders[start] = end


# We define 'add_snake' method to add snake to the Board and 'add_ladder' method to add ladder to the Board


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


# Here we define a constructor for defining the no of sides of a dice and
# roll method to roll the dice to get a random number on dice

class Snake:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # Constructor for adding the start and end positions of the snake on the board

    def move(self, player):
        player.move_to(self.end)


# Method for moving the player to the end position of the snake

class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    # Constructor for adding the start and end positions of the ladder on the board

    def move(self, player):
        player.move_to(self.end)


# Method for moving the player to the end position of the ladder

class Player():
    def __init__(self, name, board):
        self.name = name
        self.board = board
        self.position = 0

    # We define a Constructor for initializing the name of the player and the position of the player on the board

    def move(self, steps):
        self.position = self.position + steps
        if self.position > self.board.size:
            print("Oops, you rolled more than the board size! Try again.")
            self.position = self.position - steps

    # Method for moving the player a certain number of steps forward on the board

    def move_to(self, position):
        self.position = position


# Method for moving the player to a specific position on the board

class SnakesAndLadders:
    def __init__(self, board, dice, num_players):
        self.board = board
        self.dice = dice
        self.players = [Player(f"Player {i + 1}", board) for i in range(num_players)]
        self.current_player = None

    # Constructor for initializing the board, dice, number of players, and the current player

    def start(self):
        while True:
            for player in self.players:
                self.current_player = player
                input(f"{player.name}'s turn. Press enter to roll the dice...")
                dice_roll = self.dice.roll()
                print(f"{player.name} rolled a {dice_roll}!")
                player.move(dice_roll)
                if player.position in self.board.snakes:
                    snake = Snake(player.position, self.board.snakes[player.position])
                    snake.move(player)
                    print(f"Oh no, {player.name} landed on a snake!")
                elif player.position in self.board.ladders:
                    ladder = Ladder(player.position, self.board.ladders[player.position])
                    ladder.move(player)
                    print(f"Congratulations, {player.name} landed on a ladder!")
                print(f"{player.name}'s position is now {player.position}")
                if player.position == self.board.size:
                    print(f"Congratulations, {player.name}! You won!")
                    return


# example usage
board = Board(20)
board.add_snake(18, 6)
board.add_snake(12, 8)
board.add_ladder(3, 16)
board.add_ladder(10, 19)
dice = Dice(8)
game = SnakesAndLadders(board, dice, 3)
game.start()

