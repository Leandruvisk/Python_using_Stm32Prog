import subprocess
import re
import shutil
import sys
import os

import list_stlinks
import erase_flash
import write_flash

#seleciionar diretorio do elf
my_direct = os.getcwd()
directory_elf = "/elfs_tests/teste.elf"
directory_elf = my_direct + directory_elf
print("diretorio final do elf:", directory_elf)

#encontar os clients
cli = shutil.which("STM32_Programmer_CLI")
print("CLI:", cli)

if not cli:
    print("ERRO: STM32_Programmer_CLI não encontrado no PATH")
    sys.exit(1)

#listar os sklinks
stlinks = list_stlinks.list_all_stlinks(cli)
print("ST-LINK encontrados:")
print(stlinks)

option = int(input("selecione STLINK: "))
print("stlink selecionado foi: ", stlinks[option])

#apagar memoria
serialnumber_stlink = stlinks[option]
status_erase_flash = erase_flash.erase_flash_memory(cli, serialnumber_stlink)

#escreve na memoria
print("caminho do elf: ", directory_elf)
status_write_flash = write_flash.write_flash_memory(cli, serialnumber_stlink, directory_elf)

