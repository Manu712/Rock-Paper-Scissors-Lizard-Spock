import random
moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']


class Player:

    RandomPlayer = None
    HumanPlayer = None

    def move(self):
        return 'rock'

    def learn(self, HumanPlayer, RandomPlayer):
        self.HumanPlayer = HumanPlayer
        self.RandomPlayer = RandomPlayer
    score = 1


class RandomPlayer(Player):

    def move(self):
        computer_player = random.choice(moves)
        return computer_player


class HumanPlayer(Player):

    def h1(self):
        user_input = input("Please enter your move:")
        while user_input not in moves:
            user_input = input("Wrong input. Enter a valid move listed above")
            if user_input == "quit":
                print("Task aborted...")
                exit()
        if user_input == moves:
            pass
        if user_input != moves:
            return user_input
        elif user_input == "quit":
            print("Task aborted...")
            exit()
        elif user_input != "quit":
            pass


class ReflectPlayer(Player):

    def move(self):

        if self.HumanPlayer is None:
            return random.choice(moves)
        else:
            return self.RandomPlayer


class CyclePlayer(Player):

    def move(self):

        if self.HumanPlayer == "rock":
            return "paper"
        elif self.HumanPlayer == "paper":
            return "scissors"
        elif self.HumanPlayer == "scissors":
            return "lizard"
        elif self.HumanPlayer == "lizard":
            return "spock"
        else:
            return "rock"


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'rock'and two == 'lizard') or
            (one == 'lizard' and two == 'spock') or
            (one == 'spock' and two == 'scissors') or
            (one == 'scissors' and two == 'lizard') or
            (one == 'lizard' and two == 'paper') or
            (one == 'paper' and two == 'spock') or
            (one == 'spock' and two == 'rock') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

        start_msg = input(('Welcome to rock, paper, scissors, lizard, spock.\
         You will be playing against a bot,\
        the instructions are as follows:\
        Scissors cuts Paper\
        Paper covers Rock\
        Rock destroys Lizard\
        Lizard poisons Spock\
        Spock destroys Scissors\
        Scissors obliterate Lizard\
        Lizard eats Paper\
        Paper invalidates and ruins Spock\
        Spock exterminates Rock\
        and as it always has been, Rock crushes Scissors\
        if you have understood these rules please press any key\
        and the enter key to start.\
        If you would like to abort the program type "quit".\
        Good luck!'))
        if start_msg == "quit":
            print("Task aborted")
            exit()

    def play_round(self):
        move1 = self.p1.h1()
        move2 = self.p2.move()
        score1 = (self.p1_score)
        final_value1 = int(score1)
        final_value1 = str(final_value1)
        score2 = (self.p2_score)
        final_value2 = int(score2)
        final_value2 = str(final_value2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Player 1: {move1}  Player 2: {move2}")
        print('The score is for player 1:' + final_value1)
        print('The score is for player 2:' + final_value2)
        if (beats(move1, move2)):
            self.p1_score += 1
            print("Player 1 wins this round")
        elif (beats(move2, move1)):
            self.p2_score += 1
            print("Player 2 wins this round")
        elif move1 == move2:
            print("Player 1 and 2 have tied")
        elif input != moves:
            print('Try again, please enter one of the moves listed above')
            print('Score not counted due to invalid input')
            self.p1_score += 0
            self.p2_score += 0
            move1 = ('Move not played due to invalid input from user')
            move2 = ('Move not played due to invalid input from user')
            print('The current score for player 1:' + final_value1)
            print('The current score for player 2:' + final_value2)

    def play_game(self):
        print(">>>>>Game start!<<<<<")
        while True:
            move_input = (input("Enter number of rounds,\
                 you would like to play:"))
            if move_input.isnumeric() and (int(move_input)) > 0:
                break
            else:
                print(("Please enter a valid number\
                    this will allow you play a certain amount of rounds"))
                move_input

        for round in range(int(move_input)):
            print(f"Round {round+1}:")
            self.play_round()
        print("Game over!")
        print(f"The final score for player 1 was:" + (str(self.p1_score)))
        print(f"The final score for player 2 was:" + (str(self.p2_score)))
        if self.p1_score > self.p2_score:
            print("Player one wins the game!")
        elif self.p2_score > self.p1_score:
            print("Player 2 wins the game!")
        elif self.p1_score == self.p2_score:
            print("The game has tied with both players having equal scores")
        print("Thank you for playing!")

total_classes = [Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
random_players = random.choice(total_classes)

if __name__ == '__main__':
    game = Game(HumanPlayer(), random_players)
    game.play_game()
