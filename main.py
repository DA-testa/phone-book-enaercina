class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, number, name):
        self.contacts[number] = name

    def del_contact(self, number):
        if number in self.contacts:
            del self.contacts[number]

    def find_contact(self, number):
        return self.contacts.get(number, 'not found')

def process_queries(queries):
    phone_book = PhoneBook()
    result = []
    for query in queries:
        if query.type == 'add':
            phone_book.add_contact(query.number, query.name)
        elif query.type == 'del':
            phone_book.del_contact(query.number)
        else:
            result.append(phone_book.find_contact(query.number))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
