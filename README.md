# Is It an Anagram? A Prime Solution to a Classic Problem

Recently, I came across a seemingly simple interview question:

_"Write code to determine if two words are anagrams."_

At first glance, it appears trivial—almost easy. But without constraints, the question reveals its true purpose: to test a candidate’s creativity an
d understanding of data structures. Should we sort the strings and compare them? Use a frequency table (like a hash map or an array) to count each letter?

There are many valid approaches, but I found myself wondering: _What’s the most arbitrary—yet creative—solution possible?_ Can we tackle this problem from an entirely different perspective?

## Let’s Think Differently

What if we treat letters as numbers? After all, characters are represented by ASCII values. But simply summing or comparing ASCII codes doesn’t work—"ad" and "bc" would incorrectly be flagged as anagrams (both sum to 197).

## The Prime Factorization Insight

Numbers are built from primes. Every integer has a unique prime factorization—a mathematical fingerprint. For example:

- $15 = 3 × 5$

- $42 = 2 × 3 × 7$

- $123456789 = 3 × 3 × 3607 × 3803$.

This uniqueness is key. If we could map each letter to a prime number, then a word’s letters could multiply to a unique product. Two words would be anagrams _if and only if_ their products matched!

### The Prime Anagram Strategy

Assign each letter a prime number:

`a = 2, b = 3, c = 5, d = 7, e = 11, ..., z = 101`.

Compute the product of primes for each word.
Compare the products. If equal, the words are anagrams!

```python
letter_map = {
    'a': 2,
    'b': 3,
    'c': 5,
    'd': 7,
    'e': 11,
    'f': 13,
    'g': 17,
    'h': 19,
    'i': 23,
    'j': 29,
    'k': 31,
    'l': 37,
    'm': 41,
    'n': 43,
    'o': 47,
    'p': 53,
    'q': 59,
    'r': 61,
    's': 67,
    't': 71,
    'u': 73,
    'v': 79,
    'w': 83,
    'x': 89,
    'y': 97,
    'z': 101
}

def is_anagram(word1, word2):
    def normalize(letter):
        return letter_map[letter]

    anagram1 = 1
    anagram2 = 1

    for letter in word1:
        anagram1 = anagram1 * normalize(letter)

    for letter in word2:
        anagram2 = anagram2 * normalize(letter)

    return anagram1 == anagram2


print(is_anagram('listen', 'silent'))    # True
print(is_anagram('hello', 'world'))      # False
print(is_anagram('evil', 'vile'))        # True
print(is_anagram('fluster', 'restful'))  # True
```

Following the code, let's calculate the first pair of words:

- "listen" = L × I × S × T × E × N = 37 × 23 × 67 × 71 × 11 × 43 = Big number
- "silent" = S × I × L × E × N × T = 67 × 23 × 37 × 11 × 43 × 71 = Same big number

## Why It Works

It's unique—primes ensure no other letter combination produces the same product (thanks to the Fundamental Theorem of Arithmetic).

It's efficient—multiplication is `O(n)` per word, with no need for sorting or extra data structures.

## Final Thoughts

This approach isn’t necessarily _practical_, but it’s a fun reminder that even simple problems can inspire creative solutions when viewed through a different lens.

### Wait, Could We Use RSA?

If we’re already hijacking number theory, why not go further? _Technically_, we could treat this like a miniature RSA problem:

- Encode each word as a product of primes (like RSA’s public key modulus $n = p × q$).

- Anagram-checking becomes a matter of factoring the product—which is hard for large numbers (hence RSA’s security).

But this is where the analogy collapses:

- Sloth mode—factoring large numbers is deliberately slow (that’s RSA’s whole point!), making this approach absurdly inefficient for anagrams.

- Overkill—why break out cryptographic tools when any other solution solves the problem in `O(n)` time?

Still, it’s amusing to imagine forcing an interviewer to watch you derive prime mappings while muttering about Shor’s algorithm.

_Fun fact: If quantum computers ever trivialize prime factorization, even RSA won’t be safe… but your anagram checker will still work fine!_

---

Inspired by this [tweet](https://x.com/fermatslibrary/status/875340896379817984).
