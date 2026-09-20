const form = document.getElementById("form-chat");
const input = document.getElementById("input-mensagem");
const mensagens = document.getElementById("mensagens");

function adicionarMensagem(texto, autor) {
  const div = document.createElement("div");
  div.className = `mensagem ${autor}`;
  div.textContent = texto;
  mensagens.appendChild(div);
  mensagens.scrollTop = mensagens.scrollHeight;
}

form.addEventListener("submit", async (evento) => {
  evento.preventDefault();
  const texto = input.value.trim();
  if (!texto) return;

  adicionarMensagem(texto, "usuario");
  input.value = "";

  try {
    const resposta = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ mensagem: texto }),
    });
    const dados = await resposta.json();
    adicionarMensagem(dados.resposta, "bot");
  } catch (erro) {
    adicionarMensagem("Erro ao conectar com o servidor.", "bot");
  }
});
