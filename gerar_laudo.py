from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether, Image
)
from datetime import datetime
import io
import os

# ===================== CORES SSTG =====================
C_AZUL    = colors.HexColor('#282C5B')
C_VERDE   = colors.HexColor('#5A9F62')
C_LARANJA = colors.HexColor('#DC3B24')
C_AMARELO = colors.HexColor('#EBA126')
C_CINZA   = colors.HexColor('#6B6966')
C_CINZAC  = colors.HexColor('#EFEFEF')
C_BRANCO  = colors.white

# ===================== RESPONSÁVEL TÉCNICO =====================
RESP_NOME  = "Valter Moura"
RESP_MTE   = "BA000776-5"
RESP_CREA  = "PE050659691-5"

# ===================== DIMENSÕES ANALÍTICAS COPSOQ III =====================
DIMS_ANALITICAS = {
    "Cargo": {
        "questoes": ["q1", "q4", "q11", "q13", "q17"],
        "invertida": False,
        "label": "Papel na Organização",
        "severidade": "Levemente Prejudicial",
        "fontes": "Falta de clareza de metas. Ambiguidade de tarefas e responsabilidades. Desconexão com os objetivos da empresa.",
        "agravos": "Ansiedade por desempenho e desmotivação.",
        "plano": "Realizar reuniões de alinhamento para detalhar metas individuais e revisar as descrições de cargo de cada setor. Reforçar, em reuniões e comunicados, como cada tarefa contribui para a missão e visão da empresa.",
        "responsavel": "Gestores de Setor",
        "prazo": "60 dias",
    },
    "Controle": {
        "questoes": ["q2", "q10", "q15", "q19", "q25", "q30"],
        "invertida": False,
        "label": "Controle e Autonomia",
        "severidade": "Prejudicial",
        "fontes": "Sem autonomia para decidir pausas. Baixa liberdade de escolha sobre o método de trabalho. Opinião dos trabalhadores ignorada.",
        "agravos": "Distúrbios psicossomáticos e sentimento de impotência.",
        "plano": "Implementar critérios que permitam ao trabalhador ter voz na organização da rotina diária. Estabelecer pausas estruturadas. Criar canais de sugestão com retorno formal.",
        "responsavel": "Supervisão",
        "prazo": "30 dias",
    },
    "Demandas": {
        "questoes": ["q3", "q6", "q9", "q12", "q16", "q18", "q20", "q22"],
        "invertida": True,
        "label": "Demanda e Ritmo",
        "severidade": "Prejudicial",
        "fontes": "Prazos inatingíveis. Velocidade excessiva de trabalho. Pressão para trabalhar fora do horário. Impossibilidade de pausas.",
        "agravos": "Estresse crônico e Síndrome de Burnout.",
        "plano": "Inserir micropausas regulares durante a jornada e estabelecer política de desconexão (proibir mensagens de trabalho fora do expediente). Revisar o dimensionamento das equipes.",
        "responsavel": "Gerência / RH",
        "prazo": "60 dias",
    },
    "Relacionamentos": {
        "questoes": ["q5", "q14", "q21", "q34"],
        "invertida": True,
        "label": "Relacionamentos",
        "severidade": "Extremamente Prejudicial",
        "fontes": "Comportamentos duros entre colaboradores. Conflitos e tensões interpessoais. Percepção de perseguição no trabalho.",
        "agravos": "Assédio Moral e Transtorno de Estresse Pós-Traumático.",
        "plano": "Criar Canal de Denúncias anônimo e atualizar o Código de Ética com foco em prevenção ao assédio. Estimular a cooperação por meio de metas compartilhadas.",
        "responsavel": "Jurídico / RH",
        "prazo": "45 dias",
    },
    "Apoio dos Colegas": {
        "questoes": ["q7", "q24", "q27", "q31"],
        "invertida": False,
        "label": "Suporte dos Pares",
        "severidade": "Prejudicial",
        "fontes": "Isolamento entre colegas. Baixa colaboração e apoio mútuo. Falta de reconhecimento entre pares.",
        "agravos": "Sentimento de desamparo, isolamento e insegurança.",
        "plano": "Criar grupos de trabalho colaborativos e comissões para solução de problemas coletivos. Incentivar atividades de integração entre equipes.",
        "responsavel": "RH",
        "prazo": "45 dias",
    },
    "Apoio da Chefia": {
        "questoes": ["q8", "q23", "q29", "q33", "q35"],
        "invertida": False,
        "label": "Suporte dos Superiores",
        "severidade": "Prejudicial",
        "fontes": "Falta de suporte técnico da chefia. Baixo incentivo e reconhecimento. Falta de confiança na liderança imediata.",
        "agravos": "Sentimento de desamparo e baixa autoestima profissional.",
        "plano": "Realizar treinamento de liderança positiva para as chefias imediatas. Implementar avaliação de liderança por feedback 360° e capacitar gestores em liderança situacional.",
        "responsavel": "RH / Direção",
        "prazo": "90 dias",
    },
    "Comunicação e Mudanças": {
        "questoes": ["q26", "q28", "q32"],
        "invertida": False,
        "label": "Mudanças Organizacionais",
        "severidade": "Levemente Prejudicial",
        "fontes": "Ausência de espaço para esclarecimento de dúvidas. Falta de consulta aos trabalhadores. Comunicação impositiva sobre mudanças.",
        "agravos": "Irritabilidade, resistência às mudanças e queda de produtividade.",
        "plano": "Estabelecer fluxo de comunicação prévia ouvindo trabalhadores antes de implementar mudanças. Treinar gestores para repassar informações críticas em tempo hábil.",
        "responsavel": "Direção",
        "prazo": "Imediato",
    },
}

