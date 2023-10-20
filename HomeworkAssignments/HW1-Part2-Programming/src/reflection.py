from src.models import Student

print(dir(str))

s = "Cat"
print(s.count("a"))

m = getattr(s, 'count')
print(m("a"))

