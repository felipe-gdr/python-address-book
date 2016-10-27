class Group:
    """A group, which contains *people*. A group can be added to
    the address book.

    Attributes:
        name: the group's name
        members: *people* who are members of the group
    """

    def __init__(self, name):
        """Creates a group with the given *name*"""
        self.name = name
        self.members = []

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return (other != None and self.name == other.name)

    def addPerson(self, person):
        """ Adds a *person* to the group's *member* list. This method
        will also add the *group* to the *person's* group list"""
        if not person in self.members:
            self.members.append(person)
            person.groups.append(self)
        else:
            print "{0} is already a member of group {1}".format(str(person), str(self))
