from PyInquirer import style_from_dict, Token, prompt
from examples import custom_style_2

# Initialising hashtables
hashtable1 = [-9999,-9999,-9999,-9999,-9999,-9999,-9999,-9999,-9999,-9999,-9999]; 
hashtable2 = [-9999,-9999,-9999,-9999,-9999,-9999,-9999,-9999,-9999,-9999,-9999]; 
recursiveCounter = 0
addingFactor = 0
cycle = 0
# Hash function for table 1
def hash1(key):
    global addingFactor
    return (key+addingFactor)%11;

# Hash function for table 2
def hash2(key):
    global addingFactor
    return int(((key+addingFactor)/11)%11);

# Print function
def print_tables():
    global hashtable1
    global hashtable2
    print("\nTable 1: ", end=' ')
    for i in range(11):
        if hashtable1[i] == -9999:
            print("empty ",end=' ')
        else:
            print(hashtable1[i], end=' ')
    print("\nTable 2: ", end=' ');
    for i in range(11):
        if hashtable2[i] == -9999:
            print("empty ",end=' ')
        else:
            print(hashtable2[i], end=' ')
    print("\n");

# if the position in hashtable 1 is empty -> place the key there
# if not, then rehash the previous value in hashtable1 to hash2 and store it there if that place is empty
# in case recursive calls are being made more than 5 times, a cycle is present so time to rehash. 
def insert(key):
    global hashtable1
    global cycle
    global hashtable2
    global recursiveCounter
    global maxNumberOfRecursiveCalls
    global addingFactor
    if recursiveCounter == 10: 
        if cycle == 0:
            print('Cycle is present so rehashing now. \n')
            
        arr1 = []
        arr1.append(key)
        recursiveCounter = 0
        cycle += 1
        for i in range(11):
            if hashtable1[i] != -9999:
                arr1.append(hashtable1[i])
            if hashtable2[i] != -9999:
                arr1.append(hashtable2[i])
        addingFactor +=1

        for i in range(11):
            hashtable1[i] = -9999
            hashtable2[i] = -9999
        for i in arr1:
            insert(i)
        return 1

    hashkey1 = hash1(key)
    if hashtable1[hashkey1] == -9999:
        hashtable1[hashkey1] = key
        return 0
    else:
        previouskey = hashtable1[hashkey1]
        hashtable1[hashkey1] = key
        hashkey2 = hash2(previouskey)
        if hashtable2[hashkey2] == -9999:
            hashtable2[hashkey2] = previouskey
            return 0
        else:
            previouskey2 = hashtable2[hashkey2]
            hashtable2[hashkey2] = previouskey
            recursiveCounter +=1
            insert(previouskey2)



# Hash the key and then replace the index number with -9999 which indicates an empty space 
def delete(key):
    global hashtable1
    global hashtable2
    hashkey1 = hash1(key)
    if(hashtable1[hashkey1] == key):
        hashtable1[hashkey1] = -9999
        print(key, end = ' ')
        print('has been deleted successfully.')
    else:
        hashkey2 = hash2(key)
        if hashtable2[hashkey2] == key:
            hashtable2[hashkey2] = -9999
            print(key, end = ' ')
            print('has been deleted successfully.')
        else:
            print('No such number in the hash table. \n')

# Hash the key according to hashtable 1 and see if the key is present there. 
# If not, hash according to hashtable 2 and see if the key is present there.
# If its not present in both the hashtables, display that the number is not present in both of them.
def search(key):
    global hashtable1
    global hashtable2
    hashkey1 = hash1(key)
    if hashtable1[hashkey1] == key:
        print(key, end= ' ')
        print('is present in hashtable1 at index', hashkey1)
    else:
        hashkey2 = hash2(key)
        if hashtable2[hashkey2] == key:
            print(key, end = ' ')
            print('is present in hashtable2 at index',hashkey2)
        else:
            print('No such number is present in both the hashtables.\n')

# Menu 
def main():
    global hashtable1
    global hashtable2
    global recursiveCounter
    global maxNumberOfRecursiveCalls
    global numberofkeys
    while(1):
        options_prompt = {
        'type': 'list',
        'name': 'choice',
        'message': 'What do you want to do?',
        'choices': ['Insert', 'Delete', 'Search', 'Print both tables', 'Exit']
        }

        answer = prompt(options_prompt,style = custom_style_2)

        if answer['choice'] == 'Exit':
            print('Exiting...')
            break
        elif answer['choice'] == 'Print both tables':
            print_tables()
        elif answer['choice'] == 'Insert':
            insert_prompt = {
                'type' : 'input',
                'name' : 'key',
                'message' : 'Enter the key you want to insert: '
            }
            answer1 = prompt(insert_prompt, style = custom_style_2)
            answer1 = answer1['key']
            try:
                answer1 = int(answer1)
            except:
                print('You can only insert integers. \n')
                continue
            recursiveCounter = 0
            cycle = 0
            insert(answer1)
            print(answer1, end = ' ')
            print('has been inserted. \n')
        elif answer['choice'] == 'Delete':
            insert_prompt = {
                'type' : 'input',
                'name' : 'key',
                'message' : 'Enter the key you want to delete: '
            }
            answer1 = prompt(insert_prompt, style = custom_style_2)
            answer1 = answer1['key']
            try:
                answer1 = int(answer1)
            except:
                print('You can only search and delete integers. \n')
                continue

            delete(answer1)
           
        elif answer['choice'] == 'Search':
            insert_prompt = {
                'type' : 'input',
                'name' : 'key',
                'message' : 'Enter the key you want to search: '
            }
            answer1 = prompt(insert_prompt, style = custom_style_2)
            answer1 = answer1['key']
            try:
                answer1 = int(answer1)
            except:
                print('You can only search for integers. \n')
                continue

            search(answer1)
main()