import re
from hashlib import md5
from itertools import count


def run():
    key = input()

    hashes = {}
    counter = 0
    break_point = float('inf')

    for number in count(start=0):
        if number > break_point:
            return [key for key, value in hashes.items() if value is True][63]
        hsh = md5(f'{key}{number}'.encode()).hexdigest()
        first_triplet = re.search(r'(.)\1{2}', hsh)
        if first_triplet:
            old_hash_keys = [[key, value] for key, value in hashes.items() if key >= number - 1000]
            hashes[number] = first_triplet.group(1)
            for quintuplet in {q.group(1) for q in re.finditer(r'(.)\1{4}', hsh)}:
                for items in filter(lambda i: i[1] == quintuplet, old_hash_keys):
                    hashes[items[0]] = True
                    counter += 1
                    if counter == 64:
                        break_point = items[0] + 1000

    # unreachable
    return None


print(run())
