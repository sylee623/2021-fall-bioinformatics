import copy

enzyme = {
    'ABC' : 'TTTT',
    'AAA' : 'TGGG'
}

enzymes_mod = copy.copy(enzyme)

enzymes_mod['ABC'] +='G'

print(enzymes_mod.values())
print(enzyme.values())