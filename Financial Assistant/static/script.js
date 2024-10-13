const sendChatBtn = document.querySelector(".chat-input span");
const chatInput = document.querySelector(".chat-input textarea");
const chatBox = document.querySelector(".chatbox");

const url = "http://127.0.0.1:5000/get_response";

let userMsg;

const createChatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);
    let chatContent = className === "outgoing" ? `<p>${message}</p>` : `<span class="material-symbols-outlined">smart_toy</span><p>${message}</p>`;
    chatLi.innerHTML = chatContent;
    return chatLi;
}

const generateResponse = () => {
    $.post(url, {
        userMessage: userMsg
    }, function(data, status){
        console.log(data.bot_msg.toString(), status);
        chatBox.appendChild(createChatLi(data.bot_msg.toString(), "incoming"));
    } );
}

const handleChat = () => {
    userMsg = chatInput.value.trim();
    console.log(userMsg);

    if(!userMsg){
        return;
    }

    chatBox.appendChild(createChatLi(userMsg, "outgoing"));

    setTimeout(() => {
        generateResponse();
    }, 500);
}

sendChatBtn.addEventListener("click", handleChat);