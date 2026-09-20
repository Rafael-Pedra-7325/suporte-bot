"""
SuporteBot
Motor de chatbot baseado em regras (correspondência de palavras-chave por intenção).
Não usa modelos de linguagem externos — ótimo para demonstrar lógica de NLP básica
sem depender de APIs pagas ou conexão com a internet.
"""

import re

INTENCOES = [
    {
        "nome": "saudacao",
        "palavras_chave": ["oi", "ola", "olá", "bom dia", "boa tarde", "boa noite", "eae"],
        "resposta": "Olá! 👋 Sou o assistente virtual de suporte. Posso ajudar com horários, "
                    "contato ou abrir um chamado. O que você precisa?",
    },
    {
        "nome": "horario_funcionamento",
        "palavras_chave": ["horario", "horário", "funciona", "atendimento", "aberto"],
        "resposta": "Nosso atendimento funciona de segunda a sexta, das 9h às 18h (horário de Brasília).",
    },
    {
        "nome": "contato",
        "palavras_chave": ["contato", "telefone", "whatsapp", "email", "e-mail", "falar com"],
        "resposta": "Você pode falar com a equipe pelo e-mail suporte@empresa.com ou pelo WhatsApp "
                    "durante o horário comercial.",
    },
    {
        "nome": "preco",
        "palavras_chave": ["preco", "preço", "valor", "quanto custa", "plano"],
        "resposta": "Temos planos a partir de R$ 29,90/mês. Quer que eu te mostre a tabela completa de planos?",
    },
    {
        "nome": "reclamacao",
        "palavras_chave": ["problema", "reclamacao", "reclamação", "erro", "bug", "nao funciona", "não funciona"],
        "resposta": "Sinto muito pelo transtorno. Vou abrir um chamado para um atendente humano te ajudar. "
                    "Pode descrever o problema com mais detalhes?",
    },
    {
        "nome": "despedida",
        "palavras_chave": ["tchau", "ate mais", "até mais", "obrigado", "valeu", "flw"],
        "resposta": "Por nada! Se precisar de algo mais, é só chamar. Até logo! 👋",
    },
]

RESPOSTA_PADRAO = (
    "Não tenho certeza se entendi. Você pode reformular, ou perguntar sobre "
    "horário de atendimento, contato, preços ou relatar um problema."
)


def _normalizar(texto):
    texto = texto.lower().strip()
    texto = re.sub(r"[^\w\sáàâãéèêíïóôõöúçñ]", "", texto)
    return texto


class SuporteBot:
    def __init__(self):
        self.historico = []

    def responder(self, mensagem):
        texto_normalizado = _normalizar(mensagem)

        melhor_intencao = None
        melhor_pontuacao = 0

        for intencao in INTENCOES:
            pontuacao = sum(
                1 for palavra in intencao["palavras_chave"] if palavra in texto_normalizado
            )
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_intencao = intencao

        resposta = melhor_intencao["resposta"] if melhor_intencao else RESPOSTA_PADRAO
        intencao_detectada = melhor_intencao["nome"] if melhor_intencao else "fallback"

        self.historico.append({"usuario": mensagem, "bot": resposta, "intencao": intencao_detectada})

        return resposta, intencao_detectada
