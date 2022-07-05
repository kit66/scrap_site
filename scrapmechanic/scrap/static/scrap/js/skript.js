let content = document.getElementById("content")
let show = document.getElementById("showContent")
let hide = document.getElementById("hideContent")

show.addEventListener("click", () => {
    content.style.display = "block"
})

hide.addEventListener("click", () => {
    content.style.display = "none"
})