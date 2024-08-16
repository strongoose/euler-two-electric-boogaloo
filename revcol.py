from euler.reverse_collatz import CollatzTree

t = CollatzTree()

cover = 10
while t.coverage[:cover] != list(range(1, cover + 1)):
    t.grow()

# for s in t.sequences():
#     print(s)

print(t.coverage)
