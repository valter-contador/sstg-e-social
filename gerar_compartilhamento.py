#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gerador de Imagens para Compartilhamento - SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1)"""

import io
import qrcode
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

def gerar_imagem_compartilhamento(empresa_nome: str, cnpj: str, app_url: str) -> io.BytesIO:
    """
    Gera imagem de compartilhamento com QR Code e informações da empresa

    Args:
        empresa_nome: Nome da empresa
        cnpj: CNPJ da empresa
        app_url: URL base da aplicação

    Returns:
        BytesIO: Imagem em formato PNG
    """

    # Dimensões
    largura, altura = 1200, 800
    padding = 50

    # Cores SSTG
    cor_navy = (40, 44, 91)          # #282C5B
    cor_verde = (90, 159, 98)        # #5A9F62
    cor_laranja = (220, 59, 36)      # #DC3B24
    cor_fundo = (239, 239, 239)      # #EFEFEF
    branco = (255, 255, 255)
    cinza_escuro = (100, 100, 100)

    # Criar imagem
    img = Image.new('RGB', (largura, altura), cor_fundo)
    draw = ImageDraw.Draw(img)

    # Desenhar retângulo de cabeçalho com gradiente (simulado com retângulo)
    draw.rectangle(
        [(0, 0), (largura, 200)],
        fill=cor_navy
    )

    # Tentar carregar fontes (fallback para default se não encontrar)
    try:
        fonte_titulo = ImageFont.truetype("arial.ttf", 48)
        fonte_subtitulo = ImageFont.truetype("arial.ttf", 32)
        fonte_normal = ImageFont.truetype("arial.ttf", 24)
        fonte_pequena = ImageFont.truetype("arial.ttf", 20)
    except:
        fonte_titulo = ImageFont.load_default()
        fonte_subtitulo = ImageFont.load_default()
        fonte_normal = ImageFont.load_default()
        fonte_pequena = ImageFont.load_default()

    # Título: "SSTG E-SOCIAL"
    titulo = "SSTG E-SOCIAL"
    bbox = draw.textbbox((0, 0), titulo, font=fonte_titulo)
    titulo_largura = bbox[2] - bbox[0]
    x_titulo = (largura - titulo_largura) // 2
    draw.text((x_titulo, 40), titulo, fill=branco, font=fonte_titulo)

    # Subtítulo: "Avaliação de Riscos Psicossociais"
    subtitulo = "Avaliação de Riscos Psicossociais"
    bbox = draw.textbbox((0, 0), subtitulo, font=fonte_subtitulo)
    sub_largura = bbox[2] - bbox[0]
    x_sub = (largura - sub_largura) // 2
    draw.text((x_sub, 100), subtitulo, fill=cor_verde, font=fonte_subtitulo)

    # Seção de conteúdo
    y_conteudo = 250

    # Nome da empresa
    texto_empresa = f"Empresa: {empresa_nome}"
    draw.text((padding, y_conteudo), texto_empresa, fill=cor_navy, font=fonte_normal)

    y_conteudo += 70

    # Informações
    info_text = "⏱️ ~10 minutos   🔒 100% Confidencial   ✓ Validado"
    draw.text((padding, y_conteudo), info_text, fill=cinza_escuro, font=fonte_pequena)

    y_conteudo += 80

    # Gerar QR Code
    link = f"{app_url}/?cnpj={cnpj}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=cor_navy, back_color=branco)
    qr_tamanho = 200
    qr_img = qr_img.resize((qr_tamanho, qr_tamanho), Image.Resampling.LANCZOS)

    # Posicionar QR Code à esquerda
    x_qr = padding + 50
    img.paste(qr_img, (x_qr, y_conteudo))

    # Link ao lado do QR Code
    x_link = x_qr + qr_tamanho + 60
    y_link = y_conteudo + 30

    draw.text((x_link, y_link), "Escaneie o código QR", fill=cor_navy, font=fonte_normal)
    y_link += 50
    draw.text((x_link, y_link), "ou acesse:", fill=cinza_escuro, font=fonte_pequena)

    # Link em formato reduzido (com cor destaque)
    y_link += 50
    link_display = link.replace('https://', '').replace('http://', '')
    if len(link_display) > 40:
        link_display = link_display[:37] + "..."
    draw.text((x_link, y_link), link_display, fill=cor_laranja, font=fonte_pequena)

    # Rodapé com call to action
    y_rodape = altura - 80
    draw.rectangle([(0, y_rodape), (largura, altura)], fill=cor_navy)

    cta = "Clique no QR Code ou acesse o link para participar da pesquisa"
    bbox = draw.textbbox((0, 0), cta, font=fonte_normal)
    cta_largura = bbox[2] - bbox[0]
    x_cta = (largura - cta_largura) // 2
    draw.text((x_cta, y_rodape + 15), cta, fill=branco, font=fonte_normal)

    # Converter para BytesIO
    img_io = io.BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)

    return img_io


def gerar_imagem_compartilhamento_simples(empresa_nome: str, cnpj: str, app_url: str) -> io.BytesIO:
    """
    Versão simplificada otimizada para Streamlit Cloud
    Gera imagem de compartilhamento com QR Code
    """

    # Dimensões
    largura, altura = 1000, 600

    # Cores SSTG
    cor_navy = (40, 44, 91)
    cor_verde = (90, 159, 98)
    branco = (255, 255, 255)
    cinza = (200, 200, 200)

    # Criar imagem
    img = Image.new('RGB', (largura, altura), branco)
    draw = ImageDraw.Draw(img)

    # Fundo colorido no topo
    draw.rectangle([(0, 0), (largura, 150)], fill=cor_navy)

    # Título
    titulo = "SSTG - DRPS Diagnóstico de Riscos Psicossociais (NR-1)"
    try:
        fonte_titulo = ImageFont.truetype("arial.ttf", 40)
    except:
        fonte_titulo = ImageFont.load_default()

    draw.text((50, 50), titulo, fill=branco, font=fonte_titulo)

    # Subtítulo
    subtitulo = "Avaliação de Riscos Psicossociais"
    try:
        fonte_sub = ImageFont.truetype("arial.ttf", 24)
    except:
        fonte_sub = ImageFont.load_default()

    draw.text((50, 200), subtitulo, fill=cor_navy, font=fonte_sub)
    draw.text((50, 240), f"Empresa: {empresa_nome}", fill=cor_verde, font=fonte_sub)

    # Gerar QR Code
    link = f"{app_url}/?cnpj={cnpj}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=2,
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=cor_navy, back_color=branco)
    qr_tamanho = 180
    qr_img = qr_img.resize((qr_tamanho, qr_tamanho), Image.Resampling.LANCZOS)

    # Colar QR Code
    x_qr = (largura - qr_tamanho) // 2
    img.paste(qr_img, (x_qr, 320))

    # Converter para BytesIO
    img_io = io.BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)

    return img_io
