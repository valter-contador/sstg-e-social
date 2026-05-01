# 📚 SSTG E-Social — Avaliação de Riscos Psicossociais (COPSOQ III)

**Versão:** 6.0  
**Atualizado:** 30/04/2026  
**Status:** ✅ Em Produção

---

## 🎯 O que é SSTG E-Social?

Sistema **web-based** para coleta, análise e geração de **laudos de riscos psicossociais** utilizando o **protocolo COPSOQ III** (Copenhagen Psychosocial Questionnaire).

### Características Principais

✅ **Anonimato Garantido** — CPF criptografado com SHA-256  
✅ **Período Controlado** — Janela de resposta configurável por empresa  
✅ **Cadastro em Lote** — Suporte a importação via CSV  
✅ **Links Personalizados** — URL individual por empresa  
✅ **Laudo Automático** — PDF gerado com análise de risco (BS 8800)  
✅ **LGPD Compliant** — Proteção de dados pessoais  
✅ **Rede Local/Nuvem** — Funciona offline ou publicado online  

---

## 📖 Documentação

### Para Usuários RH/Administrativos

**👉 [TUTORIAL.md](TUTORIAL.md)** — Guia operacional passo a passo

- Como acessar o sistema
- Cadastro manual vs. CSV
- Gerar links para colaboradores
- Como os colaboradores respondem
- Consultar resultados e gerar laudos
- FAQ com 7 problemas comuns

**Tempo de leitura:** ~20 minutos

---

### Para Administradores de Sistema

**👉 [GUIA_INSTALACAO.md](GUIA_INSTALACAO.md)** — Instalação, setup e manutenção

- Pré-requisitos (hardware, software)
- Instalação passo a passo
- Configuração de variáveis
- Integração com Google Drive
- Publicação no Streamlit Cloud
- Backup e recuperação
- Troubleshooting

**Tempo de leitura:** ~30 minutos

---

### Para Desenvolvedores / Técnicos

**👉 [GUIA_TECNICO.md](GUIA_TECNICO.md)** — Arquitetura, fluxos e segurança

- Stack tecnológico
- Estrutura de dados (CSV)
- Fluxos de dados (4 diagramas)
- Variáveis de configuração
- Segurança (hash, período, validações)
- Troubleshooting técnico
- Próximas melhorias

**Tempo de leitura:** ~25 minutos

---

## ⚡ Início Rápido

### 1️⃣ Instalação (5 min)

```bash
# Clone ou copie os arquivos
cd C:\Users\valte\Claude

# Instale dependências
py -m pip install streamlit pandas reportlab

# Inicie o app
py -m streamlit run app.py
```

**URL de acesso:**
```
http://192.168.77.2:8501
```

### 2️⃣ Primeiro Cadastro (3 min)

1. Acesse o app
2. Selecione: **🔐 Admin SSTG (Gestão)**
3. Digite senha: `sstg2025`
4. Aba **📝 Cadastro** → Digite CNPJ, empresa, colaboradores
5. Clique **✅ SALVAR E LIBERAR ACESSOS**

### 3️⃣ Distribuir Links (2 min)

1. Scroll na **Aba 1** até **🔗 Links para Compartilhar**
2. Copie link da empresa
3. Envie no WhatsApp, email, etc.

### 4️⃣ Colaborador Responde (10 min)

1. Colaborador clica no link
2. Digita seu CPF (11 dígitos)
3. Responde 35 questões (7 blocos)
4. Envia respostas

### 5️⃣ Gerar Laudo (2 min)

1. **Aba 3** → Resultados
2. Selecione empresa
3. Clique **📄 GERAR E BAIXAR LAUDO PDF**

---

## 🏗️ Arquitetura Resumida

```
┌─────────────────────────────────────┐
│     Navegador Web (Qualquer SO)     │
│         Streamlit Frontend          │
└────────────────┬────────────────────┘
                 │ HTTP (8501)
┌────────────────▼────────────────────┐
│    Python Streamlit Application     │
│  • app.py (módulos Admin + Colab)   │
│  • gerar_laudo.py (PDF)             │
│  • config.toml (tema)               │
└────────────────┬────────────────────┘
                 │ I/O
┌────────────────▼────────────────────┐
│    Armazenamento CSV (Elegível)     │
│  • Local: C:\Users\valte\Claude\    │
│  • Google Drive: G:\Meu Drive\...   │
│  • Backup: D:\Backups\...           │
└─────────────────────────────────────┘
```

---

## 📊 Fluxo de Dados Principal

```
┌──────────────┐
│ Admin registra│
│ colaboradores│
└──────┬───────┘
       │
       ├─→ Manual (tabela)
       └─→ CSV (importação)
       │
       ▼
┌──────────────────────────────┐
│ db_acessos_autorizados.csv   │
│ (CPF, Empresa, Período, etc) │
└──────────────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│ Admin gera link:             │
│ ?cnpj=XXXXX                  │
└──────────────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│ Colaborador acessa link      │
│ → Digita CPF                 │
│ → Responde 35 questões       │
└──────────────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│ respostas_CNPJ_XXXXX.csv     │
│ (CPF_Hash, Respostas, etc)   │
└──────────────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│ Admin gera laudo PDF:        │
│ • Análise por dimensão       │
│ • Classificação de risco     │
│ • Recomendações             │
└──────────────────────────────┘
```

---

## 🔒 Segurança & LGPD

