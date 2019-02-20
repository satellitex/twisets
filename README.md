# twisets
Algebra of sets @twitter follow/followers

## How to start
```
$ git clone https://github.com/satellitex/twisets.git
$ cd twisets
$ pipenv shell
$ pipenv install
$ pipenv run main
```

### option
- `---config` : Path name to config file.(default: `conifg/act_config.yaml`) ([example](https://github.com/satellitex/twisets/blob/master/config/config.yaml))
- `--use_cache` : use cache flag. [(default: `True`), `False`]. if `False`,  this script requests twitter api client for each query.

## Example
[![asciicast](https://asciinema.org/a/OacK07YSex6GDEDB0H3Ni7CEz.svg)](https://asciinema.org/a/OacK07YSex6GDEDB0H3Ni7CEz)
```buildoutcfg
>> a = (@twitter_id1 | >@twitter_id2) & (<@twitter_id1 || <@twitter_id2)
>> p a
```

## BNF
```
?program: [(state)+]

// statement
?state: show _NL*
    | assignment _NL*
    | expr _NL*
show: "p" expr
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
