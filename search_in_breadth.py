from _collections import deque

graph = {}

graph['you'] = ['be', 'he', 'wom']
graph['wom'] = []
graph['he'] = ['by', 'she', '8']
graph['be'] = ['lan', '1x', 'by']
graph['lan'] = ['1w']
graph['1w'] = []
graph['1x'] = ['m3']
graph['m3'] = []
graph['by'] = ['zon', 'man']
graph['zon'] = []
graph['man'] = []
graph['she'] = ['cla']
graph['cla'] = ['16']
graph['16'] = []
graph['8'] = ['16']


def person_name_have_z(name):
    return 'a' in name


def search(name):  # Если кто-либо из связей будет найден по условию из предыдцщей функции, то будет выведено имя по условю, до которого кротчайший путь в связях
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # Для отслеживания уже проверенных имен
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:  # Проверяем только в том случае, если раньше не проверяли
            if person_name_have_z(person):
                print(f'{person} have "a"!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)  # Имя проверяется уже как првоеренное
    return False


search('you')