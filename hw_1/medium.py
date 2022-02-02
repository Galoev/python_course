import ast
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stack = []
        self.root = None
        self.graph = nx.Graph()   

    def generic_visit(self, node):
        print(type(node).__name__)
        node_name = type(node).__name__ 

        parent_name = None
        
        if self.stack:
            parent_name = self.stack[-1]

        self.stack.append(node_name)

        self.graph.add_node(node_name)

        if parent_name:
            self.graph.add_edge(node_name, parent_name)

        super(self.__class__, self).generic_visit(node)

        self.stack.pop()
    
    def visit_Module(self, node):
        super(self.__class__, self).generic_visit(node)

    def visit_FunctionDef(self, node):
        self.stack.append(node.name)
        return super(self.__class__, self).generic_visit(node)
    
    def visit_arguments(self, node):
        return super(self.__class__, self).generic_visit(node)
    
    def visit_Store(self, node):
        return super(self.__class__, self).generic_visit(node)
    

def main():
    with open("easy.py", "r") as source:
        ast_object = ast.parse(source.read())

    analyzer = Analyzer()
    analyzer.visit(ast_object)
    nx.draw(analyzer.graph, with_labels = True)
    pprint(ast.dump(ast_object))
    plt.show()


if __name__ == "__main__":
    main()
    # print(ast_object.body[-1].args)
    # print(ast.dump(ast_object))