import random

import pip
from flask import Flask, render_template, request

app = Flask(__name__)

# Lista de perguntas e respostas (adicione suas 200+ perguntas aqui)
perguntas = [
    {"pergunta": "Na falta da etiqueta Wi-Fi (usuário e senha do EMTA) o que deve ser realizado?",
     "alternativas": ["Anotar a numeração do SSID e SENHA em qualquer local da OS.",
                      "É obrigatório o preenchimento das informações SSID e SENHA no campo observação da OS.",
                      "Pedir para que o cliente entre em contato com a central de atendimento.",
                      "Deixar o seu numero de telefone para o cliente te ligar quando necessário."],
     "resposta_correta": "É obrigatório o preenchimento das informações SSID e SENHA no campo observação da OS."},
    {"pergunta": "Conforme procedimento de Baixa na URA, para o MAC 0023754F1608, é necessário digitar para o "
                 "caractere hexadecimal ( F ) :", "alternativas": ["*6", "*06", "6", "#6"], "resposta_correta": "*06"},
    {"pergunta": "Qual o procedimento correto para realizar a validação de retorno? ",
     "alternativas": ["Canal 262 + 8291 + Preenchimento do numero da OS e Contrato",
                      "Canal 262 + Menu +8291 Preenchimento do numero da OS e Contrato",
                      "Canal 262 + Menu + Tecla Azul + 8291 + Preenchimento do número da OS e Contrato",
                      "Canal 262 + Tecla Azul + 8291 + Preenchimento do numero da OS e Contrato."],
     "resposta_correta": "Canal 262 + Tecla Azul + 8291 + Preenchimento do numero da OS e Contrato."},
    {"pergunta": "O que é AUTO HIT? ", "alternativas": [
        "Funcionalidade que permite o envio automático de HIT pelo controle remoto em equipamentos HD e HDMAX.",
        "Funcionalidade que permite o envio automático de HIT pelo controle remoto em equipamentos SD, HD e HDMAX.",
        "Funcionalidade que permite o reset do decodificador e suas configurações através do controle remoto.",
        "Todas as alternativas estão corretas"],
     "resposta_correta": "Funcionalidade que permite o envio automático de HIT pelo controle remoto em equipamentos HD e HDMAX."},
    {
        "pergunta": "Dos padrões de redes Wi-Fi abaixo, qual nos proporciona a maior velocidade da taxa de transmissão?    ",
        "alternativas": ["g", "n", "a", "ac"], "resposta_correta": "ac"},
    {"pergunta": "Sobre a facilidade CONFIGURAÇÃO SENHA WI FI:", "alternativas": [
        "Com essa nova facilidade nosso cliente conseguiu Consultar, trocar a senha e nome da rede WI-FI de sua casa apenas através do site, ainda não está disponível pelo NETAPP.",
        "Consultar, trocar a senha e nome da rede WI-FI de sua casa através do NET APP e também pelo site MINHA NET.",
        "Consultar, trocar a senha e nome da rede WI-FI de sua casa atraves do NET APP, ainda não está disponível pelo site MINHA NET.",
        "n.d.a"],
     "resposta_correta": "Consultar, trocar a senha e nome da rede WI-FI de sua casa através do NET APP e também pelo site MINHA NET."},
    {
        "pergunta": "O recurso Facebook presente em nossos decodificadores com tecnologia HD NG, permite ao nosso cliente: ",
        "alternativas": [
            "Postar/compartilhar com seus amigos em sua timeline no Facebook, o que está assistindo em sua NET HDTV, direto de seu decodificador",
            "Navegar no Facebook, postar fotos e vídeos direto de sua TV.",
            "Espelhar a tela do Facebook de seu Smartphone ou tablet direto para sua TV.",
            "Todas as alternativas acima"],
        "resposta_correta": "Postar/compartilhar com seus amigos em sua timeline no Facebook, o que está assistindo em sua NET HDTV, direto de seu decodificador"},
    {"pergunta": "O que é Valida Retorno?", "alternativas": [
        "Pacote que dá direito ao cliente acessar via site, da NET os últimos lançamentos dos canais Telecine",
        "Validação dos dados de instalação e confirmação do pacote instalado para que o cliente possa usufruir de todos os recursos do sistema NETTV",
        "Verificação da comunicação do Decoder Digital para que o cliente possa usufruir de todos os recursos do sistema NET TV como compra pelo controle remoto e NOW (vídeo on Demand).",
        "Verificação da comunicação do televisor para que o cliente possa usufruir de todos os recursos do sistema NET TV como Full HD e 4K."],
     "resposta_correta": "Verificação da comunicação do Decoder Digital para que o cliente possa usufruir de todos os recursos do sistema NET TV como compra pelo controle remoto e NOW (vídeo on Demand)."},
    {
        "pergunta": "Qual alternativa corresponde aos problemas causados ao cliente caso ele não seja orientado sobre o uso de senhas?",
        "alternativas": ["Compra de conteúdos do NOW sem os seu conhecimento",
                         "Ligações na central para solicitar estorno de valores referente a compras",
                         "Reclamações nos órgãos de defesa ao consumidor", "Todas as alternativas estão corretas"],
        "resposta_correta": "Todas as alternativas estão corretas"},
    {"pergunta": "São características da fibra óptica.",
     "alternativas": ["Alta atenuação", "Necessidade de amplificação   a cada 2Km",
                      "Maior sensibilidade a interferências eletromagnéticas", "Nenhuma das alternativas."],
     "resposta_correta": "Nenhuma das alternativas."},
    {"pergunta": "Qual é a importância  de um cabo coaxial utilizado em CATV?",
     "alternativas": [" 75 ohms", "50 ohms", "22 ohms", "15 ohms"], "resposta_correta": "75 ohms"},
    {"pergunta": "É considerada interferência na rede HFC:",
     "alternativas": ["Tenção AC gerada  pela fonte acima do regulamento pela ANATEL.",
                      "Sinal de UHF invadindo a faixa de CATV",
                      "Nível alto de   entrada no amplificador, gerando saturação na imagem",
                      "Nível de potência  óptica muito alta no receptor óptico, gerando saturação do link."],
     "resposta_correta": "Sinal de UHF invadindo a faixa de CATV ."},
    {"pergunta": "Dentro do cabo coaxial as frequências sofrem a mesma  atenuação?",
     "alternativas": ["Sim,   tanto as mais altas como as mais baixas possuem atenuação igual",
                      "Não, as  frequências  mais baixas sofrem maior atenuação",
                      "Não,   as  frequências  mais altas sofrem maior  atenuação", " N.d.a"],
     "resposta_correta": "Não,   as  frequências  mais altas sofrem maior  atenuação"},
    {"pergunta": "O que é tilt ?",
     "alternativas": ["Nível de sinal   de portadoras distintas .", "Nível   de sinal   do canal de retorno .",
                      "Diferença entre frequências do canal direto e do canal de   retorno",
                      "Diferença de   sinal entre portadoras  distintas."],
     "resposta_correta": "Diferença de   sinal entre portadoras  distintas."},
    {"pergunta": "Qual a função do cable isolator?",
     "alternativas": ["Proteger a instalação e os equipamentos da rede da   NET  contra picos de tensão de (AC)",
                      "Proteger a rede de cabos em caso de retorno de ac gerado ,   pelo decodificador .",
                      "Isolador com casamento de impedância para adaptar a conexão dos cabos drop com o de distribuição interna.",
                      "Apenas fazer emenda do cabo preto (drop) com o cabo branco de distribuição interna."],
     "resposta_correta": " Proteger a instalação e os equipamentos da rede da NET contra picos de tensão de (AC)."},
    {
        "pergunta": "Se o cliente agendar uma visita para ser atendido das 11:00 às 14:00 e o técnico chegar às 14:20, qual Indicador será afetado?",
        "alternativas": ["ISRA.", "STFC.", " SCM.", " TEC1."], "resposta_correta": " TEC1."},
    {"pergunta": "Qual a função do CMTS?", "alternativas": [" Interligar a rede interna à rede HFC.",
                                                            "Concentrar o s dados da internet para transmitir via upstre am ao cable modem.",
                                                            "Interligar a rede de telefonia com a  internet, gerando o VOIP.",
                                                            "Fazer a comunicação e o gerenciamento dos modems."],
     "resposta_correta": "Fazer a comunicação e o gerenciamento dos modems."},
    {"pergunta": "Qual a definição de MER?",
     "alternativas": ["Taxa de erro de transmissão.", "Taxa de erro de recepção.", "Taxa de erro de modulação.",
                      "Taxa de erro de bit."], "resposta_correta": "Taxa de erro de modulação."},
    {"pergunta": "O que é BER?",
     "alternativas": ["Taxa de erro de  transmissão.", "Taxa de erro de recepção.", "Taxa de erro de modulação.",
                      " Taxa de erro de bit."], "resposta_correta": " Taxa de erro de bit."},
    {"pergunta": "O que é Canal de Retorno?",
     "alternativas": ["Sinal transmitido do equipamento do cliente para o Headend.",
                      "Sinal transmitido do Headend para o cliente.", "Sinal transmitido entre os  Headends.",
                      "Sinal transmitido entre clientes NET."],
     "resposta_correta": "Sinal transmitido do equipamento do cliente para o Headend."},
    {"pergunta": "Qual a relação ao tipo de modulação e a  sensibilidade   ao ruído?",
     "alternativas": ["Quanto maior a modulação maior a sensibilidade  ao ruido.",
                      "Quanto menor a modulação maior a sensibilidade ao  ruido.",
                      "Quanto maior a modulação menor a sensibilidade ao ruído.",
                      "Independente da modulação a sensibilidade ao ruído sempre será a mesma."],
     "resposta_correta": "Quanto maior a modulação maior a sensibilidade  ao ruido."},
    {"pergunta": "O que é Downstream ?",
     "alternativas": ["Sinal que o CMTS envia para o eMTA.", "Sinal  que o eMTA envia para o CMTS.",
                      "Sinal que o medidor envia para o eMTA.", "Sinal que o eMTA envia para o medidor."],
     "resposta_correta": "Sinal que o CMTS envia para o eMTA."},
    {"pergunta": "Quais os sinais que trafegam no Canal de Retorno?",
     "alternativas": ["Canais piloto (alto e baixo).", "Canais de Vídeo.", "Canais de Upstream.",
                      "Todas as  alternativas anteriores."], "resposta_correta": "Canais de Upstream."},
    {"pergunta": "Em relação ao poste da residência do cliente é correto afirmarmos que:",
     "alternativas": [" Utilizamos o suporte da companhia telefônica somente  com autorização de cliente.",
                      " Não é permitida a utilização do suporte da companhia  telefônica.",
                      "É necessário utilizar o U Span Clamp poste somente nos casos em que  instalarmos CLARO  Fone.",
                      "É necessário utilizar o U Span Clamp poste somente se não houver suporte da  companhia telefônica."],
     "resposta_correta": "Não é permitida a utilização do suporte da companhia  telefônica."}

    # Adicione aqui suas outras perguntas...
]


@app.route('/')
def index():
    # Selecionar 20 perguntas aleatórias
    perguntas_selecionadas = random.sample(perguntas, 20)
    return render_template('index.html', perguntas=perguntas_selecionadas)


@app.route('/result', methods=['POST'])
def result():
    respostas = request.form
    pontuacao = 0
    respostas_corretas = {}

    for pergunta in perguntas:
        pergunta_texto = pergunta['pergunta']
        resposta_correta = pergunta['resposta_correta']
        respostas_corretas[pergunta_texto] = resposta_correta

        if respostas.get(pergunta_texto) == resposta_correta:
            pontuacao += 1

    return render_template('result.html', pontuacao=pontuacao, respostas_corretas=respostas_corretas,
                           respostas=respostas)


if __name__ == '__main__':
    app.run(debug=True)
