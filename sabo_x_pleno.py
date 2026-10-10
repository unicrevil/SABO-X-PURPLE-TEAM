import random
import time
import json
from datetime import datetime

LAB_IP = "127.0.0.1"

BANNER = r"""
  ____   _    ____   ___        __  __
 / ___| / \  | __ ) / _ \      |  \/  |
 \___ \ / _ \ |  _ \| | | |_____| |\/| |
  ___) / ___ \| |_) | |_| |_____| |  | |
 |____/_/   \_\____/ \___/      |_|  |_|
 SOC PLENO PURPLE TEAM - Andre Unic
 SABO-X - Deception Grid + SOC 120%
"""
print(BANNER)
print(f"[LAB] Ambiente: {LAB_IP}")

def red_team_emulate():
    ttp = random.choice(["T1021.004", "T1190", "T1110"])
    print(f"[RED] Simulacao defensiva: {ttp} no lab local")
    return ttp

def blue_team_detect(ttp):
    print(f"[BLUE] Detectado: {ttp} | Lab {LAB_IP} | Gerando Sigma + Log")
    rule = f"detection:\n  lab_ip: {LAB_IP}\n  ttp: {ttp}\n  action: block\n  time: {datetime.now()}\n"
    with open("sigma_rule.yml", "a") as f:
        f.write(rule + "\n")
    log = {"lab_ip": LAB_IP, "ttp": ttp, "timestamp": str(datetime.now()), "status": "blocked_lab"}
    with open("iocs.json", "a") as f:
        f.write(json.dumps(log) + "\n")
    return True

def purple_validate():
    print("[PURPLE] Validando Deception Grid: BLOQUEIO OK!")

for i in range(3):
    ttp = red_team_emulate()
    time.sleep(1)
    blue_team_detect(ttp)
    purple_validate()
    print("-"*48)

print("\n[FINAL] Execucao 120% concluida!")
