import sys


def get_anagram_hash(word: str) -> (int, int, int):
    str_hash = 0
    str_sum = 0
    for char in word:
        # input file has only lowercase letters and whitespace
        char2int = ord(char) - 97
        str_hash += 1 << char2int
        str_sum += char2int
    return len(word), str_hash, str_sum


total = 0
for line in sys.stdin.readlines():
    anagram_hashes = set()
    ok = True
    for word in line.split():
        anagram_hash = get_anagram_hash(word)
        if anagram_hash in anagram_hashes:
            ok = False
            break
        anagram_hashes.add(anagram_hash)
    if ok:
        total += 1

print(total)
