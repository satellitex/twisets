# twisets
Algebra of sets @twitter follow/followers


## Eaxmpel
```buildoutcfg
>> a = (@twitter_id1 | >@twitter_id2) & (<@twitter_id1 || <@twitter_id2)
>> a
```

## BNF
```
?program: [(state)+]

// statement
?state: expr _NL*
    | assignment _NL*
assignment: new_symbol "=" expr
new_symbol: NAME

// expr
?expr: term
    | sum
    | intersection
    | difference
    | symmetric_difference
sum: expr "|" term
intersection: expr "&" term
difference: expr "-" term
symmetric_difference: expr "^" term

//term
?term: id
    | symbol
    | priority
?priority: "(" expr ")"
id: INOUT "@" ID
symbol: NAME
INOUT: /(>|<)/
ID: /[a-zA-Z0-9_]+/

_NL: /(\r?\n)+\s*/

%import common.CNAME -> NAME

%import common.WS_INLINE
%ignore WS_INLINE
```
