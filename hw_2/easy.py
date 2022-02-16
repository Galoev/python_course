from pickletools import read_uint1
from unittest import result

from matplotlib.pyplot import table

def generate_table(data, rows, cols):
    result = "\\begin{tabular} "
    
    result += "{|"
    for i in range(cols):
        result += "c|"
    result += "} "
    result += "\\hline "

    for i in range(rows):
        result += ' & '.join(map(str, data[i]))
        result += "\\\\"
        result += " \\hline "

    result += "\\end{tabular}"
    return result

def generate_latex(table):
    head = "\\documentclass{article}\\usepackage[utf8]{inputenc}\\begin{document}"
    end = "\\end{document}"

    result = head
    
    rows = len(table)
    cols = len(table[0])

    result += generate_table(table, rows, cols)    
    result += end

    return result

if __name__ == "__main__":
    table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with open('artifacts/table.tex', 'w') as f:
        f.write(generate_latex(table)) 