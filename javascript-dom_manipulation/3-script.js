const header = document.querySelector("header");
const toggle_header = document.getElementById("toggle_header")
toggle_header.addEventListener("click", () => {
  if (header.classList.contains("green")) {
    header.classList.add("red");
    header.classList.remove("green");
  } else {
    header.classList.add("green");
    header.classList.remove("red");
  }
});
