
from tree_sitter import Language, Parser
import re
import pandas as pd
import sys
sys.setrecursionlimit(50000)  # 设置递归深度限制为5000（根据需要调整）


parser = Parser()
LANGUAGE = Language('./build_languages/my-languages.so', 'cpp')
parser.set_language(LANGUAGE)
STATEMENT_ENDING_STRINGS = ['if_statement', 'compound_statement', 'for_statement', 'while_statement', 'do_statement',
                            'catch_clause', 'case_statement', 'try_statement', 'assignment_expression',
                            'member_expression',
                            'switch_statement', 'function_definition', 'expression_statement', 'continue_statement',
                            'break_statement',
                            'return_statement', 'call_expression', 'access_specifier', 'pointer_declarator']


def is_statement_node(node):
    endings = STATEMENT_ENDING_STRINGS
    end = node.type
    if end in endings:
        return True
    else:
        return False


def __statement_xsbt(node):
    xsbt = []
    if len(node.children) == 0:

        xsbt.append(node.text.decode('utf-8'))

    else:
        if is_statement_node(node):
            # print(type(node))
            xsbt.append("start_{}".format(node.type))
        for child in node.children:
            xsbt += __statement_xsbt(child)
        if is_statement_node(node):
            xsbt.append("end_{}".format(node.type))
    return xsbt


def generate_statement_xsbt(root_node, functions, flatten):
    tokens = __statement_xsbt(root_node)
    tokens = [token.replace("\n", "") for token in tokens]
    if flatten:
        function = ' '.join(tokens)
    else:
        function = '\n'.join(tokens)
    functions.append(function)


def selectFun(nodes, functions, flatten):
    if len(nodes.children) == 0:
        return
    for child_node in nodes.children:
        if child_node.type == "function_definition":
            generate_statement_xsbt(child_node, functions, flatten)
        selectFun(child_node, functions, flatten)

i = 0


def extract(code, flatten=True):

    global i
    i=i+1
    print(i)
    functions = []


    code = re.sub(r"\b[^\s(){}]+\s*\([^)]*\s*\)\s*(?:\s|\n)*\{((?:\s|\n)*\{(?:\s|\n)*\}|)(?:\s|\n)*\}", "", code)
    code = re.sub(r"//.*", "", code)  # 删除 //注释

    code =re.sub(r'/\*.*?\*/','',code, flags=re.DOTALL)
    code = re.sub(r'\\', '', code)

    # tree = parser.parse(code.encode('utf-8').decode('unicode_escape').encode())
    tree =parser.parse(bytes(code,"utf-8"))
    root_node = tree.root_node
    flatten = flatten
    selectFun(root_node, functions, flatten)
    for fun in functions:
        print(fun)
        return fun


if __name__ == '__main__':


    df = pd.read_csv(r'/home/yons/person/zc/ArVD/model/xsbt_process/data/train_index.csv')
    df['sentence'] = df['sentence'].astype(str)
    df['sentence'] = df['sentence'].apply(extract)
    df = df[df['sentence'] != 'VAR1 '] # delete description failed
    df = df.dropna(subset=['sentence'])
    df.to_csv(r'/home/yons/person/zc/ArVD/model/xsbt_process/data/train_xsbt.csv', index=False)


