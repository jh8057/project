x = dict()
y = {}

z = {
    "name" : "A",
    "age" : 20,
    0 : "Wow"
}


print (x)
print (y)

print(z["name"])
print(z["age"])
print(z[0])
print("name" in z)

print(z.keys())
print(z.values())

for key in z:
    print(key)
    print(z[key])

z[0] = "zzz"
print(z)

z[1] = "www"
print(z)

