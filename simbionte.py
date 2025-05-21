import os
import subprocess
from collections import defaultdict

# PARA FUNCIONAR É NECESSÁRIO TER O 7ZIP INSTALADO NA ET

diretorio_dos_arquivos = input("Digite o diretório onde os arquivos estão localizados: ").strip()

if not os.path.isdir(diretorio_dos_arquivos):
    print("Digite um caminho válido!")
    exit()

arquivos_com_nomes_iguais = defaultdict(list)

for arquivo in os.listdir(diretorio_dos_arquivos):
    
    localizao_completa = os.path.join(diretorio_dos_arquivos, arquivo)
    
    if os.path.isfile(localizao_completa):
        nome_base, extensao =  os.path.splitext(arquivo)
        arquivos_com_nomes_iguais[nome_base].append(localizao_completa)

for nome_base, arquivos in arquivos_com_nomes_iguais.items():
    if len(arquivos) > 1:
        destino_zip = os.path.join(diretorio_dos_arquivos, f"OI{nome_base}.7z")
        comando = ['7z', 'a', destino_zip] + arquivos
        resultado = subprocess.run(comando, capture_output=True, text=True)

        if resultado.returncode == 0:
            print(f"✅ {nome_base}.7z criado com sucesso.")
        else:
            print(f'❌ Erro ao compactar {nome_base}:')
            print(resultado.stderr) 

''' PARA DEBUGAR A COLECÃO DE NOMES IGUAIS
for nome_base, lista in arquivos_com_nomes_iguais.items():
    print(f'{nome_base}:')
    for caminho in lista:
        print(f'  - {caminho}')
'''