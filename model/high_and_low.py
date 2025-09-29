import random

class HighLowGame:
    def __init__(self, initial_chips=100):
        self.deck = list(range(1, 14))
        random.shuffle(self.deck)
        self.chips = initial_chips
        self.round = 1
        self.bet = 10
        self.history = []
        self.base_card = None
        self.choice = None
        self.result_card = None
        self.outcome = None

    def draw_base_card(self):
        if not self.base_card and self.deck:
            self.base_card = self.deck.pop(0)
        return self.base_card

    def play_round(self, choice, bet):
        self.choice = choice
        self.result_card = self.deck.pop(0)

        # 勝敗判定
        if (choice == "High" and self.result_card > self.base_card) or \
           (choice == "Low" and self.result_card < self.base_card) or \
           (choice == "Draw" and self.result_card == self.base_card):
            self.outcome = "win"
            self.chips += bet
        elif self.result_card == self.base_card:
            self.outcome = "draw"
            # チップ変動なし
        else:
            self.outcome = "lose"
            self.chips -= bet

        # 履歴に記録
        self.history.append({
            "round": self.round,
            "base_card": self.base_card,
            "choice": choice,
            "result_card": self.result_card,
            "bet": bet,
            "outcome": self.outcome,
            "chips_after": self.chips
        })

        return self.outcome, self.result_card

    def next_round(self, bet):
        self.round += 1
        self.bet = bet
        self.base_card = None
        self.choice = None
        self.result_card = None
        self.outcome = None

    def is_finished(self):
        return self.round > 3 or self.chips <= 0

    def is_round_finished(self):
        return self.outcome is not None