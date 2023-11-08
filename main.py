import re


def read_file_content(file_path):
    with open(file_path,"r") as f:
        return f.readlines()


def read_codification(file_path_codification):
    with open(file_path_codification,"r") as f:
        codification = {}
        k = 0
        for line in f.readlines():
            line = line.strip()
            codification[line] = k
            k += 1
        return codification


def is_identifier(token):
    return re.match(r'^[a-zA-Z_]+[0-9]*[a-zA-Z_]*$',token)


def is_constant(token):
    return re.match(r'^(\d+(?:\.\d+)?)$', token)


class SymbolTable:
    def __init__(self):
        self.count = 1
        self.table = {}

    def add(self, key):
        if key in self.table:
            return self.table[key]
        self.table[key] =self.count
        self.count += 1
        return self.count-1

    def __getitem__(self, key):
        return self.table[key]

    def __contains__(self, key):
        return key in self.table

    def __str__(self):
        return str(self.table)


def lexical_analysis(content,codification):
    pif = []
    st = SymbolTable()
    k = 1
    for line in content:
        line = line.strip()
        for code in codification:
            if code != "id" and code != "const":
                line = line.replace(code," "+code+" ")
        line = re.sub(r' +',' ',line)
        line = line.strip()

        line_tokens = line.split(" ")
        for token in line_tokens:
            token = token.strip()
            if token in codification:
                pif.append((codification[token],-1))
            elif is_identifier(token):
                pif.append((0,st.add(token)))
            elif is_constant(token):
                pif.append((1,st.add(token)))
            else:
                raise Exception(f"lexical error on line {k} at atom {token}!")

        k += 1
    return pif,st


content = read_file_content("test.txt")
codification = read_codification("codification.txt")
try:
    pif,st = lexical_analysis(content,codification)
    print(pif)
    print(st)
except Exception as ex:
    print(ex)