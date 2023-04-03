# Ena Daniela Ercina 2.grupa. 221RDB369
class AddressBook:
    def __init__(self):
        self.addresses = {}

    def add_address(self, number, name):
        self.addresses[number] = name

    def delete_address(self, number):
        try:
            del self.addresses[number]
        except KeyError:
            pass

    def find_address(self, number):
        try:
            return self.addresses[number]
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
    address_book = AddressBook()
    result = []
    for query in queries:
        query_type = query[0]
        query_number = int(query[1])
        if query_type == 'add':
            query_name = query[2]
            address_book.add_address(query_number, query_name)
        elif query_type == 'del':
            address_book.delete_address(query_number)
        elif query_type == 'find':
            result.append(address_book.find_address(query_number))
    return result

def write_responses(result):
    print('\n'.join(result))

if __name__ == '__main__':
    queries = read_queries()
    results = process_queries(queries)
    write_responses(results)
