# Алгоритм Дейкстры
# Не работает если у гафов отрицательная стоимость прохождения

graph = {}  # Создание хеш-таблицы графа

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}  # У конечного узла fin нет соседей

infinity = float('inf')  # Ввел переменную бесконечность

costs = {}  # Создание таблицы стоимостей
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}  # создаем родителей (для узлов)
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []  # массим для отслеживания уже обработанных узлов


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # Перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # Если это узел с наименьшей стоимостью из уже виденных и он еще не был обработан...
            lowest_cost = cost  # Он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # Найти узел с наименьшей стоимостью среди необработанных

while node is not None:  # если обработаны все узлы, цикл завершится
    cost = costs[node]
    neighbords = graph[node]  # получить стоимость соседей узла
    for n in neighbords.keys():  # перебрать соседей текущего узла
        new_cost = cost + neighbords[n]
        if costs[n] > new_cost:  # Если к соседу можно быстрее добраться через текущий узел...
            costs[n] = new_cost  # Обновить стоимость для этого узла
            parents = node  # этот узел становится новым родителем для соседа
    processed.append(node)  # Узел помечается как обработанный
    node = find_lowest_cost_node(costs)  # Найти следующий узел для обработки и повторить цикл

print(costs)