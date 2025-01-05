# Grouping Anagrams from a list of given words

def key_maker(s: str) -> str:
    return ''.join(sorted(s))

def collect_anagrams(words: list[str]) -> list[set[str]]:
    candidates = dict()
    for word in words:
        key = key_maker(word)
        if key not in candidates:
            candidates[key] = {word}
        else:
            candidates[key].add(word)
    return [anags for anags in candidates.values() if len(anags) > 1]
