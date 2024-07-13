import random

class KingsGame:
    def __init__(self):
        self.deck = [
            ('Ace', 'Waterfall', 'Everyone starts drinking at the same time. You can only stop when the person to your right stops.'),
            ('2', 'You', 'You pick someone to drink.'),
            ('3', 'Me', 'You drink.'),
            ('4', 'Floor', 'Everyone must touch the floor. The last person to do so drinks.'),
            ('5', 'Guys', 'All guys drink.'),
            ('6', 'Chicks', 'All girls drink.'),
            ('7', 'Heaven', 'Everyone must point towards the sky. The last person to do so drinks.'),
            ('8', 'Mate', 'Pick a mate. Every time you drink, they drink.'),
            ('9', 'Rhyme', 'Say a word. The person to your left has to say a word that rhymes. This continues until someone hesitates or repeats a word. That person drinks.'),
            ('10', 'Categories', 'Pick a category (e.g., car brands). The person to your left has to name something in that category. This continues until someone hesitates or repeats a word. That person drinks.'),
            ('Jack', 'Make a Rule', 'You make a rule. Everyone must follow this rule for the rest of the game. Anyone who breaks the rule drinks.'),
            ('Queen', 'Question Master', 'You become the Question Master. Whenever you ask a question, anyone who answers must drink. This continues until another Queen is drawn.'),
            ('King', 'Pour', 'You must pour some of your drink into the central cup. The person who draws the 4th King must drink the contents of the cup.')
        ]
        random.shuffle(self.deck)

    def draw_card(self):
        if not self.deck:
            return None, None, None
        return self.deck.pop()

kings_game = KingsGame()