# ===================== MATRIZ BS 8800 =====================
BS8800 = {
    ("Levemente Prejudicial", "Desprezível"):  "Trivial",
    ("Levemente Prejudicial", "Pequena"):      "Trivial",
    ("Levemente Prejudicial", "Moderada"):     "Tolerável",
    ("Levemente Prejudicial", "Significante"): "Moderado",
    ("Levemente Prejudicial", "Excessiva"):    "Substancial",
    ("Prejudicial", "Desprezível"):            "Tolerável",
    ("Prejudicial", "Pequena"):                "Tolerável",
    ("Prejudicial", "Moderada"):               "Moderado",
    ("Prejudicial", "Significante"):           "Substancial",
    ("Prejudicial", "Excessiva"):              "Substancial",
    ("Extremamente Prejudicial", "Desprezível"):  "Tolerável",
    ("Extremamente Prejudicial", "Pequena"):      "Moderado",
    ("Extremamente Prejudicial", "Moderada"):     "Substancial",
    ("Extremamente Prejudicial", "Significante"): "Intolerável",
    ("Extremamente Prejudicial", "Excessiva"):    "Intolerável",
}

PROB_MAP = {"Alto": "Excessiva", "Moderado": "Significante", "Baixo": "Pequena"}

RISCO_COR = {
    "Trivial":      colors.HexColor('#70AD47'),
    "Tolerável":    colors.HexColor('#92D050'),
    "Moderado":     C_AMARELO,
    "Substancial":  C_LARANJA,
    "Intolerável":  colors.HexColor('#7030A0'),
}

ACAO_NECESSARIA = {
    "Trivial":     "NÃO",
    "Tolerável":   "NÃO",
    "Moderado":    "SIM",
    "Substancial": "SIM",
    "Intolerável": "SIM",
}

# ===================== FUNÇÕES AUXILIARES =====================

def classificar(media: float) -> str:
    if media <= 1.49:
        return "Alto"
    elif media <= 2.99:
        return "Moderado"
    return "Baixo"

def cor_copsoq(classif: str):
    return {
        "Alto": C_LARANJA,
        "Moderado": C_AMARELO,
        "Baixo": C_VERDE,
    }.get(classif, C_CINZA)

def bs8800_nivel(sev: str, prob: str) -> str:
    return BS8800.get((sev, prob), "Moderado")

# ===================== ESTILOS =====================

def get_styles():
    s = {}
    s['titulo_capa'] = ParagraphStyle(
        'titulo_capa', fontName='Helvetica-Bold', fontSize=22,
        textColor=C_BRANCO, alignment=TA_CENTER, leading=28, spaceAfter=6
    )
    s['subtitulo_capa'] = ParagraphStyle(
        'subtitulo_capa', fontName='Helvetica', fontSize=12,
        textColor=C_BRANCO, alignment=TA_CENTER, leading=16
    )
    s['label_capa'] = ParagraphStyle(
        'label_capa', fontName='Helvetica-Bold', fontSize=9,
        textColor=C_BRANCO, alignment=TA_LEFT, leading=14
    )
    s['valor_capa'] = ParagraphStyle(
        'valor_capa', fontName='Helvetica', fontSize=9,
        textColor=C_BRANCO, alignment=TA_LEFT, leading=14
    )
    s['secao_titulo'] = ParagraphStyle(
        'secao_titulo', fontName='Helvetica-Bold', fontSize=13,
        textColor=C_AZUL, spaceBefore=16, spaceAfter=8, leading=18,
        leftIndent=10, borderPad=4
    )
    s['subsecao_titulo'] = ParagraphStyle(
        'subsecao_titulo', fontName='Helvetica-Bold', fontSize=10,
        textColor=C_AZUL, spaceBefore=10, spaceAfter=4, leading=14
    )
    s['body'] = ParagraphStyle(
        'body', fontName='Helvetica', fontSize=9,
        textColor=colors.HexColor('#333333'), alignment=TA_JUSTIFY,
        leading=14, spaceAfter=6
    )
    s['body_bold'] = ParagraphStyle(
        'body_bold', fontName='Helvetica-Bold', fontSize=9,
        textColor=colors.HexColor('#333333'), leading=14
    )
    s['lista'] = ParagraphStyle(
        'lista', fontName='Helvetica', fontSize=9,
        textColor=colors.HexColor('#333333'), leading=14,
        leftIndent=16, spaceAfter=3, bulletIndent=8
    )
    s['rodape_label'] = ParagraphStyle(
        'rodape_label', fontName='Helvetica-Bold', fontSize=7,
        textColor=C_CINZA, alignment=TA_LEFT
    )
    s['sumario_item'] = ParagraphStyle(
        'sumario_item', fontName='Helvetica', fontSize=10,
        textColor=colors.HexColor('#333333'), leading=20
    )
    s['sumario_num'] = ParagraphStyle(
        'sumario_num', fontName='Helvetica-Bold', fontSize=10,
        textColor=C_AZUL, leading=20
    )
    s['table_header'] = ParagraphStyle(
        'table_header', fontName='Helvetica-Bold', fontSize=8,
        textColor=C_BRANCO, alignment=TA_CENTER, leading=10
    )
    s['table_cell'] = ParagraphStyle(
        'table_cell', fontName='Helvetica', fontSize=8,
        textColor=colors.HexColor('#333333'), leading=11, alignment=TA_LEFT
    )
    s['table_cell_center'] = ParagraphStyle(
        'table_cell_center', fontName='Helvetica', fontSize=8,
        textColor=colors.HexColor('#333333'), leading=11, alignment=TA_CENTER
    )
    s['table_cell_bold'] = ParagraphStyle(
        'table_cell_bold', fontName='Helvetica-Bold', fontSize=8,
        textColor=colors.HexColor('#333333'), leading=11, alignment=TA_CENTER
    )
    return s

