import csv


def palindrome(fileRead, fileWrite):
    file1 = open(fileRead, 'r', newline='')
    file2 = open(fileWrite, 'w', newline='')
    i = 0
    for row in csv.reader(file1):
        i += 1
        word = ', '.join(row)
        chars = ''.join(set(word))
        csv.writer(file2).writerow([f"{i}, {word}, {chars}, {isPalindrome(word)}"])
    file1.close()
    file2.close()


def isPalindrome(word):
    return word == word[::-1]


palindrome('random.csv', 'random_wyniki.csv')
