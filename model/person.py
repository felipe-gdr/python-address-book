class Person:
    """A person who can be added to the address book. A person has the f
    following properties:

    Attributes:
        first_name: a person's first name
        last_name: a person's last name
        street_addresses: a list containing a person's street addresses
        email_addresses: a list continaing a person's email addresses
        phone_numbers: a list containg a person's phone numbers
    """

    def __init__(self, first_name, last_name):
        """Creates a person with a first name equals to *first_name* and
        a last name equals to *last_name*. """
        self.first_name = first_name
        self.last_name = last_name
        self.street_addresses = []
        self.email_addresses = []
        self.phone_numbers = []
        self.groups = []

    def __eq__(self, other):
        return (other != None and self.first_name == other.first_name and
            self.last_name == other.last_name)

    def __str__(self):
        return "{0}, {1}".format(self.last_name, self.first_name)

    def addStreetAddress(self, street_address):
        """Adds a new *street_address* to a person's *street_addresses*
        list """
        if street_address == '' or street_address == None:
            raise ValueError('Street Address cannot be empty')

        self.street_addresses.append(street_address)

    def addEmailAddress(self, email_address):
        """Adds a new *email_address* to a person's *email_addresses*
        list """
        if email_address == '' or email_address == None:
            raise ValueError('Email Address cannot be empty')

        self.email_addresses.append(email_address)

    def addPhoneNumber(self, phone_number):
        """Adds a new *phone_number* to a person's *phone_numbers*
        list """
        if phone_number == '' or phone_number == None:
            raise ValueError('Phone Number cannot be empty')

        self.phone_numbers.append(phone_number)

    def addToGroup(self, group):
        """ Adds a *group* to the person's *group* list. This method
        will also add the *person* to the *groups's* member list"""        
        if not self in group.members:
            group.members.append(self)
            self.groups.append(group)
        else:
            print "{0} is already a member of group {1}".format(str(self), str(group))