# ===================== HEADER / FOOTER =====================

def _header_footer(canvas_obj, doc, empresa=""):
    canvas_obj.saveState()
    w, h = A4

    # Header — barra navy
    canvas_obj.setFillColor(C_AZUL)
    canvas_obj.rect(0, h - 1.4*cm, w, 1.4*cm, fill=1, stroke=0)
    canvas_obj.setFillColor(C_BRANCO)
    canvas_obj.setFont("Helvetica-Bold", 8)
    canvas_obj.drawString(1*cm, h - 0.85*cm, "PGR / LAUDO — FATORES PSICOSSOCIAIS")
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.drawRightString(w - 1*cm, h - 0.85*cm, f"Pág. {doc.page}")

    # Linha verde abaixo do header
    canvas_obj.setFillColor(C_VERDE)
    canvas_obj.rect(0, h - 1.55*cm, w, 0.15*cm, fill=1, stroke=0)

    # Footer
    canvas_obj.setFillColor(C_AZUL)
    canvas_obj.rect(0, 0, w, 0.75*cm, fill=1, stroke=0)
    canvas_obj.setFillColor(C_BRANCO)
    canvas_obj.setFont("Helvetica", 6.5)
    canvas_obj.drawCentredString(w / 2, 0.22*cm,
        f"SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1) — Gestão Ocupacional  |  Laudo de Fatores Psicossociais  |  {empresa}  |  Documento Confidencial")

    canvas_obj.restoreState()

# ===================== SEÇÃO: CAPA =====================

def build_capa(st, empresa, cnpj, cnae, grau_risco, data_emissao, logo_path):
    w, h = A4
    elementos = []

    # --- Bloco hero (fundo navy, logo + título) ---
    logo_cell = ""
    if logo_path and os.path.exists(logo_path):
        logo_cell = Image(logo_path, width=4.5*cm, height=2.2*cm, kind='proportional')

    hero_data = [[
        logo_cell,
        [
            Paragraph("Laudo de Fatores Psicossociais", st['titulo_capa']),
            Paragraph("Anexo do Programa de Gerenciamento de Riscos — PGR", st['subtitulo_capa']),
        ]
    ]]
    hero = Table(hero_data, colWidths=[5.5*cm, 13*cm])
    hero.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_AZUL),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (0, 0), 20),
        ('RIGHTPADDING', (1, 0), (1, 0), 20),
        ('TOPPADDING', (0, 0), (-1, -1), 20),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 20),
        ('ROUNDEDCORNERS', [0, 0, 0, 0]),
    ]))
    elementos.append(hero)

    # Faixa laranja NR-01
    faixa = Table([[Paragraph("NR 01 — Fatores Psicossociais Relacionados ao Trabalho",
        ParagraphStyle('nr', fontName='Helvetica-Bold', fontSize=11,
                       textColor=C_BRANCO, alignment=TA_CENTER))]],
        colWidths=[18.5*cm])
    faixa.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_LARANJA),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))
    elementos.append(faixa)
    elementos.append(Spacer(1, 0.5*cm))

    # Dados do documento — duas colunas
    def campo(label, valor):
        return [
            Paragraph(label, ParagraphStyle('cl', fontName='Helvetica-Bold', fontSize=9,
                       textColor=C_AZUL, leading=13)),
            Paragraph(str(valor), ParagraphStyle('cv', fontName='Helvetica', fontSize=9,
                       textColor=colors.HexColor('#333333'), leading=13)),
        ]

    dados_esq = [
        campo("Razão Social:", empresa),
        campo("CNPJ:", cnpj),
        campo("CNAE Principal:", cnae or "—"),
        campo("Grau de Risco:", grau_risco or "—"),
    ]
    dados_dir = [
        campo("Data de Emissão:", data_emissao),
        campo("Responsável Técnico:", RESP_NOME),
        campo("MTE:", RESP_MTE),
        campo("CREA:", RESP_CREA),
    ]

    def montar_bloco(dados, titulo):
        rows = [[Paragraph(titulo, ParagraphStyle('bt', fontName='Helvetica-Bold', fontSize=9,
                           textColor=C_BRANCO, alignment=TA_CENTER))]]
        for par in dados:
            rows.append(par)
        t = Table(rows, colWidths=[4.5*cm, 4.5*cm])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), C_AZUL),
            ('SPAN', (0, 0), (-1, 0)),
            ('BACKGROUND', (0, 1), (-1, -1), C_CINZAC),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [C_CINZAC, C_BRANCO]),
        ]))
        return t

    row_dados = [[montar_bloco(dados_esq, "DADOS DA EMPRESA"),
                  Spacer(0.5*cm, 1),
                  montar_bloco(dados_dir, "IDENTIFICAÇÃO DO DOCUMENTO")]]
    t_dados = Table(row_dados, colWidths=[9*cm, 0.5*cm, 9*cm])
    t_dados.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')]))
    elementos.append(t_dados)
    elementos.append(Spacer(1, 0.5*cm))

    # Rodapé da capa
    rod = Table([[
        Paragraph("Este documento é parte integrante do PGR e deve ser mantido disponível aos trabalhadores "
                  "e à Inspeção do Trabalho. Elaborado em conformidade com a NR-01.",
                  ParagraphStyle('note', fontName='Helvetica-Oblique', fontSize=8,
                                 textColor=C_CINZA, alignment=TA_CENTER, leading=12))
    ]], colWidths=[18.5*cm])
    rod.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_CINZAC),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('BOX', (0, 0), (-1, -1), 0.5, C_VERDE),
    ]))
    elementos.append(rod)
    elementos.append(PageBreak())
    return elementos