| Aspecto | Implementação |
|--------|---------------|
| **Anonimato** | CPF → SHA-256 hash (impossível recuperar) |
| **Controle de Acesso** | Período configurável (data início/fim) |
| **Proteção de Dados** | Sem armazenamento de CPF nas respostas |
| **Inativação** | Colaboradores inativados perdem acesso |
| **Backup** | Cópia de segurança dos dados |
| **Sigilo** | Resultados acessados apenas por admin |

---

## 📋 Dimensões COPSOQ III (7 Blocos, 35 Questões)

| # | Dimensão | Questões | Descr... Invertida? |
|---|----------|----------|-----------|
| 1️⃣ | **📦 Cargo** | 5 | Clareza da função | Não |
| 2️⃣ | **🎮 Controle** | 6 | Autonomia de decisão | Não |
| 3️⃣ | **⚖️ Demandas** | 8 | Pressão e carga | ✅ Sim |
| 4️⃣ | **⚠️ Relacionamentos** | 4 | Conflitos e assédio | ✅ Sim |
| 5️⃣ | **🤝 Apoio Colegas** | 4 | Solidariedade | Não |
| 6️⃣ | **👔 Apoio Chefia** | 5 | Suporte gerencial | Não |
| 7️⃣ | **📢 Comunicação** | 3 | Transparência | Não |

**Total:** 35 questões, escala Likert 5 pontos (Nunca a Sempre)

---

## 🎨 Identidade Visual SSTG

```
Cores Primárias:
🔵 Azul Navy:    #282C5B
🟢 Verde:        #5A9F62
🟠 Laranja:      #DC3B24
⚪ Cinza Claro:  #EFEFEF

Tipografia: Sans Serif (Arial, Segoe UI)
Logo: salvar como logo_sstg.png (opcional)
```

---

## 🚀 Deployment

### Opção 1: Rede Local (Recomendado para Testes)

```bash
# Na máquina servidor:
py -m streamlit run app.py

# Acesse de outro computador:
http://192.168.77.2:8501
```

✅ **Vantagens:** Rápido, sem dependência internet  
❌ **Limitação:** Apenas na rede WiFi/LAN

---

### Opção 2: Streamlit Cloud (Recomendado para Produção)

1. Push para GitHub
2. Conectar Streamlit Cloud
3. Deploy automático
4. URL: `https://seu-app.streamlit.app`

✅ **Vantagens:** Acesso global, autoscaling  
❌ **Limitação:** Plano gratuito tem limites

---

## 📱 Compatibilidade

| Browser | Desktop | Mobile |
|---------|---------|--------|
| Chrome | ✅ | ✅ |
| Firefox | ✅ | ✅ |
| Safari | ✅ | ✅ |
| Edge | ✅ | ✅ |

**Recomendação:** Usar em desktop para cadastro, mobile para responder

---

## 💾 Requisitos de Armazenamento

| Tipo | Tamanho | Descrição |
|------|---------|-----------|
| **Aplicação** | ~50 MB | Python + deps |
| **Dados (100 colabs)** | ~2 MB | CSV com respostas |
| **Dados (1000 colabs)** | ~20 MB | CSV com respostas |
| **Backup** | 2x dados | Cópia de segurança |

**Total recomendado:** 500 MB livres

---

## 🛠️ Tecnologias Utilizadas

```
Frontend:      Streamlit 1.28+
Backend:       Python 3.9+
Data:          Pandas, CSV
PDF:           ReportLab 4.0+
Segurança:     SHA-256, validações
Deployment:    Streamlit Cloud ou VPS
```

---

## 📈 Roadmap Futuro

- [ ] Banco de dados relacional (PostgreSQL)
- [ ] Autenticação com 2FA (Google Authenticator)
- [ ] API REST para integrações
- [ ] Dashboard com gráficos avançados (Plotly)
- [ ] Exportação em múltiplos formatos (Excel, Word)
- [ ] Notificações automáticas (email)
- [ ] Versionamento de laudos (histórico)

---

## ❓ FAQ Rápido

**P: Preciso de bancário de dados?**  
R: Não, CSV é suficiente. Pode usar Google Drive.

**P: Os dados estão seguros?**  
R: Sim, CPF é criptografado (SHA-256), período bloqueado.

**P: Posso responder 2x o questionário?**  
R: Não, o sistema detecta e bloqueia duplicatas.

**P: Como faço backup?**  
R: Copie a pasta `C:\Users\valte\Claude` para outro local.

**P: Qual é o custo?**  
R: Gratuito. Streamlit Cloud tem versão free.

---

## 📞 Suporte

**Documentação:**
- [TUTORIAL.md](TUTORIAL.md) — Para usuários
- [GUIA_INSTALACAO.md](GUIA_INSTALACAO.md) — Para admins
- [GUIA_TECNICO.md](GUIA_TECNICO.md) — Para devs

**Contato:**
- Email: suporte@sstg.com.br
- WhatsApp: (XX) XXXXX-XXXX

---

## 📄 Licença

Desenvolvido para **SSTG E-Social Gestão Ocupacional**  
Versão 6.0 — Abril/2026

---

## 🙏 Agradecimentos

Desenvolvido com ❤️ para melhorar a saúde e segurança dos trabalhadores.

Protocolo validado: **COPSOQ III**  
Matriz de risco: **BS 8800**  
Conformidade: **NR-01 (Norma Regulamentadora)**

---

**Última atualização:** 30/04/2026  
**Próxima revisão:** 30/07/2026
