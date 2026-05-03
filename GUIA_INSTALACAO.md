# 🚀 Guia de Instalação e Setup

**Versão:** 6.0  
**Data:** 30/04/2026  
**Público:** Administradores de Sistema | Instaladores Técnicos

---

## 📋 Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Instalação Inicial](#instalação-inicial)
3. [Configuração do Ambiente](#configuração-do-ambiente)
4. [Integração com Google Drive](#integração-com-google-drive)
5. [Publicação Online](#publicação-online)
6. [Backup e Recuperação](#backup-e-recuperação)
7. [Manutenção Periódica](#manutenção-periódica)

---

## ✅ Pré-requisitos

### Hardware Mínimo

- **Processador:** Intel i3 ou equivalente
- **RAM:** 4 GB
- **Disco:** 500 MB livres
- **Conexão:** Internet (para dependências e Streamlit Cloud)

### Software Necessário

- **Sistema Operacional:** Windows 10/11, macOS, ou Linux
- **Python:** 3.9 ou superior (recomendado 3.11+)
- **Git:** (opcional, para versionamento)
- **Navegador:** Chrome, Firefox, Edge, Safari (compatível com HTML5)

### Verificar Python Instalado

```bash
py --version
# ou
python --version
```

Se não tiver Python, instale de: https://www.python.org/downloads/

---

## 📥 Instalação Inicial

### Passo 1: Preparar Pasta do Projeto

```bash
# Navegue até a pasta desejada (exemplo)
cd C:\Users\valte

# Crie pasta do projeto
mkdir Claude
cd Claude
```

### Passo 2: Clonar Arquivos do Projeto

**Se estiver em um repositório Git:**

```bash
git clone <url-do-repositorio>
cd sstg-esocial
```

**Se estiver instalando manualmente:**

Copie os seguintes arquivos para `C:\Users\valte\Claude\`:

```
app.py
gerar_laudo.py
TUTORIAL.md
GUIA_TECNICO.md
GUIA_INSTALACAO.md
```

### Passo 3: Criar Pasta para Configuração

```bash
# Na pasta C:\Users\valte\Claude

mkdir .streamlit
```

### Passo 4: Criar Arquivo de Configuração

Crie o arquivo `.streamlit\config.toml`:

```bash
# PowerShell ou cmd
notepad .streamlit\config.toml
```

**Cole o conteúdo:**

```toml
[client]
showErrorDetails = false

[server]
port = 8501
headless = true

[theme]
primaryColor = "#282C5B"
backgroundColor = "#EFEFEF"
secondaryBackgroundColor = "#FFFFFF"
textColor = "#000000"
font = "sans serif"
```

**Salve:** Ctrl+S → Feche

### Passo 5: Instalar Dependências Python

```bash
# Na pasta do projeto
cd C:\Users\valte\Claude

# Instale as dependências
py -m pip install --upgrade pip
py -m pip install streamlit pandas reportlab
```

**Verificar instalação:**

```bash
py -c "import streamlit; print(f'Streamlit {streamlit.__version__} ✅')"
py -c "import pandas; print(f'Pandas {pandas.__version__} ✅')"
py -c "import reportlab; print(f'ReportLab ✅')"
```

### Passo 6: Iniciar o App (Primeira Execução)

```bash
# Na pasta C:\Users\valte\Claude
py -m streamlit run app.py
```

**Resultado esperado:**

```
  Welcome to Streamlit!

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.77.2:8501
```

✅ **App iniciado com sucesso!**

---

## ⚙️ Configuração do Ambiente

### Variável 1: DATA_DIR (Armazenamento)

**Arquivo:** `C:\Users\valte\Claude\app.py`  
**Linha:** ~18

#### Opção A: Armazenamento Local (Padrão)

```python
DATA_DIR = ""
```

**Efeito:** Dados salvos em `C:\Users\valte\Claude\`

#### Opção B: Armazenamento Google Drive

```python
DATA_DIR = r"G:\Meu Drive\SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1)\dados"
```

**Pré-requisito:** Google Drive Desktop instalado e pasta sincronizada

**Como fazer:**
1. Instale Google Drive Desktop: https://support.google.com/drive/answer/7329379
2. Configure sincronização para uma pasta local
3. Crie pasta `SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1)\dados`
4. Copie o caminho: `G:\Meu Drive\SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1)\dados`
5. Altere a variável no código

**Exemplo:**
```python
# Antes:
DATA_DIR = ""

# Depois:
DATA_DIR = r"G:\Meu Drive\SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1)\dados"
```

---

### Variável 2: APP_URL (URL de Acesso)

**Arquivo:** `C:\Users\valte\Claude\app.py`  
**Linha:** ~27

#### Opção A: Rede Local (Desenvolvimento)

```python
APP_URL = "http://192.168.77.2:8501"
```

**Uso:** Teste em rede WiFi/LAN

#### Opção B: Localhost (Apenas Local)

```python
APP_URL = "http://localhost:8501"
```

**Uso:** Apenas na máquina servidor

#### Opção C: Domínio de Produção

```python
APP_URL = "https://seu-app.streamlit.app"
```

**Uso:** Depois de publicar no Streamlit Cloud

---

### Variável 3: SENHA_ADMIN (Segurança)

**Arquivo:** `C:\Users\valte\Claude\app.py`  
**Linha:** ~31

```python
SENHA_ADMIN = "sstg2025"  # ⚠️ Alterar!
```

**Para alterar:**

```python
# Antes:
SENHA_ADMIN = "sstg2025"

# Depois (exemplo):
SENHA_ADMIN = "Minha@Senha123"
```

**Requisitos de senha forte:**
- ✅ Mínimo 8 caracteres
- ✅ Combinação de maiúsculas e minúsculas
- ✅ Números e símbolos especiais
- ✅ Não usar datas ou nomes comuns

---

## 🔗 Integração com Google Drive

### Passo 1: Instalar Google Drive Desktop

1. Acesse: https://support.google.com/drive/answer/7329379
2. Clique em "Download Google Drive for desktop"
3. Execute o instalador
4. Faça login com sua conta Google

### Passo 2: Sincronizar Pasta

1. Google Drive Desktop → Configurações
2. Ativa: "Sincronizar para este computador"
3. Selecione a pasta `SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1)` (crie se não existir)
4. Clique em "Iniciar sincronização"

### Passo 3: Confirmar Caminho

```bash
# Abra o Windows Explorer
# Vá para: Google Drive (disco G:\ ou outro)
# Copie o caminho completo da pasta

# Exemplo: G:\Meu Drive\SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1)\dados
```

### Passo 4: Atualizar Configuração

**Arquivo:** `C:\Users\valte\Claude\app.py`

```python
# Linha ~18
DATA_DIR = r"G:\Meu Drive\SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1)\dados"
```

### Passo 5: Reiniciar App

```bash
# Feche o Streamlit (Ctrl+C)
# Reinicie:
py -m streamlit run app.py
```

✅ **Dados agora sincronizados com Google Drive!**

---

## 🌐 Publicação Online

### Opção 1: Streamlit Cloud (Recomendado)

#### Pré-requisito
- Conta GitHub com repositório do projeto
- Conta Streamlit Cloud (gratuita)

#### Passo 1: Preparar Repositório GitHub

```bash
# Na pasta do projeto
git init
git add .
git commit -m "Initial commit - SSTG v6.0"
git branch -M main
git remote add origin https://github.com/seu-usuario/seu-repo.git
git push -u origin main
```

#### Passo 2: Criar Conta Streamlit Cloud

1. Acesse: https://streamlit.io/cloud
2. Clique em "Sign Up"
3. Faça login com GitHub
4. Autorize Streamlit

#### Passo 3: Deploy do App

1. Dashboard Streamlit Cloud → "New app"
2. Selecione seu repositório GitHub
3. Selecione branch: `main`
4. Selecione arquivo: `app.py`
5. Clique em "Deploy"

#### Passo 4: Atualizar APP_URL

```python
# Depois de publicado, Streamlit mostrará a URL
# Exemplo: https://seu-app.streamlit.app

APP_URL = "https://seu-app.streamlit.app"
```

**Fazer commit:**

```bash
git add app.py
git commit -m "Update APP_URL to production"
git push
```

✅ **App publicado em produção!**

---

### Opção 2: Servidor Próprio (Avançado)

**Requisitos:** VPS, domínio, conhecimento de DevOps

**Passos resumidos:**
1. Alugar VPS (DigitalOcean, AWS, etc.)
2. Instalar Python e dependências
3. Usar Gunicorn/Nginx para servir
4. Configurar SSL/TLS
5. Apontar domínio

> Fora do escopo deste guia. Contacte equipe de infraestrutura.

---

## 💾 Backup e Recuperação

### Fazer Backup Manual

```bash
# Copie a pasta inteira do projeto
# Origem: C:\Users\valte\Claude
# Destino: D:\Backups\SSTG-E-Social-2026-04-30

# Ou via PowerShell:
Copy-Item -Path "C:\Users\valte\Claude" -Destination "D:\Backups\SSTG-Backup-$(Get-Date -Format 'yyyy-MM-dd')" -Recurse
```

### Backup Automático (Windows Task Scheduler)

**1. Abra Task Scheduler:**
- Iniciar → "Task Scheduler"

**2. Crie nova tarefa:**
- Ação → Criar Tarefa
- Nome: "SSTG Backup Diário"
- Gatilho: Diariamente às 02:00 AM
- Ação: Executar script PowerShell

**3. Script PowerShell:**

Crie arquivo `C:\Scripts\backup-sstg.ps1`:

```powershell
$origem = "C:\Users\valte\Claude"
$destino = "D:\Backups\SSTG-$(Get-Date -Format 'yyyy-MM-dd')"

Copy-Item -Path $origem -Destination $destino -Recurse -Force
Write-Host "Backup concluído em $destino"
```

---

### Recuperar de Backup

```bash
# 1. Parar o app (Ctrl+C)

# 2. Copiar arquivos do backup
Copy-Item -Path "D:\Backups\SSTG-2026-04-30\*" -Destination "C:\Users\valte\Claude" -Recurse -Force

# 3. Reiniciar app
py -m streamlit run app.py
```

---

## 🔧 Manutenção Periódica

### Verificação Semanal

```bash
# 1. Verificar logs de erro
# Observar console do Streamlit

# 2. Validar integridade de dados
cd C:\Users\valte\Claude
py -c "
import pandas as pd
df = pd.read_csv('db_acessos_autorizados.csv', sep=';')
print(f'✅ {len(df)} colaboradores cadastrados')
print(f'Colunas: {list(df.columns)}')
"

# 3. Verificar espaço em disco
# Windows Explorer → Disco local → Propriedades
```

### Atualização de Dependências

```bash
# Verificar versões
py -m pip list

# Atualizar (opcional)
py -m pip install --upgrade streamlit pandas reportlab

# Testar
py -m streamlit run app.py
```

### Limpeza de Dados Antigos

```bash
# ⚠️ Cuidado! Backup primeiro!

# Remover respostas antigas (exemplo: mais de 6 meses)
# Abra respostas_CNPJ_XXXXX.csv em Excel
# Delete linhas com Data_Resposta < 01/11/2025
# Salve como CSV (UTF-8, separador ;)
```

---

## 🆘 Troubleshooting Instalação

### Problema: Python não encontrado

```bash
py --version
# Se não funcionar, tente:
python --version
```

**Solução:** Reinstale Python de https://www.python.org/downloads/  
Marque: "Add Python to PATH"

---

### Problema: Dependências não instalam

```bash
# Tente:
py -m pip install --upgrade pip setuptools wheel
py -m pip install streamlit pandas reportlab --no-cache-dir
```

---

### Problema: Porta 8501 já em uso

```bash
# Encontre processo usando porta 8501
Get-NetTCPConnection -LocalPort 8501

# Ou inicie em porta diferente
py -m streamlit run app.py --server.port 8502
```

---

### Problema: Google Drive não sincroniza

**Verificações:**
1. Google Drive Desktop está rodando?
2. Pasta existe em `G:\Meu Drive\`?
3. Tem permissão de escrita na pasta?
4. Conexão internet ativa?

**Solução:**
- Desinstale e reinstale Google Drive Desktop
- Configure sincronização novamente

---

## 📞 Suporte Pós-Instalação

**Para problemas técnicos:**
- Documentação: TUTORIAL.md, GUIA_TECNICO.md
- Logs de erro: Console do Streamlit
- Contato: equipe@sstg.com.br

---

**Guia de Instalação — SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1) v6.0**  
**Última atualização: 30/04/2026**
