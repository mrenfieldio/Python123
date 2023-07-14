"""a={1,2,3,"abc",3}
print(a)
a.add(110)
print(a)
a.update("m","n","p")
print(a)
c=["man","car"]
a.update(c)
print(a)
d=[20,21,21]
a.update(d)
print(a)"""

d={
    "name":"ashish",
    "age": 25,
    "place" : "konni",
    "institution":"synnefo"

}
print(d)
d.update({"place":"kochi"})
print(d)
d["name"]="karthik"
print(d)
d.pop("name")
print(d)

