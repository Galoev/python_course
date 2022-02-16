from functools import reduce


def generate_table_head(cols):
    return " {" + reduce(lambda el_prev, el: el_prev + "c|", range(cols), "|") + "} "

def generate_table(data, rows, cols):
    result = "\\begin{tabular} " + generate_table_head(cols)
    
    result += "\\hline "
    for i in range(rows):
        result += ' & '.join(map(str, data[i]))
        result += "\\\\"
        result += " \\hline "

    return result + "\\end{tabular}"

def generate_latex(table):
    return "\\documentclass{article}\\usepackage[utf8]{inputenc}\\begin{document}" + \
            generate_table(table, len(table), len(table[0])) + \
            "\\end{document}"

if __name__ == "__main__":
    table = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with open('artifacts/table.tex', 'w') as f:
        f.write(generate_latex(table)) 