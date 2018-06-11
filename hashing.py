
import hashlib


def sha_256(string):
    stored_hash = hashlib.sha256(string.encode()) #string literal must be encoded
    return stored_hash.hexdigest()





if __name__ == "__main__":
    print('You can begin hashing')