class automate {
  constructor() {
    this.lista = [];
  }
  logic(cadena) {
    let estado = true;
    let posicion = 0;
    let size = cadena.length;
    this.state0(cadena, posicion, size, estado);

    let lista_comparacion = [["Q0", "bbaaababbabbaab", "L"],
    ["Q0", "baaababbabbaab", "C"],
    ["Q0", "aaababbabbaab", "L"],

    ["Q1", "aababbabbaab", "C"],
    ["Q1", "ababbabbaab", "C"],
    ["Q1", "babbabbaab", "L"],

    ["Q2", "abbabbaab", "R"],
    ["Q1", "bbabbaab", "L"],
    ["Q2", "babbaab", "L"],

    ["Q3", "abbaab", "C"],
    ["Q3", "bbaab", "C"],
    ["Q3", "baab", "C"],
    ["Q3", "aab", "C"],
    ["Q3", "ab", "C"],
    ["Q3", "b", "C"],];

    for (let i = 0; i < this.lista.length; i++) {
      let aux = this.lista[i];
      let aux2 = lista_comparacion[i];

      let aux3 = aux + " " + aux2;
      console.log(aux3);
    }
  }

  state0(cadena, posicion, size, estado) {
    if (cadena[posicion] == "b") {
      /* console.log(cadena[posicion]); */
      this.lista.push(["Q0", cadena.substring(posicion, size), "L"]);
      console.log(cadena.substring(posicion, size));
      posicion++;

      while (cadena[posicion] == "b") {
        /* console.log(cadena[posicion]); */
        this.lista.push(["Q0", cadena.substring(posicion, size), "C"]);
        console.log(cadena.substring(posicion, size));
        posicion++;
      }
    }
    if (cadena[posicion] == "a") {
      /* console.log(cadena[posicion]); */
      this.lista.push(["Q0", cadena.substring(posicion, size), "L"]);
      console.log(cadena.substring(posicion, size));

      if (posicion == size) {
        this.lista.push(["Q0", "Q0 no  pertenece a los estados finales", "T"]);
        console.log("Q0 no  pertenece a los estados finales");
        return false;
      }
      else {
        posicion++;
        this.state1(cadena, posicion, size, estado);
      }
    }
    else {
      this.lista.push(["Q0", "Q0 no  pertenece a los estados finales", "F"]);
      console.log("Q0 no  pertenece a los estados finales");
      return false;
    }
  }

  state1(cadena, posicion, size, estado) {
    while (cadena[posicion] == "a") {
      /*  console.log(cadena[posicion]); */
      this.lista.push(["Q1", cadena.substring(posicion, size), "C"]);
      console.log(cadena.substring(posicion, size));
      posicion++;
    }


    if (cadena[posicion] == "b") {
     /*  console.log(cadena[posicion]); */;
      console.log(cadena.substring(posicion, size));
      this.lista.push(["Q1", cadena.substring(posicion, size), "L"]);


      if (posicion == size) {
        this.lista.push(["Q1", "Q1 no  pertenece a los estados finales", "T"]);
        console.log("Q1 no  pertenece a los estados finales");
        return false;
      }
      else {
        posicion++;
        this.state2(cadena, posicion, size, estado);
      }
    }
    else {
      this.lista.push(["Q1", "Q1 no  pertenece a los estados finales", "T"]);
      console.log("Q1 no  pertenece a los estados finales");
      return false;
    }
  }

  state2(cadena, posicion, size, estado) {
    if (cadena[posicion] == "b") {
      /* console.log(cadena[posicion]); */
      console.log(cadena.substring(posicion, size));
      this.lista.push(["Q2", cadena.substring(posicion, size), "L"]);
      console.log(cadena.substring(posicion, size));

      if (posicion == size) {
        this.lista.push(["Q2", "Q2 no  pertenece a los estados finales", "T"]);
        console.log("Q2 no  pertenece a los estados finales");
        return false;
      }

      if (cadena[posicion] == "a") {
        /* console.log(cadena[posicion]); */
        this.lista.push(["Q2", cadena.substring(posicion, size), "R"]);
        console.log(cadena.substring(posicion, size));
        posicion++;

        this.state1(cadena, posicion, size, estado);
      }
      else {
        /* console.log(cadena[posicion]); */
        this.lista.push(["Q2", cadena.substring(posicion, size), "L"]);
        console.log(cadena.substring(posicion, size));
        this.state3(cadena, posicion, size, estado);
      }
    }

    else if ((cadena[posicion] == "a")) {
      posicion++;
      /*  console.log(cadena[posicion]); */
      this.lista.push(["Q2", cadena.substring(posicion, size), "R"]);
      console.log(cadena.substring(posicion, size));

    }
    else {
      this.lista.push(["Q2", "Q2 no  pertenece a los estados finales", "T"]);
      console.log("Q2 no  pertenece a los estados finales");
      return false;
    }
  }

  state3(cadena, posicion, size, estado) {
    while (cadena[posicion] == "a" || cadena[posicion] == "b" && posicion != size) {
      /* console.log(cadena[posicion]); */
      this.lista.push(["Q3", cadena.substring(posicion, size), "C"]);
      console.log(cadena.substring(posicion, size));
      posicion++;
    }

    if (posicion == size) {
      this.lista.push(["Q3", "Q3 pertenece a los estados finales", "F"]);
      console.log("Q3 pertenece a los estados finales");
      return true;
    }
    else {
      this.lista.push(["Q3", "Q3 no  pertenece a los estados finales", "T"]);
      console.log("Q3 no  pertenece a los estados finales");
      return false;
    }
  }
}

const automata = new automate();
automata.logic("bbaaababbabbaab");  // Punto 1