const chatContainer = document.getElementById('chat');
const userInput = document.getElementById('user-input');

function appendMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.className = sender;
    messageElement.innerText = message;
    chatContainer.appendChild(messageElement);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function sendMessage() {
    const userMessage = userInput.value.trim();
    if (userMessage !== '') {
        appendMessage(`You: ${userMessage}`, 'user');
        userInput.value = '';

        // Send user message to Flask server (replace with your actual endpoint)
        fetch('http://127.0.0.1:5000', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: userMessage }),
        })
        .then(response => response.json())
        .then(data => {
            const botMessage = data.message;
            appendMessage(`Bot: ${botMessage}`, 'bot');
        })
        .catch(error => console.error('Error:', error));
    }
}
