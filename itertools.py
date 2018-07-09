
import itertools

def custom_increment(start, stop, increment):
    for i in itertools.count(start, increment):
        if i < stop + increment:
            print(i)
        else:
            break


one_to_ten = list(range(1,11))
twenty_one_to_thirty = list(range(21,31))
combined = one_to_ten + twenty_one_to_thirty

chained = itertools.chain(range(1,11),range(21,31))

chain_match = None
if chained == combined:
    chain_match = True



if __name__ == "__main__":
    print("Ready to iterate")