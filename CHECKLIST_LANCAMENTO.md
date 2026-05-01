# ✅ Checklist de Lançamento — SSTG E-Social v6.0

**Data:** 30/04/2026  
**Responsável:** _______________  
**Assinado em:** _______________

---

## 📋 Pré-requisitos Técnicos

- [ ] **Python 3.9+** instalado (`py --version`)
- [ ] **Dependências instaladas** (`py -m pip list | findstr streamlit`)
  - [ ] `streamlit >= 1.28.0`
  - [ ] `pandas >= 2.0.0`
  - [ ] `reportlab >= 4.0.0`
- [ ] **Pasta `.streamlit\`** criada
- [ ] **Arquivo `config.toml`** presente
- [ ] **Arquivos principais presentes:**
  - [ ] `app.py`
  - [ ] `gerar_laudo.py`
  - [ ] `.streamlit/config.toml`

---

## ⚙️ Configuração

- [ ] **Variável `DATA_DIR`** definida
  - [ ] Vazia (local) OU
  - [ ] Apontando para Google Drive válido
- [ ] **Variável `APP_URL`** configurada
  - [ ] `http://192.168.77.2:8501` (rede local) OU
  - [ ] `http://localhost:8501` (apenas local) OU
  - [ ] URL de produção (após publicar)
- [ ] **Variável `SENHA_ADMIN`** alterada
  - [ ] Senha forte (8+ chars, maiús/minús/números/símbolos)
  - [ ] Não é a senha padrão `sstg2025`
- [ ] **Arquivo `db_acessos_autorizados.csv`** criado (vazio é OK)

---

## 🚀 Inicialização e Testes

- [ ] **App inicia sem erros**
  ```bash
  py -m streamlit run app.py
  ```
- [ ] **Tela de saudação apareça**
  ```
  Local URL: http://localhost:8501
  Network URL: http://192.168.77.2:8501
  ```
- [ ] **Acesso via navegador**
  - [ ] http://localhost:8501 (local)
  - [ ] http://192.168.77.2:8501 (rede)
- [ ] **Módulo Admin acessível**
  - [ ] Senha correia aceita
  - [ ] 4 abas aparecem (Cadastro, Conferência, Resultados, Movimentação)

---

## 📝 Teste de Cadastro Manual

- [ ] **Aba 1 — Cadastro / Entrada Manual**
  - [ ] Formulário exibe corretamente
  - [ ] Campos: CNPJ, Razão Social, Data Início, Data Fim
  - [ ] Data fim > Data início (validação)
  - [ ] Tabela dinâmica funciona
  - [ ] Botão ➕ adiciona linhas
  - [ ] Botão ✅ SALVAR funciona
- [ ] **Mensagens esperadas após salvar**
  - [ ] ✅ "X colaborador(es) cadastrado(s) com sucesso"
  - [ ] ⚠️ (se houver duplicatas)
  - [ ] ❌ (se houver CPF inválido)
- [ ] **Links gerados**
  - [ ] Seção **🔗 Links para Compartilhar** aparece
  - [ ] Link no formato: `http://192.168.77.2:8501/?cnpj=XXXXX`
  - [ ] Link pode ser copiado

---

## 📊 Teste de Cadastro via CSV

- [ ] **Aba 1 — Cadastro / Importar via CSV**
  - [ ] Tab aparece corretamente
  - [ ] Botão **⬇️ Baixar Template CSV** funciona
  - [ ] Arquivo `template_colaboradores.csv` baixado
- [ ] **Validar template baixado**
  - [ ] Coluna 1: CPF
  - [ ] Coluna 2: Função
  - [ ] Coluna 3: Departamento
  - [ ] Separador: `;` (ponto-e-vírgula)
  - [ ] 2 linhas de exemplo
- [ ] **Teste de upload**
  - [ ] Preparar CSV com 3+ linhas
  - [ ] Upload com sucesso
  - [ ] Preview exibe dados corretamente
  - [ ] Botão **💾 SALVAR COLABORADORES** salva
  - [ ] Mensagem de sucesso exibida

---

## 👥 Teste de Resposta (Colaborador)

