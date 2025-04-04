document.addEventListener('DOMContentLoaded', () => {
  let elem_hello = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((result) => result.json())
    .then((data) => {
      elem_hello.textContent = data.hello;
      })
    .catch(() => {
      elem_hello.textContent = 'Error fetching movies';
    });
});
