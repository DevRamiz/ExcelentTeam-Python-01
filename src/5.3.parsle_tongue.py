def parsle_tongue():
    def is_subsequence(word, text):
        it = iter(text)
        return all(char in it for char in word)

    with open("code.txt") as f:
        lines = f.read().splitlines()

    hidden_words = []
    targets = ['python', 'isawesome', 'welldone', 'goodjob']
    for line in lines:
        for word in targets:
            if word in hidden_words:
                continue
            if is_subsequence(word, line):
                hidden_words.append(word)

    return hidden_words
