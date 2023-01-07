# 백준 2941번
croa_alphabet = ['c=', 'c-', 'dz=',
                 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for w in croa_alphabet:
    word = word.replace(w, 'a')

print(len(word))
