# clarice cli v0.1
# (c) 2021 kaiete
# MIT license
while True:
  print("> ",end="")
  msg = input()
  if "hello" in msg or "hi" in msg:
    print("hello there!")
  elif "goodbye" in msg or "bye" in msg or "cya" in msg:
    print("bye! see you later!")
    exit("clarice left the conversation")