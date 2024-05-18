def vowels(text) -> int:
    vowels_counts = 0
    all_vowels = "aeiouAEIOU"

    for letter in text:
        if letter in all_vowels:
            vowels_counts += 1

    return vowels_counts


