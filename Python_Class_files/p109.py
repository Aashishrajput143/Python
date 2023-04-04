#string formatting
n="Rohit"
#s="n is the captain of indian cricket team.n is a good captain."

s="%s is the captain of indian cricket team.%s is a good captain."%(n,n)
print(s)

s="{0} is the captain of indian cricket team.{1} is a good captain.".format(n,n)
print(s)

s="{0} is the captain of indian cricket team.{0} is a good captain.".format(n)
print(s)

s="{i} is the captain of indian cricket team.{i} is a good captain.".format(i=n)
print(s)

s=f"{n} is the captain of indian cricket team.{n} is a good captain."
print(s)
