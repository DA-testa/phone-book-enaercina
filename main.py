class Phonebook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, number, name):
        self.contacts[number] = name

    def delete_contact(self, number):
        try:
            del self.contacts[number]
        except KeyError:
            pass

    def find_contact(self, number):
        try:
            return self.contacts[number]
        except KeyError:
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
    print('\n'.join(result))

if __name__ == '__main__':
    queries = read_queries()
    results = process_queries(queries)
    write_responses(results)
