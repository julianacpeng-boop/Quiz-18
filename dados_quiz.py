# Juh Quiz 18 — 15 temas, 45 perguntas, três perguntas por vídeo.
# Cada item imagem aponta para um PNG transparente incluído no pacote.

QUIZZES = {
    "Dinossauros e fósseis": [
        {"pergunta": "O que os fósseis ajudam os cientistas a conhecer?", "alternativas": ["A vida de épocas antigas", "A previsão do tempo de amanhã", "A composição atual do ar"], "correta": 0, "imagem": "q18_20261027_t01_p01.png"},
        {"pergunta": "Como se chama a ciência que estuda os fósseis?", "alternativas": ["Astronomia", "Paleontologia", "Oceanografia"], "correta": 1, "imagem": "q18_20261027_t01_p02.png"},
        {"pergunta": "O que pode ser considerado um fóssil?", "alternativas": ["Uma marca ou resto preservado de um ser vivo antigo", "Uma rocha derretida recém-formada", "Uma planta que ainda está crescendo"], "correta": 0, "imagem": "q18_20261027_t01_p03.png"},
    ],
    "Plantas: sementes e germinação": [
        {"pergunta": "Durante a germinação, qual parte costuma surgir primeiro da semente?", "alternativas": ["A flor", "A raiz", "O fruto"], "correta": 1, "imagem": "q18_20261027_t02_p01.png"},
        {"pergunta": "Qual parte da planta absorve água do solo?", "alternativas": ["As raízes", "As pétalas", "Os frutos"], "correta": 0, "imagem": "q18_20261027_t02_p02.png"},
        {"pergunta": "Qual elemento é essencial para a planta realizar a fotossíntese?", "alternativas": ["Areia", "Sal", "Luz"], "correta": 2, "imagem": "q18_20261027_t02_p03.png"},
    ],
    "Alimentação saudável e nutrientes": [
        {"pergunta": "Qual grupo de nutrientes é uma importante fonte de energia para o corpo?", "alternativas": ["Carboidratos", "Vitaminas", "Água"], "correta": 0, "imagem": "q18_20261027_t03_p01.png"},
        {"pergunta": "Qual nutriente ajuda na construção e reparação dos tecidos do corpo?", "alternativas": ["Proteínas", "Fibras", "Água"], "correta": 0, "imagem": "q18_20261027_t03_p02.png"},
        {"pergunta": "Por que é importante incluir frutas e verduras variadas na alimentação?", "alternativas": ["Porque fornecem fibras e diferentes nutrientes", "Porque substituem a necessidade de beber água", "Porque todas têm exatamente os mesmos nutrientes"], "correta": 0, "imagem": "q18_20261027_t03_p03.png"},
    ],
    "Música e instrumentos musicais": [
        {"pergunta": "Qual instrumento produz som principalmente pela vibração de cordas?", "alternativas": ["Tambor", "Violino", "Flauta"], "correta": 1, "imagem": "q18_20261027_t04_p01.png"},
        {"pergunta": "Na música, o que o andamento indica?", "alternativas": ["A velocidade da música", "O tamanho do palco", "A cor dos instrumentos"], "correta": 0, "imagem": "q18_20261027_t04_p02.png"},
        {"pergunta": "Como se chama um grupo de músicos que toca junto?", "alternativas": ["Orquestra", "Plateia", "Biblioteca"], "correta": 0, "imagem": "q18_20261027_t04_p03.png"},
    ],
    "Segurança no trânsito": [
        {"pergunta": "O que uma pessoa deve fazer antes de atravessar uma rua?", "alternativas": ["Olhar para os dois lados e verificar se é seguro", "Correr sem observar o movimento", "Atravessar olhando para o celular"], "correta": 0, "imagem": "q18_20261027_t05_p01.png"},
        {"pergunta": "Se houver uma ciclovia disponível, por onde o ciclista deve circular?", "alternativas": ["Pela ciclovia", "Pelo meio da calçada", "Entre os carros parados"], "correta": 0, "imagem": "q18_20261027_t05_p02.png"},
        {"pergunta": "Por que usar itens refletivos à noite pode ajudar um ciclista?", "alternativas": ["Para ser visto com mais facilidade", "Para aumentar a velocidade da bicicleta", "Para iluminar o caminho sem farol"], "correta": 0, "imagem": "q18_20261027_t05_p03.png"},
    ],
    "Biomas brasileiros": [
        {"pergunta": "O que caracteriza um bioma?", "alternativas": ["Uma região com clima, plantas e animais relacionados", "Um tipo único de animal", "Uma área formada somente por cidades"], "correta": 0, "imagem": "q18_20261027_t06_p01.png"},
        {"pergunta": "Qual fator influencia fortemente os tipos de vegetação de um bioma?", "alternativas": ["O clima da região", "A cor das casas", "O idioma falado"], "correta": 0, "imagem": "q18_20261027_t06_p02.png"},
        {"pergunta": "Como os seres vivos de um bioma costumam se relacionar com o ambiente?", "alternativas": ["Possuem características que ajudam a viver nas condições locais", "Vivem sem depender de água ou alimento", "São todos da mesma espécie"], "correta": 0, "imagem": "q18_20261027_t06_p03.png"},
    ],
    "Profissões e ferramentas": [
        {"pergunta": "Qual profissional planeja projetos de edifícios e outros espaços?", "alternativas": ["Arquiteto", "Padeiro", "Músico"], "correta": 0, "imagem": "q18_20261027_t07_p01.png"},
        {"pergunta": "Qual profissional cuida da saúde dos animais?", "alternativas": ["Veterinário", "Jardineiro", "Piloto"], "correta": 0, "imagem": "q18_20261027_t07_p02.png"},
        {"pergunta": "Qual ferramenta ajuda um marceneiro a conferir o comprimento de uma peça?", "alternativas": ["Trena", "Pincel", "Concha"], "correta": 0, "imagem": "q18_20261027_t07_p03.png"},
    ],
    "Rochas, minerais e vulcões": [
        {"pergunta": "Como se chama a rocha formada pelo resfriamento do magma ou da lava?", "alternativas": ["Ígnea", "Sedimentar", "Metamórfica"], "correta": 0, "imagem": "q18_20261027_t08_p01.png"},
        {"pergunta": "Onde o magma fica antes de alcançar a superfície?", "alternativas": ["No interior da Terra", "No alto das nuvens", "No fundo dos rios"], "correta": 0, "imagem": "q18_20261027_t08_p02.png"},
        {"pergunta": "Como muitas rochas sedimentares se formam?", "alternativas": ["Pelo acúmulo e compactação de sedimentos", "Pelo congelamento do ar", "Pelo crescimento de folhas"], "correta": 0, "imagem": "q18_20261027_t08_p03.png"},
    ],
    "Patrimônios históricos do Brasil": [
        {"pergunta": "Por que um prédio antigo pode ser considerado patrimônio histórico?", "alternativas": ["Porque ajuda a contar a história e os modos de vida de uma época", "Porque é sempre o prédio mais alto da cidade", "Porque precisa ser usado como moradia"], "correta": 0, "imagem": "q18_20261027_t09_p01.png"},
        {"pergunta": "O que a preservação de um bem histórico busca proteger?", "alternativas": ["Sua importância cultural e histórica", "Somente sua pintura externa", "Apenas o terreno ao redor"], "correta": 0, "imagem": "q18_20261027_t09_p02.png"},
        {"pergunta": "O que objetos preservados em um museu podem revelar?", "alternativas": ["Como as pessoas viviam e trabalhavam no passado", "A previsão exata do tempo futuro", "A idade de todas as pessoas atuais"], "correta": 0, "imagem": "q18_20261027_t09_p03.png"},
    ],
    "Culinária regional brasileira": [
        {"pergunta": "Acarajé é um prato tradicional especialmente associado a qual estado?", "alternativas": ["Bahia", "Paraná", "Acre"], "correta": 0, "imagem": "q18_20261027_t10_p01.png"},
        {"pergunta": "Qual ingrediente é a base do cuscuz nordestino tradicional?", "alternativas": ["Milho", "Maçã", "Cacau"], "correta": 0, "imagem": "q18_20261027_t10_p02.png"},
        {"pergunta": "Qual ingrediente dá nome ao pão de queijo?", "alternativas": ["Queijo", "Chocolate", "Peixe"], "correta": 0, "imagem": "q18_20261027_t10_p03.png"},
    ],
    "Materiais do cotidiano e suas propriedades": [
        {"pergunta": "Por que o cobre é usado em muitos fios elétricos?", "alternativas": ["Porque conduz bem a eletricidade", "Porque é feito de madeira", "Porque não pode ser dobrado"], "correta": 0, "imagem": "q18_20261027_t11_p01.png"},
        {"pergunta": "Que propriedade permite que um elástico estique e depois volte à forma?", "alternativas": ["Elasticidade", "Transparência", "Fragilidade"], "correta": 0, "imagem": "q18_20261027_t11_p02.png"},
        {"pergunta": "O que pode acontecer com muitos metais expostos por muito tempo à água e ao oxigênio?", "alternativas": ["Podem sofrer corrosão", "Podem virar tecido", "Podem se transformar em vidro"], "correta": 0, "imagem": "q18_20261027_t11_p03.png"},
    ],
    "Som, eco e acústica": [
        {"pergunta": "O que normalmente precisa acontecer para um som ser produzido?", "alternativas": ["Algo precisa vibrar", "A luz precisa apagar", "O ar precisa ficar imóvel"], "correta": 0, "imagem": "q18_20261027_t12_p01.png"},
        {"pergunta": "Como um eco costuma se formar?", "alternativas": ["Quando o som reflete em uma superfície e retorna", "Quando a luz muda de cor", "Quando o vento para de soprar"], "correta": 0, "imagem": "q18_20261027_t12_p02.png"},
        {"pergunta": "Por que algumas salas de espetáculo usam painéis acústicos?", "alternativas": ["Para controlar reflexões e reverberação do som", "Para aumentar a quantidade de luz solar", "Para deixar o piso mais macio"], "correta": 0, "imagem": "q18_20261027_t12_p03.png"},
    ],
    "Jogos olímpicos e modalidades": [
        {"pergunta": "De quantos em quantos anos acontecem os Jogos Olímpicos de verão?", "alternativas": ["A cada quatro anos", "Todos os meses", "A cada dez anos"], "correta": 0, "imagem": "q18_20261027_t13_p01.png"},
        {"pergunta": "Qual modalidade é disputada com raquete e peteca?", "alternativas": ["Badminton", "Natação", "Judô"], "correta": 0, "imagem": "q18_20261027_t13_p02.png"},
        {"pergunta": "O que os corredores passam de mão em mão em uma prova de revezamento?", "alternativas": ["Um bastão", "Uma bola de futebol", "Uma bandeira de chegada"], "correta": 0, "imagem": "q18_20261027_t13_p03.png"},
    ],
    "Sinais, símbolos e códigos": [
        {"pergunta": "O que é um pictograma?", "alternativas": ["Um desenho simples que transmite uma informação", "Uma ferramenta para medir temperatura", "Um tipo de rocha vulcânica"], "correta": 0, "imagem": "q18_20261027_t14_p01.png"},
        {"pergunta": "Que elementos são combinados no código Morse?", "alternativas": ["Pontos e traços", "Círculos e quadrados coloridos", "Notas musicais e pausas"], "correta": 0, "imagem": "q18_20261027_t14_p02.png"},
        {"pergunta": "Para que serve a legenda de um mapa?", "alternativas": ["Explicar o significado de símbolos e cores", "Mostrar a idade de quem desenhou o mapa", "Indicar o preço dos lugares"], "correta": 0, "imagem": "q18_20261027_t14_p03.png"},
    ],
    "Construções e arquitetura": [
        {"pergunta": "O que uma planta de construção representa?", "alternativas": ["A organização planejada dos espaços", "A previsão do clima no bairro", "A lista de moradores do prédio"], "correta": 0, "imagem": "q18_20261027_t15_p01.png"},
        {"pergunta": "Qual é uma função importante da fundação de um edifício?", "alternativas": ["Ajudar a sustentar a construção e transferir seu peso ao solo", "Decorar o telhado com desenhos", "Levar água diretamente às janelas"], "correta": 0, "imagem": "q18_20261027_t15_p02.png"},
        {"pergunta": "Como se chama a face externa principal de um edifício?", "alternativas": ["Fachada", "Escada", "Fundação"], "correta": 0, "imagem": "q18_20261027_t15_p03.png"},
    ],
}

# Uma legenda por vídeo, com no máximo quatro hashtags em cada uma.
LEGENDAS = {
    tema: f"Vamos aprender com três perguntas sobre {tema.lower()}!\n#JuhQuiz #Aprendizado #Curiosidades #Quiz"
    for tema in QUIZZES
}

# Distribui a posição da resposta correta entre A, B e C sem mudar o conteúdo.
_posicao_desejada = 0
for _perguntas in QUIZZES.values():
    for _item in _perguntas:
        _resposta = _item["alternativas"][_item["correta"]]
        _distratores = [a for i, a in enumerate(_item["alternativas"]) if i != _item["correta"]]
        _destino = _posicao_desejada % 3
        _distratores.insert(_destino, _resposta)
        _item["alternativas"] = _distratores
        _item["correta"] = _destino
        _posicao_desejada += 1
