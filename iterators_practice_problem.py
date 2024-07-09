class Sentence:
    def __init__(self, words: str) -> None:
        self.words = words
        self.curr = 0
        self.splitted = words.split(' ')
        self.end = len(words)

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr >= self.end:
            raise StopIteration
        word = self.splitted[self.curr]
        self.curr += 1
        return word


def my_sentence(words: str):
    # words: list = words.split(' ')
    # stop = len(words)
    # curr = 0
    # while curr < stop:
    #     yield words[curr]
    #     curr += 1
    for word in words.split():
        yield word


# test = Sentence("the boy bought the basketball")

# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
test2 = my_sentence("the boy bought the basketball")
print(next(test2))
print(next(test2))
print(next(test2))
print(next(test2))
print(next(test2))
print(next(test2))
print(next(test2))
