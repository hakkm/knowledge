from logic import Symbol, And, Not, Xor, Or, Implication, model_checking
from termcolor import cprint

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons


def check_knowldege(knowldege):
    for symbol in symbols:
        if model_checking(knowldege, symbol):
            cprint(f"{symbol}: YES", "green")
        elif not model_checking(knowldege, Not(symbol)):
            print(f"{symbol}: MAYBE")


kb = And(
    Xor(mustard, plum, scarlet),
    Xor(ballroom, kitchen, library),
    Xor(knife, revolver, wrench),
)

# cprint(f"Knowledge Base: {kb.formula()}", "yellow")

kb.add(Not(mustard))
kb.add(Not(kitchen))
kb.add(Not(revolver))

# at minimum, one of the following must not be inside the envelope
kb.add(Or(
    Not(scarlet), Not(library), Not(wrench)
    ))

# not Prom 
kb.add(Not(plum))

# if scarlet then ballroom
kb.add(Implication(scarlet, Not(ballroom)))

check_knowldege(kb)
