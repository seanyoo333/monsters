spookiness = int(input().strip())
if not 2 <= spookiness <= 20:
    exit(f"!= 2 <= {spookiness} <=20")

spooky_word = "sp" + "o"*spookiness + "ky"

print(spooky_word)
