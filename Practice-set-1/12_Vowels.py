sentence = input().lower()
vowel_count = 0

for ch in sentence:
    if ch in "aeiou":
        vowel_count += 1

print(vowel_count)