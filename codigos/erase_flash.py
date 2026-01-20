import subprocess
import re
import shutil
import sys

def erase_flash_memory(cli, sn):
    print(f"\nApagando flash do SN {sn}")

    result = subprocess.run(
        [cli, "-c", f"port=SWD sn={sn}", "-e", "all"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print("ERRO ao apagar flash")
        sys.exit(1)

    print("Flash apagada com sucesso")
