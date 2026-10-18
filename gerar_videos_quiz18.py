from pathlib import Path
import argparse
import asyncio
import math
import os
import re
import shutil
import subprocess
import unicodedata

from PIL import Image, ImageDraw, ImageFont

from dados_quiz import LEGENDAS, QUIZZES

W, H = 1080, 1920
FPS = 30
ANIM_FPS = 20
VOICE = "pt-BR-AntonioNeural"
VOICE_RATE = "+10%"
ASSETS = Path(".")
IMAGENS = Path("imagens_perguntas")
SAIDA = Path("output_quiz18")
DRIVE_BASE = "destino:saida/Juh-Quiz-18"
PALETTES = (
    ("verde_roxo", "quiz_verde_roxo.png", "resultado_verde_roxo.png", (105, 28, 207)),
    ("azul_ciano", "quiz_azul_ciano.png", "resultado_azul_ciano.png", (20, 62, 255)),
    ("petroleo_turquesa", "quiz_petroleo_turquesa.png", "resultado_petroleo_turquesa.png", (0, 112, 117)),
    ("laranja_amarelo", "quiz_laranja_amarelo.png", "resultado_laranja_amarelo.png", (246, 111, 0)),
    ("vinho_coral", "quiz_vinho_coral.png", "resultado_vinho_coral.png", (119, 17, 61)),
)
PRETO = (14, 14, 18)
BRANCO = (255, 255, 255)
VERDE_CORRETA = (40, 190, 85)
LETRAS = ("A", "B", "C")

def executar(cmd):
    print(" ".join(map(str, cmd)), flush=True)
    subprocess.run(cmd, check=True)

def slug(texto):
    s = unicodedata.normalize("NFKD", texto)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower() or "quiz"

def fonte(size, bold=False):
    paths = (
        ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
         "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"]
        if bold else
        ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
         "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"]
    )
    for path in paths:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def line_height(draw, font):
    b = draw.textbbox((0, 0), "Ag", font=font)
    return b[3] - b[1]

def wrap_text(draw, text, font, max_width):
    words = str(text).split()
    lines, current = [], ""
    for word in words:
        candidate = word if not current else current + " " + word
        box = draw.textbbox((0, 0), candidate, font=font)
        if box[2] - box[0] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def fit_lines(draw, text, max_width, max_height, max_size, min_size, max_lines):
    for size in range(max_size, min_size - 1, -2):
        font = fonte(size, bold=True)
        lines = wrap_text(draw, text, font, max_width)
        h = len(lines) * (line_height(draw, font) + 8)
        if len(lines) <= max_lines and h <= max_height:
            return font, lines
    font = fonte(min_size, bold=True)
    lines = wrap_text(draw, text, font, max_width)
    if len(lines) > max_lines:
        raise ValueError(f"Texto não cabe no layout sem cortes: {text}")
    return font, lines

