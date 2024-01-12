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