- [ ] **Acesso via link**
  - [ ] URL: `http://192.168.77.2:8501/?cnpj=[CNPJ_TESTADO]`
  - [ ] Página carrega sem erros
- [ ] **Tela de Login Colaborador**
  - [ ] Mensagem de boas-vindas exibe
  - [ ] Nome da empresa aparece: "🏢 Você está respondendo..."
  - [ ] Campo de CPF presente
  - [ ] Botão ACESSAR presente
- [ ] **Validações de CPF**
  - [ ] CPF válido (cadastrado) → Acesso
  - [ ] CPF inválido → ❌ "CPF inválido"
  - [ ] CPF não cadastrado → ❌ "Seu CPF não está autorizado"
- [ ] **Período válido**
  - [ ] Data hoje dentro do período → ✅ Acesso
  - [ ] Data hoje fora do período → ❌ Bloqueado
- [ ] **Resposta ao Questionário**
  - [ ] 7 blocos COPSOQ III aparecem
  - [ ] 35 questões totais
  - [ ] Botões "Anterior / Próximo" funcionam
  - [ ] Progresso exibido corretamente
  - [ ] Opções de resposta (1-5) funcionam
- [ ] **Envio de Respostas**
  - [ ] Botão **✅ ENVIAR** presente
  - [ ] Mensagem de confirmação: "Respostas salvas com sucesso"
- [ ] **Prevenção de Duplicata**
  - [ ] Mesmo CPF tenta acessar novamente
  - [ ] ⚠️ "Você já respondeu este questionário"

---

## 📊 Teste de Resultados

- [ ] **Aba 2 — Conferência e Correção**
  - [ ] Cadastro geral exibe (tabela)
  - [ ] Métricas aparecem: Total, Ativos, Inativos, Último cadastro
  - [ ] Filtro por empresa funciona
  - [ ] Botão **⬇️ Baixar lista filtrada** funciona
  - [ ] Expander **📅 Gerenciar Período** funciona
  - [ ] Alteração de datas funciona
- [ ] **Aba 3 — Resultados**
  - [ ] Gráfico de barras exibe
  - [ ] Mostra: Autorizados vs Respondidos
  - [ ] Seletor de empresa presente
  - [ ] Botão **📄 GERAR E BAIXAR LAUDO PDF**
- [ ] **Geração de Laudo PDF**
  - [ ] PDF gerado sem erros
  - [ ] Arquivo baixado para Downloads
  - [ ] Abre corretamente em leitor PDF
  - [ ] Contém:
    - [ ] Título e dados da empresa
    - [ ] Tabela de dimensões
    - [ ] Classificação de risco
    - [ ] Gráficos

---

## 🔄 Teste de Movimentação

- [ ] **Aba 4 — Movimentação de Pessoal**
  - [ ] Seção "Inativar colaborador" presente
  - [ ] CPF selecionável em dropdown
  - [ ] Botão **🚫 INATIVAR** funciona
  - [ ] Colaborador inativado não consegue acessar
- [ ] **Reativar Colaborador**
  - [ ] Seção "Reativar colaborador" presente
  - [ ] CPFs inativos listados
  - [ ] Botão **✅ REATIVAR** funciona
  - [ ] Colaborador reativado consegue acessar

---

## 🔐 Testes de Segurança

- [ ] **Criptografia de CPF**
  - [ ] CPF na tabela de resposta é um hash
  - [ ] Hash diferente para cada CPF
  - [ ] Não é possível reverter o hash
- [ ] **Período Bloqueado**
  - [ ] Colaborador fora do período não consegue acessar
  - [ ] Admin consegue alterar período e reabilitar
- [ ] **Senha Admin**
  - [ ] Senha padrão (`sstg2025`) rejeita
  - [ ] Senha configurada aceita
  - [ ] Botão "Sair" funciona

---

## 📁 Teste de Armazenamento

- [ ] **Armazenamento Local**
  - [ ] `db_acessos_autorizados.csv` criado
  - [ ] Contém dados cadastrados
  - [ ] `respostas_CNPJ_*.csv` criado após resposta
- [ ] **Google Drive (Se configurado)**
  - [ ] Google Drive Desktop ativo
  - [ ] Pasta sincronizada
  - [ ] Dados salvos em `G:\Meu Drive\...`
  - [ ] Sincronização em tempo real

