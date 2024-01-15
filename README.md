# Knowledge

## Propositional Logic 
Propositional logic is a formal system in mathematics and logic. It is also called propositional calculus, sentential calculus, or sentential logic. It deals with propositions (which can be true or false) and argument flow. Compound propositions are formed by connecting propositions by logical connectives. Propositions are represented by capital letters such as P, Q and R. Connectives are represented by symbols such as ∧, ∨ and ¬. The following table shows the truth tables for negation, conjunction, and disjunction.

Propositional symbols are atomic propositions. They are the basic building blocks of propositional logic. They can be either true or false but not both. They are represented by capital letters such as P, Q and R.

Proposition: A declarative sentence that is either true or false, but not both.

## Logical connective:
- Not (¬)
- And (∧)
- Or (∨)
- Implication (→)
- Bi-conditional (↔)

### NOT
The negation of a proposition P is notated as ¬P, and pronounced "not P". It has a truth value opposite to P. The truth table of ¬P is as follows:

| P | ¬P |
|---|----|
| T | F  |
| F | T  |

### AND
The conjunction of propositions P and Q is notated as P ∧ Q, and can be read as "P and Q". The truth table of P ∧ Q is as follows:

| P | Q | P ∧ Q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | F     |
| F | F | F     |

### OR
The disjunction of propositions P and Q is notated as P ∨ Q, and can be read as "P or Q". The truth table of P ∨ Q is as follows:

| P | Q | P ∨ Q |
|---|---|-------|
| T | T | T     |
| T | F | T     |
| F | T | T     |
| F | F | F     |

### Implication
The implication of propositions P and Q is notated as P → Q, and can be read as "if P then Q". The truth table of P → Q is as follows:

| P | Q | P → Q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | T     |
| F | F | T     |

Don't get the third line? Let's look at the following example:
If it is raining → then i go home.
               P → Q
if P is false, then i can be anywhere, so Q can be true or false.
So this statement (false → True) is true.


### Bi-conditional - Equivalence
The bi-conditional of propositions P and Q is notated as P ↔ Q, and can be read as "P if and only if Q". The truth table of P ↔ Q is as follows:

| P | Q | P ↔ Q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | F     |
| F | F | T     |

---
Now That we know the logical connectives, we need a way of knowing what's actually true or false about the world.
To do that we need to introduce the concept of a model, and 

## Model
Assignment of truth values to propositional symbols (a "possible world").

We need a way to represent that knowledge.
We can do that with a knowledge base.

## Knowledge Base
Set of sentences known by a knowledge-based agent.

We give this knowledge base to the agent, then the agent can use it to draw conclusions.
And What those conclusions look like?
We need to introduce the concept of Entailment.

## Entailment

KB ⊨ α (KB entails α): In every model where KB is true, α is also true.


Example: 
KB = {P → Q, Q → R, R → S}
α = P → S 
KB ⊨ α is true because in every model where KB is true, α is also true.

## Inference
The process of deriving new sentences from old ones.

Example:
P = "It is Monday"
Q = "It is raining"
R = "I go to park"
KB = {P ∧ ¬Q → R}  and lets' say P and not Q are true.
So we can infer that R is true.


All of this is the beginning of what we call Inference Algorithms.

## Inference Algorithms
We're going to answer the question of entailment:  Does KB entail α?
KB: Knowledge base
α: Query, something we're wondering about the world.

### Model Checking 
To determine weather KB entails α.
    - Enumerate all possible models.
    - If in Every model where KB is true, α is also true, then KB entails α.
    - Otherwise, KB does not entail α.

## Knowledge Engineering
The process of designing a knowledge base. Simply put, it's the process of taking what we know about the world and putting it into a knowledge base.
How to encode ideas into logical sentences?

## Example:
### Puzzle

Given 4 people: Alice, Bob, Cindy and Jack.
And given 4 houses: Red, Green, Blue and Yellow.

Only one house per person.
Only one person per house.

### Mastermind 
Given 4 pegs: Red, Green, Blue and Yellow.
Given 4 slots: 1, 2, 3 and 4.

Each color has exactly one position

--- 
Conclusion: The Model Checking algorithm is not practical for real-world problems. It's too slow.

