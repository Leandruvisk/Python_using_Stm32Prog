import subprocess
import re
import shutil
import sys
import os

def write_flash_memory(cli, sn, directory_elf):
    print(f"\nEscrevendo na flash do SN {sn}")
    print("Arquivo:", directory_elf)

    if not os.path.isfile(directory_elf):
        print("ERRO: arquivo ELF não encontrado")
        return False

    result = subprocess.run(
        [
            cli,
            "-c", f"port=SWD sn={sn}",
            "-w", directory_elf,
            "-v",
            "-rst"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print("ERRO ao escrever flash")
        return False

    print("Flash escrita com sucesso")
    return True