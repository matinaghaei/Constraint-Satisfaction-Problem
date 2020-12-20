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
        self.answer = []
        self.ac3()
        if self.search(self.minimum_remaining_values_node()):
            self.print_result()
        else:
            print("FAILURE")

    def search(self, current_node):
        if current_node is None:
            return True
        self.answer.append(current_node)
        while True:
            if current_node.iterate_value_index() is False:
                self.answer.pop()
                return False
            if self.check_constraints():
                if current_node.forward_check():
                    if self.search(self.minimum_remaining_values_node()):
                        return True
                current_node.restore_domains()

    def minimum_remaining_values_node(self):
        mrv_node, remaining = None, None
        for node in self.nodes:
            if node not in self.answer:
                if mrv_node is None or node.remaining_values() < remaining:
                    mrv_node, remaining = node, node.remaining_values()
        return mrv_node

    def check_constraints(self):
        for node in self.answer:
            if node.check_constraints() is False:
                return False
        return True

    def print_result(self):
        for node in self.nodes:
            print(node.get_value(), end=' ')

    def ac3(self):
        reduced = True
        while reduced:
            reduced = False
            for node in self.nodes:
                if len(node.reduce_domain()) != 0:
                    reduced = True