# ===================== SEÇÃO: SUMÁRIO =====================

def build_sumario(st):
    el = []
    el.append(_titulo_secao("SUMÁRIO", st))
    itens = [
        ("1.", "Identificação"),
        ("2.", "Contexto Legal e Justificativa"),
        ("3.", "Metodologia de Avaliação"),
        ("4.", "Inventário de Riscos Psicossociais"),
        ("5.", "Plano de Ação"),
        ("6.", "Conclusão"),
    ]
    rows = [[Paragraph(n, st['sumario_num']), Paragraph(t, st['sumario_item'])] for n, t in itens]
    t = Table(rows, colWidths=[1.5*cm, 17*cm])
    t.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor('#dddddd')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [C_BRANCO, C_CINZAC]),
    ]))
    el.append(t)
    el.append(PageBreak())
    return el

# ===================== SEÇÃO 1: IDENTIFICAÇÃO =====================

def build_s1(st, empresa, cnpj, cnae, grau_risco, data_laudo, data_pgr="—", status_pgr="Vigente"):
    el = []
    el.append(_titulo_secao("1. IDENTIFICAÇÃO", st))

    el.append(_subtitulo("1.1. Dados da Unidade Operacional", st))
    dados = [
        ["Razão Social:", empresa],
        ["CNPJ:", cnpj],
        ["CNAE Principal:", cnae or "—"],
        ["Grau de Risco:", grau_risco or "—"],
    ]
    el.append(_tabela_dados(dados))
    el.append(Spacer(1, 0.3*cm))

    el.append(_subtitulo("1.2. Referência do Documento Principal (PGR)", st))
    dados2 = [
        ["Título do Documento Principal:", "Programa de Gerenciamento de Riscos — PGR"],
        ["Data de Emissão do PGR Base:", data_pgr],
        ["Responsável Técnico pelo PGR Base:", RESP_NOME],
        ["Status do PGR Base:", status_pgr],
    ]
    el.append(_tabela_dados(dados2))
    el.append(Spacer(1, 0.3*cm))

    el.append(_subtitulo("1.3. Responsável pela Elaboração", st))
    dados3 = [
        ["Nome:", RESP_NOME],
        ["Registro Profissional (MTE):", RESP_MTE],
        ["Registro Profissional (CREA):", RESP_CREA],
        ["Data de Elaboração:", data_laudo],
    ]
    el.append(_tabela_dados(dados3))
    el.append(PageBreak())
    return el

# ===================== SEÇÃO 2: CONTEXTO LEGAL =====================

