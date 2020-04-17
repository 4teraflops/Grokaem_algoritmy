graph = {}

graph['start'] = {}
graph['start']['a'] = 5
graph['start']['c'] = 2
graph['a'] = {}
graph['a']['b'] = 4
graph['a']['d'] = 2
graph['b'] = {}
graph['b']['fin'] = 3
graph['b']['d'] = 6
graph['c'] = {}
graph['c']['a'] = 8
graph['c']['d'] = 7
graph['d'] = {}
graph['d']['fin'] = 1
graph['fin'] = {}

infinity = float('inf')

costs = {}
costs['a'] = 5
costs['b'] = infinity
costs['c'] = 2
costs['d'] = infinity
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'a'
parents['c'] = 'start'
parents['d'] = None
parents['fin'] = None

processed = []


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