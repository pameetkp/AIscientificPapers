
#the basis of this code was taken from multiple internet searches and compiled by chatGPT and then tweaked#
import random

#initialises payers with sore and the type they are playinhg as and with what strategy
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def reset(self):
        self.score = 0

    def strategy(self, opponent):
        pass
#cooperating algorithm
class Cooperator(Player):
    def __init__(self):
        super().__init__("Cooperator")

    def strategy(self, opponent):
        return 1  # Always cooperate
#de3fecor algorithm
class Defector(Player):
    def __init__(self):
        super().__init__("Defector")

    def strategy(self, opponent):
        return 0  # Always defect
#titfor tat algorithm
class TitForTat(Player):
    def __init__(self):
        super().__init__("TitForTat")
        self.last_opponent_move = 1  # Initially cooperate
#if last move was defect, player will defect
    def strategy(self, opponent):
        return self.last_opponent_move
#random control variable to test against
class Random(Player):
    def __init__(self, prob_cooperate):
        super().__init__("Random")
        self.prob_cooperate = prob_cooperate

    def strategy(self, opponent):
        return 1 if random.random() < self.prob_cooperate else 0

#the game initialised
class Match:
    def __init__(self, player1, player2, turns):
        self.player1 = player1
        self.player2 = player2
        self.turns = turns

    def play(self):
        self.player1.reset()
        self.player2.reset()
        
        for turn in range(self.turns):
            move1 = self.player1.strategy(self.player2)
            move2 = self.player2.strategy(self.player1)

            # Ccalculates scores, apecific to each variable of the game
            if move1 == 1 and move2 == 1:  # Both cooperate
                self.player1.score += 3
                self.player2.score += 3
            elif move1 == 1 and move2 == 0:  # Player 1 cooperates, Player 2 defects
                self.player1.score += 0
                self.player2.score += 5
            elif move1 == 0 and move2 == 1:  # Player 1 defects, Player 2 cooperates
                self.player1.score += 5
                self.player2.score += 0
            elif move1 == 0 and move2 == 0:  # Both defect
                self.player1.score += 1
                self.player2.score += 1

        return self.player1.score, self.player2.score

#plays the game
class Tournament:
    def __init__(self, players, turns=50, repetitions=100):
        self.players = players
        self.turns = turns
        self.repetitions = repetitions

    def play(self):
        results = {player.name: {'wins': 0, 'score': 0} for player in self.players}
        
        for _ in range(self.repetitions):
            for i in range(len(self.players)):
                for j in range(i + 1, len(self.players)):
                    match = Match(self.players[i], self.players[j], self.turns)
                    score1, score2 = match.play()

                    if score1 > score2:
                        results[self.players[i].name]['wins'] += 1
                    elif score2 > score1:
                        results[self.players[j].name]['wins'] += 1

                    results[self.players[i].name]['score'] += score1
                    results[self.players[j].name]['score'] += score2

        return results

#runs it 100 times
def torn(players):
    tournament = Tournament(players, turns=50, repetitions=100)
    results = tournament.play()

    # Print results: Wins and scores for each player
    for player in players:
        print(f"{player.name}: Wins = {results[player.name]['wins']}, Score = {results[player.name]['score']}")

    # Rank players by wins
    ranked_players = sorted(players, key=lambda p: results[p.name]['wins'], reverse=True)
    print("\nRanked Players by Wins:")
    for rank, player in enumerate(ranked_players, 1):
        print(f"{rank}. {player.name} - Wins: {results[player.name]['wins']}")

    return results

# Example usage of the functions
players = [
    Random(0.5), Random(0.8), Random(0.2),
    Defector(), Cooperator(), TitForTat()
]

# Call the tournament function
torn(players)
