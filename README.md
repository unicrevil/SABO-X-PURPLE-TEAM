# 🛡️ SABO-X SOC PLENO PURPLE TEAM 💜
### by Andre Unic (Unicrevil) | Caxias do Sul - RS | 120% Mode

> Jr detecta IP. Pleno explica o ataque. **120% cria o ataque, detecta e engana de volta.**

**Autonomous Threat Hunting & Deception Framework that runs on Android (Termux - Redmi Note 12)**

### 🔴 RED TEAM - APT Emulator
Emula TTPs reais:
- `T1110` Credential Access (Brute Force)
- `T1190` Exploit Public-Facing App
- `T1021.004` Lateral Movement via SSH

### 🔵 BLUE TEAM - Hunter Engine
- Detecção comportamental em tempo real
- Geração automática de `Sigma Rules / YARA / KQL`
- Bloqueio automático + Forense em `iocs.json`

### 🟣 PURPLE TEAM - Validation
Valida se a defesa funcionou - Gap Analysis automático

### 🎯 DECEPTION GRID
Canary Tokens: `senhas.xlsx`, `aws_keys.txt`, `backup.sql` | Honeypot low-interaction: 22, 8080, 3306, 4444

### 🚀 Como rodar
```bash
python sabo_x_pleno.py
EOF
E0F
