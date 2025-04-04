let characterSW = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((result) => result.json())
  .then((data) => {
    characterSW.textContent = data.name;
  })
  .catch(() => {
    characterSW.textContent = 'Error fetching character';
  });
