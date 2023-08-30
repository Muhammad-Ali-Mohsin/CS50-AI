from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave), # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A isn't both a knight and a knave
    
    Implication(AKnight, And(AKnight, AKnave)), # If A is a knight, they are both a knight and a knave
    Implication(AKnave, Not(And(AKnight, AKnave))), # If A is a knave, they are not both a knight and a knave
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave), # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A isn't both a knight and a knave

    Or(BKnight, BKnave), # B is either a knight or a knave
    Not(And(BKnight, BKnave)), # B isn't both a knight and a knave
    
    Implication(AKnight, And(AKnave, BKnave)),  # If A is a knight, they are both knaves
    Implication(AKnave, Not(And(AKnave, BKnave))) # If A is a knave, they are not both knaves
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave), # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A isn't both a knight and a knave

    Or(BKnight, BKnave), # B is either a knight or a knave
    Not(And(BKnight, BKnave)), # B isn't both a knight and a knave

    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))), # If A is a knight, they are both knights or they are both knaves
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))), # If A is a knave, they are both not knights or they are both not knaves

    Implication(BKnight, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))), # If B is a knight, they are both not knights or they are both not knaves
    Implication(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave))) # If B is a knave, they are both knights or they are both knaves
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave), # A is either a knight or a knave
    Not(And(AKnight, AKnave)), # A isn't both a knight and a knave

    Or(BKnight, BKnave), # B is either a knight or a knave
    Not(And(BKnight, BKnave)), # B isn't both a knight and a knave

    Or(CKnight, CKnave), # C is either a knight or a knave
    Not(And(CKnight, CKnave)), # C isn't both a knight and a knave

    Or(
        And(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight))), # If A said they are a knight, they are telling the truth if they are a knight and lying if they are a knave
        And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))) # If A said they are a knave, they are telling the truth if they are a knight and lying if they are a knave
    ),

    # A can't have said both they are a knight and they are a knave
    Not(And(
        And(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight))), # If A said they are a knight, they are telling the truth if they are a knight and lying if they are a knave
        And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))) # If A said they are a knave, they are telling the truth if they are a knight and lying if they are a knave
    )),

    # If B is a knight and A is a knight then A is a knave
    # If B is a knight and A is a knave then A is not a Knave
    Implication(BKnight, And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))),

    Implication(BKnave, Not(And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))))), # If B is a knave, then whatever they say is Not true

    Implication(BKnight, CKnave), # If B is a knight then C must be a knave
    Implication(BKnave, Not(CKnave)), # If B is a knave then C must not be a knave

    Implication(CKnight, AKnight), # If C is a knight then A must be a knight
    Implication(CKnave, Not(AKnight)) # If C is a knave then A must be not be a knight
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