def build_s2(st):
    el = []
    el.append(_titulo_secao("2. CONTEXTO LEGAL E JUSTIFICATIVA", st))

    el.append(_subtitulo("2.1. Amparo Normativo", st))
    el.append(Paragraph(
        "Este documento fundamenta-se na <b>NR-01 (Disposições Gerais e Gerenciamento de Riscos Ocupacionais)</b>, "
        "que estabelece a obrigatoriedade de o gerenciamento de riscos abranger, além dos agentes físicos, químicos "
        "e biológicos, ergonômicos e de acidentes, também os <b>fatores de risco psicossociais relacionados ao trabalho</b>. "
        "A avaliação desses riscos deve considerar as exigências da atividade de trabalho e a eficácia das medidas de "
        "prevenção já implementadas pela organização.", st['body']))
    el.append(Paragraph(
        "Vale ressaltar que os fatores psicossociais encontram-se classificados dentro do grupo de agentes ergonômicos.",
        st['body']))

    el.append(_subtitulo("2.2. Da Integração ao PGR", st))
    el.append(Paragraph(
        "Em conformidade com o subitem <b>1.5.3.1.3</b>, o Programa de Gerenciamento de Riscos (PGR) deve contemplar "
        "ou estar integrado com planos, programas e outros documentos previstos na legislação de SST. "
        "Portanto, a organização opta pela modalidade deste documento complementar, garantindo que:", st['body']))
    for item in [
        "As informações aqui contidas integrem o <b>Inventário de Riscos</b> e o <b>Plano de Ação</b> do PGR principal;",
        "Seja mantida a unidade do Gerenciamento de Riscos Ocupacionais (GRO) sem a necessidade de reestruturação "
        "dos riscos já inventariados e controlados no documento base.",
    ]:
        el.append(Paragraph(f"• {item}", st['lista']))

    el.append(_subtitulo("2.3. Objetivo deste Documento", st))
    el.append(Paragraph(
        "O presente documento tem como objetivo identificar perigos e avaliar riscos especificamente voltados à "
        "saúde mental e organização do trabalho, visando prevenir lesões e agravos à saúde. A implementação destas "
        "medidas de prevenção segue a ordem de prioridade estabelecida na norma, priorizando a eliminação de "
        "fatores de risco e a adoção de medidas administrativas ou de organização do trabalho.", st['body']))

    el.append(_subtitulo("2.4. Declaração de Vinculação", st))
    el.append(Paragraph(
        "A organização declara que este documento complementar é parte indissociável do <b>PGR identificado no "
        "Item 1.2</b>. Toda a documentação encontra-se datada e assinada sob a responsabilidade da organização, "
        "permanecendo disponível aos trabalhadores, seus representantes e à Inspeção do Trabalho.", st['body']))
    el.append(PageBreak())
    return el

# ===================== SEÇÃO 3: METODOLOGIA =====================

def build_s3(st, total_respondentes):
    el = []
    el.append(_titulo_secao("3. METODOLOGIA DE AVALIAÇÃO", st))

    el.append(_subtitulo("3.1. Base Científica e Ferramenta de Coleta", st))
    el.append(Paragraph(
        "Para a identificação dos perigos e avaliação dos riscos psicossociais, foi utilizado o "
        "<b>Questionário de Fatores Psicossociais COPSOQ III</b> (Copenhagen Psychosocial Questionnaire — versão III), "
        "baseado em metodologia científica validada e publicada pela <b>Revista Brasileira de Medicina do Trabalho "
        "(RBMT)</b>, com validação formal confirmada pela Rede COPSOQ Internacional em 2025. Esta ferramenta permite "
        "uma análise quantitativa e qualitativa da percepção dos trabalhadores sobre a organização do trabalho, "
        "com foco na Health Safety Executive - Management Standard (HSE-MS).", st['body']))
    el.append(Paragraph(
        f"Nesta avaliação participaram <b>{total_respondentes} trabalhador(es)</b>, respondendo ao questionário "
        "de forma anônima e voluntária por meio de sistema digital com controle de duplicidade.",
        st['body']))

    el.append(_subtitulo("3.2. Categorias Analisadas", st))
    el.append(Paragraph(
        "A avaliação consiste em <b>35 questões</b> que rastreiam o nível de exposição dos trabalhadores em "
        "<b>7 dimensões críticas</b>:", st['body']))
    dims_desc = [
        ("Demanda e Ritmo", "Avalia o ritmo de trabalho, prazos e intensidade das tarefas."),
        ("Controle e Autonomia", "Mede a autonomia do trabalhador e sua participação nas decisões sobre como executar o trabalho."),
        ("Suporte dos Superiores", "Verifica o incentivo, a confiança e o apoio recebido da chefia imediata."),
        ("Suporte dos Pares", "Analisa a colaboração e o apoio entre os colegas de equipe."),
        ("Relacionamentos", "Identifica a presença de conflitos, condutas duras ou situações de perseguição no ambiente laboral."),
        ("Papel na Organização", "Checa a clareza quanto às metas, responsabilidades e objetivos da empresa."),
        ("Mudanças Organizacionais", "Avalia como as alterações nos processos de trabalho são comunicadas e conduzidas."),
    ]
    for nome, desc in dims_desc:
        el.append(Paragraph(f"• <b>{nome}:</b> {desc}", st['lista']))

    el.append(_subtitulo("3.3. Escala de Respostas e Pontuação (Escala Likert)", st))
    likert_data = [
        [Paragraph("Resposta", st['table_header']), Paragraph("Pontuação", st['table_header']),
         Paragraph("Interpretação", st['table_header'])],
        ["Nunca", "0", "Ausência total da situação"],
        ["Raramente", "1", "Situação muito esporádica"],
        ["Às vezes", "2", "Situação intermediária"],
        ["Frequentemente", "3", "Situação recorrente"],
        ["Sempre", "4", "Situação permanente"],
    ]
    tl = Table(likert_data, colWidths=[4*cm, 3*cm, 11.5*cm])
    tl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_AZUL),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [C_CINZAC, C_BRANCO]),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#cccccc')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#333333')),
    ]))
    el.append(tl)
    el.append(Spacer(1, 0.2*cm))

    el.append(_subtitulo("3.4. Critérios de Avaliação de Risco", st))
    el.append(Paragraph(
        "Em conformidade com o subitem <b>1.5.4.4.2.1</b> da NR-01, o nível de risco é determinado pela "
        "frequência das respostas, calculando-se a <b>média aritmética</b> por dimensão de todos os respondentes. "
        "<b>Importante:</b> para as dimensões de risco direto (Demandas e Relacionamentos), a pontuação é "
        "invertida antes do cálculo (pontuação final = 4 − pontuação bruta), pois nestas dimensões maior "
        "frequência equivale a maior sofrimento.", st['body']))
    class_data = [
        [Paragraph("Média por Dimensão", st['table_header']),
         Paragraph("Classificação COPSOQ III", st['table_header']),
         Paragraph("Probabilidade (BS 8800)", st['table_header']),
         Paragraph("Interpretação", st['table_header'])],
        ["0,00 — 1,49", "ALTO", "Excessiva", "Trabalhadores frequentemente expostos. Ação imediata necessária."],
        ["1,50 — 2,99", "MODERADO", "Significante", "Exposição recorrente. Medidas preventivas recomendadas."],
        ["3,00 — 4,00", "BAIXO", "Pequena", "Exposição eventual. Manter e monitorar controles atuais."],
    ]
    tc = Table(class_data, colWidths=[4*cm, 3.5*cm, 4*cm, 7*cm])
    tc.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_AZUL),
        ('TEXTCOLOR', (0, 0), (-1, 0), C_BRANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#333333')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (3, 1), (3, -1), 'LEFT'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#cccccc')),
        ('BACKGROUND', (1, 1), (1, 1), colors.HexColor('#FFD7D7')),
        ('BACKGROUND', (1, 2), (1, 2), colors.HexColor('#FFF3CC')),
        ('BACKGROUND', (1, 3), (1, 3), colors.HexColor('#D7F0DD')),
        ('ROWBACKGROUNDS', (0, 1), (0, -1), [C_CINZAC, C_BRANCO, C_CINZAC]),
    ]))
    el.append(tc)
    el.append(Paragraph(
        "A classificação do Nível de Risco final é obtida pelo cruzamento da Severidade (característica do "
        "perigo psicossocial por dimensão) com a Probabilidade (derivada da classificação COPSOQ III acima), "
        "conforme a <b>Matriz BS 8800 — OHSAS 18.001 (Anexo D)</b>.", st['body']))
    el.append(PageBreak())
    return el

