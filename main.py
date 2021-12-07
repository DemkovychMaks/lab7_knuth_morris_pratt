from Knuth import KnuthMorris

if __name__ == '__main__':
    text = "maksdemmaksmdemaksmaksdemmaksdmakdamke"
    pattern = "maksdem"
    print(KnuthMorris(text, pattern).Knuth_Morris_Pratt_algorithm())
