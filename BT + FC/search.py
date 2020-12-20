from node import Node


class Search:

    def __init__(self, node_types, neighbours):
        self.nodes = []
        for node_type in node_types:
            self.nodes.append(Node(node_type))
        for neighbour in neighbours:
            n1, n2 = self.nodes[neighbour[0]], self.nodes[neighbour[1]]
            n1.add_neighbour(n2)
            n2.add_neighbour(n1)
        if self.search(0):
            self.print_result()
        else:
            print("FAILURE")

    def search(self, current):
        if current == len(self.nodes):
            return True
        current_node = self.nodes[current]
        while True:
            if current_node.iterate_value_index() is False:
                return False
            if self.check_constraints(current):
                if current_node.forward_check():
                    if self.search(current + 1):
                        return True
                current_node.restore_domains()

    def check_constraints(self, current):
        for i in range(current + 1):
            if self.nodes[i].check_constraints() is False:
                return False
        return True

    def print_result(self):
        for node in self.nodes:
            print(node.get_value(), end=' ')
