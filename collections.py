
import collections

result_order = ['Rotich', 'Lilesa','Rupp','Ghebreslassie','Simbu','Ward','Abraham']

marathoners = {'Ghebreslassie':'Eritrea','Simbu':'Tanzania','Rotich':'Kenya',
    'Rupp':'USA','Ward':'USA', 'Lilesa':'Ethiopia','Abraham':'Switzerland'}

results_dict = collections.OrderedDict()

for name in result_order:
    results_dict[name] = marathoners[name]




with open('gettysburg_address.txt') as f:
    words = [word for line in f for word in line.split()]

lincolns_words = collections.Counter(words)

top_10 = lincolns_words.most_common(10)


dq = collections.deque(list('sesquipedalian'))




if __name__ == "__main__":
    print("Collections file is running")

    print("Marathoners:")
    print(marathoners)
    print("Marathon results:")
    print(result_order)
    print("Ordered Dictionary of results:")
    print(results_dict)
    print("Ten most used words in Gettysburg Address: ")
    print(top_10)
    print("Deque functions:")
    print(dq)
    print("Pop: ", dq.pop())
    print("Pop left: ", dq.popleft())
    print(dq)
    print("Extend left: 'new'", dq.extendleft(list('new')))
    print("Extend right: 'new'", dq.extend(list('new')))
    print(dq)
    print("Reverse: ", dq.reverse())
    print(dq)
