class Sentence():

    def evaluate(self, model):
        """Evaluates the logical sentence."""
        raise Exception("nothing to evaluate")

    def formula(self):
        """Returns string formula representing logical sentence."""
        return ""

    def symbols(self):
        """Returns a set of all symbols in the logical sentence."""
        return set()

    @classmethod
    def validate(cls, sentence):
        if not isinstance(sentence, Sentence):
            raise TypeError("must be a logical sentence")

    @classmethod
    def parenthesize(cls, s):
        """Parenthesizes an expression if not already parenthesized."""
        def balanced(s):
            """Checks if a string has balanced parentheses."""
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    if count <= 0:
                        return False
                    count -= 1
            return count == 0
        if not len(s) or s.isalpha() or (
            s[0] == "(" and s[-1] == ")" and balanced(s[1:-1])
        ):
            return s
        else:
            return f"({s})"


class Symbol(Sentence):

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self):
        return hash(("symbol", self.name))

    def __repr__(self):
        return self.name

    def evaluate(self, model):
        try:
            return bool(model[self.name])
        except KeyError:
            raise Exception(f"variable {self.name} not in model")

    def formula(self):
        return self.name

    def symbols(self):
        return {self.name}


class Not(Sentence):
    def __init__(self, operand: Sentence):
        Sentence.validate(operand)
        self.operand = operand

    def __eq__(self, other):
        return isinstance(other, Not) and self.operand == other.operand

    def __hash__(self):
        return hash(("not", hash(self.operand)))

    def __repr__(self):
        return f"Not({self.operand})"

    def evaluate(self, model):
        return not self.operand.evaluate(model)

    def formula(self):
        return "¬" + Sentence.parenthesize(self.operand.formula())

    def symbols(self):
        return self.operand.symbols()


class And(Sentence):
    def __init__(self, *conjuncts):
        for conjunct in conjuncts:
            Sentence.validate(conjunct)
        self.conjuncts = list(conjuncts)

    def __eq__(self, other):
        return isinstance(other, And) and self.conjuncts == other.conjuncts

    def __hash(self):
        return hash(("and", hash(self.conjuncts)))

    def __repr__(self):
        conjuncts = ", ".join(str(conjunct) for conjunct in self.conjuncts)
        return f"And({conjuncts})"

    def add(self, conjunct):
        Sentence.validate(conjunct)
        self.conjuncts.add(conjunct)

    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)

    def formula(self):
        if len(self.conjuncts) == 1:
            return self.conjuncts[0].formula()
        conjuncts = " ∧ ".join(
            Sentence.parenthesize(conjunct.formula()) for conjunct in self.conjuncts
        )
        return conjuncts

    def symbols(self):
        return set.union(*(conjunct.symbols() for conjunct in self.conjuncts))


class Or(Sentence):
    def __init__(self, *disjuncts):
        for disjunct in disjuncts:
            Sentence.validate(disjunct)
        self.disjuncts = set(disjuncts)

    def __eq__(self, other):
        return isinstance(other, Or) and self.disjuncts == other.disjuncts

    def __hash__(self):
        return hash(("or", tuple(hash(disjunct) for disjunct in self.disjuncts)))

    def __repr__(self):
        disjuncts = ", ".join(str(disjunct) for disjunct in self.disjuncts)
        return f"Or({disjuncts})"

    def add(self, disjunct):
        Sentence.validate(disjunct)
        self.disjuncts.add(disjunct)

    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)

    def formula(self):
        disjuncts = " ∨ ".join(
            disjunct.formula() for disjunct in self.disjuncts
        )
        return disjuncts

    def symbols(self):
        return set.union(*(disjunct.symbols() for disjunct in self.disjuncts))


class Implication(Sentence):
    def __init__(self, antecedent: Sentence, consequent: Sentence):
        Sentence.validate(antecedent)
        Sentence.validate(consequent)
        self.antecedent = antecedent
        self.consequent = consequent

    def __eq__(self, other):
        return (
            isinstance(other, Implication)
            and self.antecedent == other.antecedent
            and self.consequent == other.consequent
        )

    def __hash__(self):
        return hash(("implies", hash(self.antecedent), hash(self.consequent)))

    def __repr__(self):
        return f"Implication({self.antecedent}, {self.consequent})"

    def evaluate(self, model):
        return (
            not self.antecedent.evaluate(model)
            or self.consequent.evaluate(model)
        )

    def formula(self):
        antecedent = self.antecedent.formula()
        consequent = self.consequent.formula()
        return f"{antecedent} => {consequent}"

    def symbols(self):
        return set.union(self.antecedent.symbols(), self.consequent.symbols())


class BiImplication(Sentence):
    def __init__(self, left: Sentence, right: Sentence):
        Sentence.validate(left)
        Sentence.validate(right)
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (
            isinstance(other, BiImplication)
            and self.left == other.left
            and self.right == other.right
        )

    def __hash__(self):
        return hash(("iff", hash(self.left), hash(self.right)))

    def __repr__(self):
        return f"BiImplication({self.left}, {self.right})"

    def evaluate(self, model):
        return (
            self.left.evaluate(model)
            == self.right.evaluate(model)
        )

    def formula(self):
        left = self.left.formula()
        right = self.right.formula()
        return f"{left} <=> {right}"

    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())


class Xor(Sentence):
    def __init__(self, *operands):
        for operand in operands:
            Sentence.validate(operand)
        self.operands = set(operands)

    def __eq__(self, other):
        return isinstance(other, Xor) and self.operands == other.operands

    def __hash__(self):
        return hash(("xor", tuple(hash(operand) for operand in self.operands)))

    def __repr__(self):
        operands = ", ".join(str(operand) for operand in self.operands)
        return f"Xor({operands})"

    def add(self, operand):
        Sentence.validate(operand)
        self.operands.add(operand)

    def evaluate(self, model):
        return sum(operand.evaluate(model) for operand in self.operands) == 1

    def formula(self):
        operands = " ⊕  ".join(
            operand.formula() for operand in self.operands
        )
        return operands

    def symbols(self):
        return set.union(*(operand.symbols() for operand in self.operands))


def model_checking(knowledge, query):
    """Checks if knowledge base entails query."""
    def check_all(knowledge, query, symbols, model):
        """Checks if knowledge base entails query, given a particular model."""
        if not symbols:
            if knowledge.evaluate(model):
                return query.evaluate(model)
            else:
                return True
        else:
            # choose a symbol to assign
            remaining = symbols.copy()
            p = remaining.pop()

            # create a modal where the symbol is true
            modal_true = model.copy()
            modal_true[p] = True

            # create a modal where the symbol is False
            modal_false = model.copy()
            modal_false[p] = False

            # check if the knowledge base entails the query in both modals
            return (
                check_all(knowledge, query, remaining, modal_true) and
                check_all(knowledge, query, remaining, modal_false)
            )
    symbols = set.union(knowledge.symbols(), query.symbols())
    return check_all(knowledge, query, symbols, dict())