def fundo_base(indice_tema):
    paleta = PALETTES[((indice_tema - 1) // 3) % len(PALETTES)]
    path = ASSETS / paleta[1]
    if not path.exists():
        raise FileNotFoundError(f"Template ausente: {path}")
    img = Image.open(path).convert("RGB")
    if img.size != (W, H):
        img = img.resize((W, H), Image.Resampling.LANCZOS)
    return img, paleta

def draw_centered_lines(draw, lines, font, center_x, y, fill, stroke_fill=None, stroke_width=0, gap=4):
    for line in lines:
        box = draw.textbbox((0, 0), line, font=font, stroke_width=stroke_width)
        width = box[2] - box[0]
        draw.text((center_x - width / 2, y), line, font=font, fill=fill,
                  stroke_width=stroke_width, stroke_fill=stroke_fill)
        y += line_height(draw, font) + gap
    return y

def desenhar_tema(img, tema, cor_tema):
    draw = ImageDraw.Draw(img)
    font, lines = fit_lines(draw, tema.upper(), 720, 145, 40, 24, 3)
    altura = len(lines) * (line_height(draw, font) + 5)
    y = max(10, 87 - altura / 2)
    draw_centered_lines(draw, lines, font, W // 2 + 150, int(y), BRANCO,
                        stroke_fill=(18, 18, 22), stroke_width=6, gap=4)

def resolver_imagem(pergunta):
    value = pergunta.get("imagem")
    if not value:
        return None
    path = Path(str(value).strip())
    candidates = [path]
    if not path.is_absolute() and path.parent == Path("."):
        candidates.append(IMAGENS / path)
    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate
    print(f"Imagem opcional não localizada; pergunta seguirá sem imagem: {value}", flush=True)
    return None

def desenhar_pergunta(indice_tema, tema, numero, pergunta):
    img, palette = fundo_base(indice_tema)
    cor_tema = palette[3]
    desenhar_tema(img, tema, cor_tema)
    draw = ImageDraw.Draw(img)

    # Cartão grande de pergunta (o cartão branco já vem do modelo Canva).
    qx1, qx2 = 66, 1014
    qtop, qbottom = 365, 930
    imagem_path = resolver_imagem(pergunta)
    question_max_height = 230 if imagem_path else 440
    qfont, qlines = fit_lines(draw, pergunta["pergunta"], qx2 - qx1 - 70,
                              question_max_height, 54 if imagem_path else 62, 30, 5)
    qline = line_height(draw, qfont) + 10
    total_qh = len(qlines) * qline
    qy = qtop + (question_max_height - total_qh) // 2
    underlines = []
    for line in qlines:
        box = draw.textbbox((0, 0), line, font=qfont)
        x = W // 2 - (box[2] - box[0]) / 2
        draw.text((x, qy), line, font=qfont, fill=PRETO)
        underline_y = qy + line_height(draw, qfont) + 8
        underlines.append((int(x), int(underline_y), int(x + box[2] - box[0]), int(underline_y)))
        qy += qline

    if imagem_path:
        figure = Image.open(imagem_path).convert("RGBA")
        figure.thumbnail((650, 300), Image.Resampling.LANCZOS)
        px = (W - figure.width) // 2
        py = min(qtop + 250, qbottom - figure.height - 18)
        img.paste(figure, (px, py), figure)

    # Alternativas nos três campos A/B/C do modelo; cada texto quebra em até 2 linhas.
    options = []
    rows = [(990, 1160), (1200, 1380), (1420, 1600)]
    for idx, alt in enumerate(pergunta["alternativas"]):
        top, bottom = rows[idx]
        text = str(alt)
        max_width = 690
        font, lines = fit_lines(draw, text, max_width, bottom - top - 28, 47, 28, 2)
        text_h = len(lines) * (line_height(draw, font) + 5)
        y = top + (bottom - top - text_h) // 2 - 2
        draw_centered_lines(draw, lines, font, 660, y, PRETO, gap=5)
        options.append({
            "row": (77, top, 1005, bottom),
            "index": idx,
            "lines": lines,
            "font": font,
            "text_y": y,
        })
    return img, underlines, options

def aplicar_sublinhado(img, strokes, progresso, color):
    if not strokes:
        return img, (W // 2, 360)
    progreso = max(0.0, min(1.0, progresso))
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    n = len(strokes)
    tip = (strokes[0][0], strokes[0][1])
    for i, (x1, y1, x2, _) in enumerate(strokes):
        start, end = i / n, (i + 1) / n
        if progresso <= start:
            break
        local = 1.0 if progresso >= end else (progresso - start) / (end - start)
        x = x1 + int((x2 - x1) * local)
        d.line([(x1, y1), (x, y1)], fill=color + (190,), width=8)
        tip = (x, y1)
        if local < 1.0:
            break
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB"), tip

def desenhar_lapis(img, x, y):
    pencil = Image.new("RGBA", (150, 45), (0, 0, 0, 0))
    d = ImageDraw.Draw(pencil)
    d.rounded_rectangle([18, 12, 126, 33], radius=5, fill=(255, 205, 35, 255))
    d.rectangle([108, 12, 122, 33], fill=(229, 70, 120, 255))
    d.rounded_rectangle([122, 12, 143, 33], radius=5, fill=(245, 115, 150, 255))
    d.polygon([(18, 12), (18, 33), (0, 22)], fill=(230, 190, 130, 255))
    pencil = pencil.rotate(-8, expand=True, resample=Image.Resampling.BICUBIC)
    out = img.convert("RGBA")
    out.alpha_composite(pencil, (int(x), int(y)))
    return out.convert("RGB")

def pintar_resposta(img, option, progresso):
    x1, y1, x2, y2 = option["row"]
    progresso = max(0.0, min(1.0, progresso))
    out = img.convert("RGBA")
    overlay = Image.new("RGBA", out.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)

    # Preenche todo o cartão correto, mantendo o texto preto e o marcador A/B/C.
    verde = (70, 211, 91)
    d.rounded_rectangle(
        [x1, y1, x2, y2], radius=50,
        fill=verde + (int(255 * progresso),),
        outline=(20, 130, 55, int(255 * progresso)),
        width=max(2, int(6 * progresso)),
    )
    out = Image.alpha_composite(out, overlay)
    d = ImageDraw.Draw(out)

    cx, cy, radius = 164, (y1 + y2) // 2, 78
    d.ellipse(
        [cx - radius, cy - radius, cx + radius, cy + radius],
        fill=(248, 0, 65), outline=BRANCO, width=8,
    )
    badge_font = fonte(88, bold=True)
    letter = LETRAS[option["index"]]
    box = d.textbbox((0, 0), letter, font=badge_font, stroke_width=1)
    d.text(
        (cx - (box[2] - box[0]) / 2, cy - (box[3] - box[1]) / 2 - 8),
        letter, font=badge_font, fill=BRANCO, stroke_width=1,
        stroke_fill=(200, 0, 45),
    )
    draw_centered_lines(
        d, option["lines"], option["font"], 660, option["text_y"],
        PRETO, gap=5,
    )
    return out.convert("RGB")


def desenhar_tela_final(indice_tema, tema):
    paleta = PALETTES[((indice_tema - 1) // 3) % len(PALETTES)]
    path = ASSETS / paleta[2]
    if not path.exists():
        raise FileNotFoundError(f"Template de resultado ausente: {path}")
    final_img = Image.open(path).convert("RGB")
    if final_img.size != (W, H):
        final_img = final_img.resize((W, H), Image.Resampling.LANCZOS)

    # Os modelos de resultado trazem "Conhecimentos Gerais" impresso no cabeçalho.
    # Limpa apenas a faixa do título e escreve nela o tema deste quiz.
    draw = ImageDraw.Draw(final_img)
    mascot_left = final_img.crop((0, 0, 215, 205))
    mascot_part = final_img.crop((0, 130, 245, 205))
    for y in range(175):
        draw.line((0, y, W, y), fill=final_img.getpixel((W - 5, y)))
    final_img.paste(mascot_left, (0, 0))
    final_img.paste(mascot_part, (0, 130))
    desenhar_tema(final_img, tema, paleta[3])
    d = ImageDraw.Draw(final_img)
    return final_img, paleta

def desenhar_contagem(img, numero):
    out = img.copy()
    d = ImageDraw.Draw(out)
    cx, cy, r = W // 2, 1700, 72
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=BRANCO, outline=(22, 22, 22), width=6)
    f = fonte(74, bold=True)
    text = str(numero)
    b = d.textbbox((0, 0), text, font=f)
    d.text((cx - (b[2]-b[0])/2, cy - (b[3]-b[1])/2 - 7),
           text, font=f, fill=(20, 20, 25))
    return out

def criar_beep(path, dur=0.20, freq=880):
    executar(["ffmpeg", "-y", "-f", "lavfi", "-i",
              f"sine=frequency={freq}:sample_rate=48000:duration={dur}",
              "-ar", "48000", "-ac", "2", "-c:a", "libmp3lame", "-q:a", "4", str(path)])

async def _tts(texto, saida):
    import edge_tts
    await edge_tts.Communicate(texto, VOICE, rate=VOICE_RATE).save(str(saida))

def tts_salvar(texto, saida):
    saida.parent.mkdir(parents=True, exist_ok=True)
    asyncio.run(_tts(texto, saida))

def duracao_audio(path):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                             "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
                            capture_output=True, text=True, check=True)
    return float(result.stdout.strip())

def criar_clipe_imagem(img_path, duracao, out_path, audio_path=None):
    cmd = ["ffmpeg", "-y", "-loop", "1", "-i", str(img_path)]
    if audio_path:
        cmd += ["-i", str(audio_path)]
    else:
        cmd += ["-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000"]
    cmd += ["-t", f"{duracao:.3f}", "-vf", f"scale={W}:{H},fps={FPS}",
            "-c:v", "libx264", "-pix_fmt", "yuv420p"]
    if audio_path:
        cmd += ["-af", "apad,aresample=48000", "-ar", "48000", "-ac", "2",
                "-c:a", "aac", "-b:a", "192k"]
    else:
        cmd += ["-ar", "48000", "-ac", "2", "-c:a", "aac", "-b:a", "128k"]
    executar(cmd + [str(out_path)])

def criar_clipe_animado(frames_dir, duracao, out_path, audio_path=None):
    cmd = ["ffmpeg", "-y", "-framerate", str(ANIM_FPS), "-i", str(frames_dir / "frame_%04d.jpg")]
    if audio_path:
        cmd += ["-i", str(audio_path)]
    else:
        cmd += ["-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000"]
    cmd += ["-t", f"{duracao:.3f}", "-vf", f"scale={W}:{H},fps={FPS}",
            "-c:v", "libx264", "-pix_fmt", "yuv420p"]
    if audio_path:
        cmd += ["-af", "apad,aresample=48000", "-ar", "48000", "-ac", "2",
                "-c:a", "aac", "-b:a", "192k"]
    else:
        cmd += ["-ar", "48000", "-ac", "2", "-c:a", "aac", "-b:a", "128k"]
    executar(cmd + [str(out_path)])

def concatenar(clipes, saida):
    lista = saida.parent / "concat.txt"
    with lista.open("w", encoding="utf-8") as f:
        for clip in clipes:
            f.write("file '" + str(clip.resolve()) + "'\n")
    executar(["ffmpeg", "-y", "-fflags", "+genpts", "-f", "concat", "-safe", "0",
              "-i", str(lista), "-c:v", "copy", "-c:a", "aac", "-ar", "48000", "-ac", "2",
              "-b:a", "192k", "-movflags", "+faststart", str(saida)])

def criar_transicao(anterior, proxima, pasta, numero):
    frames = pasta / f"frames_scroll_{numero:02d}"
    frames.mkdir(parents=True, exist_ok=True)
    total = 18
    for i in range(total):
        desloc = int(H * i / (total - 1))
        frame = Image.new("RGB", (W, H), BRANCO)
        frame.paste(anterior.crop((0, desloc, W, H)), (0, 0))
        frame.paste(proxima.crop((0, 0, W, desloc)), (0, H - desloc))
        frame.save(frames / f"frame_{i:04d}.jpg", quality=92)
    clip = pasta / f"{numero:02d}_rolagem.mp4"
    criar_clipe_animado(frames, total / ANIM_FPS, clip)
    return clip

def gerar_video_tema(indice_tema, tema, perguntas, legenda, lote_drive=None):
    paleta = PALETTES[((indice_tema - 1) // 3) % len(PALETTES)]
    print(f"Cor do modelo: {paleta[0]}", flush=True)
    pasta = SAIDA / f"{indice_tema:02d}_{slug(tema)}"
    if pasta.exists():
        shutil.rmtree(pasta)
    pasta.mkdir(parents=True, exist_ok=True)
    clipes, tela_anterior = [], None
    beep = pasta / "beep.mp3"
    criar_beep(beep)

    for q_idx, pergunta in enumerate(perguntas, start=1):
        base, strokes, options = desenhar_pergunta(indice_tema, tema, q_idx, pergunta)
        if tela_anterior is not None:
            clipes.append(criar_transicao(tela_anterior, base, pasta, q_idx))

        audio_q = pasta / f"q{q_idx:02d}_pergunta.mp3"
        tts_salvar(pergunta["pergunta"], audio_q)
        qdur = duracao_audio(audio_q) + 0.75
        frames_q = pasta / f"frames_q{q_idx:02d}"
        frames_q.mkdir(parents=True, exist_ok=True)
        total = max(18, int(math.ceil(qdur * ANIM_FPS)))
        for fidx in range(total):
            progress = fidx / max(1, total - 1)
            frame, (tip_x, tip_y) = aplicar_sublinhado(base.copy(), strokes, progress, paleta[3])
            frame = desenhar_lapis(frame, tip_x - 18, tip_y - 34)
            frame.save(frames_q / f"frame_{fidx:04d}.jpg", quality=92)
        clip_q = pasta / f"{q_idx:02d}_pergunta.mp4"
        criar_clipe_animado(frames_q, qdur, clip_q, audio_q)
        clipes.append(clip_q)
        marcada, _ = aplicar_sublinhado(base.copy(), strokes, 1.0, paleta[3])

        for numero in (3, 2, 1):
            png = pasta / f"q{q_idx:02d}_count_{numero}.png"
            desenhar_contagem(marcada, numero).save(png)
            clip = pasta / f"{q_idx:02d}_count_{numero}.mp4"
            criar_clipe_imagem(png, 0.78, clip, beep)
            clipes.append(clip)

        correta = int(pergunta["correta"])
        resposta = pergunta["alternativas"][correta]
        audio_a = pasta / f"q{q_idx:02d}_resposta.mp3"
        tts_salvar(f"A resposta correta é: {resposta}.", audio_a)
        adur = duracao_audio(audio_a) + 0.70
        frames_a = pasta / f"frames_a{q_idx:02d}"
        frames_a.mkdir(parents=True, exist_ok=True)
        total_a = max(14, int(math.ceil(adur * ANIM_FPS)))
        for fidx in range(total_a):
            p = fidx / max(1, total_a - 1)
            answer_frame = pintar_resposta(marcada.copy(), options[correta], min(1.0, p * 2.4))
            answer_frame.save(frames_a / f"frame_{fidx:04d}.jpg", quality=92)
        clip_a = pasta / f"{q_idx:02d}_resposta.mp4"
        criar_clipe_animado(frames_a, adur, clip_a, audio_a)
        clipes.append(clip_a)
        tela_anterior = pintar_resposta(marcada.copy(), options[correta], 1.0)

    final_img, paleta = desenhar_tela_final(indice_tema, tema)
    final_png = pasta / "final.png"
    final_img.save(final_png)
    final_clip = pasta / "99_final.mp4"
    
    final_audio = pasta / "99_final.mp3"
    tts_salvar("Quantas você acertou?", final_audio)
    final_duration = max(2.2, duracao_audio(final_audio) + 0.35)
    criar_clipe_imagem(final_png, final_duration, final_clip, final_audio)
    clipes.append(final_clip)

    saida = SAIDA / f"{indice_tema:02d}_{slug(tema)}.mp4"
    concatenar(clipes, saida)
    arquivo_legenda = saida.with_suffix(".txt")
    arquivo_legenda.write_text(f"CAPA_SEGUNDOS=2\n\n{legenda.strip()}\n", encoding="utf-8")
    print(f"Gerado: {saida}", flush=True)

    token = os.getenv("RCLONE_CONFIG_DESTINO_TOKEN", "").strip()
    if lote_drive is not None and token:
        for arquivo in (saida, arquivo_legenda):
            executar(["rclone", "copyto", str(arquivo),
                      f"{DRIVE_BASE}/execucao-{lote_drive}/{arquivo.name}"])
    elif lote_drive is not None:
        print("RCLONE_DRIVE_TOKEN ausente; MP4/TXT ficam no artefato do GitHub.", flush=True)

def main():
    parser = argparse.ArgumentParser(description="Gera vídeos Juh Quiz com layout Canva.")
    parser.add_argument("--enviar-drive", action="store_true")
    parser.add_argument("--lote", default=None)
    args = parser.parse_args()
    lote = (args.lote or "manual") if args.enviar_drive else None
    if not QUIZZES:
        raise RuntimeError("O dicionário QUIZZES está vazio.")
    SAIDA.mkdir(parents=True, exist_ok=True)
    for indice, (tema, perguntas) in enumerate(QUIZZES.items(), start=1):
        if not perguntas:
            continue
        if len(perguntas) > 5:
            raise ValueError(f'O tema "{tema}" passou do limite de 5 perguntas.')
        for pergunta in perguntas:
            if len(pergunta.get("alternativas", [])) != 3:
                raise ValueError(f'O tema "{tema}" precisa ter exatamente 3 alternativas por pergunta.')
            if int(pergunta.get("correta", -1)) not in (0, 1, 2):
                raise ValueError(f'O tema "{tema}" possui índice "correta" inválido.')
        legenda = LEGENDAS.get(tema, "").strip()
        if not legenda:
            raise ValueError(f'Não há legenda cadastrada para o tema "{tema}".')
        gerar_video_tema(indice, tema, perguntas, legenda, lote)
    print("Todos os vídeos foram gerados.", flush=True)

if __name__ == "__main__":
    main()

