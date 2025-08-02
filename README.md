# 💰 Sistema Bancário em Python

Este é um projeto simples de terminal que simula um sistema bancário, permitindo ao usuário realizar operações como **depósito**, **saque**, **ver extrato** e **sair do sistema**.

---

## 🚀 Funcionalidades

- [x] Depósito de valores (float ou int)
- [x] Saque com:
  - Limite diário de saques
  - Limite máximo por saque
  - Verificação de saldo
- [x] Impressão do extrato bancário
- [x] Validação de entradas
- [x] Mensagens amigáveis de erro e sucesso

---

## 🧪 Requisitos

- Python 3.7 ou superior

---

## 🔐 Ambiente Virtual (recomendado)

1. Crie o ambiente virtual:
   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:

   - **Windows**
     ```bash
     venv\Scripts\activate
     ```

   - **Linux/macOS**
     ```bash
     source venv/bin/activate
     ```

3. (Opcional) Instale dependências, caso existam:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario.git
   cd sistema-bancario
   ```

2. Ative o ambiente virtual (veja acima)

3. Execute o script:
   ```bash
   python sistema_bancario.py
   ```

---

## 📝 Exemplo de Uso

```text
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 250
Depósito de R$ 250.00 realizado com sucesso!

=> s
Informe o valor do saque: 100
Saque de R$ 100.00 realizado com sucesso!

=> e
========== EXTRATO ==========
Depósito: R$ 250.00
Saque: R$ 100.00

Saldo atual: R$ 150.00
==============================
```

---

## ⚠️ Limitações

- Máximo de **2 saques** por execução
- Valor máximo de saque: **R$ 500,00**
- Apenas operações por terminal

---

## 📌 Licença

Este projeto está licenciado sob a licença MIT.
