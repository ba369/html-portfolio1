
for line in open("nlp.py.txt"):
  for word in line.split():
    if word.endswith('ing'):
     print(word)
     print(len(word))