# ===================== SEÇÃO 4: INVENTÁRIO =====================

def build_s4(st, medias_por_dim):
    el = []
    el.append(_titulo_secao("4. INVENTÁRIO DE RISCOS PSICOSSOCIAIS", st))
    el.append(Paragraph(
        "Este inventário consolida a identificação dos perigos e a avaliação dos riscos ocupacionais de natureza "
        "psicossocial levantados nesta unidade, com base na percepção direta dos trabalhadores coletada por meio do "
        "Questionário COPSOQ III. Os dados contemplam a caracterização das atividades, a descrição das fontes "
        "geradoras de estresse e carga mental, e a indicação das possíveis lesões ou agravos à saúde.",
        st['body']))

    # Cabeçalho da tabela
    header = [
        Paragraph("Categoria / Dimensão", st['table_header']),
        Paragraph("Fontes e Circunstâncias", st['table_header']),
        Paragraph("Possíveis Lesões ou Agravos", st['table_header']),
        Paragraph("Medidas Preventivas Atuais", st['table_header']),
        Paragraph("Sev.", st['table_header']),
        Paragraph("Prob.", st['table_header']),
        Paragraph("Nível de Risco", st['table_header']),
        Paragraph("Plano?", st['table_header']),
    ]
    rows = [header]
    risco_cells = []

    for i, (dim_key, cfg) in enumerate(DIMS_ANALITICAS.items()):
        col_key = f"Dim_{dim_key.replace(' ', '_')}"
        media = medias_por_dim.get(col_key, 2.0)
        classif = classificar(media)
        prob = PROB_MAP[classif]
        sev = cfg["severidade"]
        nivel = bs8800_nivel(sev, prob)
        plano = ACAO_NECESSARIA.get(nivel, "SIM")

        row = [
            Paragraph(f"<b>{cfg['label']}</b>\n\nMédia: {media:.2f} | <b>{classif}</b>",
                      st['table_cell']),
            Paragraph(cfg["fontes"], st['table_cell']),
            Paragraph(cfg["agravos"], st['table_cell']),
            Paragraph("Nenhuma medida implementada." if classif == "Alto" else
                      "Medidas parciais em execução." if classif == "Moderado" else
                      "Controles implementados e monitorados.", st['table_cell']),
            Paragraph(sev[:3] + ".", st['table_cell_center']),
            Paragraph(prob[:3] + ".", st['table_cell_center']),
            Paragraph(nivel, st['table_cell_bold']),
            Paragraph(plano, st['table_cell_bold']),
        ]
        rows.append(row)
        risco_cells.append((i + 1, nivel, classif))

    col_w = [3.5*cm, 3.5*cm, 3*cm, 3*cm, 1.4*cm, 1.4*cm, 2.2*cm, 1.5*cm]
    t = Table(rows, colWidths=col_w, repeatRows=1)

    style = [
        ('BACKGROUND', (0, 0), (-1, 0), C_AZUL),
        ('TEXTCOLOR', (0, 0), (-1, 0), C_BRANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 7.5),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (4, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 7.5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [C_CINZAC, C_BRANCO]),
    ]
    for row_i, nivel, classif in risco_cells:
        cor = RISCO_COR.get(nivel, C_AMARELO)
        style.append(('BACKGROUND', (6, row_i), (6, row_i), cor))
        style.append(('TEXTCOLOR', (6, row_i), (6, row_i), C_BRANCO))
        # Cor da classificação COPSOQ
        cor_c = cor_copsoq(classif)
        style.append(('TEXTCOLOR', (0, row_i), (0, row_i), cor_c))

    t.setStyle(TableStyle(style))
    el.append(t)

    # Legenda de cores
    el.append(Spacer(1, 0.3*cm))
    legenda_data = [[
        Paragraph("Legenda de Nível de Risco (Matriz BS 8800):", st['body_bold']),
        _chip("Trivial", RISCO_COR["Trivial"]),
        _chip("Tolerável", RISCO_COR["Tolerável"]),
        _chip("Moderado", RISCO_COR["Moderado"]),
        _chip("Substancial", RISCO_COR["Substancial"]),
        _chip("Intolerável", RISCO_COR["Intolerável"]),
    ]]
    tl = Table(legenda_data, colWidths=[5*cm, 2.5*cm, 2.5*cm, 2.5*cm, 2.7*cm, 2.7*cm])
    tl.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ]))
    el.append(tl)
    el.append(PageBreak())
    return el

