def check_list():
    trie = {}
    n = int(raw_input())

    def check_insert(number, position, store):
        digit = number[position]
        store.setdefault(digit, {})
        if store[digit] == 1:
            return False
        if position+1 == len(number):
            store[digit] = 1
            return True
        else:
            return check_insert(number, position+1, store[digit])

    for i in range(n):
        number = str(raw_input()).strip()
        if not check_insert(number, 0, trie):
            print "NO"
            return
    print "YES"

t = int(raw_input())
for i in range(t):
    check_list()