## Inference Rules 
Instead of looking at all possible worlds and checking if KB entails α, we can use inference rules to derive new sentences from old ones.
### Modus Ponens
If P then Q and P is true, then Q is true.
So P → Q and P is equivalent to Q

### And Elimination 
If P and Q are true, then P is true.
So P ∧ Q is equivalent to P

### Double Negation Elimination 
If P is true, then not not P is true.
So ¬¬P is equivalent to P

### Implication Elimination 
If P then Q is true, then not P or Q is true.
So P → Q is equivalent to ¬P ∨ Q

### Bi-conditional Elimination
If P if and only if Q is true, then P implies Q and Q implies P are true.
So P ↔ Q is equivalent to (P → Q) ∧ (Q → P)

### De Morgan's Law
not (P and Q) is equivalent to (not P) or (not Q): P ∧ Q is equivalent to ¬(¬P ∨ ¬Q)
not (P or Q) is equivalent to (not P) and (not Q): P ∨ Q is equivalent to ¬(¬P ∧ ¬Q)

### Distributive Law
P and (Q or R) is equivalent to (P and Q) or (P and R): P ∧ (Q ∨ R) is equivalent to (P ∧ Q) ∨ (P ∧ R)

---
Now we have a set of inference rules, we can use them to build a proof of a query.

Search Problems 
- Initial state 
- Actions 
- Transition model 
- Goal test 
- Path cost 

We can treat our sentences as an Initial state, and we can use inference rules as actions to get to the goal state.

## Theorem Proving 

The process of finding a proof for a query.
- Initial state: KB 
- Actions: Inference rules 
- Transition model: New KB after inference 
- Goal test: Check statement α we're trying to prove
- Path cost: Number of steps in proof


--- 
It turns out that there are another way to apply inference: Resolution.

## Resolution
Resolution is based on another inference rule called unit resolution.
If P ∨ Q is true, and ¬P is true, then Q is true: (P ∨ Q) ∧ ¬P is equivalent to Q
Q can be any sentence, not just a propositional symbol: (P ∨ (Q1 ∧ ... ∧ Qn)) ∧ ¬P is equivalent to (Q1 ∧ ... ∧ Qn)

Other inference rules can be derived from unit resolution:
If P ∨ Q and ¬P ∨ R are true, then Q ∨ R is true: (P ∨ Q) ∧ (¬P ∨ R) is equivalent to Q ∨ R
Q and R can be any sentences, not just propositional symbols: (P ∨ (Q1 ∧ ... ∧ Qn)) ∧ (¬P ∨ (R1 ∧ ... ∧ Rm)) is equivalent to (Q1 ∧ ... ∧ Qn) ∨ (R1 ∧ ... ∧ Rm)

### Clause 
A disjunction of literals.
Disjunction: Things connected with or. 
Conjunction: Things connected with and.
Literal: A propositional symbol or its negation.

### Empty Clause 
A disjunction of no literals. It is always false.
If P and ¬P are true, then the empty clause. Which is always false.

### Conjunctive Normal Form (CNF)
A conjunction of clauses. e.g. (P ∨ Q) ∧ (¬P ∨ R) is in CNF.

#### How to convert a sentence to CNF?
1. Eliminate biconditionals: P ↔ Q is equivalent to (P → Q) ∧ (Q → P)
2. Move ¬ inwards using De Morgan's Law: ¬(P ∧ Q) is equivalent to (¬P ∨ ¬Q)
3. Use distributive law to get a conjunction of disjunctions: P ∧ (Q ∨ R) is equivalent to (P ∧ Q) ∨ (P ∧ R)

## Inference by Resolution
Why do we care about CNF? Because we can use resolution to do inference.
Given a knowledge base KB and a query α, we can use resolution to determine if KB entails α.
It's based on 

To determine if KB entails α: 
- Check if KB ∧ ¬α is a contradiction.
    - If so, then KB entails α.
    - Otherwise, KB does not entail α.

Let's implement CNF To determine if KB entails α:
- Convert KB ∧ ¬α to CNF.
- Keep checking if we can derive the empty clause using resolution.
    - If ever we produce the empty clause, then KB entails α.
    - Otherwise, KB does not entail α.