# ===================== SEÇÃO 5: PLANO DE AÇÃO =====================

def build_s5(st, medias_por_dim):
    el = []
    el.append(_titulo_secao("5. PLANO DE AÇÃO", st))
    el.append(Paragraph(
        "As medidas de prevenção abaixo foram propostas com base na classificação de risco obtida no Inventário. "
        "A organização deve acompanhar o desempenho dessas medidas para verificar sua eficácia e realizar "
        "ajustes sempre que necessário. Dimensões classificadas como <b>Trivial</b> ou <b>Tolerável</b> "
        "não requerem plano de ação, porém devem ser monitoradas.", st['body']))

    header = [
        Paragraph("Categoria / Risco", st['table_header']),
        Paragraph("Medida de Prevenção Proposta (O que fazer)", st['table_header']),
        Paragraph("Responsável", st['table_header']),
        Paragraph("Prazo", st['table_header']),
    ]
    rows = [header]

    for dim_key, cfg in DIMS_ANALITICAS.items():
        col_key = f"Dim_{dim_key.replace(' ', '_')}"
        media = medias_por_dim.get(col_key, 2.0)
        classif = classificar(media)
        prob = PROB_MAP[classif]
        nivel = bs8800_nivel(cfg["severidade"], prob)

        if ACAO_NECESSARIA.get(nivel, "SIM") == "NÃO":
            continue

        cor = RISCO_COR.get(nivel, C_AMARELO)
        rows.append([
            Paragraph(f"<b>{cfg['label']}</b>\nRisco: {nivel}\nMédia: {media:.2f} ({classif})",
                      st['table_cell']),
            Paragraph(cfg["plano"], st['table_cell']),
            Paragraph(cfg["responsavel"], st['table_cell_center']),
            Paragraph(cfg["prazo"], st['table_cell_bold']),
        ])

    if len(rows) == 1:
        rows.append([
            Paragraph("—", st['table_cell_center']),
            Paragraph("Nenhuma ação necessária. Manter monitoramento periódico.", st['table_cell']),
            Paragraph("—", st['table_cell_center']),
            Paragraph("—", st['table_cell_center']),
        ])

    t = Table(rows, colWidths=[4*cm, 9*cm, 3*cm, 2.5*cm], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), C_AZUL),
        ('TEXTCOLOR', (0, 0), (-1, 0), C_BRANCO),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#333333')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [C_CINZAC, C_BRANCO]),
    ]))
    el.append(t)
    el.append(PageBreak())
    return el

# ===================== SEÇÃO 6: CONCLUSÃO =====================

