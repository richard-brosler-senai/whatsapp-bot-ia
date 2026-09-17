const statusElement = document.querySelector("#status");
const chatElement = document.querySelector("#chat");
const messageInput = document.querySelector("#message");
const sendButton = document.querySelector("#send");


async function checkStatus() {

    try {

        const response = await fetch("/api/health");

        if (!response.ok) {
            throw new Error("Erro ao consultar API");
        }

        const data = await response.json();

        statusElement.textContent =
            `Online - ${data.environment}`;

    } catch (error) {

        statusElement.textContent =
            "Servidor indisponível";

    }

}


function addMessage(text, type) {

    const message = document.createElement("div");

    message.classList.add(
        type === "user"
            ? "user-message"
            : "bot-message"
    );

    message.textContent = text;

    chatElement.appendChild(message);

    chatElement.scrollTop =
        chatElement.scrollHeight;
}


function sendMessage() {

    const text = messageInput.value.trim();

    if (!text) {
        return;
    }

    addMessage(text, "user");

    messageInput.value = "";

    // Resposta temporária
    setTimeout(() => {

        addMessage(
            "A integração com a Groq será implementada na próxima etapa.",
            "bot"
        );

    }, 500);

}


sendButton.addEventListener(
    "click",
    sendMessage
);


messageInput.addEventListener(
    "keydown",
    event => {

        if (event.key === "Enter") {
            sendMessage();
        }

    }
);


checkStatus();