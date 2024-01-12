from logic import *

rain = Symbol("rain")
park = Symbol("park")
home = Symbol("home")

kb = And(
    Implication(Not(rain), park),   # if not raining, then harry goes to park
    Xor(park, home),                # harry goes to either park or home
    home                            # harry visited park today
)

print(kb.formula())

print(f"Is it Raining: {model_checking(kb, rain)}")
print(f"Is Harry at the Park: {model_checking(kb, park)}")
print(f"Is Harry at Home: {model_checking(kb, home)}")
print(f"Is it not Raining: {model_checking(kb, Not(rain))}")

model = {rain: True, park: False, home: True}
# print(kb.evaluate(model))
