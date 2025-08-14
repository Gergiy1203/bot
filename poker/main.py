import fastapi
import random
from treys import Evaluator, Deck, Card


def monte_carlo(hero_cards: list,
                board_cards: list,
                active: int,
                n_simulatioons: int)  -&gt; float:

"""
    :param hero_cards: рука игрока
    :param board_cards: карты доски
    :param active: количество активных игроков
    :param n_simulations: количество симуляций
    :return: equity
    """



remaining_cards = []
deck = Deck()
userd_cards = set(hero_cards + board_cards)
remaining_cards = [c for c in deck.cards if c not in userd_cards]


wins = ties = losses = 0


for _ in range(n_simulations):


    random.shuffle(remaining_cards)


card_index = 0
villains = []
for _ in range(active - 1):
    villain = remaining_cards[card_index:card_index + 2]
    villains.append(villain)
    card_index += 2


    sim_board = board_cards[:]
    cards_needed = 5 - len(sim_board)
    if cards_needed &gt; 0:
        sim_board.extend(remaining_cards[card_index:card_index + cards_needed])

        hero_score = EVALUATOR.evaluate(sim_board, villain)
        if villains_score &lt; best_villain_score:
            best_villain_score = villains_score



         if hero_score &lt; best_villain_score:
             wins += 1
         elif hero_score == best_villain_score:
             ties += 1
         else:
             losses += 1

         equity = (wins + 0.5 * ties)  / n_simulations

        return equity