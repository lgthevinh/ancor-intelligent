function showGPT(btnId){
    document.getElementById("ask-gpt").classList.remove("d-none");
    document.getElementById("edit-mistake").classList.add("d-none");
    document.getElementById("create-image").classList.add("d-none");

    var btnGroup = document.querySelectorAll(".btn");
    for(let i = 0; i < btnGroup.length; i++){
        btnGroup[i].classList.remove("active")
    }
    document.getElementById(btnId).classList.add("active");
}

function showMistake(btnId){
    document.getElementById("ask-gpt").classList.add("d-none");
    document.getElementById("edit-mistake").classList.remove("d-none");
    document.getElementById("create-image").classList.add("d-none");

    var btnGroup = document.querySelectorAll(".btn");
    for(let i = 0; i < btnGroup.length; i++){
        btnGroup[i].classList.remove("active")
    }
    document.getElementById(btnId).classList.add("active");
}

function showImage(btnId){
    document.getElementById("ask-gpt").classList.add("d-none");
    document.getElementById("edit-mistake").classList.add("d-none");
    document.getElementById("create-image").classList.remove("d-none");

    var btnGroup = document.querySelectorAll(".btn");
    for(let i = 0; i < btnGroup.length; i++){
        btnGroup[i].classList.remove("active")
    }
    document.getElementById(btnId).classList.add("active");
}