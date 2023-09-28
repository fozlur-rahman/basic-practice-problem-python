s=list(map(str, input().split()))
reverse_word = [word[::-1] for word in s]
print(*reverse_word)