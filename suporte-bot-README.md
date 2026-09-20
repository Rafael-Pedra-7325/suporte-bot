# 🤖 SuporteBot

Chatbot de atendimento baseado em regras (correspondência de palavras-chave por intenção), com um widget de chat web em Flask — sem depender de modelos de linguagem externos ou conexão com a internet.

## ✨ Funcionalidades
- Reconhecimento de intenções por palavras-chave (saudação, horário, contato, preço, reclamação, despedida)
- Resposta padrão ("fallback") quando nada é reconhecido
- Histórico de conversa em memória
- Widget de chat web (HTML/CSS/JS) consumindo uma API Flask

## 🏗️ Arquitetura
```
suporte-bot/
├── app.py            # API Flask (rota /api/chat)
├── chatbot.py         # motor de regras do bot (sem Flask, testável isoladamente)
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── tests/
    └── test_chatbot.py
```

A lógica do bot (`chatbot.py`) é totalmente desacoplada do Flask — pode ser testada, reaproveitada em uma CLI ou plugada em outro canal (Telegram, WhatsApp) sem alterações.

## 🚀 Como executar
```bash
pip install -r requirements.txt
python app.py
```
Acesse `http://localhost:5002`.

## 📖 Endpoint da API

| Método | Rota | Descrição |
|---|---|---|
| POST | `/api/chat` | Envia `{"mensagem": "..."}` e recebe `{"resposta": "...", "intencao": "..."}` |

## 🧠 Conceitos praticados
- Lógica de NLP básica por correspondência de palavras-chave
- Separação entre lógica de negócio (`chatbot.py`) e camada web (`app.py`)
- Consumo de API via `fetch` no front-end
- Testes automatizados cobrindo cada intenção e o caso de fallback

## 🧪 Testes
```bash
python -m unittest tests.test_chatbot -v
```

## 🔭 Próximos passos
- Persistir o histórico por usuário/sessão em banco de dados
- Integração com WhatsApp/Telegram via webhook
- Evoluir a correspondência por palavras-chave para um modelo de NLP mais robusto
