template = "myname %s age:%.2f"
print(template)
print(template % ("Sviatoslav" , 20))
print(template % ("Anastia" , 18))

template = "myname: {} age:{}"

print(template.format("Sviatoslav" , 18))

template = "myname: {name} age:{age} {name}"

print(template.format(age = 20, name="Sviatoslav"))

print(f"name={input("myne")} age = {59**9}")

s = "abcdf"
print(s[0])
# print (s[50])
print(s[-1])
print(s[-2])
print(s[0:3])
print(s[2:-1])
print(s[2:-1:2])
print(s[:-1:2])
print(s[2::2])
