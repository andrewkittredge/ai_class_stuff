from itertools import product

def generate_models(symbols):
    permutations = product((True, False), repeat=len(symbols))
    for permutation in permutations:
        yield dict(zip(symbols, permutation))
        
def check_models(sentence, models):
    for model in models:
        matches = True
        for symbol, value in sentence.iteritems():
            if model[symbol] != value:
                matches = False
                break
        if matches:
            yield model
            
if __name__ == '__main__':
    symbols = ('Breeze11', 'Breeze21', 'Pit11', 'Pit12', 'Pit21', 'Pit22', 'Pit31')
    print list(check_models({'Pit11' : False, 'Breeze11' : False, 'Breeze21' : True}, generate_models(symbols)))