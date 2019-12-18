def gen1(n):
    for i in n:
        yield i
        #print(i)

def gen2(s):
    for i in range(s):
        yield i

gen = gen1('Виталий')
num = gen2(7)

tasks = [
    gen,
    num,
]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        print("THE END")
