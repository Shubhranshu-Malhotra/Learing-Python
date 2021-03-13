class SuperList(list):
    def __len__(self):
        return 1000

superlist1 = SuperList()
superlist1.append(5)
print(superlist1)
print(len(superlist1))
print(superlist1[0])
print(issubclass(SuperList, list))
print(issubclass(list, object))