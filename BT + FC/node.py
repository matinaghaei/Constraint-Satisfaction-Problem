class Node:

    def __init__(self, node_type):
        self.node_type = node_type
        self.neighbours = []
        self.values = list(range(1, 10))
        self.value_index = len(self.values)
        self.reduced_nodes = []

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def iterate_value_index(self):
        if self.value_index == len(self.values):
            self.value_index = 0
        else:
            self.value_index += 1
        return self.value_index < len(self.values)

    def get_value_index(self):
        return self.value_index

    def get_value(self):
        if self.get_value_index() == len(self.values):
            return None
        return self.values[self.value_index]

    def check_constraints(self):
        if self.node_type == 'T':
            p = 1
            for neighbour in self.neighbours:
                if neighbour.get_value() is None:
                    return True
                p *= neighbour.get_value()
            return self.left_most_digit(p) == self.get_value()
        elif self.node_type == 'S':
            none_neighbour = False
            p = 1
            for neighbour in self.neighbours:
                value = neighbour.get_value()
                if value is None:
                    none_neighbour = True
                    continue
                if value % 2 == 0 and self.get_value() % 2 == 1:
                    return False
                p *= value
            return none_neighbour or self.right_most_digit(p) == self.get_value()
        elif self.node_type == 'P':
            s = 0
            for neighbour in self.neighbours:
                if neighbour.get_value() is None:
                    return True
                s += neighbour.get_value()
            return self.left_most_digit(s) == self.get_value()
        elif self.node_type == 'H':
            s = 0
            for neighbour in self.neighbours:
                if neighbour.get_value() is None:
                    return True
                s += neighbour.get_value()
            return self.right_most_digit(s) == self.get_value()
        else:
            return True

    @staticmethod
    def left_most_digit(number):
        while number >= 10:
            number /= 10
        return number

    @staticmethod
    def right_most_digit(number):
        return number % 10

    def forward_check(self):
        for node in self.neighbours:
            if node.not_set():
                reduced_values = node.reduce_domain()
                self.reduced_nodes.append({"Node": node, "Values": reduced_values})
                if node.is_domain_empty():
                    return False
        return True

    def restore_domains(self):
        for reduced_node in self.reduced_nodes:
            reduced_node["Node"].add_to_domain(reduced_node["Values"])

    def is_domain_empty(self):
        return len(self.values) == 0

    def contains_value(self, value):
        return value in self.values

    def reduce_domain(self):
        reduced_values = []
        self.value_index = 0
        while self.value_index < len(self.values):
            if not self.check_constraints():
                reduced_values.append(self.get_value())
                self.values.remove(self.get_value())
            else:
                self.value_index += 1
        return reduced_values

    def add_to_domain(self, values):
        self.values.extend(values)
        self.values.sort()
        self.value_index = len(self.values)

    def not_set(self):
        return self.value_index == len(self.values)
