def touchscreen_keyboard():
    adjacency_matrix = [
        'qwertyuiop',
        'asdfghjkl',
        'zxcvbnm'
    ]

    # Read input
    # cases
    n = int(input())
    for _ in range(n):
        base_string, num_of_sug = input().split(' ')
        suggestions = []
        sorted_suggestions = {}
        for i in range(int(num_of_sug)):
            suggestions.append(input())

        # sort suggestions
        suggestions = sorted(suggestions)

        for suggestion in suggestions:
            total_distance = 0
            for l1, l2 in zip(base_string, suggestion):
                x1, y1 = -1, -1
                x2, y2 = -1, -1
                if l1 in adjacency_matrix[0]:
                    x1 = 0
                    y1 = adjacency_matrix[0].find(l1)
                if l1 in adjacency_matrix[1]:
                    x1 = 1
                    y1 = adjacency_matrix[1].find(l1)
                if l1 in adjacency_matrix[2]:
                    x1 = 2
                    y1 = adjacency_matrix[2].find(l1)

                if l2 in adjacency_matrix[0]:
                    x2 = 0
                    y2 = adjacency_matrix[0].find(l2)
                if l2 in adjacency_matrix[1]:
                    x2 = 1
                    y2 = adjacency_matrix[1].find(l2)
                if l2 in adjacency_matrix[2]:
                    x2 = 2
                    y2 = adjacency_matrix[2].find(l2)

                total_distance += abs(x2 - x1) + abs(y2 - y1)

            sorted_suggestions[suggestion] = total_distance

        sorted_suggestions = [f'{k} {v}' for k, v in sorted(sorted_suggestions.items(), key=lambda item: item[1])]
        print('\n'.join(sorted_suggestions))


touchscreen_keyboard()
