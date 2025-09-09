from collections import defaultdict


class Calculator:
    def get_connected(self, node_count, edges):

        if not edges:
            return node_count

        nodes_dict = defaultdict(list)
        for node in edges:
            nodes_dict[node[0]].append(node[1])
            nodes_dict[node[1]].append(node[0])

        # 0: [1], 1: [0, 2, 3], 2: [1, 4], 3: [1], 4: [2], 5: [6], 6: [5]}

        seen = set()
        result = 0

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for node in nodes_dict[node]:
                dfs(node)

        for key, _ in nodes_dict.items():
            if key not in seen:
                result += 1
                dfs(key)

        return result
