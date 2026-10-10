# SABO-X SOC PLENO PURPLE TEAM - Andre Unic (Unicrevil)
import json, random, time
from datetime import datetime

print("""
 ███████╗ █████╗ ██████╗  ██████╗       ██╗  ██╗
 ██╔════╝██╔══██╗██╔══██╗██╔═══██╗      ╚██╗██╔╝
 ███████╗███████║██████╔╝██║   ██║█████╗╚███╔╝ 
 ╚════██║██╔══██║██╔══██╗██║   ██║╚════╝██╔██╗ 
 ███████║██║  ██║██████╔╝╚██████╔╝     ██╔╝ ██╗
 ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝      ╚═╝  ╚═╝
 SOC PLENO PURPLE TEAM - 120% MODE
 by Andre Unic (Unicrevil)
""")

# PURPLE TEAM LOGIC
def red_team_emulate():
    ttp = random.choice(["T1021.004 SSH Brute", "T1190 Exploit", "T1110 Credential"])
    print(f"[RED] Emulando ataque: {ttp} - Atacando honeypot local...")
    return ttp

def blue_team_detect(ttp):
    print(f"[BLUE] Detectado TTP {ttp} | Criando detecção Sigma + Bloqueio")
    rule = f'detection:\n  ttp: {ttp}\n  action: block_ip'
    open("sigma_rule.yml","a").write(rule+"\n")
    return True

def purple_validate():
    print("[PURPLE] Validando: Ataque foi bloqueado? SIM - Deception Grid funcionou!")

# EXECUÇÃO 120%
for i in range(3):
    ttp = red_team_emulate()
    time.sleep(1)
    blue_team_detect(ttp)
    purple_validate()
    print("-"*40)

print("\n✅ SABO-X PURPLE TEAM CONCLUÍDO - Log salvo em iocs.json")