def build_s6(st, empresa):
    el = []
    el.append(_titulo_secao("6. CONCLUSÃO", st))
    el.append(Paragraph(
        f"A elaboração deste documento complementar de Fatores Psicossociais para a organização "
        f"<b>{empresa}</b> reafirma o compromisso com o Gerenciamento de Riscos Ocupacionais (GRO) integral, "
        "atendendo à obrigatoriedade estabelecida pela NR-01. A identificação de perigos e a avaliação de "
        "riscos aqui registradas demonstram que a saúde mental e a organização do trabalho são partes "
        "indissociáveis da segurança e saúde no trabalho.", st['body']))
    el.append(Paragraph(
        "Ressalta-se que a eficácia deste documento depende da implementação fiel do <b>Plano de Ação "
        "(Item 5)</b>. A organização deve assegurar que as medidas propostas sejam acompanhadas de forma "
        "planejada, com a participação ativa dos trabalhadores e da CIPA, quando houver.", st['body']))
    el.append(Paragraph(
        "Este documento deverá ser revisado sempre que houver mudanças nos processos de trabalho, ocorrência "
        "de doenças relacionadas ao trabalho ou, no máximo, <b>a cada dois anos</b>, de forma a manter o "
        "Inventário de Riscos sempre atualizado e em conformidade com as diretrizes legais vigentes.",
        st['body']))
    el.append(Spacer(1, 1*cm))

    # Assinatura
    ass = Table([
        [Paragraph("____________________________", st['body']),
         Paragraph("____________________________", st['body'])],
        [Paragraph(RESP_NOME, st['body_bold']),
         Paragraph("Representante Legal da Organização", st['body_bold'])],
        [Paragraph(f"MTE: {RESP_MTE} | CREA: {RESP_CREA}", st['body']),
         Paragraph("Cargo: ________________________________", st['body'])],
    ], colWidths=[9*cm, 9*cm])
    ass.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    el.append(ass)
    el.append(Spacer(1, 0.5*cm))

    # Rodapé legal
    nota = Table([[Paragraph(
        "Fonte metodológica: Questionário COPSOQ III — validado pela Rede COPSOQ Internacional (2025). "
        "Classificação de riscos: Matriz BS 8800 (Anexo D) — OHSAS 18.001, traduzida livremente. "
        "Referência normativa: NR-01 — Portaria MTE nº 1.419/2024.",
        ParagraphStyle('nota', fontName='Helvetica-Oblique', fontSize=7, textColor=C_CINZA,
                       alignment=TA_CENTER, leading=11))]], colWidths=[18.5*cm])
    nota.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_CINZAC),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('BOX', (0, 0), (-1, -1), 0.3, C_CINZA),
    ]))
    el.append(nota)
    return el

# ===================== HELPERS =====================

def _titulo_secao(texto, st):
    t = Table([[Paragraph(texto, ParagraphStyle(
        'ts', fontName='Helvetica-Bold', fontSize=12, textColor=C_BRANCO,
        leading=16, leftIndent=4))]],
        colWidths=[18.5*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), C_AZUL),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('LINEBELOW', (0, 0), (-1, -1), 2, C_VERDE),
    ]))
    s = Spacer(1, 0.3*cm)
    return KeepTogether([s, t, Spacer(1, 0.2*cm)])

def _subtitulo(texto, st):
    return Paragraph(texto, st['subsecao_titulo'])

def _tabela_dados(dados):
    rows = [[Paragraph(l, ParagraphStyle('tl', fontName='Helvetica-Bold', fontSize=8.5,
                       textColor=C_AZUL, leading=12)),
             Paragraph(str(v), ParagraphStyle('tv', fontName='Helvetica', fontSize=8.5,
                       textColor=colors.HexColor('#333333'), leading=12))]
            for l, v in dados]
    t = Table(rows, colWidths=[5.5*cm, 13*cm])
    t.setStyle(TableStyle([
        ('ROWBACKGROUNDS', (0, 0), (-1, -1), [C_CINZAC, C_BRANCO]),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.3, colors.HexColor('#dddddd')),
    ]))
    return t

def _chip(texto, cor):
    t = Table([[Paragraph(texto, ParagraphStyle('chip', fontName='Helvetica-Bold', fontSize=7,
                           textColor=C_BRANCO, alignment=TA_CENTER))]],
              colWidths=[None])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), cor),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('ROUNDEDCORNERS', [4, 4, 4, 4]),
    ]))
    return t

# ===================== FUNÇÃO PRINCIPAL =====================

def gerar_laudo_pdf(
    dados_empresa: dict,
    medias_por_dim: dict,
    total_respondentes: int,
    logo_path: str = "logo_sstg.png"
) -> bytes:
    """
    Gera o Laudo de Fatores Psicossociais em PDF e retorna os bytes.

    dados_empresa: dict com chaves 'Empresa', 'CNPJ', 'CNAE', 'Grau_Risco'
    medias_por_dim: dict com chaves 'Dim_X' → média float (já com inversão aplicada)
    total_respondentes: int
    logo_path: caminho para a imagem da logo (opcional)
    """
    buffer = io.BytesIO()
    empresa = dados_empresa.get("Empresa", "—")
    cnpj    = dados_empresa.get("CNPJ", "—")
    cnae    = dados_empresa.get("CNAE", "—")
    grau    = dados_empresa.get("Grau_Risco", "—")
    data_emissao = datetime.now().strftime("%d/%m/%Y")

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=1.5*cm,
        rightMargin=1.5*cm,
        topMargin=2.2*cm,
        bottomMargin=1.5*cm,
        title=f"Laudo Psicossocial — {empresa}",
        author=RESP_NOME,
        subject="Laudo de Fatores Psicossociais — NR-01",
    )

    st = get_styles()

    def _callback(canvas_obj, doc_obj):
        if doc_obj.page > 1:
            _header_footer(canvas_obj, doc_obj, empresa)

    story = []
    story += build_capa(st, empresa, cnpj, cnae, grau, data_emissao, logo_path)
    story += build_sumario(st)
    story += build_s1(st, empresa, cnpj, cnae, grau, data_emissao)
    story += build_s2(st)
    story += build_s3(st, total_respondentes)
    story += build_s4(st, medias_por_dim)
    story += build_s5(st, medias_por_dim)
    story += build_s6(st, empresa)

    doc.build(story, onFirstPage=_callback, onLaterPages=_callback)
    return buffer.getvalue()
