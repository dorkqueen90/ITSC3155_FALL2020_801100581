# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts): #takes in array of emails, dictionary contacts
    # return the contacts dictionary with emails populated from the array
    for i in range(0, len(emails)):
       contacts[list(contacts.keys())[i]] = emails[i]

    return contacts;

# # Part B.
def array2d_2_dict(contact_info, contacts):
    # YOUR CODE HERE

    return

# # Part C.
def dict_2_array(contacts):
    # YOUR CODE HERE

    return

