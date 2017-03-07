import pickle,sys,os


class AddressBook:
    def load_ab(self):
        global ab
        if not os.path.exists(addressbook_path):
            os.mkdir(addressbook_path)
        if os.path.exists(addressbook_path):
            f = open(addressbook_path,'rb')
            ab = pickle.load(f)
            f.close()
        else:
            ab = []
#
    def get_ab(self):
        name = input("Enter contact's name:")
        email = input("Enter contact's email:")
        phone = input("Enter contact's phone:")
        kind = input("Enter your relastionship with the contact:")
        contact_info = {'name':name,'email':email,'phone':phone,'kind':kind}
        ab.append(contact_info)

    def save_ab(self):
        f = open(addressbook_path,'wb')
        pickle.dump(ab,f)
        f.close

    def browse_ab(self):
        f = open(addressbook_path,'rb')
        ab = pickle.load(f)
        for contact in ab:
            for key,value in contact.items():
                print (' - {1}'.format(key,value))
            print('\n\n')

        print ('\n\n###!!!For browsing structure only!!!###',ab,'\n\n')

    def search_ab(self,searchterm,searchby='name'):
        f = open(addressbook_path,'rb')
        ab = pickle.load(f)
        for contact in ab :
            for key1,value1 in contact.items():
                if searchby == key1:
                    if searchterm == value1:
                        for key2,value2 in contact.items():
                            print ('- {0} '.format(value2),end='')
                        print ('\n')

    def delete_ab(self,searchterm):
        global ab
        f = open(addressbook_path,'rb')
        ab = pickle.load(f)
        count = -1
        for contact in ab:
            count += 1
            for key,value in contact.items():
                if searchterm == value:
                    print ('You have deleted the details of '+value+'.')
                    del ab[count]
                    AddressBook.save_ab(self)

    def modify_ab(self,searchby,searchterm,newterm):
        global ab
        f = open(addressbook_path,'rb')
        ab = pickle.load(f)
        count = 0-1
        for contact in ab:
            count += 1
            for key,value in contact.items():
                if searchby == key:
                    if searchterm == value:
                        contact[searchby] = newterm
                        ab[count] = contact
                        AddressBook.save_ab(self)


addressbook_path = '/Users/CrazyLazy/AddressBook/address_book.data'

if len(sys.argv[1:]) != 0:
    mode = sys.argv[1]
else:
    mode = input('Type what would you like to do:\nbrowse,add,modify,delete or search?:\n\n')

if  mode == 'browse':
    abc = AddressBook()
    abc.browse_ab()

elif mode == 'add':
    abc = AddressBook()
    abc.load_ab()
    abc.get_ab()
    abc.save_ab()

elif mode == 'modify':
    searchby = input('Please enter what field type you would like to modify?\n\nFor example, name, mail, relationship etc.\n\n')
    searchterm = input("Please enter the detail that you would like  to change of your old contact\n\n")
    newterm = input('Please enter the new value:\n')
    abc = AddressBook()
    abc.modify_ab(searchby,searchterm,newterm)

elif mode == 'delete':
    if len(sys.argv[2:]) != 0:
        searchterm = sys.argv[2]
    else:
        searchterm = input("\n\nWho's detail would you like to delete.\n\n")
        abc = AddressBook()
        abc.delete_ab(searchterm)

elif mode == 'search':
    if len(sys.argv[2:]) != 0:
        searchterm = sys.argv[2]
    else:
        searchterm = input("\n\nWho's details would your like to search for\n\n")
    if len(sys.argv[3:]) != 0:
        searchby = sys.argv[3]
    else:
        searchby = input("\n\nWould you like to search by name(default),mail or phone?\n\n")
        abc = AddressBook()
        abc.search_ab(searchterm,searchby)

else:
    print ('\nTypo bro!\n')
