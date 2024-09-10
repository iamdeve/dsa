employee = {
    'name': 'John',
    'age': 30,
    'salary': 50000,
    'position': 'Manager'
}

print(employee['name'])

def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end = " ")
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
        print()

HashTable = [[] for _ in range(10)]

def Hashing(key):
    return key % len(HashTable)


def insert(Hashtable, key, value):
    hash_key = Hashing(key)
    Hashtable[hash_key].append(value)


insert(HashTable, 10, 'John')
insert(HashTable, 25, 'Peter')
insert(HashTable, 20, 'Michael')
insert(HashTable, 9, 'Terry')
insert(HashTable, 21, 'Terry')
insert(HashTable, 21, 'Terry')

display_hash(HashTable)

