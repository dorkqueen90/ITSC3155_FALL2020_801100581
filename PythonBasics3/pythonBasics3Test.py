
import pythonBasics3
# main() is already set up to call the functions
# we want to test with a few different inputs,
# printing 'OK' when each function is correct.
# the simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# Calls the functions in pythonBasics3 with interesting inputs.
def main():
    # set which functions to test
    starts_with_number = True
    starts_with_consonant = False
    binary_multiple_of_4 = False

    if starts_with_number:
        print('starts_with_number')
        test(pythonBasics3.starts_with_number('12'), True)
        test(pythonBasics3.starts_with_number('21'), True)
        test(pythonBasics3.starts_with_number('31'), True)
        test(pythonBasics3.starts_with_number('41'), True)
        test(pythonBasics3.starts_with_number('51'), True)
        test(pythonBasics3.starts_with_number('61'), True)
        test(pythonBasics3.starts_with_number('71'), True)
        test(pythonBasics3.starts_with_number('81'), True)
        test(pythonBasics3.starts_with_number('91'), True)
        test(pythonBasics3.starts_with_number('Aadfdf'), False)
        test(pythonBasics3.starts_with_number('#foo'), False)
        test(pythonBasics3.starts_with_number(''), False)

    if starts_with_consonant:
        print('starts_with_consonant')
        test(pythonBasics3.starts_with_consonant('vest'), True)
        test(pythonBasics3.starts_with_consonant('cast'), True)
        test(pythonBasics3.starts_with_consonant('cast'), True)
        test(pythonBasics3.starts_with_consonant('cast'), True)
        test(pythonBasics3.starts_with_consonant('#3'), False)
        test(pythonBasics3.starts_with_consonant('east'), False)
        test(pythonBasics3.starts_with_consonant('Eat'), False)
        test(pythonBasics3.starts_with_consonant('Ice'), False)
        test(pythonBasics3.starts_with_consonant('in'), False)
        test(pythonBasics3.starts_with_consonant('at'), False)
        test(pythonBasics3.starts_with_consonant('All'), False)
        test(pythonBasics3.starts_with_consonant('on'), False)
        test(pythonBasics3.starts_with_consonant('Out'), False)
        test(pythonBasics3.starts_with_consonant('unlock'), False)
        test(pythonBasics3.starts_with_consonant('Unique'), False)
        test(pythonBasics3.starts_with_consonant(''), False)

    if binary_multiple_of_4:
        print()
        print('binary_multiple_of_4')
        testset1 = ["1010101010100", "0101010101010100", "100", "0"]

        for case in testset1:
            test(pythonBasics3.binary_multiple_of_4(case),True)

        testset2 = ["101", "1000000000001", "1001", "a100", ""]

        for case in testset2:
            test(pythonBasics3.binary_multiple_of_4(case),False)


if __name__ == '__main__':
  main()
