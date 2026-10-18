# Quiz-18 — Juh Quiz

Versão do fluxo do Quiz-17 usando o layout visual criado no Canva.

## O que permanece do Quiz-17

- Voz masculina `pt-BR-AntonioNeural` em +10%.
- Pergunta narrada com o lápis sublinhando o texto.
- Contagem regressiva 3, 2, 1 com bipes.
- Resposta correta narrada e destacada com o cartão inteiro em verde, mantendo a alternativa legível.
- Um TXT para cada vídeo, com `CAPA_SEGUNDOS=2`.
- Vídeos e TXT como artefatos da execução do GitHub Actions.
- Envio ao Drive usando o segredo `RCLONE_DRIVE_TOKEN`, se estiver cadastrado neste repositório.

## Layout do Canva

O tema de cada vídeo aparece no cabeçalho, no lugar de “Conhecimentos Gerais”. As perguntas ocupam o cartão grande, e as três alternativas são colocadas nos campos A, B e C. O layout alterna entre cinco cores; a cada três vídeos, passa para a próxima paleta.

As imagens em raiz do repositório são as cinco bases do Canva, com o espaço do título limpo para o tema ser inserido pelo código. As imagens de cada pergunta são opcionais; coloque os arquivos em `imagens_perguntas/` e indique o nome em `dados_quiz.py`. Se uma imagem opcional não existir, o vídeo continua sem ela.

O workflow também gera três prévias visuais: duas perguntas com imagens extraídas das referências do Quiz-17 e a tela final com o placar `___ / 3`. Essas imagens são apenas para validar o layout; não são associadas às perguntas dos nove temas do Quiz-18.

## Gerar

1. Abra **Actions**.
2. Selecione **Gerar Juh Quiz - Canva**.
3. Clique em **Run workflow**.
4. Baixe o artefato `JUH-QUIZ-18` quando terminar.

O arquivo `dados_quiz.py` inclui 15 temas com três perguntas cada (45 no total). As ilustrações correspondentes ficam em `imagens_perguntas/`, em PNG com fundo transparente. Edite temas, perguntas, alternativas, resposta correta e legenda antes de gerar um novo lote. Cada tema pode ter até cinco perguntas; o índice de `correta` começa em zero.

Para ativar o envio ao Drive, cadastre neste repositório o segredo `RCLONE_DRIVE_TOKEN` usado no fluxo do Quiz-13/17. Sem ele, os arquivos continuam disponíveis no artefato do Actions.

