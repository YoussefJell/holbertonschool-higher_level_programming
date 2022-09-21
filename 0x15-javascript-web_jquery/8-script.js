$(function () {
  $.get("https://swapi-api.hbtn.io/api/people/5/?format=json", function (data) {
    for (const movie of data.results) {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    }
  });
});
