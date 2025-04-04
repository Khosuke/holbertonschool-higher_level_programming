let list_movies = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((result) => result.json())
  .then((data) => data.results.forEach((film) => {
    let title_item = document.createElement("li");
    title_item.textContent = `${film.title}`;
   list_movies.appendChild(title_item);
    }))
  .catch(() => {
    list_movies.textContent = 'Error fetching movies';
  });
