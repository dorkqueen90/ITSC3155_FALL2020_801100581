import pythonBasics4


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
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the functions in pythonBasics3 with interesting inputs.
def main():
    # set which functions to test
    array_2_dict = True
    array2d_2_dict = True
    dict_2_array = True

    if array_2_dict:
        print('array_2_dict')

        emailArray = []
        contact_dict = {"Bob Smith": "", "Sally Field": "", "Mark Dole": ""}
        test(pythonBasics4.array_2_dict(emailArray, contact_dict), contact_dict)

        emailArray = ["bobsmith@example.com", "sallyfield@example.com", "markdole@example.com"]
        contact_dict = {"Bob Smith": "", "Sally Field": "", "Mark Dole": ""}
        test(pythonBasics4.array_2_dict(emailArray, contact_dict),
             {"Bob Smith": "bobsmith@example.com", "Sally Field": "sallyfield@example.com",
              "Mark Dole": "markdole@example.com"})

        emailArray = ["bobsmith@example.com", "sallyfield@example.com", "markdole@example.com", "foo@example.com"]
        contact_dict = {"Bob Smith": "", "Sally Field": "", "Mark Dole": "", "Foo Fighter": ""}
        test(pythonBasics4.array_2_dict(emailArray, contact_dict),
             {"Bob Smith": "bobsmith@example.com", "Sally Field": "sallyfield@example.com",
              "Mark Dole": "markdole@example.com", "Foo Fighter": "foo@example.com"})

    if array2d_2_dict:
        print('array2d_2_dict')
        info_array = []
        contact_dict = {"Bob Smith": "", "Sally Field": "", "Foo Fighter": ""}
        test(pythonBasics4.array2d_2_dict(info_array, contact_dict), contact_dict)

        info_array = [[]]
        contact_dict = {"Bob Smith": "", "Sally Field": "", "Foo Fighter": ""}
        test(pythonBasics4.array2d_2_dict(info_array, contact_dict), contact_dict)

        info_array = [["bobsmith@example.com", "555-555-5555"], ["sallyfield@example.com", "111-111-1111"]]
        contact_dict = {"Bob Smith": "", "Sally Field": ""}
        test(pythonBasics4.array2d_2_dict(info_array, contact_dict),
             {"Bob Smith": {"email": "bobsmith@example.com", "phone": "555-555-5555"},
              "Sally Field": {"email": "sallyfield@example.com", "phone": "111-111-1111"}})

        info_array = [["bobsmith@example.com", "555-555-5555"], ["sallyfield@example.com", "111-111-1111"],
                      ["foofighter@example.com", "777-777-7777"]]
        contact_dict = {"Bob Smith": "", "Sally Field": "", "Foo Fighter": ""}
        test(pythonBasics4.array2d_2_dict(info_array, contact_dict),
             {"Bob Smith": {"email": "bobsmith@example.com", "phone": "555-555-5555"},
              "Sally Field": {"email": "sallyfield@example.com", "phone": "111-111-1111"},
              "Foo Fighter": {"email": "foofighter@example.com", "phone": "777-777-7777"}})

    if dict_2_array:
        print()
        print('dict_2_array')

        contact_dict = {}
        test(pythonBasics4.dict_2_array(contact_dict), [[], [], []])

        contact_dict = {"Bob Smith": {"email": "bobsmith@example.com", "phone": "555-555-5555"},
                        "Sally Field": {"email": "sallyfield@example.com", "phone": "111-111-1111"},
                        "Foo Fighter": {"email": "foofighter@example.com", "phone": "777-777-7777"}}
        test(pythonBasics4.dict_2_array(contact_dict),
             [["bobsmith@example.com", "sallyfield@example.com", "foofighter@example.com"],
              ["555-555-5555", "111-111-1111", "777-777-7777"], ["Bob Smith", "Sally Field", "Foo Fighter"]])


if __name__ == '__main__':
    main()
