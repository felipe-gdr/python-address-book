# Python Address Book

Design-only questions
=====================

Q: Find person by email address (can supply any substring, ie. "comp" should work assuming "alexander@company.com" is an email address in the address book) - discuss how you would implement this without coding the solution.

A: This could be easily achieved by changing the regex expression used in the AddressBook.__emailMatch function.

Public API
==========

* Add a person to the address book.

*address_book*.**AddressBook**.addPerson(person)

Add a *person* to the Address Book. If the person is a member of any group, those groups will be added to the Address Book as well

```python
        address_book = AddressBook()
        jerry = Person('Jerry', 'Garcia')
        address_book.addPerson(jerry)
```

* Add a group to the address book.
*address_book*.**AddressBook**.addGroup(group)

Add a *group* to the Address Book. If the group has any members, those members will be added to the Address Book as well

```python
        address_book = AddressBook()
        grateful = Group('Grateful Dead')
        address_book.addGroup(grateful)
```

* Given a group we want to easily find its members.
*address_book*.**AddressBook**.getMembers(group, group_name)

Returns a *list* containing the members of a certain group. The group can be passed as an object *group*, or just as its name *group_name*

```python
        address_book = AddressBook()
        address_book.getMembers(group_name='Jacksons 5')
        jackson5 = Group('Jackson 5')
        address_book.getMembers(group=jackson5)
```

* Given a person we want to easily find the groups the person belongs to.
*address_book*.**AddressBook**.getGroups(person, person_full_name)

Returns a *list* containing the groups a person is a member of. The person can passed as an object *person*, or just as its *full_name*

```python
        address_book = AddressBook()
        address_book.getGroups(person_full_name='Ritchie, Lionel')
        lionel = Person('Lionel', 'Ritchie')
        address_book.getGroups(person=lionel)
```

* Find person by name (can supply either first name, last name, or both).
*address_book*.**AddressBook**.findPeopleByName(first_name, last_name)

Finds people by first and/or last names. This function will return a *list* of matches ordered by last and first names

```python
        address_book = AddressBook()
        # find by first and last names
        address_book.findPeopleByName(last_name='Jackson', first_name='Tito')
        # find by last name only
        address_book.findPeopleByName(last_name='Jackson')
        # find by first name only
        address_book.findPeopleByName(first_name='Tito')
```


* Find person by email address (can supply either the exact string or a prefix string, ie. both "alexander@company.com" and "alex" should work)
*address_book*.**AddressBook**.findPeopleByEmail(email_search):

Finds people by email address. This function will return a *list* of matches ordered by last and first names

```python
        address_book = AddressBook()
        # find by begining of email address
        address_book.findPeopleByEmail('mich')
        # find by complete email address
        address_book.findPeopleByEmail('lionel.ritchie@singers.com')
```
