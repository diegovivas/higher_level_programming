$.getJSON( "https://swapi.co/api/people/5/?format=json", function( json ) {
  $("#character").text(json.name);
 });
