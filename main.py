def countVowels(word, vowels_list):
    count = 0
    
    # iterate through each character in the word
    for ch in word:
        # check if character is present in vowels list
        if ch in vowels_list:
            count += 1
    
    return count


vowels_list = ['a', 'e', 'i', 'o', 'u']
word = input('Enter the string word : ')

numberOfVowels = countVowels(word, vowels_list)

print(f"Number of vowels in the given word : {numberOfVowels}")