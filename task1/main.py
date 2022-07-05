from itertools import permutations as comb


# The shortest path search function takes two parameters, since the origin can be associated with the post office.
# The first parameter is List[Tuple[x,y],...], the points that the postman should visit.
# The second parameter is Tuple[x,y], the coordinates of the post office.
def shortest_route(map_delivery, post_office=(0, 0)):
    # Function for finding the length of the route.
    def length_route(map_route):
        length = 0.0
        for j in range(len(map_route) - 1):
            length += ((map_route[j + 1][0] - map_route[j][0]) ** 2 + (
                    map_route[j + 1][1] - map_route[j][1]) ** 2) ** 0.5
        return length

    # Route Generator.
    def generator_route():
        route = [post_office]
        for i in comb(range(len(map_delivery)), len(map_delivery)):
            for j in i:
                route.append(map_delivery[j])
            route.append(post_office)
            yield route
            route = [post_office]

    # Function for finding the shortest route.
    def search_route():
        min_route = [post_office] + map_delivery + [post_office]
        min_length_route = length_route(min_route)
        for i in generator_route():
            length_route_i = length_route(i)
            if length_route_i < min_length_route:
                min_length_route = length_route_i
                min_route = i
        return min_route

    # Function for beautiful output of the result.
    def print_result():
        length = 0.0
        result = search_route()
        result_str = str(post_office)
        for j in range(len(result) - 1):
            length += ((result[j + 1][0] - result[j][0]) ** 2 + (
                    result[j + 1][1] - result[j][1]) ** 2) ** 0.5
            result_str += '->' + str(result[j + 1]) + str([length])
        result_str += '=' + str(length)
        return result_str

    return print_result()


card = [(1, 4), (4, 1), (5, 5), (7, 2)]
post = (0, 1)
print(shortest_route(card, post_office=post))
