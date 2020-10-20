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
def array2d_2_dict(contact_info, contacts): #contact info: 2D arr of emails & phone nums. contacts: dict for contacts 
    # return the contacts dictionary with the email address and phone number dictionary populated for each contact
    if not contact_info:
      return contacts
    else:
      if not contact_info[0]:
        return contacts
      else:
        for i in range(0, len(contact_info)):
          innerDict = {
           "email": contact_info[i][0],
           "phone": contact_info[i][1]
          }
          contacts[list(contacts.keys())[i]] =  innerDict;

    return contacts;

# # Part C.
def dict_2_array(contacts):
   # create three arrays of type string from the dictionary
    # return an array that contains these three arrays (a three dimensional array!)
   emails = []
   phones = []
   names = []
   for nameInDict, info in contacts.items():
    names.append(nameInDict);
    emails.append(info["email"]);
    phones.append(info["phone"]);

   arr = [];
   arr.append(emails);
   arr.append(phones);
   arr.append(names);

   return arr;

