function getPokemon(a) {
    for (var i = 1; i <= a; i++) {
        $("#pokeList").append(`<img id="` + i + `" src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/` + i + `.png" alt="Pokemon #` + i + `">`);
    }
}
getPokemon(150);