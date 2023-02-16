import random

boys = ['mohammad', 'sobhan', 'abdollah', 'kiya', 'mahdi', 'sajjad', 'homan', 'arman']
girls = ['mahtab', 'hane', 'harir', 'fateme', 'kiana', 'faezeh', 'minoo', 'mina', 'soghra']

pair = []
print('pairs =',end=' ')
for i in range(min(len(boys),len(girls))):
    boy = boys[random.randint(0, len(boys)-1)]
    girl = girls[random.randint(0, len(girls)-1)]
    pair.append([boy,girl])
    boys.remove(boy)
    girls.remove(girl)
    print(f'({boy},{girl})',end=' ')
print('')
if len(girls):
    print(girls,'are single 😑')
elif len(boys):
    print(boys,'are single 😑')
