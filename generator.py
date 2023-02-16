def line_by_line(item):
    while len(item) > 0:
        yield item[0]
        item.pop(0)


james = [
    "Things not what they used to be",
    "Missing one inside of me",
    "Deathly loss, this can't be real",
    "Cannot stand this hell I feel",
    "Emptiness is filling me",
    "To the point of agony",
    "Growing darkness taking dawn",
    "I was me, but now he's gone"
]
line_by_line(james)
for lines in line_by_line(james):
    print(lines)


def multiply(a, b):
    i = 1
    while i <= a:
        yield i * b
        i += 1


def test_line_by_line():
    input_list = ['water', 'air', 'fire']
    expected_output = ['water', 'air', 'fire']
    result = list(line_by_line(input_list))
    assert result == expected_output
    print("line_by_line function passed")


def test_multiply():
    result = list(multiply(5, 3))
    expected = [3, 6, 9, 12, 15]
    assert result == expected
    print("multiply function pass")


if __name__ == "__main__":
    test_multiply()
    test_line_by_line()