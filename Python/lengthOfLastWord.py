def lengthOfLastWord(s: str) -> int:
        return len(s.split()[-1])
    
print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord(" "))
print(lengthOfLastWord(""))