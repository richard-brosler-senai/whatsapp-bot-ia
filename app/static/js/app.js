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

    message.innerHTML = text;

    chatElement.appendChild(message);

    chatElement.scrollTop =
        chatElement.scrollHeight;

    return message;
}


async function sendMessage() {

    const text = messageInput.value.trim();

    if (!text) {
        return;
    }

    addMessage(text, "user");

    messageInput.value = "";

    messageInput.disabled = true;
    sendButton.disabled = true;

    const loadingMessage =
        addMessage("Pensando...", "bot");

    try {

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: text
            })
        });

        const data = await response.json();

        loadingMessage.remove();

        if (!response.ok) {

            addMessage(
                data.error ||
                "Não foi possível processar a mensagem.",
                "bot"
            );

            return;
        }

        addMessage(
            data.answer,
            "bot"
        );

    } catch (error) {

        loadingMessage.remove();

        addMessage(
            "Não foi possível comunicar com o servidor.",
            "bot"
        );

        console.error(error);

    } finally {

        messageInput.disabled = false;
        sendButton.disabled = false;

        messageInput.focus();
    }
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