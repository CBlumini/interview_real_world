# nums = [1, 2, 3]

# i_nums = iter(nums)


# # print(dir(i_nums))
# # print(i_nums)

# # print(dir(nums))

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))


class Range:
    def __init__(self, start, end) -> None:
        self.val = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.val >= self.end:
            raise StopIteration
        current = self.val
        self.val += 1
        return current

# Same but with a generator


def myrange(start, end):
    current = start
    while current < end:
        yield current
        current += 1


def my_inf(start):
    current = start
    while True:
        yield current
        current += 1


# nums = Range(1, 10)
nums = myrange(1, 10)

for num in nums:
    print(num)


inf_thing = my_inf(3)

print(next(inf_thing))
print(next(inf_thing))
print(next(inf_thing))
print(next(inf_thing))
