const my_list = document.getElementsByClassName("my_list");
const add_item = document.getElementById("add_item");
add_item.addEventListener("click", () => {
  let li_item = document.createElement("li");
  li_item.textContent = "Item";
  my_list[0].appendChild(li_item);
});
