# twisets
Algebra of sets @twitter follow/followers

## BNF
```
?program: [(state)+]

// statement
?state: expr
    | assignment
assignment: new_symbol "=" expr
new_symbol: WORD

// expr
?expr: term
    | sum
    | intersection
    | not
sum: expr "&" term
intersection: exor "|" term
not: "~" expr
    
//term
?term: id
    | symbol
    | priority
?priority: "(" expr ")"
id: /(i|o)@[a-zA-Z_0-9]+/
symbol: WORD

%import common.WORD
%import common.WS
%ignore WS
```

## Eaxmpel
```buildoutcfg
a = !(i@twitter_id1 || i@twitter_id2) && (o@twitter_id1 || o@twitter_id2)
a
```