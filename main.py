class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, number, name):
        self.contacts.append((number, name))

    def delete_contact(self, number):
        for i in range(len(self.contacts)):
            if self.contacts[i][0] == number:
                del self.contacts[i]
                break

    def find_contact(self, number):
        for contact in self.contacts:
            if contact[0] == number:
                return contact[1]
        return 'not found'

def read_queries():
    n = int(input())
    queries = []
    for i in range(n):
        query = input().split()
        queries.append(query)
    return queries

def process_queries(queries):
    phonebook = Phonebook()
    result = []
    for query in queries:
        query_type = query[0]
        query_number = int(query[1])
        if query_type == 'add':
            query_name = query[2]
            phonebook.add_contact(query_number, query_name)
        elif query_type == 'del':
            phonebook.delete_contact(query_number)
        elif query_type == 'find':
            result.append(phonebook.find_contact(query_number))
    return result

def write_responses(result):
    print('\n'.join(str(r) for r in result))

if __name__ == '__main__':
    queries = read_queries()
    results = process_queries(queries)
    write_responses(results)
