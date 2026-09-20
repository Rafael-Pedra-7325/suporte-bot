from flask import Flask, jsonify, request, render_template
from chatbot import SuporteBot

app = Flask(__name__)

# Uma instância simples em memória (suficiente para demonstração).
# Em produção, o histórico ficaria por sessão/usuário em um banco de dados.
bot = SuporteBot()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    dados = request.get_json(silent=True) or {}
    mensagem = dados.get("mensagem", "").strip()

    if not mensagem:
        return jsonify({"erro": "Envie uma mensagem no campo 'mensagem'."}), 400

    resposta, intencao = bot.responder(mensagem)
    return jsonify({"resposta": resposta, "intencao": intencao})


if __name__ == "__main__":
    app.run(debug=True, port=5002)
