# renomear_arquivos.py

import os

def renomear_arquivos(pasta, novo_nome):
    for count, filename in enumerate(os.listdir(pasta)):
        dst = f"{novo_nome}{count}{os.path.splitext(filename)[1]}"
        src = f"{pasta}/{filename}"
        dst = f"{pasta}/{dst}"
        os.rename(src, dst)

# Uso
if __name__ == "__main__":
    renomear_arquivos('caminho/para/pasta', 'novo_nome_')
