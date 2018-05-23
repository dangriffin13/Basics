import itertools

def odds(upper_limit):
    return [i for i in range(1,upper_limit,2)]

def evens(upper_limit):
    return [i for i in range(0,upper_limit,2)]

nested = [i**j for i in range(1,10) for j in range(1,4)]

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = [chr(i) for i in range(97,123) if chr(i) not in vowels]

ascii_table = {i:chr(i) for i in itertools.chain(range(65,91), range(97,123))}

ascii_lowercase = {i:chr(i) for i in ascii_table.keys() if chr(i) == chr(i).lower()}



if __name__ == "__main__":
    print('odds', odds(12))
    print('evens', evens(11))
    print('consonants', consonants)
    print('ord of vowels', [ord(char) for char in vowels]) 
    print('nested', nested)   


