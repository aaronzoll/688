class mylist(list):
    def __init__(self):
        self.list=[]
x=mylist()
x.append(9)
x.list.append(10)
print(x.list[0])
