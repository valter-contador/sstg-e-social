# 🔧 Guia Técnico SSTG E-Social

**Versão:** 6.0  
**Data:** 30/04/2026  
**Público:** Administradores de Sistema | Desenvolvedores

---

## 📋 Índice

1. [Arquitetura do Sistema](#arquitetura)
2. [Estrutura de Dados](#estrutura-de-dados)
3. [Fluxo de Dados](#fluxo-de-dados)
4. [Variáveis de Configuração](#variáveis-de-configuração)
5. [Banco de Dados](#banco-de-dados)
6. [Segurança](#segurança)
7. [Troubleshooting Técnico](#troubleshooting-técnico)

---

## 🏗️ Arquitetura

### Stack Tecnológico

```
┌──────────────────────────────────────────────────────┐
│                   Frontend (Navegador)               │
│         HTML5 + JavaScript (Streamlit)               │
└────────────────────┬─────────────────────────────────┘
                     │ HTTP
┌────────────────────▼─────────────────────────────────┐
│          Aplicação (Streamlit - Python)              │
│  • app.py - Lógica principal                         │
│  • gerar_laudo.py - Geração de PDFs                  │
│  • config.toml - Configuração visual                 │
└────────────────────┬─────────────────────────────────┘
                     │ I/O
┌────────────────────▼─────────────────────────────────┐
│            Armazenamento (CSV)                       │
│  • db_acessos_autorizados.csv                        │
│  • respostas_CNPJ_XXXXX.csv                          │
│  • Opcional: Google Drive Desktop                    │
└──────────────────────────────────────────────────────┘
```

### Componentes Principais

#### 1. **app.py** (Núcleo)
- Interfaz Streamlit com 2 módulos
- Gerenciamento de sessão (session_state)
- Validações e fluxos

#### 2. **gerar_laudo.py** (Geração de PDF)
- Cálculo de dimensões COPSOQ III
- Classificação de risco (BS 8800)
- Geração PDF com reportlab

#### 3. **config.toml** (Configuração Visual)
- Tema SSTG (cores, fontes)
- Configurações da sessão

---

## 📊 Estrutura de Dados

### Arquivo: `db_acessos_autorizados.csv`

**Separador:** `;` (ponto-e-vírgula)  
**Encoding:** UTF-8 with BOM

| Campo | Tipo | Exemplo | Descrição |
|-------|------|---------|-----------|
| CPF | string | 06320453451 | 11 dígitos, sem formatação |
| Empresa | string | SSTG E-Social Ltda | Nome da empresa |
| CNPJ | string | 49405001000105 | 14 dígitos, sem formatação |
| Função | string | Assist. Adm | Cargo/posição |
| Departamento | string | Atendimento | Setor |
| Data_Acesso_Liberado | date | 30/04/2026 | Formato DD/MM/YYYY |
| Data_Inicio_Periodo | date | 30/04/2026 | Início da janela de resposta |
| Data_Fim_Periodo | date | 30/05/2026 | Fim da janela de resposta |
| Status | enum | Ativo / Inativo | Controle de acesso |
| Data_Movimentacao | date | 30/04/2026 | Quando foi ativado/inativado |
| Motivo_Movimentacao | string | Desligado | Motivo (opcional) |

**Exemplo:**
```csv
CPF;Empresa;CNPJ;Função;Departamento;Data_Acesso_Liberado;Data_Inicio_Periodo;Data_Fim_Periodo;Status;Data_Movimentacao;Motivo_Movimentacao
06320453451;SSTG E-Social Ltda;49405001000105;Assist. Adm;Atendimento;30/04/2026;30/04/2026;30/05/2026;Ativo;;
```

### Arquivo: `respostas_CNPJ_XXXXX.csv`

**Nome:** respostas_CNPJ_[CNPJ].csv  
**Exemplo:** respostas_CNPJ_49405001000105.csv

| Campo | Tipo | Exemplo | Descrição |
|-------|------|---------|-----------|
| CPF_Hash | string | 4f3a2b... | SHA-256(CPF) para anonimato |
| Funcao | string | Assist. Adm | Função do colaborador |
| Departamento | string | Atendimento | Departamento |
| Resp_Q1 | int | 4 | Resposta questão 1 (1-5) |
| Resp_Q2 | int | 3 | Resposta questão 2 (1-5) |
| ... | int | ... | Respostas Q3 a Q35 |
| Data_Resposta | datetime | 30/04/2026 14:30:45 | Timestamp |

**Escala de Respostas:**
- 1 = Nunca
- 2 = Raramente
- 3 = Às vezes
- 4 = Frequentemente
- 5 = Sempre

---

## 🔄 Fluxo de Dados

### Fluxo 1: Cadastro de Colaborador (Manual)

```
┌─────────────┐
│ Admin preenche│
│ formulário   │
└────────┬────┘
         │
         ▼
┌─────────────────────────┐
│ validar_cpf_formato()   │
│ • 11 dígitos?           │
│ • Sem duplicata?        │
└────────┬────────────────┘
         │
    ❌ Inválido → Exibir erro
         │ ✅ Válido
         ▼
┌─────────────────────────┐
│ salvar_cadastro_completo()│
│ Adiciona ao CSV          │
└────────┬────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ db_acessos_autorizados.csv   │
│ + 1 nova linha               │
└──────────────────────────────┘
```

### Fluxo 2: Importação via CSV

```
┌──────────────────┐
│ Admin faz upload │
│ arquivo CSV      │
└────────┬─────────┘
         │
         ▼
┌──────────────────────────┐
│ Validar:                 │
│ • Colunas obrigatórias   │
│ • Formato CPF            │
│ • Sem duplicatas         │
└────────┬─────────────────┘
         │
    ❌ Erro → Exibir erros
         │ ✅ OK
         ▼
┌──────────────────────────┐
│ Preview na tela          │
│ (para confirmação)       │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Admin clica SALVAR       │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ salvar_cadastro_completo()   │
│ • Adiciona múltiplas linhas  │
│ • Classifica: novos,         │
│   duplicados, inválidos      │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ db_acessos_autorizados.csv   │
│ + N novas linhas             │
└──────────────────────────────┘
```

### Fluxo 3: Responder Questionário

```
┌──────────────────────────┐
│ Colaborador acessa link  │
│ ?cnpj=XXXXX              │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ Detecta CNPJ via         │
│ st.query_params          │
└────────┬─────────────────┘
         │
         ▼
┌────────────────────────────────┐
│ Exibe nome da empresa          │
│ (busca em db_acessos)          │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│ Colaborador digita CPF         │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│ Validações:                    │
│ • CPF existe?                  │
│ • Já respondeu?                │
│ • Status Ativo?                │
│ • Dentro do período?           │
└────────┬───────────────────────┘
         │
    ❌ Falha → Exibir erro
         │ ✅ Sucesso
         ▼
┌────────────────────────────────┐
│ Exibe 7 blocos COPSOQ III      │
│ • 35 questões                  │
│ • Escala 1-5                   │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│ Colaborador responde tudo      │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│ hash_cpf() = SHA-256(CPF)      │
│ Salva anônimamente + metadata  │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────────┐
│ respostas_CNPJ_XXXXX.csv           │
│ + 1 nova linha (CPF_Hash, Respostas)│
└────────────────────────────────────┘
```

### Fluxo 4: Gerar Laudo PDF

```
┌──────────────────────────┐
│ Admin seleciona empresa  │
│ Clica: GERAR LAUDO      │
└────────┬─────────────────┘
         │
         ▼
┌────────────────────────────────┐
│ Lê respostas_CNPJ_XXXXX.csv    │
│ Calcula média por dimensão     │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│ Inverte dimensões:             │
│ • Demandas: 4.0 - média        │
│ • Relacionamentos: 4.0 - média  │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│ Classifica risco (BS 8800):    │
│ • Baixo:   média >= 3.5        │
│ • Médio:   2.5 - 3.49          │
│ • Alto:    < 2.5               │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│ Gera PDF com reportlab:        │
│ • Título e dados               │
│ • Tabelas de resultados        │
│ • Gráficos por dimensão        │
│ • Recomendações                │
└────────┬───────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│ laudo_CNPJ_XXXXX.pdf           │
│ Pronto para download           │
└────────────────────────────────┘
```

---

## ⚙️ Variáveis de Configuração

### app.py

```python
# ─── DIRETÓRIO DE DADOS ───────────────────────────────────
DATA_DIR = ""  # Local vazio = pasta do projeto
# Para Google Drive, use: r"G:\Meu Drive\SSTG E-Social\dados"

# ─── URL BASE ─────────────────────────────────────────────
APP_URL = "http://192.168.77.2:8501"  # Atualizar para URL de produção

# ─── SEGURANÇA ────────────────────────────────────────────
ARQUIVO_ACESSOS = caminho("db_acessos_autorizados.csv")
SENHA_ADMIN = "sstg2025"  # ⚠️ Alterar em produção!
```

### .streamlit/config.toml

```toml
[client]
showErrorDetails = false

[server]
port = 8501
headless = true

[theme]
primaryColor = "#282C5B"    # Azul navy SSTG
backgroundColor = "#EFEFEF" # Cinza claro
secondaryBackgroundColor = "#FFFFFF"
textColor = "#000000"
font = "sans serif"
```

---

## 💾 Banco de Dados

### Localização

**Padrão (Local):**
```
C:\Users\valte\Claude\
├── db_acessos_autorizados.csv
└── respostas_CNPJ_*.csv
```

**Google Drive (Configurado):**
```
G:\Meu Drive\SSTG E-Social\dados\
├── db_acessos_autorizados.csv
└── respostas_CNPJ_*.csv
```

### Operações de Leitura/Escrita

#### Ler dados
```python
df = carregar_dados(ARQUIVO_ACESSOS)
# Retorna DataFrame ou DataFrame vazio se arquivo não existe
```

#### Salvar dados (APPEND)
```python
df_novo.to_csv(
    ARQUIVO_ACESSOS,
    mode='a',              # APPEND (não sobrescreve)
    index=False,
    sep=';',
    header=not os.path.exists(ARQUIVO_ACESSOS),
    encoding='utf-8-sig'
)
```

#### Salvar dados (TRUNCATE)
```python
df_atualizado.to_csv(
    ARQUIVO_ACESSOS,
    index=False,
    sep=';',
    encoding='utf-8-sig'
)
```

---

## 🔒 Segurança

### Proteção de CPF

**Método:** SHA-256 hash

```python
def hash_cpf(cpf: str) -> str:
    return hashlib.sha256(cpf.encode()).hexdigest()

# Exemplo:
# CPF: 06320453451
# Hash: 4f3a2b1c9e8d7f6a5b4c3d2e1f0a9b8c7d6e5f4a
```

**Por que?**
- ✅ Anonimato nas respostas
- ✅ Impossível reverse-engineer o CPF
- ✅ Permite verificar duplicatas sem expor CPF

### Validação de Período

```python
def periodo_valido(dados: dict) -> tuple:
    hoje = date.today()
    data_inicio = datetime.strptime(dados['Data_Inicio_Periodo'], "%d/%m/%Y").date()
    data_fim = datetime.strptime(dados['Data_Fim_Periodo'], "%d/%m/%Y").date()
    
    if data_inicio <= hoje <= data_fim:
        return True, ""
    else:
        return False, f"Período encerrado em {dados['Data_Fim_Periodo']}"
```

**Fluxo:**
1. CPF digitado
2. Valida período
3. Se fora → **bloqueia**
4. Se dentro → **libera acesso**

### Variáveis Sensíveis

⚠️ **NUNCA** comitar em Git:
- `SENHA_ADMIN` (atualmente hardcoded)
- Arquivos `.csv` com dados reais
- Google Drive credentials

**Recomendação futura:**
```python
import os
SENHA_ADMIN = os.getenv("SSTG_SENHA_ADMIN", "sstg2025")
```

---

## 🐛 Troubleshooting Técnico

### Problema: ModuleNotFoundError: No module named 'reportlab'

**Causa:** Dependência não instalada.

**Solução:**
```bash
py -m pip install reportlab --quiet
```

---

### Problema: UnicodeDecodeError ao ler CSV

**Causa:** Encoding incorreto.

**Solução:** Verificar se o arquivo foi salvo com UTF-8 with BOM:
```python
df = pd.read_csv(arquivo, sep=';', encoding='utf-8-sig')
```

---

### Problema: ValueError ao converter data

**Causa:** Formato de data incorreto no CSV.

**Verificar:**
```python
# ✅ Correto:
"30/04/2026"

# ❌ Errado:
"2026-04-30"
"30/4/26"
"30 de abril de 2026"
```

---

### Problema: Streamlit não encontra arquivo

**Causa:** Caminho relativo vs. absoluto.

**Verificar:**
```python
# DEBUG
import os
print(os.getcwd())  # Pasta atual
print(os.path.exists("db_acessos_autorizados.csv"))
```

---

### Problema: Google Drive não sincroniza

**Causa:** Google Drive Desktop não está rodando.

**Solução:**
1. Instale Google Drive Desktop
2. Configure pasta de sincronização
3. Aguarde sincronização completar
4. Verifique permissões

---

## 📦 Dependências

```
streamlit >= 1.28.0
pandas >= 2.0.0
reportlab >= 4.0.0
```

**Instalar tudo:**
```bash
py -m pip install streamlit pandas reportlab
```

---

## 📈 Próximas Melhorias

- [ ] Banco de dados relacional (PostgreSQL/SQLite)
- [ ] Autenticação com 2FA
- [ ] API REST para integração
- [ ] Dashboard avançado com mais visualizações
- [ ] Exportação em múltiplos formatos
- [ ] Backup automático

---

**Documento técnico — SSTG E-Social v6.0**
