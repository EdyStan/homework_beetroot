from task_2_classes import Worker, Boss

b1 = Boss(1, 'Allan Walker', 'Coca Cola')
w1 = Worker(2, 'Ray Misterio', 'Coca Cola', b1)
w2 = Worker(3, 'John Cena', 'Coca Cola', b1)

b1.workers = w1, w2
print(b1.workers)
del b1.workers
print(b1.workers)

w1.boss = b1
print(w1.boss)
del w1.boss
print(w1.boss)
