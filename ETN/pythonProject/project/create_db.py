import sqlite3
import os

def create_db():
    # Caminho absoluto para o banco de dados
    db_path = os.path.join(os.path.dirname(__file__), 'quiz.db')
    print(f"Criando banco de dados em: {db_path}")

    # Conectar ao banco de dados
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Criar tabelas
    c.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            image TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER,
            option_text TEXT NOT NULL,
            option_label TEXT NOT NULL,
            FOREIGN KEY (question_id) REFERENCES questions (id)
        )
    ''')

    # Inserir perguntas e opções
    print("Inserindo perguntas...")

    questions = [
        {
            "question_text": "Na falta da etiqueta Wi-Fi (usuário e senha do EMTA) o que deve ser realizado?",
            "options": [
                ("Anotar a numeração do SSID e SENHA em qualquer local da OS.", "A"),
                ("Deixar o seu número de telefone para o cliente te ligar quando necessário.", "D"),
                ("É obrigatório o preenchimento das informações SSID e SENHA no campo observação da OS.", "B"),
                ("Pedir para que o cliente entre em contato com a central de atendimento.", "C")
            ],
            "correct_answer": "B",
            "image": None
        },
        {
            "question_text": "Conforme procedimento de Baixa na URA, para o MAC 0023754F1608, é necessário digitar para o caractere hexadecimal ( F ) :",
            "options": [
                ("*6", "A"),
                ("*06", "B"),
                ("6", "C"),
                ("#6", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {
            "question_text": "Qual o procedimento correto para realizar a validação de retorno? ",
            "options": [
                ("Canal 262 + 8291 + Preenchimento do numero da OS e Contrato", "A"),
                ("Canal 262 + Menu +8291 Preenchimento do numero da OS e Contrato", "B"),
                ("Canal 262 + Tecla Azul + 8291 + Preenchimento do numero da OS e Contrato.", "C"),
                ("Canal 262 + Menu + Tecla Azul + 8291 + Preenchimento do número da OS e Contrato", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {
            "question_text": " O que é AUTO HIT?",
            "options": [
                ("Funcionalidade que permite o envio automático de HIT pelo controle remoto em equipamentos SD, HD e HDMAX.", "A"),
                ("Funcionalidade que permite o envio automático de HIT pelo controle remoto em equipamentos HD e HDMAX", "B"),
                ("Funcionalidade que permite o reset do decodificador e suas configurações através do controle remoto.", "C"),
                ("Todas as alternativas estão corretas", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {
            "question_text": "Dos padrões de redes Wi-Fi abaixo, qual nos proporciona a maior velocidade da taxa de transmissão?",
            "options": [
                ("a", "A"),
                ("g", "B"),
                ("n", "C"),
                ("ac", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {
            "question_text": "Sobre a facilidade CONFIGURAÇÃO SENHA WI FI:",
            "options": [
                ("Com essa nova facilidade nosso cliente conseguiu Consultar, trocar a senha e nome da rede WI-FI de sua casa apenas através do site, ainda não está disponível pelo NETAPP.", "A"),
                ("n.d.a", "B"),
                ("Consultar, trocar a senha e nome da rede WI-FI de sua casa através do NET APP e também pelo site MINHA NET", "C"),
                ("Consultar, trocar a senha e nome da rede WI-FI de sua casa atraves do NET APP, ainda não está disponível pelo site MINHA NET.", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {
            "question_text": "O recurso Facebook presente em nossos decodificadores com tecnologia HD NG, permite ao nosso cliente:",
            "options": [
                ("Postar/compartilhar com seus amigos em sua timeline no Facebook, o que está assistindo em sua NET HDTV, direto de seu decodificador", "A"),
                ("Espelhar a tela do Facebook de seu Smartphone ou tablet direto para sua TV.", "B"),
                ("Navegar no Facebook, postar fotos e vídeos direto de sua TV.", "C"),
                ("Todas as alternativas acima", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {
            "question_text": "O que é Valida Retorno?",
            "options": [
                ("Verificação da comunicação do televisor para que o cliente possa usufruir de todos os recursos do sistema NET TV como Full HD e 4K", "A"),
                ("Validação dos dados de instalação e confirmação do pacote instalado para que o cliente possa usufruir de todos os recursos do sistema NETTV", "B"),
                ("Verificação da comunicação do Decoder Digital para que o cliente possa usufruir de todos os recursos do sistema NET TV como compra pelo controle remoto e NOW (vídeo on Demand)", "C"),
                ("Pacote que dá direito ao cliente acessar via site, da NET os últimos lançamentos dos canais Telecine", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {
            "question_text": "Qual alternativa corresponde aos problemas causados ao cliente caso ele não seja orientado sobre o uso de senhas?",
            "options": [
                ("Compra de conteúdos do NOW sem os seu conhecimento", "A"),
                ("Ligações na central para solicitar estorno de valores referente a compras", "B"),
                ("Reclamações nos órgãos de defesa ao consumidor", "C"),
                ("Todas as alternativas estão corretas", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {
            "question_text": "São características da fibra óptica.",
            "options": [
                ("Alta atenuação", "A"),
                ("Necessidade de amplificação a cada 2Km", "B"),
                ("Maior sensibilidade a interferências eletromagnéticas", "C"),
                ("Nenhuma das alternativas", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {
            "question_text": "Qual é a impedância  de um cabo coaxial utilizado em CATV?",
            "options": [
                ("75 ohms", "A"),
                ("50 ohms", "B"),
                ("22 ohms", "C"),
                ("15 ohms", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {
            "question_text": "É considerada interferência na rede HFC",
            "options": [
                ("Tenção AC gerada  pela fonte acima do regulamento pela ANATEL", "A"),
                ("Sinal de UHF invadindo a faixa de CATV", "B"),
                ("Nível alto de   entrada no amplificador, gerando saturação na imagem", "C"),
                ("Nível de potência  óptica muito alta no receptor óptico, gerando saturação do link", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {
            "question_text": "Dentro do cabo coaxial as frequências sofrem a mesma  atenuação?",
            "options": [
                ("Sim,   tanto as mais altas como as mais baixas possuem atenuação igual", "A"),
                ("Não, as  frequências  mais baixas sofrem maior atenuação", "B"),
                ("Não,   as  frequências  mais altas sofrem maior  atenuação", "C"),
                ("N.d.a", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {
            "question_text": "O que é tilt ?",
            "options": [
                ("Nível de sinal   de portadoras distintas", "A"),
                ("Nível   de sinal   do canal de retorno", "B"),
                ("Diferença entre frequências do canal direto e do canal de   retorno", "C"),
                (" Diferença de   sinal entre portadoras  distintas", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {#15
            "question_text": "Qual a função do cable isolator?",
            "options": [
                ("Proteger a instalação e os equipamentos da rede da   NET  contra picos de tensão de (AC)", "A"),
                ("Proteger a rede de cabos em caso de retorno de ac gerado ,   pelo decodificador", "B"),
                ("Isolador com   casamento de  impedância para adaptar   a conexão dos   cabos   drop  com   o   de   distribuição interna", "C"),
                ("Apenas fazer   emenda do cabo preto (drop) com o   cabo  branco  de 'distribuição interna", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {#16
            "question_text": "Se o cliente agendar uma visita para ser atendido das 11:00 às 14:00 e o técnico chegar às 14:20, qual Indicador será afetado?",
            "options": [
                ("TEC1", "A"),
                ("ISRA", "B"),
                ("SCM", "C"),
                ("STFC", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {#17
            "question_text": "Qual a função do CMTS?",
            "options": [
                ("Interligar a rede interna à rede   HFC", "A"),
                ("Concentrar  o s dados da internet para transmitir via upstre am   ao cable modem", "B"),
                ("Interligar a rede de telefonia com a  internet, gerando o VOIP", "C"),
                ("Fazer a comunicação e o gerenciamento dos modems", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {#18
            "question_text": "Qual a definição de MER?",
            "options": [
                ("Taxa de erro de transmissão", "A"),
                ("Taxa de erro de recepção", "B"),
                ("Taxa de erro de modulação", "C"),
                ("Taxa de erro de bit", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {#19
            "question_text": "O que é BER?",
            "options": [
                ("Taxa de erro de  transmissão", "A"),
                ("Taxa de erro de recepção", "B"),
                ("Taxa de erro de modulação", "C"),
                ("Taxa de erro de bit", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {#20
            "question_text": "O que é Canal de Retorno?",
            "options": [
                ("Sinal transmitido do equipamento do cliente para o Headend", "A"),
                ("Sinal transmitido do Headend para o cliente", "B"),
                ("Sinal transmitido entre clientes NET", "C"),
                ("Sinal transmitido entre os  Headends", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {#21
            "question_text": "Qual a relação ao tipo de modulação e a  sensibilidade   ao ruído?",
            "options": [
                ("Quanto maior a modulação maior a sensibilidade  ao ruido", "A"),
                ("Independente da modulação a sensibilidade ao ruído sempre será a mesma", "B"),
                ("Quanto menor a modulação maior a sensibilidade ao  ruido", "C"),
                ("Quanto maior a modulação menor a sensibilidade ao  ruído", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {#22
            "question_text": "O que é Downstream  ?",
            "options": [
                ("Sinal que o CMTS envia para o eMTA", "A"),
                ("Sinal  que o eMTA envia para o CMTS", "B"),
                ("Sinal que o medidor envia para o eMTA", "C"),
                ("Sinal que o eMTA envia para o medidor", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {#23
            "question_text": "Quais os sinais que trafegam no Canal de Retorno?",
            "options": [
                ("Canais piloto (alto e baixo)", "A"),
                ("Canais de Vídeo", "B"),
                ("Canais de Upstream", "C"),
                ("Todas as  alternativas anteriores", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {#24
            "question_text": "Em relação ao poste da residência do cliente é correto afirmarmos que:",
            "options": [
                ("Utilizamos o suporte da companhia telefônica somente  com autorização de cliente", "A"),
                ("Não é permitida a utilização do suporte da companhia  telefônica", "B"),
                ("É necessário utilizar o U Span Clamp poste somente nos casos em que  instalarmos CLARO  Fone", "C"),
                ("É necessário utilizar o U Span Clamp poste somente se não houver   suporte da  companhia   telefônica", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {#25
            "question_text": "Para fixação de cabos  coaxiais   em cantos de rodapés e portas, devemos respeitar a curvatura  mínima de:",
            "options": [
                ("5cm", "A"),
                ("12cm", "B"),
                ("8cm", "C"),
                ("20cm", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {#26
            "question_text": "O técnico Jonny deve configurar o padrão de   transmissão WI - FI para rede:",
            "options": [
                ("Transmissão Somente 802.11n", "A"),
                ("Transmissão MISTA - 802.11 b, 802.11g e 802.11n", "B"),
                ("Transmissão Somente 802.11g", "C"),
                ("Transmissão MISTA 802.11g e 802.11n", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {#27
            "question_text": "Durante os testes de potência do WI - FI   o   Técnico Jonny se lembra de que o ideal  em   relação à  potência do WI - FI:",
            "options": [
                ("80% dos cómodos com a potência entre  - 10dBm e   - 70 dBm", "A"),
                ("60% dos cômodos com a potência entre  - 10dbm e  - 70dBm", "B"),
                ("80% dos cômodos com a potência entre  - 50dBm e - 120dBm", "C"),
                ("60% dos cômodos com a  potência entre  - 50dBm e  - 12dBm", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {#28
            "question_text": " Porque não devemos utilizar os passivos   de rede interna em áreas abertas?",
            "options": [
                ("Devido a estética", "A"),
                ("Os passivos de rede interna são sensíveis a umidade  e chuva e por isso oxidam causando  degradação nos sinais", "B"),
                ("Podemos utilizar em áreas abertas desde que utilizarmos fita isolante", "C"),
                ("Todas estão corretas", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {#29
            "question_text": "Durante a instalação da extensão  telefônica , caso  o   cliente queira adicionar outros pontos de  extensão qual o   procedimento que você deve tomar?",
            "options": [
                ("Você deve instalar as extensões solicitadas pelo cliente e efetuar a cobrança em dinheiro referente a cada ponto de extensão instalado", "A"),
                ("Caso o ponto solicitado pelo cliente não esteja contemplado na W.O, oriente o cliente solicita-las via CRN, antes de baixar o serviço. pois a O.S referente aos novos pontos serão agrupado na mesma W.O.", "B"),
                ("O cliente deve solicitar a instalação dos novos pontos de extensão na CRN após o fechamento da W.O que você se encontra.", "C"),
                ("N.d.a", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {#30
            "question_text": "Sobre o Mini Isolator, onde ele deve ser utilizado?",
            "options": [
                ("No ponto que o cliente possuir um equipamento Virtua (eMTA)", "A"),
                ("Em todos os pontos que o cliente possuir um equipamento Fone", "B"),
                ("Em todos os  pontos que o cliente possuir um equipamento (DECODER SD/HD, eMTA e CABLE MODEM)", "C"),
                ("Deve ser utilizado antes do primeiro divisor. Ponto comum dos equipamentos", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {#31
            "question_text": "O uso do torque nos termina i s ( Decoder , eMTA e T V do cliente) deve:",
            "options": [
                ("Ser feito com a Mão com auxilio do 'chaveirinho ou similar', sem a necessidade da chave  torque", "A"),
                ("Ser  feito com alicate universal ou ferramenta similar", "B"),
                ("Ser feito sempre com a chave de torque 15 lbs ho mo logada pela área de serviços", "C"),
                ("Nenhuma das alternativas, pois não necessário  utilizar o torque nesses equipamentos", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {#32
            "question_text": "O que é Cable Isolator?",
            "options": [
                ("É um componente que tem a função de proteger a instalação e equipamentos contra picos  de tensão gerados por surtos de energia ou descargas elétricas, evitando também o retorno de AC para a nossa rede", "A"),
                ("É um dispositivo que tem a função de Isolar os pico e ruídos gerados pelos pontos Pay TV", "B"),
                ("É um tipo de cabo que possui maior Isolação à ruídos ou Interferências externas", "C"),
                ("É um dispositivo para emendar o cabo branco e preto (drop)", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {#33
            "question_text": "O que é RQUAL?",
            "options": [
                ("É uma nova regulamentação da Anatel que consolida e simplifica todas as normas de  qualidade de serviços para operadores de Telecomunicações em um regulamento único.", "A"),
                ("É uma nova regulamentação da Anatel que consolida e simplifica todas as normas de  qualidade de serviços para operadores de fibra optica em um Regulamento único.", "B"),
                ("É uma nova regulamentação da ANA que consolida e s implifica   todas as normas de  qualidade de serviços para operadores de saneamento em um regulamento único.", "C"),
                ("É uma nova regulamentação da CableLabs que consolida e simplifica todas as normas de qualidade de serviços para operadora de cabo mundial em um regulamento único.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {#34
            "question_text": "Qual a diferença entre sinal Flat e Tilt?",
            "options": [
                ("Flat é quando há alguma diferença entre os níveis dos canais medidos no mesmo ponto e Tilt é quando não há diferença de nível de Sinal medido no mesmo ponto.", "A"),
                ("Flat é quando o sinal passou por alguma equalização e Tilt é quando o sinal passou por alguma amplificação.", "B"),
                ("Tilt é quando há alguma diferença entre os níveis de sinal dos canais medidos e Flat é quando não há diferença de nível de sinal.", "C"),
                ("Tilt é quando o sinal passou por alguma equalização e Flat é quando o sinal passou por alguma amplificação.", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {#35
            "question_text": "Dentre as alternativas abaixo, qual delas apresenta uma melhor qualidade de sinal?",
            "options": [
                ("BER 1.0 E-05", "A"),
                ("BER 1.0 E-07", "B"),
                ("BER 2.0 E-08", "C"),
                ("BER 9.0 E-06", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {#36
            "question_text": "Para considerarmos um Decoder On-line, qual opção abaixo é a correta?",
            "options": [
                ("Nas configurações verificar se o IP Inicia em 10.xxx.xxxxxx", "A"),
                ("Nas configurações verificar se o IP inicia em 168.xxx.xxx.xx", "B"),
                ("Nas configurações verificar se o IP inicia 189.xxx.xx.xx", "C"),
                ("Nas configurações verificar se o IP Inicia em 192.xxx.xx.xxx", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  #37
            "question_text": "Conforme vimos durante a aula pratica de configuração Claro TV+ HD, devemos utilizar qual canal para verificação dos endereçáveis (CA-ID e Smart Card) para realizar abaixa?",
            "options": [
                ("250", "A"),
                ("252", "B"),
                ("270", "C"),
                ("262", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 38
            "question_text": "Ao término de uma Instalação, o Instalador Identifica que o serviço de gravação não está funcionando, qual o procedimento ele deverá seguir?",
            "options": [
                ("Confere o Update ID", "A"),
                ("Conferir se o serviço está ativo em seu contrato", "B"),
                ("Enviar HIT para o Decoder e após seguir o procedimento de HIT", "C"),
                ("Todas as alternativas estão corretas", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 39
            "question_text": "Sobre a Configuração dos serviços  Inteligentes do Fone, qual das Informações abaixo está correta?",
            "options": [
                ("O SIGA - ME não está disponível para os pacotes que  não possuem  o Busca Automática. Ou seja, o cliente deve escolher entre o Busca Automática e o SIGA-ME", "A"),
                ("SIGA - ME só pode ser habilitado após o  pagament o da fatura.", "B"),
                ("SEMPRE que configurar o SIGA-ME, desative o serviço de CHAMADA EM ESPERA, pois o mesmo é incompatível com o funcionamento do sistema de redirecionamento", "C"),
                ("Todas as opções estão corretas", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 40
            "question_text": "O SNR do Retorno fora do padrão tem alguma influencia nos equipamentos que possuem um Cable Modem Interno?",
            "options": [
                ("Não, porque ele só afeta o Decoder Digital", "A"),
                ("Não, porque essa informação não se aplica ao Modem", "B"),
                ("Sim, por exemplo, pode causar lentidão na internet e mal funcionamento do NOW", "C"),
                ("Sim, porque pode travar o Notebook do cliente", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 41
            "question_text": "Para obter o título de Técnico Certificado, quais são os parâmetros que devem ser cumpridos?",
            "options": [
                ("Cumprimento de Agenda, Revisita e Produtividade", "A"),
                ("Contact Rate, Revisita e Produtividade", "B"),
                ("TEC1, ISRA e AT", "C"),
                ("N.d.a", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 42
            "question_text": "Quais os níveis de RX e TX padronizados pela NET?",
            "options": [
                ("RX:  - 12dBmv à +12dBmv; TX: 37 à 50dBmv", "A"),
                ("RX:  - 12dBmv à +12dBmv; TX: 38 à 51dBmv", "B"),
                ("RX:  - 15dBmv à +15dBmv; TX: 40 à 51 dBmv", "C"),
                ("RX:  - 15dBmv à +15dBmv; TX: 40 à 55 dBmv", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 43
            "question_text": "O que é FEC?",
            "options": [
                ("Código detector e corretor de erros", "A"),
                ("Código detector de erro de bit", "B"),
                ("Código detector de sinal", "C"),
                ("Código detector de transmissão digital", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 44
            "question_text": "O que é Canal Direto?",
            "options": [
                ("Sinal transmitido do equipamento do cliente até Headend", "A"),
                ("Sinal transmitido do Headend até o cliente", "B"),
                ("Sinal transmitido entre os Headends", "C"),
                ("Sinal  transmitido entre clientes NET", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 45
            "question_text": "Quais são as faixas de frequências disponíveis para o Canal de Retorno?",
            "options": [
                ("55 MHz a 750MHz/104 MHz a 1 GHz", "A"),
                ("213 MHz a 550 MHz/85MHz a 104 MHz", "B"),
                ("5 MHz a 42 MHz/5 MHz a 85 MHz", "C"),
                ("5 MHz a 55 MHz/5 MHz a 104 MHz", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 46
            "question_text": "O que é Upstream?",
            "options": [
                ("Sinal que o CMTS envia para o eMTA", "A"),
                ("Sinal  que o eMTA envia para o CMTS", "B"),
                ("Sinal que o medidor envia para o eMTA", "C"),
                ("Sinal que o eMTA envia para o medidor", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 47
            "question_text": "Quais os sinais que trafegam no Canal Direto?",
            "options": [
                ("Canais piloto (alto e baixo)", "A"),
                ("Canais de  Vídeo", "B"),
                ("Canais Downstream", "C"),
                ("Todas as alternativas anteriores", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 48
            "question_text": "O que é portabilidade?",
            "options": [
                ("É a facilidade que permite o cliente manter o número de telefone fixo ou móvel, independentemente da operadora a que estiver vinculado", "A"),
                ("É a facilidade que permite o cliente trocar um número de telefone fixo para um móvel", "B"),
                ("É a facilidade que permite o cliente manter o número de telefone fixo ou móvel, independentemente da operadora mesmo com titulares diferentes", "C"),
                ("N.d.a", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 49
            "question_text": "O que acontece com o sinal da NET se no momento da instalação amassarmos o cabo?",
            "options": [
                ("Há um aumento na blindagem do cabo contra interferências externas", "A"),
                ("Há uma alteração na impedância característica do cabo", "B"),
                ("Inversão do Tilt entre canal alto e canal baixo", "C"),
                ("Satura as frequências mais altas do espectro", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 50
            "question_text": "Qual a importância de alternar corretamente o Status no PDA?",
            "options": [
                ("Não faz diferença alterar o Status para execução do trabalho", "A"),
                ("Não tem importância, pois os únicos Status utilizados são o deslocamento e Iniciar a rota.", "B"),
                ("O  Status é importante para que o Field consiga otimizar a rota dos Instaladores e evitar deslocamento indevido", "C"),
                ("O Status é importante para que o Supervisor consiga visualizar onde o Instalador está.", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 51
            "question_text": "Qual o procedimento correto quando o cliente possui uma antena de TV UHF para sinal aberto?",
            "options": [
                ("Deixar o cabo de sinal da TV aberta desligado da TV do Cliente.", "A"),
                ("Deixar o sinal da TV aberta ligado na TV do Cliente e orienta-lo quanto a utilização, quando necessário", "B"),
                ("Retirar o cabo de antena do cliente, pois ele não irá utilizá-lo mais", "C"),
                ("Utilizar o cabo de antena como guia para passar o cabo da NET", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 52
            "question_text": "Durante a fixação externa do cabo RG06, podemos afirmar que:",
            "options": [
                ("Os fixadores devem ser colocados a cada 50 cm", "A"),
                ("Os fixadores devem ser fixados a cada 5 cm", "B"),
                ("Devemos utilizar cola quente", "C"),
                ("Devemos solicitar ao cliente a compra de canaletas", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 53
            "question_text": "Com relação à distribuição interna de sinal é correto afirmar que:",
            "options": [
                ("Devemos utilizar a passagem de cabos por tubulações de rede elétrica", "A"),
                ("Só podemos passar o cabeamento caso haja tubulação", "B"),
                ("Devemos passar o cabeamento solto por cima do telhado", "C"),
                ("É proibida a passagem de cabos por tubulação elétrica", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 54
            "question_text": "O que é um Headend?",
            "options": [
                ("Local onde ficam os materiais como decodificadores, massivos , OS's, etc...", "A"),
                ("Local onde são recebidos os sinais das emissoras, faz o processamento, ajuste, codificação e transmissão para o restante da rede HFC", "B"),
                ("Local onde são gerados os conteúdos assistidos pelos  clientes da NET", "C"),
                ("Local onde há todo o processamento dos sinais, inclusive da rede pública de telefonia comutada (RPTC)", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 55
            "question_text": "Qual é a largura de banda de um canal de TV digital?",
            "options": [
                ("6 MHz", "A"),
                ("8 MHz", "B"),
                ("4 MHz", "C"),
                ("42 MHz", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 56
            "question_text": "Quais as partes que compõem um cabo de Coaxial?",
            "options": [
                ("Condutor Central", "A"),
                ("Dielétrico", "B"),
                ("Condutor Externo", "C"),
                ("Todas as alternativas estão corretas", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 57
            "question_text": "O que é uma Rede HFC?",
            "options": [
                ("Rede híbrida que mistura fibra óptica e cabo coaxial", "A"),
                ("Regiões atendidas pelas fibras  ópticas", "B"),
                ("Rede híbrida que mistura fibra óptica com dados IP", "C"),
                ("Rede heterogênea de fibra ótica e portadoras digitais", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 58
            "question_text": "Sobre o curso Direção Consciente, é correto afirmar que:",
            "options": [
                ("Em frenagens, os veículos de grande porte precisam do dobro ou até o triplo de tempo para parar", "A"),
                ("Em frenagens, os veículos de pequeno porte param apos 5 segundos", "B"),
                ("Em frenagens, os veículos de pequeno porte param rapidamente e por isso não precisam manter uma distancia muito grande do veículo à frente", "C"),
                ("Em frenagens, os veículos de pequeno porte nunca derrapam", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 59
            "question_text": "Dos padrões de criptografia Wi-Fi listados abaixo, qual é considerado o mais seguro?",
            "options": [
                ("RADIUS - PSK", "A"),
                ("WEP", "B"),
                ("WPA + TKIP", "C"),
                ("WPA2+AES", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 60
            "question_text": "Em relação ao Virtua WI-FI, o que é importante analisar antes de realizar a instalação?",
            "options": [
                ("Melhor caminho para se passar o cabeamento, independente do local onde será instalado", "A"),
                ("Melhor local para não interferir esteticamente na sala do cliente", "B"),
                ("Melhor local para propagação do sinal WI-FI, de preferencia em um cômodo central da residência", "C"),
                ("Onde fica a sala para instalar o Virtua, pois neste local será utilizado com maior frequência internet através da TV e dos Celulares", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 61
            "question_text": "Para verificar se o sinal de Wi-Fi de qualquer local da casa do cliente é suficiente para se conectar a internet, você deve verificar",
            "options": [
                ("Intensidade da conexão usando o Wi-Fi Analyzer, que deve ser de  -40 a -70 dBm", "A"),
                ("A visão geral do WiFi Analyzer, prestando atenção à curvatura do sinal, que não deve ser muito acentuada estando entre 40dBmV e 52dBmV", "B"),
                ("O canal utilizado, pois se houver muitos roteadores o sinal será mais forte ficando entre -12dBmV e +12dBmV", "C"),
                ("O canal utilizado, pois usar um canal livre deixa o sinal fraco", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 62
            "question_text": "A funcionalidade USB Media permite ao nosso cliente:",
            "options": [
                ("Visualizar fotos, vídeos e músicas através de um pendrive ou HD Externo conectado em seu decodificador através da porta USB", "A"),
                ("Utilizar um pen drive ou HD Externo como gravador digital, onde o cliente poderá gravar os seus programas favoritos e assistir quando quiser", "B"),
                ("Visualizar qualquer tipo de arquivo presente no pendrive, através de seu decodificador", "C"),
                ("Todas as alternativas acima", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 63
            "question_text": "Qual é a principal diferença entre uma portadora de sina digital com a portadora de sinal analógico?",
            "options": [
                ("A portadora de  sinal digital transporta menos informação que a portadora analógica", "A"),
                ("A portadora de sinal digital é agrupada, portanto todas as informações trafegam na mesma portadora até o seu. destino, diferentemente da analógica, onde as informações trafegam separadamente até o seu destino", "B"),
                ("A portadora de sinal digital é constituída das subportadoras de vídeo, cor e áudio, enquanto a portadora de sinal analógico, é constituída do sinal de informação", "C"),
                ("A portadora de sinal digital tem uma largura de faixa em Hertz maior que a analógica", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 64
            "question_text": "Marque a alternativa correta:",
            "options": [
                ("O CMTS se comunica com o Cable Modem através do padrão DOCSIS", "A"),
                ("A 'downstream' é enviada via canal de retorno", "B"),
                ("O CMTS se comunica diretamente com o televisor do cliente NET", "C"),
                ("Todas as alternativas  anteriores estão corretas", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 65
            "question_text": "Qual hierarquia de conexão de cabos devemos respeitar para termos a melhor experiência em assistir TV?",
            "options": [
                ("Vídeo Componente; Áudio e Vídeo; S-VHS; HDMI", "A"),
                ("HDMI; Vídeo Componente; S-VHS; Áudio e Vídeo", "B"),
                ("S-VHS; HDMI; Vídeo Componente; Áudio e Vídeo", "C"),
                ("HDMI; S-VHS; Vídeo Componente; Áudio e Vídeo", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 66
            "question_text": "O que você entende por Combo Multi?",
            "options": [
                ("A mais completa seleção de serviços de telecomunicações do País, reunindo o melhor das três marcas: NET, Claro e Embratel", "A"),
                ("A mais nova banda larga da NET, Claro e Embratel", "B"),
                ("É a nova seleção de TV da Claro e Embratel", "C"),
                ("É a nova seleção de TV da NET, Claro e Embratel", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 67
            "question_text": "Um técnico finalizou uma instalação no período da manhã e no período da tarde o cliente entrou em contato reclamando que a imagem estava com chuviscos/ macro blocos, resultando em nova visita no  dia seguinte para correção da falha reclamada. Qual indicador foi afetado?",
            "options": [
                ("AT5", "A"),
                ("I5", "B"),
                ("IDS", "C"),
                ("TEC 1", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 68
            "question_text": "No momento de qualquer instalação do produto HD/HD MAX, devemos sempre efetuar o teste de funcionalidade do NOW acessando um conteúdo grátis no próprio portal do NOW. Qual dos links abaixo devo acessar no portal para demonstrar ao cliente?",
            "options": [
                ("NOW Filmes", "A"),
                ("NOW Free", "B"),
                ("NOW Gratis", "C"),
                ("Programas de TV", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 69
            "question_text": "Qual o objetivo do EPI? (Segurança no Trabalho NR 35)",
            "options": [
                ("Garantir a segurança e a saúde dos trabalhadores envolvidos direta ou indiretamente com trabalhos em altura", "A"),
                ("Analisar as condições de segurança e saúde dos colaboradores que trabalham em altura", "B"),
                ("Propor dicas de segurança para os trabalhos em altura", "C"),
                ("Evitar que os fiscais de segurança apliquem multas pelo não uso dos equipamentos de segurança", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 70
            "question_text": "Referente ao preenchimento da ORDEM DE SERVIÇO, quando o assinante ou preposto realiza a entrega da cópia  do documento, o Instalador deve:",
            "options": [
                ("Assinalar a opção 'SIM' no campo 'CÓPIA DO RG/CNPJ', Relatar na 'OBSERVAÇÃO DA O.S.', Anexar o documento junto a O.S., Deixar a 3ª via da O.S. do assinante totalmente preenchida para o cliente ou preposto", "A"),
                ("Assinalar NÃO no campo 'CÓPIA DE RG/CNPJ', relatar na 'OBSERVAÇÃO' da OS e pedir ao cliente que assinale uma das três opções de entrega dos documentos", "B"),
                ("Comunicar ao gestor a entrega para que o indicador AT3 seja alcançado", "C"),
                ("Conferir a documentação, Inserir a entrega no campo Observação da O.S., Devolver a cópia dos documentos ao assinante", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 71
            "question_text": "Das opções abaixo qual Update ID disponibiliza o serviço de GRAVAÇÃO do produto HD Max?",
            "options": [
                ("ID 01", "A"),
                ("ID 02", "B"),
                ("ID 05", "C"),
                ("ID 08", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 72
            "question_text": "Conforme podemos observar na atividade conhecendo os decoders, qual a função e o problema que pode acontecer quando não utilizamos a fonte certa para o equipamento desejado?",
            "options": [
                ("As fontes tem a função de ligar os equipamentos. A utilização de uma fonte correta acarreta o mau funcionamento do equipamento, porem o mesmo não para de funcionar", "A"),
                ("As fontes tem a função de transformar a corrente AC da rede elétrica residencial em corrente DC, para o correto funcionamento dos equipamentos. A utilização de uma fonte correta acarreta o mau funcionamento do equipamento, que dependendo do caso poderá ser seriamente danificado", "B"),
                ("As fontes tem a função de transformar a corrente AC da rede elétrica residencial em corrente DC, para  o correto funcionamento dos equipamentos. A utilização de uma fonte incorreta acarreta o mau funcionamento do equipamento, que dependendo do caso poderá ser seriamente danificado", "C"),
                ("As fontes tem a função de transformar a corrente elétrica residencial em corrente AC, para o funcionamento dos equipamentos. A utilização de uma fonte incorreta acarreta na maioria dos casos o mau funcionamento do equipamento, porem o mesmo não para de funcionar", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 73
            "question_text": "Para qual dos serviços abaixo é necessário que o cliente ligue na CRN (CENTRAL DE RELACIONAMENTO NET) para solicitar ativação?",
            "options": [
                ("Identificador de chamadas", "A"),
                ("Siga-me", "B"),
                ("Chamada em espera", "C"),
                ("Conferência a três", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 74
            "question_text": "Dos problemas abaixo, quais podem ser causados por um TX e RX fora do padrão?",
            "options": [
                ("Aumento no consumo do Vírtua e aquecimento do modem", "A"),
                ("Lentidão, Intermitência e sem sinal", "B"),
                ("Não ocorre nada, é somente um verificação da NET", "C"),
                ("Pode afetar o alcance do WI-FI", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 75
            "question_text": "Qual das alternativas abaixo NÃO gera ruído?",
            "options": [
                ("Amplificador saturado", "A"),
                ("Conectores irregulares ou inexistentes assim como portas não terminadas/casadas", "B"),
                ("Conexão clandestina de todo tipo", "C"),
                ("Utilização do cabo de rede (dados) com mais de 60 metros", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 76
            "question_text": "Qual site o Técnico pode acessar para medir os níveis de sinal de um Cable Modem/eMTA?",
            "options": [
                ("www.anatel.gov.br", "A"),
                ("www.brasilbandalarga.com.br", "B"),
                ("niveis.virtua.com.br", "C"),
                ("www.speedtest.net", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 77
            "question_text": "Um dos indicadores do Programa Geral de Metas da Qualidade da Anatel é o ISRA. Qual o significado da sigla e o que ele mede?",
            "options": [
                ("Indicador de Solicitação de Reajuste Atendido, mede o percentual de reajustes na fatura cadastrados no sistema em menos de 24horas", "A"),
                ("Indicador de Serviços Relacionados ao Atendimento, mede o percentual de ligações na central", "B"),
                ("Índice de Serviços de Realizados Avulsos, mede o percentual de reparos atendidos sem cadastrado no sistema", "C"),
                ("Indice de  Solicitação de Reparo Atendido, mede o percentual de reparos atendidos em 24h da data/período cadastrado no sistema", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 78
            "question_text": "Calcule os níveis de CA, CB, TX e RX no ponto abaixo?",
            "options": [
                ("Sinal Tv - Cha= 3,0 - Chb= 6,5 / Sinal MTA - RX= -1 -TX= 42,5", "A"),
                ("Sinal Tv - Cha= 3,0 - Chb= 6,2 / Sinal MTA - RX= -0,5 -TX= 42,5", "B"),
                ("Sinal Tv - Cha= 3,0 - Chb= 6,5 / Sinal MTA - RX= -0,5 -TX= 42,5", "C"),
                ("Sinal Tv - Cha= 3,0 - Chb= 6,2 / Sinal MTA - RX= -1 -TX= 42,5", "D")
            ],
            "correct_answer": "C",
            "image": "TXRX.jpeg"
        },
        {  # 79
            "question_text": "Qual a função do cable Isolator?",
            "options": [
                ("Proteger a Instalação e os equipamentos da NET contra picos de tensão e retorno de (AC)", "A"),
                ("Amplificar o sinal luminoso da fibra ótica", "B"),
                ("Dividir os sinais elétricos em Igual valor", "C"),
                ("Filtrar as frequências acima de 350 Mh", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 80
            "question_text": "Qual a função da Carga Casada?",
            "options": [
                ("Adequação da rede, faz o casamento de Impedância do circuito", "A"),
                ("Tem a função de proteger a instalação e equipamentos contra picos de tensão", "B"),
                ("Utilizada para unir dois conectores ou cabos distintos", "C"),
                ("Utilizada para minimizar a pirataria nos equipamentos internos e externos", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 81
            "question_text": "Selecione a alternativa correta. Quais dos Itens abaixo não devem ser utilizados no espaço confinado?",
            "options": [
                ("Celulares, óculos de proteção, calçado de proteção e velas", "A"),
                ("Celulares, cigarros, velas, fósforos, e isqueiros", "B"),
                ("Lanterna, velas, fósforos, e Isqueiros", "C"),
                ("Celulares, Lanternas, velas, fósforos, e Isqueiros;", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 82
            "question_text": "O NET Fone só funciona em telefones homologados pela ANATEL e que utiliza o padrão de discagem:",
            "options": [
                ("FSK", "A"),
                ("Pulse", "B"),
                ("DTMF ou TOM", "C"),
                ("VoIP", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 83
            "question_text": "O que significa cabo Drop?",
            "options": [
                ("Cabo que faz a ligação do decodificador com a televisão", "A"),
                ("Cabo que conecta o eMTA ao computador", "B"),
                ("Cabo que faz a ligação do divisor até o equipamento NET", "C"),
                ("Fazer a conexão do poste da Companhia de Energia Elétrica, onde está instalada a rede da NET, até o ponto de entrada da casa do cliente.", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 84
            "question_text": "Quais são os tipos de Modulação Digital?",
            "options": [
                ("QPSK e TDM", "A"),
                ("QAM e XADSL", "B"),
                ("QPSK e QAM", "C"),
                ("QAM e TDM", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 85
            "question_text": "IPCONFIG /RELEASE é um comando digitado para forçar a renovação de um IPV4 ou IPV6 dinâmico em um determinado hardware (placa de rede ou WiFi). Essa afirmação é verdadeira?",
            "options": [
                ("Não é possível forçar a renovação do IP.", "A"),
                ("Não, o comando que utilizamos para renovação do IPCHKDSK", "B"),
                ("Não, o comando que utilizamos para renovação do IP IPCONFIG /RENEW", "C"),
                ("Sim, a afirmação está correta", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 86
            "question_text": "Sobre o #NET WIFI, podemos afirmar:"
                             "I. Rede de hotspots/pontos de acesso Wi-Fi instalados pelas ruas e aeroportos das principais cidades do Brasil;"
                             "II. A rede #NET-WIFI também é exibida nos eMTA's 3.0 compatíveis",
            "options": [
                ("As afirmações I e II estão corretas", "A"),
                ("Apenas a afirmação I está correta", "B"),
                ("Apenas a afirmação II está correta", "C"),
                ("As afirmações não são corretas", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 87
            "question_text": "O que é PIP?",
            "options": [
                ("O PIP (Picture in Picture) é um recurso que possibilita visualizar outro canal através de uma pequena janela, ao mesmo tempo que assiste a um programa na tela principal", "A"),
                ("O PIP (Picture in Picture) é um recurso que possibilita a transferência de dados e arquivos  entre os clientes NET Vírtua, podendo assim compartilha arquivos entre eles através dessa funcionalidade.", "B"),
                ("O PIP (Picture in Picture) é um recurso que possibilita a visualização das imagens  armazenadas na rede do cliente em seu telefone, smartphone, tablet ou computador  utilizando o NOW.", "C"),
                ("O PIP (Picture in Picture) é um recurso que possibilita o pagamento da fatura NET através do controle remoto acessando o Minha NET pela Smart TV ou celular.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 88
            "question_text": "Dentre as opções abaixo, qual representa baixo potencial de barreira/interferência para o sinal de Wi-Fi?",
            "options": [
                ("Madeira e Gesso.", "A"),
                ("Agua e Arvores.", "B"),
                ("Concreto e Metal.", "C"),
                ("Micro-ondas e Telefone sem fio.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 89
            "question_text": "Sobre o teste de Tracert, é correto afirmar que:",
            "options": [
                ("É um comando para configurar, habilitar desabilitar o Firewall da máquina.", "A"),
                ("É um teste de rota que visualiza a solicitação   de acesso a uma determinada página ou servidor com o objetivo de verificar lentidão, bloqueio ou gargalo ao site solicitado.", "B"),
                ("É um teste para determinar se a velocidade da navegação do cliente está dentro ou fora da velocidade contratada.", "C"),
                ("É um teste para verificar a existência de vírus ou Cavalo de Tróia no computador do cliente", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 90
            "question_text": "A configuração 1920 x 1080 pixels refere-se a qual tipo de resolução de TV?",
            "options": [
                ("SD", "A"),
                ("HD", "B"),
                ("FULL HD", "C"),
                ("ISDB", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 91
            "question_text": "Sobre o Anel de Vedação é correto afirmar que:?",
            "options": [
                ("Deve ser instalado em todos os passivos da residência ou MDU.", "A"),
                ("Deve ser instalado apenas em passivos que estão em calhas.", "B"),
                ("Deve ser instalado em conectores que ficam expostos ao tempo, como por exemplo no TAP da Rede Externa ou Cable Isolator.", "C"),
                ("N.d.a", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 92
            "question_text": "O cliente possui uma TV de LCD com alta definição é um decoder HD, qual das opões abaixo o cliente consegue ter imagem em alta definição?",
            "options": [
                ("Utilizando o cabo HDMI", "A"),
                ("Utilizando o cabo SPDIF", "B"),
                ("Utilizando o cabo Vídeo Componente", "C"),
                ("Utilizando o cabo S-VHS", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 93
            "question_text": "Sobre o NOW/nowonline selecione a alternativa correta:"
                             "I.O aluguel de conteúdo pago pode ser feito pela TV, computador e aplicativo Android e podem ser assistidos em todos os dispositivos pelo período de 48h, a partir do momento do aluguel;"
                             "II. O cliente pode cadastrar até 2 dispositivos móveis (Smartphone/Tablet) e um computador;"
                             "III. Pode dar play em 1 dispositivo móvel e 1 computador ao mesmo tempo, além da TV que é independente.",
            "options": [
                ("Apenas a afirmação I está correta", "A"),
                ("Apenas a afirmação II está correta", "B"),
                ("Apenas as afirmações I e III estão corretas", "C"),
                ("Todas as afirmações estão corretas", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 94
            "question_text": "Selecione a alternativa que contem corretamente o nome de cada perda do passivo:",
            "options": [
                ("A - inserção; B - Isolação; C - Derivação", "A"),
                ("A - Derivação; B - Inserção; C - Isolação", "B"),
                ("A - Inserção; B - Derivação; C - Isolação", "C"),
                ("A - Isolação; B - Inserção; C - Derivação", "D")
            ],
            "correct_answer": "C",
            "image": "DC.JPG"
        },
        {  # 95
            "question_text": "Em que faixa de frequência trabalham os sinais de CATV?",
            "options": [
                ("KHz", "A"),
                ("MHz", "B"),
                ("GHz", "C"),
                ("THz", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 96
            "question_text": "Qual a finalidade da pingadeira?",
            "options": [
                ("Evitar que haja infiltração de água na casa do cliente através do cabo.", "A"),
                ("Apenas para deixar a estética da instalação ideal", "B"),
                ("Serve como reserva técnica caso o cliente queira mudar local", "C"),
                ("Ocasionar infiltração de água na casa do cliente", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 97
            "question_text": "Quais as partes que compõem um cabo de Fibra Óptica?",
            "options": [
                ("Capa protetora", "A"),
                ("Casca", "B"),
                ("Núcleo", "C"),
                ("Todas as alternativas acima", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 98
            "question_text": "Em alta frequência, a corrente tende a migrar para a extra m idade do condutor, que fenômeno é esse?",
            "options": [
                ("Efeito Migratório", "A"),
                ("Efeito Quasi Square", "B"),
                ("Efeito Senoidal", "C"),
                ("Efeito Skin", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 99
            "question_text": "Ao executar o teste de navegação após a instalação do produto Virtua, o teste de download apresenta uma taxa de transferência de 7,5 MBps, qual é a velocidade contratada desse cliente?",
            "options": [
                ("100 Mbps", "A"),
                ("12 Mbps", "B"),
                ("120 Mbps", "C"),
                ("60 Mbps", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 100
            "question_text": "Como deve acontecer o preenchimento da O.S?",
            "options": [
                ("Em dois momentos: os campos 1 e 2 ao chegar no cliente e os demais campos após o término da execução do serviço", "A"),
                ("Em dois momentos: os campos 1, 2 e 7 ao chegar no cliente e os demais campos após o término da execução do serviço", "B"),
                ("Todos os campos somente no final quando todo o serviço estiver concluído", "C"),
                ("Todas as alternativas", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 101
            "question_text": "A conexão SPDIF é uma conexão",
            "options": [
                ("De vídeo digital SD", "A"),
                ("De vídeo digital HD", "B"),
                ("De áudio digital", "C"),
                ("De áudio analógico", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 102
            "question_text": "Qual é o padrão do telefone para que o identificador de camadas (BINA) funcione?",
            "options": [
                ("FSK", "A"),
                ("DBMV", "B"),
                ("DTMF", "C"),
                ("DVB-T", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 103
            "question_text": "Em uma visita técnica com problemas no NOW, observou-se que o decodificador está com o LED de sincronismo piscando. Qual a possível causa desse problema?",
            "options": [
                ("O decodificador não é HD", "A"),
                ("A potência de sinal do Canal Alto está muito baixa", "B"),
                ("O cliente não possui NOW contratado em seu pacote de TV", "C"),
                ("A potência de sinal de TX e RX está fora do padrão", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 104
            "question_text": "Quando o Cliente possui um sistema de VPN e abre reclamação que parou de funcionar, devemos observar abaixo:",
            "options": [
                ("Se o Cliente possui um IP dinâmico e o E-MTA em Bridged", "A"),
                ("Se o Cliente possui um IP Nateado", "B"),
                ("Se o Cliente possui um IP Fixo", "C"),
                ("Se o Cliente possui um IP dinâmico", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 105
            "question_text": "O espectro de frequência foi dividido em 2 canais de transmissão (Direto e Retorno). Quais os sinais que trafegam em cada canal?",
            "options": [
                ("Direto (CA, CB e TX) e Retorno (RX)", "A"),
                ("Direto (CA, CB e RX) e Retorno (TX)", "B"),
                ("Direto (CA e TX) e Retorno (CB e RX)", "C"),
                ("Direto (CA e CB) e Retorno (TX e RX)", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 106
            "question_text": "Um cliente Claro TV quer contratar os canais a la carte PFC e UFC pelo controle remoto, o que devo observar para que ele consiga fazer esta contratação sem precisar ligar na central de atendimento?",
            "options": [
                ("Testar os canais pilotos CA, CB e RX", "A"),
                ("Verificar o LED de sincronismo se está aceso, realizar a verificação do IP (10.X.X.X) e fazer o Report Back", "B"),
                ("TX deve estar dentro do padrão 40 a 51 dBmv", "C"),
                ("Se o controle remoto do cliente é Universal", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 107
            "question_text": "Sobre o procedimento de Instalação Wi-Fi, selecione a alternativa correta: (Treinamento de 1 Ponto 196 A)",
            "options": [
                ("Sempre priorize a melhor cobertura de sinal nos cômodos onde o cliente informar que mais utilizará o WI-FI;", "A"),
                ("A cobertura deve ser garantida em 80% dos cômodos com potência entre -10dBm e -70dBm, nos outros 20% dos cômodos, a cobertura deve estar entre -70dBm e -90dBm", "B"),
                ("A cobertura deve ser garantida em 80% dos cômodos com potência entre -10dBm e -70dBm, nos outros 20% dos cômodos, a cobertura deve estar entre -70dBm e -90dBm", "C"),
                ("Todas as alternativas estão corretas", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 108
            "question_text": "O cliente com UPDate ID 1, tem qual serviço disponível em seu decodificador HD?",
            "options": [
                ("Serviço de Gravação", "A"),
                ("Serviço NOW e Alta definição", "B"),
                ("Serviço NOW e serviço de Gravação", "C"),
                ("Alta definição e serviço de Gravação", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 109
            "question_text": "Dos padrões de redes Wi-Fi abaixo para um Cliente de (1Gbps), qual nos proporciona a maior velocidade da taxa de transmissão? (EAD Procedimentos NET Wi Fi).",
            "options": [
                ("ac", "A"),
                ("g", "B"),
                ("ax", "C"),
                ("n", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 110
            "question_text": "Referente ao BER padrão Claro abaixo qual representa a melhor Qualidade",
            "options": [
                ("1.0 E-7", "A"),
                ("2.3 E-8", "B"),
                ("0.0 E-9", "C"),
                ("1.0 E-9", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 111
            "question_text": "Referente as redes 2.4GHZ e 5.8Ghz qual a afirmação abaixo esta correta",
            "options": [
                ("A de 2.4Ghz possui menor alcance e maior volume de transmissão WI-FI do que a de 5.8Ghz", "A"),
                ("A de 2.4Ghz possui o mesmo alcance e volume de transmissão WI-FI do que a de 5.8Ghz", "B"),
                ("A de 2.4Ghz possui maior alcance e menor volume de transmissão WI-FI do que a de 5.8Ghz", "C"),
                ("A de 2.4Ghz possui maior alcance e maior volume de transmissão WI-FI do que a de 5.8Ghz", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 112
            "question_text": "QSobre o TNPS e o NPS (Medição de Satisfação do Cliente) assinale abaixo a correta informação.",
            "options": [
                ("I - TNPS é referente ao atendimento do Técnico e o NPS é referente a Satisfação do Produto ou Marca", "A"),
                ("II- TNPS é referente a Satisfação do Produto ou Marca e o NPS é referente ao atendimento do Técnico", "B"),
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 113
            "question_text": "Dos padrões de criptografia Wi-Fi listados abaixo, qual é considerado o mais seguro? (EAD ETN Wi-Fi)",
            "options": [
                ("RADIUS-PSK", "A"),
                ("WEP", "B"),
                ("WPA", "C"),
                ("WPA2", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 114
            "question_text": "Código detector e corretor de erros é chamado de:",
            "options": [
                ("FEC", "A"),
                ("BER", "B"),
                ("MER", "C"),
                ("QAM", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 115
            "question_text": "Qual sigla define  Taxa de erro de bit.",
            "options": [
                ("BER", "A"),
                ("MER", "B"),
                ("FEC", "C"),
                ("QPSK", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 116
            "question_text": "Qual Sigla define Taxa de erro de modulação:",
            "options": [
                ("MER", "A"),
                ("BER", "B"),
                ("FEC", "C"),
                ("QAM", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 117
            "question_text": "O que é Modulação QAM (Quadrature Amplitude Modulation) (EAD Medidas II)",
            "options": [
                ("Modulação que altera os símbolos em função da amplitude", "A"),
                ("Modulação que altera os simbolos em função da fase e amplitude", "B"),
                ("Modulaçāo que altera os simbolos em funçāo da fase", "C"),
                ("Modulação que altera os símbolos em função da frequência", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 118
            "question_text": "Qual o procedimento adotado para o acesso a página de validação do REPORT BACK nos Decoders HD/HD MAX?",
            "options": [
                ("Colocar no canal 262 e digitar no controle 'azul' + 'MENU' + '8291'", "A"),
                ("Colocar no canal 262 e digitar no controle 'verde' + '8291'", "B"),
                ("Colocar no canal 270 e digitar no controle 'azul' + '8291'", "C"),
                ("Colocar no canal 262 e digitar no controle 'azul' + '8291'", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 119
            "question_text": "Em uma casa com dois pontos de TV, existe um Two-Way (splitter) onde o cabo de entrada da casa foi ligado em uma de suas saídas, e o primeiro ponto em outra saída, e o segundo ponto foi ligado na entrada, o que está acontecendo com as televisōes?",
            "options": [
                ("Os dois pontos estão funcionando, porém sem áudio", "A"),
                ("O primeiro ponto funciona e o segundo não", "B"),
                ("O segundo ponto funciona e o primeiro não", "C"),
                ("Os dois pontos estão parados", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 120
            "question_text": "Complete com a alternativa correta. Um cliente contratou uma velocidade de 60___. Com esta Velocidade ele pode realizar download até 7,5___.",
            "options": [
                ("MBps; MBps", "A"),
                ("MBps; Mbps", "B"),
                ("Mbps; MBps", "C"),
                ("Mbps; Mbps", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 121
            "question_text": "Qual a função do teste de velocidade, ping e Tracert, respectivamente?",
            "options": [
                ("Testa a velocidade, pinga e testa o traço", "A"),
                ("Testa a velocidade, verificar o tempo da conexão, traça a rota no mapa", "B"),
                ("Testa a velocidade do pacote, vê o tempo da conexão, vê rota somente dentro da NET", "C"),
                ("Testa se velocidade está dentro da contratada, testa a latência, faz um ping em todos os computadores no caminho até o endereço de internet desejado", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 122
            "question_text": "O cliente reclama que em alguns canais de seu decoder HD ele não consegue alterar o volume pelo controle remoto NET, somente com o da TV. O que deve ser feito para solucionar este problema?",
            "options": [
                ("Solicitar ao cliente que troque sua TV por uma que tenha entrada HDMI", "A"),
                ("Configurar o controle remoto universal para controle do áudio da TV, e entregar um novo caso o cliente não possua", "B"),
                ("Trocar o cabeamento RG06 por RG11", "C"),
                ("Instruir cliente sobre este problema que não tem solução", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 123
            "question_text": "Uma aplicação em IPv4 consegue comunicar-se usando o protocolo IPv6?",
            "options": [
                ("Não, pois IPv6 não é dinâmico e o IPv4 é", "A"),
                ("Não, pois um protocolo não é compatível com o outro", "B"),
                ("Sim, pois ambos são protocolos de 32 bits", "C"),
                ("Sim, pois são protocolos compatíveis", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 124
            "question_text": "Um eMTA está com o LED TEL1 piscando, porém o telefone está no gancho e cliente reclama que não faz e nem recebe chamadas. Dentre as opções abaixo, qual é o possível defeito?",
            "options": [
                ("Cadastro correto na Embratel", "A"),
                ("Extensões em curto", "B"),
                ("Saída RJ 45 queimada", "C"),
                ("Telefone em modo pulse", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 125
            "question_text": "Dos problemas abaixo, quais podem ser causados por um TX e RX fora do padrão?",
            "options": [
                ("Aumento no consumo do Vírtua e aquecimento do modem", "A"),
                ("Lentidão, Intermitência e sem sinal", "B"),
                ("Não ocorre nada, é somente um verificação da NET", "C"),
                ("Pode afetar o alcance do WI-FI", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 126
            "question_text": "O que significa efetuar um ROLLBACK em clientes com IP Nateado?",
            "options": [
                ("A possibilidade do retorno do cliente para o IPv4", "A"),
                ("É o comando dado para que o assinante receba o IPv6", "B"),
                ("É uma das etapas de migração para o IPv6", "C"),
                ("Todas as afirmações acima estão corretas", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 127
            "question_text": "Após termos certeza de que os níveis e cabeamento estão dentro dos padrões, qual é o procedimento para atualização das versões do Firmware e NET TV?",
            "options": [
                ("Com o decoder ligado envie um hit para o equipamento, aguarde de 2 a 5 minutos e depois desligue o decoder utilizando o controle remoto, aguarde que o processo de atualização irá começar, aguarde aproximadamente de 5 a 10 minutos", "A"),
                ("Desligue o decoder pelo cabo de força, aguarde de 2 a 5 minutos e depois que ligar executar o Forced Download, aguarde aproximadamente de 5 a 10 minutos", "B"),
                ("Executando o Forced Download e enviando um HIT após a conclusão desse processo", "C"),
                ("Executando o processo em que forçamos a execução da atualização (Forced Download)", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 128
            "question_text": "O ___ é um sinal que é enviado através do Canal___ do Headend até a casa do cliente. Uma vez sincronizado o equipamento inicia o sincronismo do Sinal de___ através do Canal___. Preencha os termos corretos ",
            "options": [
                ("RX - Canal Direto - TX - Canal de Retorno", "A"),
                ("TX - Canal Direto - RX - Canal de Retorno", "B"),
                ("RX-Canal de Retorno - TX - Canal Direto", "C"),
                ("RX-Canal Analógico - TX - Canal Digital", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 129
            "question_text": "O que é Ponto Ultra?",
            "options": [
                ("Um produto que permite ao cliente conectar seus dispositivos a partir do eMTA, por meio de uma conexão de cabo ethernet, em diferentes cômodos de sua casa.", "A"),
                ("Um produto que utiliza eMTA dual band. Na prática, a conexão da sua casa pode ficar até 5x mais rápida e com muito menos interferências do que rede a convencional.", "B"),
                ("Um produto que utiliza decodificadores HDNG e 4K nos pontos adicionais.", "C"),
                ("Ponto adicional que utiliza decodificador UHD 4K.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 130
            "question_text": "É utilizado para Transformar o sinal Luminoso que chega por meio da fibra óptica em sinal elétrico para ser transmitido via cabos coaxiais.",
            "options": [
                ("Headend", "A"),
                ("Transceptor óptico", "B"),
                ("Hub", "C"),
                ("Amplificador", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 131
            "question_text": "Os amplificadores de CATV possuem um componente responsável em separar o sinal do canal direto, do canal de retorno. Este componente é o: (EAD Ativos de Rede Externa I)",
            "options": [
                ("Eq. Interstage;", "A"),
                ("Filtro Diplex;", "B"),
                ("Híbrido de retorno;", "C"),
                ("Híbrido do direto;", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 132
            "question_text": "A utilização do mini isolador é obrigatoria em todos os teinais instalados na casa do cliente, qual a é função deste componente?",
            "options": [
                ("O mini isolador amplifica o sinal e melhora a qualidade do sinal recebido nos equipamentos.", "A"),
                ("O mini isolador serve para proteger os terminais contra surtos de tensão e retorno de AC", "B"),
                ("O mini isolador serve para corrigir defeitos somente do Virtua", "C"),
                ("O mini isolador ajuda no controle dos terminais pelo datacenter", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 133
            "question_text": "O aplicativo técnico nota 10 possui diversas funções, uma delas é a verificação de TAP lotado. Assinale a alternativa correta:",
            "options": [
                ("A função TAP lotado mostra quais domicilios conectados no TAP são clientes ativos e inativos, auxiliando no momento da instalação.", "A"),
                ("A função TAP lotado ajuda o técnico a medir o sinal de CA e CB no TAP", "B"),
                ("A função de TAP lotado auxilia o técnico no momento do deslocamento para a visita", "C"),
                ("A função de TAP lotado auxilia o técnico  a medir a velocidade do virtua", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 134
            "question_text": "Quando o cabo entrar na fachada do domicílio do cliente, é necessário efetuar furo na parede, colocação de bucha de acabamento e realização de pingadeira. Qual o diâmetro da pingadeira?",
            "options": [
                ("35cm", "A"),
                ("15cm", "B"),
                ("20cm", "C"),
                ("27cm", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 135
            "question_text": "Ao acomodar o cabo passado de forma exposta, qual a distância a ser respeitada entre os fixa-fios?",
            "options": [
                ("50cm", "A"),
                ("25cm", "B"),
                ("19cm", "C"),
                ("100cm", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 136
            "question_text": "Na acomodação do cabo coaxial RG06, é necessário bastante cuidado para não amassar ou dobrar o cabo. O que acontece caso o cabo sofra dobraduras, vincos ou amassados?",
            "options": [
                ("Não acontecerá nada, já que o cabo coaxial é bastante resistente.", "A"),
                ("Ajudará na qualidade do sinal recebido pelo equipamento", "B"),
                ("O serviço funcionará perfeitamente, aumentando o seu upload", "C"),
                ("O cabo sofrerá descasamento de impedância, causando atenuações excessivas e defeito nos produtos que trabalham em alta frequência.", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 137
            "question_text": "Quais os defeitos causados pelo ingresso de ruido na rede?",
            "options": [
                ("Lentidão e queda na navegação", "A"),
                ("Macroblocos na imagem e falha nas ligações do telefone", "B"),
                ("Intermitência e travamentos", "C"),
                ("Todas as alternativas anteriores", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 138
            "question_text": "Qual site deve ser acessado em casos de problemas com portabilidade?",
            "options": [
                ("Voip.claro.com.br", "A"),
                ("Consultanunero.abrtelecom.com.br", "B"),
                ("Anatel.gov.br", "C"),
                ("Claro.com/telefoniavoip", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 139
            "question_text": "Ao término do seu atendimento, o cliente realiza uma pesquisa que avalia o seu atendimento. Qual é este indicador?",
            "options": [
                ("Revisita", "A"),
                ("Cumprimento de agenda", "B"),
                ("TNPS", "C"),
                ("Pesquisa Claro +", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 140
            "question_text": "Durante o atendimento ao cliente, é necessário zelar pela ótima experiência do cliente com a nossa atuação. Quais quesitos são fundamentais para encantar o cliente durante o atendimento?",
            "options": [
                ("Ética e planejamento", "A"),
                ("Apresentação pessoal e empatia com o cliente", "B"),
                ("Testar e explicar todos os produtos instalados", "C"),
                ("Todas as alternativas", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 141
            "question_text": "Quais são as formas que cliente pode utilizar o auto atendimento pelo Minha Claro Residencial?",
            "options": [
                ("Somente Site", "A"),
                ("Whatsapp, Site e Aplicativo", "B"),
                ("Somente aplicativo", "C"),
                ("Somente Whatsapp", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 142
            "question_text": "Qual a função do controle de qualidade?",
            "options": [
                ("Garantir aderência dos processos de instalação para que falhas de execução não impactem a experiência do cliente com os produtos Claro", "A"),
                ("Apenas apontar as falhas dos instaladores", "B"),
                ("Mostrar os acertos dos instaladores", "C"),
                ("N.d.a", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 143
            "question_text": "Qual aplicativo devemos utilizar para a realização da baixa do serviço e habilitação dos terminais?",
            "options": [
                ("Work Assure", "A"),
                ("OFSC TOA", "B"),
                ("Autenticador Microsoft", "C"),
                ("Autenticador Oracle", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 144
            "question_text": "O Minha Claro Residencial, permite ao cliente realizar várias atividades. Selecione a alternativa correta:",
            "options": [
                ("Trocar rede e senha do Wi-Fi", "A"),
                ("Segunda via de fatura", "B"),
                ("Abrir visitas técnicas", "C"),
                ("Todas as alternativas", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 145
            "question_text": "Quais são as etapas do atendimento consultivo?",
            "options": [
                ("Planejamento, sondagem, diagnóstico, atendimento consultivo, encerramento do atendimento", "A"),
                ("Planejamento, sondagem, atendimento consultivo, encerramento do atendimento", "B"),
                ("Sondagem, diagnóstico, atendimento consultivo, encerramento do atendimento", "C"),
                ("Planejamento, sondagem, diagnóstico, encerramento do atendimento", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 146
            "question_text": "O que é o atendimento consultivo?",
            "options": [
                ("É um atendimento especializado prestado pela área comercial", "A"),
                ("É um atendimento de cliente caso crítico", "B"),
                ("É um atendimento convencional", "C"),
                ("É uma consultoria técnica focada em entregar a melhor experiência do cliente com os produtos Claro", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 147
            "question_text": "Qual é a meta de revisita de acordo com as métricas do técnico certificado?",
            "options": [
                ("Acima de 7%", "A"),
                ("Abaixo de 7%", "B"),
                ("Até 10%", "C"),
                ("Entre 8% e 10%", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 148
            "question_text": "Quais indicadores compõe o título de técnico certificado?",
            "options": [
                ("Revisita, cumprimento de agenda e produtividade", "A"),
                ("IND4, IND5, IND6 e IND7", "B"),
                ("IND8, IND9 e INF1", "C"),
                ("Todos os indicadores do RQUAL", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 149
            "question_text": "Sobre o Led de sinalização na cor amarela, podemos afirmar:",
            "options": [
                ("Os extensores estão se comunicando na rede de 2.4GHz. Aproxime os extensores até obter o Led Azul fixo ou interligue-os via cabo de rede ethernet.", "A"),
                ("Os extensores estão se comunicando na rede de 5GHz, e isso é imprescindível para a melhor performance da rede Mesh.", "B"),
                ("Somente quando o extensor for o 1° ponto da rede mesh ele estará com o led amarelo.", "C"),
                ("Não há opção para Led amarelo nos extensores", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 150
            "question_text": "Qual das seguintes opções descreve corretamente a política de instalação dos extensores Wi-Fi Mesh, de acordo com a informação fornecida?",
            "options": [
                ("A instalação via cabo de rede é necessária apenas quando os extensores forem instalados com eMTA/ONT diferente de CBN.", "A"),
                ("A instalação via cabo de rede é obrigatória em todos os pontos, exceto quando há tubulação obstruída. Nesse caso utilize o código de baixa #477 - Instalação Mesh cabeada, para todas as tarefas de instalação efetuadas com cabo de rede Ethernet.", "B"),
                ("A instalação via Wi-Fi é sempre preferível em todos os casos. Nesses casos você deve utilizar o código de baixa # 409 - Instalação efetuada, para as tarefas de instalação dos módulos mesh via Wi-Fi.", "C"),
                ("A instalação via cabo de rede é opcional, independentemente das condições.", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 151
            "question_text": "Para parear o eMTA CBN com os extensores via WPS, qual o procedimento correto?",
            "options": [
                ("I - Pressione primeiro o botão WPS do extensor por 1 segundo."
                 "II - Em seguida, com o extensor indicando o Led piscando em vermelho, pressione o botão WPS do eMTA por 5 segundos."
                 "III - Ao final do processo, se existir uma conexão de qualidade entre os extensores, todos ficarão com o Led Amarelo.", "A"),
                ("I - Pressione primeiro o botão WPS do eMTA por 5 segundos."
                 "II - Em seguida, com o extensor adicional indicando o Led fixo vermelho, pressione o botão WPS por 5 segundos."
                 "III - Ao final do processo, se existir uma conexão de qualidade entre os extensores, todos ficarão com o Led Azul fixo.", "B"),
                ("I - Pressione primeiro o botão WPS do eMTA por 20 segundos."
                 "II - Em seguida, com o extensor indicando o Led vermelho piscando, pressione o botão WPS por 15 segundos."
                 "III - Ao final do processo, se existir uma conexão de qualidade entre os extensores, todos ficarão com o Led Verde.", "C"),
                ("Não é possivel parear os extensores com o eMTA CBN via WPS", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 152
            "question_text": "Diferente de outros modelos de eMTA, o CBN CH8568 pode ser configurado com a função Mesh, atuando como a 1ª célula da rede. A afirmação acima é:",
            "options": [
                ("Verdadeira", "A"),
                ("Falsa", "B"),
                ("Não é possivel realizar a configuração", "C"),
                ("N.d.a", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 153
            "question_text": "Até quantos extensores podem ser conectados à mesma rede?",
            "options": [
                ("8 extensores.", "A"),
                ("2 extensores.", "B"),
                ("5 extensores.", "C"),
                ("4 extensores.", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 154
            "question_text": "Sobre o Led de sinalização na cor azul fixo, podemos afirmar:",
            "options": [
                ("Conexão com qualidade média entre os extensores. Conexão estabelecida entre eles em 2.4GHz com potência superior à -65dBm.", "A"),
                ("Conexão estabelecida entre eles em 5GHz. Melhor conexão entre os extensores para a performance ideal com potência de até -55dBm.", "B"),
                ("Conexão com qualidade média entre os extensores. Conexão estabelecida entre eles em 5.8GHz com potência superior à -65dBm", "C"),
                ("Conexão estabelecida entre eles em 2.4GHz. Melhor conexão entre os extensores para a performance ideal com potência de até -55dBm", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 155
            "question_text": "O modelo de comercialização do Mesh CBN AP5541 será no formato:",
            "options": [
                ("O modelo de comercialização do Mesh CBN será no formato Aluguel, ou seja, o cliente paga uma mensalidade para cada extensor instalado e a Claro fica responsável pela assistência e manutenção desses aparelhos", "A"),
                ("O modelo de comercialização do Mesh CBN será no formato Mercantil, no qual o Cliente compra o equipamento, porém a Claro não fica responsável pela manutenção desses aparelhos.", "B"),
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 156
            "question_text": "Selecione a alternativa correta sobre as vantagens do Wi-Fi Mesh CBN?",
            "options": [
                ("Ampliar a cobertura na casa do cliente, criando uma rede inteligente que determina o melhor ponto de conexão para cada dispositivo.", "A"),
                ("Ampliar a cobertura do sinal igual um sistema de repetidores, onde o cliente pode se deslocar sem queda do sinal wi-fi.", "B"),
                ("Criar uma rede com performance melhor do que o cabo ethernet.", "C"),
                ("Somente ampliar cobertura do sinal.", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 157
            "question_text": "Para os cenários onde a instalação é com eMTA/ONT de outras marcas, no qual o extensor é a 1° célula da rede mesh, qual o procedimento deve ser adotado?",
            "options": [
                ("Deixar o Wi-Fi do eMTA do cliente ativo normalmente, com isso haverá um balanceamento entre as redes, o que é ótimo pra rede mesh.", "A"),
                ("Desativar o Wi-Fi do eMTA/ONT do cliente, para que o dispositivo acesse à rede Wi-Fi Mesh exclusivamente através dos extensores, além de configurar o extensor principal em modo router.", "B"),
                ("Configurar as redes Wi-Fi de 2.4GHz e 5GHz com SSID distintos, para que o cliente escolha em qual rede conectar.", "C"),
                ("Ativar o BandSteering e configurar os extensores como Acess Point.", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 158
            "question_text": "Para a instalação dos extensores Mesh, a Claro recomenda:",
            "options": [
                ("Se a área for de até 60m² podemos instalar dois extensores Wi-Fi mesh, se for 90m² podemos instalar três extensores, ou seja um extensor a cada 30m².", "A"),
                ("Se a área for de até 150m² podemos instalar um extensor para cada comodo, totalizando três extensores.", "B"),
                ("Se a área for de até 200m² podemos instalar 02 estensores wi-fi mesh para uma cobertura ideial.", "C"),
                ("Um extensor é sufuciente para cobrir uma residência de alvenaria.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 159
            "question_text": "Ao iniciar uma instalação você identifica que não há disponibilidade de HP no TAP da rede externa. Ao entrar em contato com o COP Tivit/TelTelematica e certificar que as casas conectadas fisicamente ao TAP são Clientes ativos, o que você deve fazer?",
            "options": [
                ("Não realizar a instalação e solicitar ao operador para realizar a baixa da O.S com o código #205 e abrir a ocorrência PE1", "A"),
                ("Tentar resolver o problema por conta própria, realizando a instalação sem a disponibilidade de HP no TAP e registrando a situação posteriormente.", "B"),
                ("Aguardar a disponibilidade de HP no TAP da rede externa antes de prosseguir com a instalação, garantindo assim a qualidade do serviço.", "C"),
                ("Informar ao COP Tivit/TelTelematica sobre a falta de disponibilidade de HP no TAP, aguardar suas instruções e seguir as orientações fornecidas para resolver a situação.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 160
            "question_text": "Apos uma instalação, o técnico identificou no terminal que o nivel de SNR de downstream estava fora do padrão. Selecione a alternativa que contem a possivel causa para esse problema:",
            "options": [
                ("Interferência externa de sinais de rádio.", "A"),
                ("Problemas na fonte de alimentação do decodificador.", "B"),
                ("Falta de Torque nos terminais, e nos passivos de instalação.", "C"),
                ("Instabilidade na rede de distribuição de sinal.", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 161
            "question_text": "O que você entende por DOCSIS?",
            "options": [
                ("Padrão utilizado para interface de transmissão de dados via cabo", "A"),
                ("Padrão utilizado para interface de recepção de imagem via cabo", "B"),
                ("É a tecnologia utilizada nos eMTA's a partir da velocidade de 50 Mega;", "C"),
                ("É a tecnologia utilizada em todos os decodificadores HD para o recebimento do sinal através do cabo.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 162
            "question_text": "Porque utilizamos o Canal Alto como referência para calcularmos a perda de sinal?",
            "options": [
                ("Porque o Canal Alto tem menor atenuação de sinal em comparação com o Canal Baixo.", "A"),
                ("O Canal Alto possui maior capacidade de transmissão de dados, portanto, é usado como referência.", "B"),
                ("A perda de sinal é menor no Canal Alto devido à sua posição geográfica em relação ao transmissor.", "C"),
                ("Devido a característica do cabo coaxial sofrer maior perca nas frequencias mais altas.", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 163
            "question_text": "Sobre a função AUTODESLIGAR nos decodificadores HDNGs, qual é o procedimento mais adequado a ser realizado durante o atendimento?",
            "options": [
                ("Desabilitar a função AUTODESLIGAR sem informar o cliente para evitar interrupções no funcionamento do decodificador.", "A"),
                ("A função AUTODESLIGAR não deve ser desabilitado e o cliente deve ser informado sobre essa funcionalidade, para que o decodificador sempre fique atualizado com as ultimas versões de software.", "B"),
                ("Não realizar nenhuma ação em relação à função AUTODESLIGAR, pois isso não afeta o desempenho do equipamento.", "C"),
                ("Informar ao cliente que a função AUTODESLIGAR é opcional e não necessária para o funcionamento correto do decodificador.", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 164
            "question_text": "Para a banda de retorno e em condições normais, qual das modulações abaixo produz um melhor desempenho do sistema de transmissão?",
            "options": [
                ("32 QAM", "A"),
                ("8 QAM", "B"),
                ("QPSK", "C"),
                ("64 QAM", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 165
            "question_text": "O ruído é um dos principais fatores de defeitos nos produtos Claro. Como é possível evitar ingresso de ruído na instalação?",
            "options": [
                ("Deixando os conectores frouxos", "A"),
                ("Passando o cabeamento junto de redes elétricas", "B"),
                ("Deixando os conectores todos sem crimpar", "C"),
                ("Crimpando todos os conectores e aplicando torque em todas as conexões", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 166
            "question_text": "Utilizando como referência os níveis de sinal - Canal Alto 15 dBmV; Canal Baixo 12 dBmV, quais níveis estarão na saída TAP do DC 06?(Componentes Passivos 1 - EAD)",
            "options": [
                ("CA: 12,5 dBmV, CB: 9,5 dBmV", "A"),
                ("CA: 13,5 dBmV, CB: 10,5 dBmV", "B"),
                ("CA: 15 dBmV, CB: 12 dBmV", "C"),
                ("CA: 9 dBmV, CB: 06 dBmV", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 167
            "question_text": "Usando como referência o sinal de 19 dBmV em 550 MHz, ao passar por um DC 12 dB, qual o valor do sinal nas saídas OUT e TAP, respectivamente? (EAD - Componentes Passivo 1)",
            "options": [
                ("16 dBmV e 7 dBmV", "A"),
                ("17 dBmV e 8 dBmV", "B"),
                ("18 dBmV e 7 dBmV", "C"),
                ("19 dBmV e 8 dBmV", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 168
            "question_text": "Os modems instalados na casa dos clientes realizam uma comunicação com o CMTS. Através de qual canal estes modems RECEBEM o sinal?",
            "options": [
                ("CANAL DO DIRETO", "A"),
                ("CANAL DE RETORNO", "B"),
                ("CANAL FECHADO", "C"),
                ("CANAL ABERTO", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 169
            "question_text": "Um Técnico está realizando uma Adesão constatou que os sinais que o cliente estava RECEBENDO estavam fora do padrão. Quais sinais o Tecnico está observando?",
            "options": [
                ("Canal Alto", "A"),
                ("Canal Baixo", "B"),
                ("RX", "C"),
                ("Todas as alternativas.", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 170
            "question_text": "A migração do IPv4 para o IPv6 exige que configuremos o e-MTA do cliente em qual modo? (TRILHA IPV6/CGNAT)",
            "options": [
                ("Bridge", "A"),
                ("Cable", "B"),
                ("eMTA", "C"),
                ("Router", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 171
            "question_text": "Qual  a atenuação de um divisor three way Balanceado?",
            "options": [
                ("6dB em todas as portas", "A"),
                ("4,5dB em todas as portas", "B"),
                ("8dB em todas as portas", "C"),
                ("4,5/7,5/7,5dB", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 172
            "question_text": "O que é o Band Steering?",
            "options": [
                ("Band Steering é uma funcionalidade que estimula os dispositivos dos clientes a se conectarem na melhor frequência disponível e compatível no local.", "A"),
                ("O Band Steering permite apenas a conexão em 5GHz.", "B"),
                ("O Band Steering permite apenas a conexão em 2.4GHz", "C"),
                ("O Band steering é a função de desbloqueio dos eMTAs", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 173
            "question_text": "Ao instalar o produto Claro Virtua em uma residência, é necessário configurar o Wi-Fi e conectar dispositivos via cabo de rede. Qual modo de operação do eMTA para garantir conectividade para todos os dispositivos?",
            "options": [
                ("Modo Bridge", "A"),
                ("Modo Bridge + WAN", "B"),
                ("Modo Router", "C"),
                ("Modo Flyer", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 174
            "question_text": "Qual o comando usado no CMD para medir o tempo de resposta da comunicação entre o seu computador e o servidor de destino?",
            "options": [
                ("Ipconfig", "A"),
                ("Ping", "B"),
                ("Ipconfig/all", "C"),
                ("Flush DNS", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 175
            "question_text": "Os dispositivos Wi-Fi 6 funcionam com as frequências:",
            "options": [
                ("Somente 5GHz", "A"),
                ("Somente 2.4GHz", "B"),
                ("2.4GHz e 5GHz", "C"),
                ("Somente 6GHz", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 176
            "question_text": "Diferente dos decodificadores tradicionais, o 'SAGEMCOM S4KCW3' reúne as duas tecnologias 'HFC' e 'IPTV' no mesmo terminal. Selecione a alternativa correta para utilização em clientes com pacote HFC: (T1 Nº 318 - DECODIFICADOR 4K SAGEMCOM S4KCW3)",
            "options": [
                ("Esse modelo não possui tecnologia IPTV", "A"),
                ("Esse modelo possui uma entrada RF, porém não será utilizada. A recepção do sinal de TV e os demais recursos de interatividade do decodificador (Replay TV, NOW, Apps, etc) funcionarão via internet.", "B"),
                ("Esse modelo possui uma entrada RF que será utilizada para recepção do sinal de TV e para sincronizar o modem interno que é responsável pelos recursos de interatividade do decodificador (Replay TV, NOW, Apps, etc) funcionarão via internet.", "C"),
                ("Esse modelo possui uma entrada RF para conexão do cabo do coaxial. Essa entrada será responsável pela recepção do sinal de TV (QAM). A ligação via Internet é obrigatória para o funcionamento da interatividade com o decodificador (Replay TV, NOW, Apps, etc).", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 177
            "question_text": "O que são Transceptores Ópticos?",
            "options": [
                ("Equipamentos ativos que convertem sinal RF em óptico e óptico em RF", "A"),
                ("Equipamentos ativos que convertem sinal óptico em RF", "B"),
                ("Equipamentos passivos que convertem sinal óptico em RF", "C"),
                ("Equipamentos passivos que convertem sinal RF em óptico e", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 178
            "question_text": "O espectro de frequências dentro do cabo se divide em dois sentidos:",
            "options": [
                ("Canal de Retorno e Canal do Direto.", "A"),
                ("Canal Alto e Canal Baixo.", "B"),
                ("Canal Aberto e Canal Fechado.", "C"),
                ("Canal RX e Canal TX.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 179
            "question_text": "A Tecnologia MIMO (Multiple-Input Multiple-Output) já é presente em eMTAs com padrão 802.11ac. O que isso significa comparado aos eMTAs sem essa tecnologia? (Vídeo Aula Freq e Segur das redes Wi-Fi App Conectado)",
            "options": [
                ("A tecnologia MIMO permite que o dispositivo do cliente alterne automaticamente entre as redes de 2.4 e 5.8 GHz, equanto os terminais sem essa tecnologia não possui esse recurso.", "A"),
                ("A tecnologia MIMO permite que o dispositivo do cliente alterne automaticamente entre os canais de transmissão, equanto os terminais sem essa tecnologia não possui esse recurso.", "B"),
                ("A tecnologia MIMO consegue alcançar maiores taxas de transmissão em redes sem fio, usando várias antenas que transmitem sinais simultâneamente, enquanto os terminais sem essa tecnologia transmite sinal apenas para um dispositivo por vez.", "C"),
                ("É a tecnologia no qual você configura a largura do canal de transmissão no modo de múltiplas antenas, ou seja automático, para que o Cliente consiga usufruir a sua rede sem fio com a máxima performance e velocidade.", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 180
            "question_text": "O local de instalação do eMTA é ponto chave para minimizar problemas referente a cobertura do sinal wi-fi na residência do cliente, portanto:",
            "options": [
                ("Você deve posicionar o eMTA na cozinha, pois é sempre o lugar em que ficam mais pessoas dentro de uma casa e desde que o sinal esteja em -70dBm não há com o que se preocupar com os demais cômodos.", "A"),
                ("No ponto mais alto da residência do cliente, ou seja no teto ou sótão, pois assim o sinal se propagará sem interferência ou barreiras. O sinal deve estar entre -70 dBm e -90dBm no ponto que o cliente mais usa.", "B"),
                ("Você deve posicionar o eMTA no quarto com cobertura entre -10dBm e -70dBm, pois geralmente é onde o cliente estuda ou trabalha. Os demais cômodos podem estar com 20% de cobertura.", "C"),
                ("Você deve perguntar qual o local em que a família mais usa o Wi-Fi, depois identificar o cômodo central entre os locais informados pelo cliente para que o sinal chegue em pelo menos 80% dos cômodos da casa entre -10dBm e -70dBm.", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 181
            "question_text": "Um cliente com produto Streaming (Claro Box TV) solicitou uma mudança de pacote para HFC(Cabo) em seu único ponto de TV com um decodificador S4KCW3. Selecione o procedimento correto para essa mudança: (T1 N° 342 - S4KCW3 MUDANÇA DE PACOTE STREAMING PARA HFC)",
            "options": [
                ("O decodificador não deverá ser trocado, pois já possui uma entrada RF. O técnico deverá realizar a instalação dos cabos coaxiais, conectar no decodificador e baixar a tarefa de mudança de pacote no TOA para liberar o Software HFC.", "A"),
                ("O decodificador deverá ser trocado por decodificadores que não são usados em pacotes Streaming (Box Claro TV)", "B"),
                ("O decodificador deverá ser trocado, pois não possui uma entrada de RF.", "C"),
                ("O decodificador não deverá ser trocado, pois já possui uma entrada RF. O técnico deverá primeiro atualizar o Software para HFC e na sequência realizar a instalação dos cabos coaxiais.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 182
            "question_text": "O cliente adquiriu uma TV 4K com aplicativos de programação que transmitem conteúdos em Ultra HD. Essa TV será conectada via Wi-Fi e além de ser compatível ela recebe com qualidade as 2 redes (2.4 e 5 GHz) disponibilizadas pelo eMTA dual band. Das opções a seguir, qual é adequada para essa instalação?",
            "options": [
                ("Conectar a Tv na rede de 2,4 Ghz que sofre menos interferência apesar da banda de transmissão ser menor", "A"),
                ("Conectar a Tv na rede de 2,4 Ghz que sofre mais interferência e possui uma banda de transmissão maior", "B"),
                ("Conectar a Tv na rede de 5 Ghz que sofre mais interferência apesar da banda de transmissão ser maior", "C"),
                ("Conectar a Tv na rede de 5 Ghz que sofre menos interferência e possui uma banda de transmissão maior", "D")
            ],
            "correct_answer": "D",
            "image": None
        },
        {  # 183
            "question_text": "Para configurar corretamente um IP Fixo em nosso eMTA, precisamos de quais informações? (EAD Procedimentos NET Virtua II)",
            "options": [
                ("Endereço IP, Máscara de rede, Gateway e DNS primário e secundário.", "A"),
                ("Endereço IP, Máscara de rede, Gateway.", "B"),
                ("Apenas do Endereço IP.", "C"),
                ("Não configuramos IP Fixo em nossos eMTA's.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 184
            "question_text": "Em todas as situações de atendimento, temos a obrigação de encantar o cliente e direcioná-lo para a melhor experiência com os produtos e serviços oferecidos. Das opções a seguir, quais são as informações que não podem faltar durante um atendimento de excelência?",
            "options": [
                ("Telefone da Central de atendimento, telefone do coordenador", "A"),
                ("Utilização do Now, Instruções do controle Remoto, Apresentação do aplicativo MINHA CLARO RESIDENCIAL", "B"),
                ("Nunca esqueça de informar seu telefone para caso o cliente precise", "C"),
                ("Todas as opções estão corretas", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 185
            "question_text": "Sobre a Autoinspecção é correto afirmar que: (T1 294)."
                             "I. A funcionalidade de Autoinspecção deve ser utilizada em novas Instalações e Mudança de Endereço."
                             "II. Para as visitas improdutivas, o Botão de Inspeção deverá ser utilizado também para registrar eventos como: Chuva, Endereço não localizado, Entrada não autorizada e Área de risco."
                             "III. No campo de observações, coloque informações pertinentes à vistoria realizada."
                             "IV. A Autoinspecção tira a obrigatoriedade do preenchimento da OS Digital.",
            "options": [
                ("I, II e III estão incorretas", "A"),
                ("I, II e IV estão corretas", "B"),
                ("I, II e III estão corretas", "C"),
                ("I, II e IV estão incorretas", "D")
            ],
            "correct_answer": "C",
            "image": None
        },
        {  # 186
            "question_text": "Um cliente está realizando um download de um arquivo de aproximadamente 4GB, sua taxa de transferência segue constante em 3,75MBps. Sabendo que a velocidade aceitável é no mínimo 80% da velocidade contratada pelo cliente, qual a velocidade contratada neste caso?",
            "options": [
                ("10 Mbps;", "A"),
                ("30 Mbps;", "B"),
                ("1500 Kbps;", "C"),
                ("27 MBps.", "D")
            ],
            "correct_answer": "B",
            "image": None
        },
        {  # 187
            "question_text": "Sobre a confecção de conectores: ''Não é aconselhável encostar os dedos no condutor central, pois, o suor e outras substâncias liberadas pelas mãos, oxidam o condutor central. Talvez a oxidação não seja percebida em um curto tempo, mas a longo prazo ela poderá resultar em problemas no sinal.'' A afirmação acima é:",
            "options": [
                ("Verdadeira, devemos utilizar de pincel/escova apropriada, para abaixar a malha e não contaminar o conector.", "A"),
                ("Falso, não devemos utilizar de pincel/escova para abaixar a malha. Pois o conector e malha já vem com uma proteção específica.", "B"),
                ("Verdadeira, é proibido utilizar qualquer tipo de ferramenta ou equipamento. Pois pode danificar o condutor central e a malha do cabo.", "C"),
                ("Todas as alternativas estão erradas.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 188
            "question_text": "A respeito da Norma Regulamentadora no 35 (NR-35) – Trabalho em Altura, no que diz respeito e cabe ao empregador quanto à avaliação do estado de saúde dos trabalhadores que exercem atividade em altura, assinale a alternativa correta.",
            "options": [
                ("A NR-35 não estabelece periodicidade para avaliação dos trabalhadores que executam trabalho em altura; cabe ao médico responsável estabelecer a periodicidade dos exames, considerar a relevância da NR-07 e analisar o histórico de cada trabalhador.", "A"),
                ("Os exames médicos realizados, bem como a sistemática implementada, para trabalhadores em altura, não fazem parte do Programa de Controle Médico de Saúde Ocupacional (PCMSO) da empresa, considerando-se a situação desses trabalhadores uma situação a se trat.", "B"),
                ("De acordo com a NR-35, a avaliação de saúde do trabalhador em altura deve ser realizada trimestralmente e contemplar a avaliação de esforço físico; a avaliação de acuidade visual só precisa ser realizada uma vez a cada ano.", "C"),
                ("De acordo com a NR-35 e com a NR-07, os trabalhadores com histórico de epilepsia, desde que devidamente medicados, podem participar do quadro de trabalhadores em altura.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
        {  # 189
            "question_text": "Um EMTA passa por um processo chamado de sincronismo, onde é estabelecido uma comunicação com o CMTS. A respeito deste processo, selecione a alternativa correta:",
            "options": [
                ("RX é o sinal que vem por meio das portadoras de Downstream, enquanto o TX é o sinal que trafega por meio das portadoras de Upstream.", "A"),
                ("Quanto maior o pacote de internet contratado pelo cliente, mais rápido é realizado sincronismo.", "B"),
                ("No sincronismo do EMTA os sinais de CA e CB devem estar com suas potências dentro do padrão, -5dBmV até 5 dBmV.", "C"),
                ("O sincronismo do equipamento vai acontecer quando o técnico solicitar a habilitação do EMTA para que o serviço de internet seja disponibilizado.", "D")
            ],
            "correct_answer": "A",
            "image": None
        },
    ]

    # Limpar o banco de dados anterior (opcional)
    c.execute("DELETE FROM questions")
    c.execute("DELETE FROM options")

    # Inserir perguntas e alternativas
    for question in questions:
        c.execute('''
            INSERT INTO questions (question_text, correct_answer, image) VALUES (?, ?, ?)
        ''', (question['question_text'], question['correct_answer'], question['image']))
        question_id = c.lastrowid

        for option in question['options']:
            c.execute('''
                INSERT INTO options (question_id, option_text, option_label) VALUES (?, ?, ?)
            ''', (question_id, option[0], option[1]))

    conn.commit()
    conn.close()

    print("Banco de dados criado com sucesso.")

if __name__ == '__main__':
    create_db()
