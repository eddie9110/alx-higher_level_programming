$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  const reslt = data.results;
  const movie_list = $('ul#list_movies');
  for (let i = 0; i < reslt.length; i++) {
    movie_list.append(`<li>${reslt[i].title}</li>`);
  }
});