---

## 🔗 Teste de Links

- [ ] **Link Gerado Válido**
  - [ ] Copiado e colado em novo navegador
  - [ ] Carrega página de resposta
  - [ ] Identifica empresa corretamente
- [ ] **Compartilhamento**
  - [ ] Link enviado via WhatsApp funciona
  - [ ] Link enviado via email funciona
  - [ ] Acessível de outro computador (mesmo WiFi)

---

## 📚 Documentação

- [ ] **README.md** presente e legível
- [ ] **TUTORIAL.md** presente (operacional)
- [ ] **GUIA_INSTALACAO.md** presente (setup)
- [ ] **GUIA_TECNICO.md** presente (técnico)
- [ ] Todos os arquivos com markup correto
- [ ] Links internos funcionam

---

## 🎨 Testes Visuais

- [ ] **Cores SSTG aplicadas**
  - [ ] Azul navy (#282C5B) em elementos primários
  - [ ] Verde (#5A9F62) em botões sucesso
  - [ ] Laranja (#DC3B24) em CTAs
- [ ] **Responsividade**
  - [ ] Layout funciona em desktop
  - [ ] Layout funciona em tablet
  - [ ] Layout funciona em mobile (visualização)
- [ ] **Fonts e Tipografia**
  - [ ] Sans Serif consistente
  - [ ] Tamanhos legíveis
  - [ ] Contrast adequado

---

## 🧪 Testes de Erro & Edge Cases

- [ ] **CPF Vazio** → Erro apropriado
- [ ] **CNPJ Vazio** → Erro apropriado
- [ ] **Data Fim < Data Início** → Erro apropriado
- [ ] **Arquivo CSV inválido** → Erro apropriado
- [ ] **Sem conexão internet** → Comportamento gracioso
- [ ] **Porta 8501 ocupada** → Mensagem clara

---

## 📱 Compatibilidade de Browser

- [ ] **Google Chrome** → Funciona
- [ ] **Mozilla Firefox** → Funciona
- [ ] **Microsoft Edge** → Funciona
- [ ] **Safari** (se aplicável) → Funciona

---

## 🚀 Pré-Produção

- [ ] **Backup** realizado
  - [ ] Cópia de todos os arquivos
  - [ ] Armazenado em local seguro
- [ ] **Plano de Rollback** documentado
  - [ ] Como voltar à versão anterior
  - [ ] Contacts de suporte

---

## 📊 Performance

- [ ] **Tempo de carregamento**
  - [ ] App inicia em < 5 segundos
  - [ ] Página de resposta carrega em < 2 segundos
  - [ ] PDF gerado em < 10 segundos
- [ ] **Uso de memória**
  - [ ] App consome < 500 MB RAM
  - [ ] Sem memory leaks (testes longos)

---

## 📞 Suporte Preparado

- [ ] **Documentação impressa** (opcional)
  - [ ] TUTORIAL.md impresso
  - [ ] FAQ anexado
- [ ] **Contatos de Suporte**
  - [ ] Email informado
  - [ ] Telefone disponível
  - [ ] Horário de atendimento claro
- [ ] **Treinamento Realizado**
  - [ ] Admin consegue usar
  - [ ] RH consegue distribuir links
  - [ ] Dúvidas esclarecidas

---

## ✅ Assinatura Final

```
Data de Conclusão:        ___/___/_____

Responsável Técnico:      _____________________
Assinatura:               _____________________

Responsável RH:           _____________________
Assinatura:               _____________________

Diretor/Gerente:          _____________________
Assinatura:               _____________________
```

---

## 📋 Observações Finais

```
_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
```

---

## 🎉 Status Geral

- [ ] ✅ **APROVADO PARA PRODUÇÃO**
- [ ] ⚠️ **APROVADO COM RESSALVAS** (listar abaixo)
- [ ] ❌ **REPROVADO** (retest necessário)

**Ressalvas (se aplicável):**
```
_________________________________________________________________

_________________________________________________________________
```

---

**Checklist de Lançamento — SSTG E-Social v6.0**  
**Última atualização: 30/04/2026**
