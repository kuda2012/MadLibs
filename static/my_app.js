const inputs = document.getElementsByClassName("inputText");
const form = document.getElementById("theForm");
const submitButton = document.getElementById("submitButton");

form.addEventListener("submit", function (evt) {
  evt.preventDefault();
  //   console.log(inputs);
  for (input of inputs) {
    if (input.value === "") return;
  }
  form.action = "/story";
  form.submit();
});
