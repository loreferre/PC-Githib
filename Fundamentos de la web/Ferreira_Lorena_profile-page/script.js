console.log("page loaded...");

function changeName() {
    var username = document.querySelector("#username");
    username.innerText = "New Title";
}



function acceptIcon(id) {
    var requestElement = document.querySelector("#" + id);
    requestElement.remove();
    var requestSpan = document.querySelector(".badge");
    requestSpan.innerText = Number(requestSpan.innerText) - 1;
    var connectionSpan = document.querySelector(".badge-2");
    connectionSpan.innerText = Number(connectionSpan.innerText) + 1;
}

function closeIcon(id) {
    var requestElement = document.querySelector("#" + id);
    requestElement.remove();
    var requestSpan = document.querySelector(".badge");
    requestSpan.innerText = Number(requestSpan.innerText) - 1;
}