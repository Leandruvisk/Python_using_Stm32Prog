import subprocess
import re
import shutil
import sys


def list_all_stlinks(cli):

    # Lista ST-LINKs
    result = subprocess.run(
        [cli, "-l"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    out = result.stdout

    sns = re.findall(
        r"ST-?LINK\s*(?:SN|Serial)\s*:\s*([0-9A-Fa-f]+)",
        out
    )

    if not sns:
        print("Nenhum ST-LINK encontrado")
        sys.exit(1)

    
    return sns