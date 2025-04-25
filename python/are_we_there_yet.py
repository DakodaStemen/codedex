# ask "Are we there yet?" -> 'answer'

answer = input("Are we there yet?")

while answer not in ("Yes", "yes", "YES"):
      print("Not yet.")
      answer = input("Are we there yet?")

print("Yes.")