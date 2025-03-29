import random
from core.slots import Slot
from core.constants import PLAYER_COINS_INITIAL


slot_types = []
slot_types += [Slot(display="🍒", value=1.1)] * 10
slot_types += [Slot(display="💎", value=1.2)] * 8
slot_types += [Slot(display="🎲", value=1.3)] * 6
slot_types += [Slot(display="🪙", value=3)] * 5
slot_types += [Slot(display="🍀", value=5)] * 3
slot_types += [Slot(display="💵", value=8)] * 4
slot_types += [Slot(display="🃏", value=13)] * 3
slot_types += [Slot(display="🍋", value=17)] * 2
slot_types += [Slot(display="7️⃣", value=30)]
slot_types += [Slot(display="♥️", value=40)]
slot_types += [Slot(display="♦️", value=63)]
slot_types += [Slot(display="♠️", value=71)]
slot_types += [Slot(display="🍉", value=80)]
slot_types += [Slot(display="🍊", value=100)]


def random_slot():
    slot = random.choice(slot_types)
    return slot.copy(deep=True)


def reset_game(player, game):
    player.coins = PLAYER_COINS_INITIAL