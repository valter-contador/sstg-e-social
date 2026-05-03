# 📚 SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1) — Tutorial Operacional

**Versão:** 6.1  
**Data:** 30/04/2026 (Atualizado)  
**Público:** Equipe de Gestão RH | Pessoal Administrativo | Usuários Finais

**Última atualização:** Publicação no Streamlit Cloud, Gerador de Imagens, Documentação Integrada

---

## 📋 Índice

1. [Acesso ao Sistema](#acesso-ao-sistema)
2. [Módulo Admin — Gestão de Empresas](#módulo-admin)
3. [Cadastro Manual](#cadastro-manual)
4. [Cadastro via CSV (Em Lote)](#cadastro-via-csv)
5. [Gerar Links para Colaboradores](#gerar-links-para-colaboradores)
6. [Gerar Imagem de Compartilhamento (QR Code)](#gerar-imagem-de-compartilhamento)
7. [Módulo Colaborador — Responder Questionário](#módulo-colaborador)
8. [Consultar Resultados](#consultar-resultados)
9. [Documentação Integrada](#documentação-integrada)
10. [FAQ e Troubleshooting](#faq-e-troubleshooting)

---

## 🔓 Acesso ao Sistema

### URL de Acesso

#### Online (Recomendado - Streamlit Cloud)

```
https://sstg-e-social-687zwalcuokbggvtc7iy9m.streamlit.app
```

✅ **Acesso de qualquer lugar**  
✅ **Sem necessidade de servidor local**  
✅ **Sempre disponível online**

#### Local (Desenvolvimento)

```
http://192.168.77.2:8501
```

> **⚠️ Nota:** Apenas quando o app está rodando na máquina servidor local.

### Tela Inicial

Ao acessar a URL, você verá:

```
┌────────────────────────────────────────────┐
│  SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1) — Avaliação Psicossocial   │
│                                            │
│  [Dropdown] Módulo:                        │
│  ⭕ Questionário Psicossocial              │
│  🔐 Admin SSTG (Gestão)                    │
│                                            │
│  📋 Questionário Psicossocial [Selecionado]│
└────────────────────────────────────────────┘
```

**Selecione: `🔐 Admin SSTG (Gestão)`** para acessar o painel de administração.

---

## 🛠️ Módulo Admin

### Autenticação

**Tela:** Login Admin  
**Campo:** Senha  
**Valor padrão:** `sstg2025`

```
Digite sua senha de administrador:
[___________________]  [ACESSAR ▶]
```

> ⚠️ **Segurança:** Altere a senha padrão assim que possível.

---

### Interface Principal

Após login, você verá **4 abas**:

| Aba | Descrição |
|-----|-----------|
| **🆕 Cadastro / Inclusão** | Registrar novas empresas e colaboradores |
| **📋 Conferência e Correção** | Visualizar, editar e gerenciar acessos |
| **📊 Resultados** | Gráficos de resposta e gerar laudos PDF |
| **🔄 Movimentação de Pessoal** | Ativar/inativar colaboradores |

---

## 📝 Cadastro Manual

### Passo 1: Selecionar Método

Na **Aba 1 — Cadastro**, clique em: **✏️ Entrada Manual**

```
┌─────────────────────────────────────────────┐
│ ✏️ Entrada Manual  │  📊 Importar via CSV  │
└─────────────────────────────────────────────┘
      [Ativa]              [Inativa]
```

### Passo 2: Preencher Dados da Empresa

```
CNPJ (somente números)           Razão Social
[__________________]             [___________________]
Ex: 49405001000105              Ex: SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1) Ltda
```

### Passo 3: Definir Período de Aplicação

```
Data de início                   Data de encerramento
[__________]                     [__________]
Ex: 30/04/2026                  Ex: 30/05/2026

⚠️ Fora desse período, colaboradores NÃO conseguem acessar o questionário.
```

### Passo 4: Adicionar Colaboradores

**Clique em: `➕ Adicionar linha`** para cada colaborador

```
╔════════════════════════════════════════════════════════════╗
║  CPF (11 dígitos)  │  Função / Cargo  │  Departamento      ║
╠════════════════════════════════════════════════════════════╣
║ [06320453451]      │ [Assist. Adm]    │ [Atendimento]      ║
╟────────────────────────────────────────────────────────────╢
║ [70164124403]      │ [Assist. ST]     │ [Seg. Trabalho]    ║
╟────────────────────────────────────────────────────────────╢
║ [29545382449]      │ [Assist. Adm]    │ [Administração]    ║
╚════════════════════════════════════════════════════════════╝
```

**Colunas obrigatórias:**
- **CPF:** 11 dígitos, sem pontos ou traços
- **Função:** Cargo ou posição do colaborador
- **Departamento:** Setor ou área de trabalho

### Passo 5: Salvar

Clique em: **✅ SALVAR E LIBERAR ACESSOS**

```
Mensagens esperadas:

✅ 3 colaborador(es) cadastrado(s) com sucesso.
⚠️ CPF(s) já cadastrados: [lista]
❌ CPF(s) inválidos: [lista]
```

---

## 📊 Cadastro via CSV

### Quando Usar

✅ **Ideal para:**
- Cadastro de 10+ colaboradores
- Importação de dados de outro sistema
- Atualização em lote

### Passo 1: Selecionar Método

Na **Aba 1 — Cadastro**, clique em: **📊 Importar via CSV**

### Passo 2: Baixar Template

```
┌──────────────────────────────────────────┐
│  ⬇️ Baixar Template CSV                  │
│  [Clique para download]                  │
│  → template_colaboradores.csv            │
└──────────────────────────────────────────┘
```

O arquivo será baixado com as colunas:

```csv
CPF;Função;Departamento
06320453451;Assist. Adm;Atendimento
70164124403;Assist. ST;Seg. Trabalho
29545382449;Assist. Adm;Administração
```

### Passo 3: Preencher Arquivo

**Em Excel ou Bloco de Notas:**

1. Abra o arquivo `template_colaboradores.csv`
2. Mantenha as colunas: `CPF`, `Função`, `Departamento`
3. **Separe por `;` (ponto-e-vírgula)**
4. Adicione uma linha por colaborador

**Exemplo completo:**

```csv
CPF;Função;Departamento
06320453451;Desenvolvedor;TI
70164124403;Analista;RH
29545382449;Coordenador;Administrativo
18765432100;Gerente;Financeiro
```

> **⚠️ Importante:**
> - CPF deve ter exatamente 11 dígitos
> - Sem pontos (.) ou traços (-)
> - Sem linhas em branco

### Passo 4: Preencher Dados da Empresa

```
CNPJ (somente números)           Razão Social
[__________________]             [___________________]

Data de início                   Data de encerramento
[__________]                     [__________]
```

### Passo 5: Fazer Upload do Arquivo

```
┌──────────────────────────────────────────┐
│  Escolha um arquivo CSV                  │
│                                          │
│  [Clique para selecionar arquivo]        │
│  ou arraste o arquivo aqui               │
└──────────────────────────────────────────┘
```

Selecione seu arquivo preenchido.

### Passo 6: Revisar Dados

O sistema mostrará uma **prévia dos dados** que serão importados:

```
✅ Arquivo válido: 4 linhas detectadas

╔════════════════════════════════════════════════════════════╗
║  CPF           │  Função           │  Departamento        ║
╠════════════════════════════════════════════════════════════╣
║  06320453451   │  Desenvolvedor    │  TI                  ║
║  70164124403   │  Analista         │  RH                  ║
║  29545382449   │  Coordenador      │  Administrativo      ║
║  18765432100   │  Gerente          │  Financeiro          ║
╚════════════════════════════════════════════════════════════╝
```

### Passo 7: Confirmar Importação

Clique em: **💾 SALVAR COLABORADORES DO CSV**

```
Mensagens esperadas:

✅ 4 colaborador(es) cadastrado(s) com sucesso.
⚠️ CPF(s) já cadastrados: [lista]
❌ CPF(s) inválidos: [lista]
```

---

## 🔗 Gerar Links para Colaboradores

### Visualizar Links

Na **Aba 1 — Cadastro**, scroll down até: **🔗 Links para Compartilhar**

```
┌─────────────────────────────────────────────────────────────┐
│  🔗 Links para Compartilhar                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Empresa 1: SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1) Ltda                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ http://192.168.77.2:8501/?cnpj=49405001000105     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Empresa 2: XYZ Consultoria                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ http://192.168.77.2:8501/?cnpj=12345678000100     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  💡 Copie e envie o link correspondente ao RH da empresa.  │
└─────────────────────────────────────────────────────────────┘
```

### Distribuir Links

**Cada empresa recebe um link único:**

1. **Copie** o link correspondente
2. **Envie** para o RH ou responsável
3. **Divulgue** aos colaboradores (WhatsApp, email, etc.)

---

## 🖼️ Gerar Imagem de Compartilhamento

### Nova Funcionalidade: Imagem com QR Code

A partir da **Aba 3 (Resultados)**, você pode gerar uma imagem visual atrativa com QR Code para compartilhar o questionário com colaboradores.

### Passo 1: Acessar Gerador de Imagem

Na **Aba 3 — Resultados**:

1. Selecione a empresa
2. Expanda: **🖼️ Gerar Imagem para Compartilhamento**

### Passo 2: Gerar Imagem

```
┌────────────────────────────────────────────┐
│ 🖼️ Gerar Imagem para Compartilhamento     │
├────────────────────────────────────────────┤
│                                            │
│ Gere uma imagem com QR Code para           │
│ compartilhar nas redes sociais ou enviar   │
│ por email.                                 │
│                                            │
│ [🎨 Gerar Imagem com QR Code]             │
│                                            │
└────────────────────────────────────────────┘
```

Clique no botão **🎨 Gerar Imagem com QR Code**

### Passo 3: Visualizar e Baixar

A imagem gerada conterá:

```
┌──────────────────────────────────────┐
│ SSTG E-SOCIAL (branco sobre azul)    │
│ Avaliação de Riscos Psicossociais    │
│ Empresa: SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1) Ltda          │
│                                      │
│          [QR CODE]                   │
│         (escanear)                   │
│                                      │
│ Clique no QR Code ou acesse...       │
└──────────────────────────────────────┘
```

**Opções:**
- 📸 **Visualizar:** Vê a imagem na tela
- ⬇️ **Baixar (PNG):** Salva em seu computador

### Passo 4: Compartilhar

Use a imagem para:

| Canal | Como Usar |
|-------|-----------|
| 📧 **Email** | Anexar a imagem em campanha de sensibilização |
| 📱 **WhatsApp** | Enviar para grupos de colaboradores |
| 🌐 **Redes Sociais** | Postar no Facebook, LinkedIn ou Instagram |
| 🖨️ **Impressão** | Criar adesivos ou cartazes na empresa |

💡 **Dica:** O QR Code direciona automaticamente para o questionário da empresa específica!

---

## 👥 Módulo Colaborador

### Acesso via Link

O colaborador recebe um link como:

```
http://192.168.77.2:8501/?cnpj=49405001000105
```

### Tela de Boas-vindas

Ao abrir o link, o colaborador verá:

```
┌─────────────────────────────────────────────────────────┐
│     Avaliação de Riscos Psicossociais                   │
│  Protocolo COPSOQ III — Diagnóstico do Ambiente        │
│                                                         │
│  🔒 100% Confidencial    👤 Totalmente Anônimo         │
│  ⏱️ ~10 minutos          🏆 Protocolo Validado          │
│                                                         │
│  🏢 Você está respondendo o questionário de:            │
│     **SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1) Ltda**                              │
│                                                         │
│  Participe da nossa pesquisa de fatores psicossociais! │
│  É rápido, totalmente anônima e essencial...           │
│                                                         │
│  🔒 100% Confidencial: Suas respostas individuais são   │
│     protegidas e nunca expostas.                        │
│                                                         │
│  ✨ Foco na Verdade: Seja sincero, sua percepção é      │
│     o que importa para mudarmos o que for preciso.      │
│                                                         │
│  Digite seu CPF (11 números, sem pontos):              │
│  [_________________]      [ACESSAR ▶]                  │
└─────────────────────────────────────────────────────────┘
```

### Passo 1: Informar CPF

**Campo:** Digite seu CPF  
**Formato:** 11 dígitos, sem pontos ou traços

```
Exemplo:
[06320453451]
```

### Passo 2: Validações

O sistema verifica:

| Validação | Mensagem |
|-----------|----------|
| CPF não existe | ❌ Seu CPF não está autorizado |
| CPF já respondeu | ⚠️ Você já respondeu este questionário |
| CPF inativo | ❌ Seu acesso está inativo |
| **Fora do período** | ⚠️ O período de resposta encerrou em XX/XX/XXXX |
| ✅ Tudo OK | → Acessa o questionário |

### Passo 3: Responder Questionário

```
┌───────────────────────────────────────────────────┐
│  Bloco 1: 📦 Cargo                                │
├───────────────────────────────────────────────────┤
│  1. Questão 1                                     │
│     ⭕ Nunca   ⭕ Raramente   ⭕ Às vezes         │
│     ⭕ Frequentemente   ⭕ Sempre                 │
│                                                   │
│  2. Questão 2                                     │
│     ⭕ Nunca   ⭕ Raramente   ⭕ Às vezes         │
│     ⭕ Frequentemente   ⭕ Sempre                 │
│                                                   │
│  ... (5 questões no total)                        │
│                                                   │
│  [← Anterior]  [⊙⊙⊙ Progresso 20%]  [Próximo →] │
└───────────────────────────────────────────────────┘
```

**7 Blocos do COPSOQ III:**

1. **📦 Cargo** — Clareza e significado da função (5 questões)
2. **🎮 Controle** — Autonomia e poder de decisão (6 questões)
3. **⚖️ Demandas** — Pressão e carga de trabalho (8 questões)
4. **⚠️ Relacionamentos** — Conflitos e assédio (4 questões)
5. **🤝 Apoio dos Colegas** — Solidariedade (4 questões)
6. **👔 Apoio da Chefia** — Suporte do gestor (5 questões)
7. **📢 Comunicação e Mudanças** — Transparência (3 questões)

**Total: 35 questões**

### Passo 4: Enviar Respostas

```
┌───────────────────────────────────────────────────┐
│  [← Anterior]                    [✅ ENVIAR]     │
└───────────────────────────────────────────────────┘
```

Clique em **✅ ENVIAR** para salvar.

### Confirmação

```
┌───────────────────────────────────────────────────┐
│  ✅ Respostas salvas com sucesso!                 │
│                                                   │
│  Muito obrigado pela sua participação. Suas      │
│  respostas são fundamentais para melhorar o       │
│  ambiente de trabalho.                            │
│                                                   │
│  🔐 Seus dados permanem 100% confidenciais.       │
└───────────────────────────────────────────────────┘
```

---

## 📊 Consultar Resultados

### Aba 3: Resultados

Na **Aba 3 — Resultados**, você verá:

#### Gráfico de Resposta

```
Autorizados vs Respondidos
┌─────────────────────────────────────┐
│ 100│                                │
│    │  ┌─────┐    ┌─────┐           │
│  50│  │ 98  │    │ 45  │           │
│    │  └─────┘    └─────┘           │
│   0│  Autorizados Respondidos       │
└─────────────────────────────────────┘
  Legenda: Azul = Pessoas autorizadas
           Verde = Pessoas que responderam
```

**Interpretação:**
- **Autorizados:** Total de CPFs cadastrados
- **Respondidos:** Quantos já enviaram respostas

#### Gerar Laudo PDF

```
┌─────────────────────────────────────┐
│  Gerar Laudo Psicossocial (PDF)     │
│                                     │
│  Selecione a Empresa:               │
│  [SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1) Ltda    ▼]          │
│                                     │
│  [📄 GERAR E BAIXAR LAUDO PDF]      │
└─────────────────────────────────────┘
```

**O laudo contém:**
- ✅ Análise por dimensão COPSOQ III
- ✅ Classificação de risco (Baixo/Médio/Alto)
- ✅ Gráficos de resultados
- ✅ Recomendações de ação
- ✅ Conforme NR-01 (Protocolo Validado)

---

## 📋 Aba 2: Conferência e Correção

### Visualizar Cadastro

```
┌──────────────────────────────────────────────────────────┐
│  Cadastro Geral de Colaboradores Autorizados             │
│                                                          │
│  Total de CPFs: 3      ✅ Ativos: 3      🚫 Inativos: 0 │
│  Último cadastro: 30/04/2026                             │
│                                                          │
│  Filtrar por empresa:                                    │
│  [Todas ▼]                                               │
│                                                          │
│  ╔════════════════════════════════════════════════════╗  │
│  ║ CPF        │ Empresa  │ Função │ Depart. │ Status  ║  │
│  ╠════════════════════════════════════════════════════╣  │
│  ║ 063204... │ SSTG     │ Assist │ Atend.  │ Ativo   ║  │
│  ║ 701641... │ SSTG     │ Assist │ ST      │ Ativo   ║  │
│  ║ 295453... │ SSTG     │ Assist │ Admin   │ Ativo   ║  │
│  ╚════════════════════════════════════════════════════╝  │
│                                                          │
│  [⬇️ Baixar lista filtrada (.csv)]                      │
└──────────────────────────────────────────────────────────┘
```

### Gerenciar Período de Aplicação

```
┌─────────────────────────────────────────────────────────┐
│  📅 Gerenciar Período de Aplicação [Expandir ▼]        │
├─────────────────────────────────────────────────────────┤
│  Altere as datas para reabrir ou encerrar o período.   │
│                                                         │
│  Selecione empresa:                                     │
│  [SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1) — CNPJ: 49405001000105 ▼]             │
│                                                         │
│  Nova data de início                                    │
│  [__________]  (Atualmente: 30/04/2026)               │
│                                                         │
│  Nova data de encerramento                              │
│  [__________]  (Atualmente: 30/05/2026)               │
│                                                         │
│  [💾 SALVAR PERÍODO]                                    │
└─────────────────────────────────────────────────────────┘
```

---

## 🔄 Aba 4: Movimentação de Pessoal

### Inativar Colaborador

Para desligar um colaborador sem apagar dados:

```
┌──────────────────────────────────────────────────┐
│  Inativar colaborador desligado                  │
│                                                  │
│  Selecione o CPF:                                │
│  [06320453451 ▼] (Assist. Adm - Atendimento)   │
│                                                  │
│  Motivo (opcional):                              │
│  [________________________________]              │
│  Ex: Desligado em 30/04/2026                     │
│                                                  │
│  [🚫 INATIVAR COLABORADOR]                       │
└──────────────────────────────────────────────────┘
```

**Efeito:** O colaborador não conseguirá mais acessar o questionário.

### Reativar Colaborador

Para restaurar acesso:

```
┌──────────────────────────────────────────────────┐
│  Reativar colaborador                            │
│                                                  │
│  CPFs inativos:                                  │
│  ☐ 06320453451 (Assist. Adm)                    │
│  ☐ 70164124403 (Assist. ST)                     │
│                                                  │
│  [✅ REATIVAR SELECIONADOS]                      │
└──────────────────────────────────────────────────┘
```

---

## ❓ FAQ e Troubleshooting

### P1: O colaborador digita o CPF e diz "Seu CPF não está autorizado"

**Causa:** O CPF não foi cadastrado no sistema.

**Solução:**
1. Volte para **Aba 1 — Cadastro**
2. Verifique se o CPF foi realmente salvo
3. Cheque se não há erro de digitação (pontos/traços)
4. **Aba 2 — Conferência:** Procure pelo CPF

---

### P2: "O período de resposta encerrou em XX/XX/XXXX"

**Causa:** A data de hoje está fora do período configurado.

**Solução:**
1. **Aba 2 — Conferência**
2. Expanda: **📅 Gerenciar Período de Aplicação**
3. Selecione a empresa
4. Altere as datas para o futuro
5. Clique: **💾 SALVAR PERÍODO**

---

### P3: "Você já respondeu este questionário"

**Causa:** O colaborador já enviou respostas (não pode responder 2x).

**Solução:**
- Isso é **normal e desejado** (impede duplicação)
- Se precisa resetar um colaborador específico, entre em contato com a equipe técnica

---

### P4: O app não está acessível no IP 192.168.77.2

**Causa:** O app não está rodando na máquina servidor.

**Solução:**
1. Na máquina servidor, abra **PowerShell** ou **Prompt de Comando**
2. Navegue até: `C:\Users\valte\Claude`
3. Execute: `py -m streamlit run app.py`
4. Você verá: "Local URL: http://localhost:8501"
5. Acesse de outro computador: `http://192.168.77.2:8501`

---

### P5: Erro ao importar CSV: "CPF inválido"

**Causa:** O CPF não tem exatamente 11 dígitos.

**Verificar:**
```csv
Correto:     06320453451
❌ Errado:   6320453451   (10 dígitos)
❌ Errado:   063.204.534-51 (com pontos/traços)
```

**Solução:** Remova pontos e traços, mantenha apenas números.

---

### P6: Erro ao importar CSV: "O arquivo deve conter as colunas: CPF, Função, Departamento"

**Causa:** As colunas estão nomeadas incorretamente ou faltando.

**Verificar:**
```csv
✅ Correto:
CPF;Função;Departamento

❌ Errado:
CPF;FUNCAO;DEPART
CPF;Função
```

**Solução:** Baixe o template novamente e copie os dados nele.

---

### P7: Como alterar a senha de admin?

**Nota:** Atualmente a senha está fixa no código (`sstg2025`).

**Para alterar:**
1. Abra: `C:\Users\valte\Claude\app.py`
2. Procure por: `SENHA_ADMIN = "sstg2025"`
3. Altere para: `SENHA_ADMIN = "suanova_senha"`
4. Salve e reinicie o app

---

## 📚 Documentação Integrada

### Acessar Documentação no App

O sistema possui uma **Aba 5 (Documentação)** com 6 documentos disponíveis:

#### Dentro do App

1. **Login** como Admin SSTG
2. Vá para **Aba 5 — 📚 Documentação**
3. Escolha um documento:

| Documento | Descrição | Público |
|-----------|-----------|---------|
| **📄 README.md** | Visão geral, características, FAQ | Todos |
| **👥 TUTORIAL.md** | Este documento - passo a passo | RH / Admin |
| **🚀 SETUP** | Instalação, configuração, Google Drive | Técnico |
| **🔧 TÉCNICO** | Arquitetura, dados, fluxos, segurança | Desenvolvedor |
| **✅ CHECKLIST** | Validação pré-produção (60+ itens) | Admin |
| **🚀 PUBLICAÇÃO** | Processo de publicação, Streamlit Cloud | Técnico |

#### Opções de Visualização

Para cada documento:
- **📖 Ler:** Visualizar no navegador
- **⬇️ PDF:** Baixar arquivo completo

#### Menu Lateral

Você também pode acessar via menu lateral:

```
📚 Documentação
├── 📖 Guias e Tutoriais (Expander)
│   ├── 📄 README
│   ├── 👥 TUTORIAL
│   ├── 🚀 SETUP
│   ├── 🔧 TÉCNICO
│   ├── ✅ CHECKLIST
│   └── 🚀 PUBLICAÇÃO
```

### Documentação de Publicação

A **DOCUMENTACAO_PUBLICACAO.md** detalha:

✅ Como o sistema foi publicado no Streamlit Cloud  
✅ Recursos e sistemas utilizados  
✅ Processo passo a passo  
✅ Configurações realizadas  
✅ Troubleshooting e manutenção  
✅ Próximos passos recomendados  

**Use essa documentação para:**
- Entender a arquitetura do deployment
- Manter e atualizar o sistema
- Resolver problemas de publicação
- Planejar melhorias futuras

---

## 📞 Suporte

Para dúvidas técnicas ou problemas, contacte a equipe SSTG.

---

**Documento preparado para treinamento interno**  
**SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1) Gestão Ocupacional**  
**Sistema versão 6.0**
