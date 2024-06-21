class prueba{
    entrada(entry){
        let lista = [];
        let cadena = entry;
        let posicion = 0;
        let longitud = cadena.length;
        let seg = 1000;

        this.Q0(cadena, posicion, longitud, lista,seg);

        this.enviar_pantalla(lista);
    }

    Q0(cadena, posicion, longitud, lista,seg){

        
        setTimeout(function(){ document.getElementById("imagen").src = "automataQ0.png";}, seg);
        seg=seg+1000;
        setTimeout(function(){ document.getElementById("imagen").src = "automataBase.png";}, seg);
        seg=seg+1000;
        

        if(cadena[posicion] == "a" || cadena[posicion] == "b"){

            if(cadena[posicion] == "b"){
                //colocar la sigueente imagen
                

                /* document.getElementById("imagen").src = "automataQ0Ciclo.png";
                setTimeout(function(){ document.getElementById("imagen").src = ""; }, 1000);  */

                lista.push(["Q0: ", cadena.substring(posicion, longitud), "L"]);

                //posicion++;
                let conta=0;
                while(cadena[posicion] == "b"){
                    lista.push(["Q0: ", cadena.substring(posicion, longitud), "C"]);
                    posicion++;
                    setTimeout(function(){ document.getElementById("imagen").src = "automataQ0Ciclo.png";}, seg);
                    seg=seg+1000;
                    setTimeout(function(){ document.getElementById("imagen").src = "automataBase.png";}, seg);
                    seg=seg+1000;
                    conta++;
                    console.log(conta);
                    /* document.getElementById("imagen").src = "automataQ0Ciclo.png";
                    setTimeout(function(){ document.getElementById("imagen").src = ""; }, 1000); */
                
                }
            }
            /* setTimeout(function(){ document.getElementById("imagen").src = "automataBase.png";}, seg);
            seg=seg+1000; */
            if(cadena[posicion] == "a"){
 
                lista.push(["Q0: ", cadena.substring(posicion, longitud), "L"]);
                posicion++;
                setTimeout(function(){ document.getElementById("imagen").src = "automataQ0Trancision.png";}, seg);
                seg=seg+1000;
                setTimeout(function(){ document.getElementById("imagen").src = "automataBase.png";}, seg);
                seg=seg+1000;
                if(posicion == longitud){
                    lista.push(["Q0: ", "no pertenece al conjunto de los estados finales ", "T"]);
                    return;
                }
                else{
                    this.Q1(cadena, posicion, longitud, lista,seg);
                }
            }
        }
        else{
            lista.push(["Q0: ","no pertenece al conjunto de los estados finales ", "T"])
            return;
        }
    }

    Q1(cadena, posicion, longitud, lista,seg){
        if (cadena[posicion]=="a"){
       
        while(cadena[posicion] == "a"){
            lista.push(["Q1: ", cadena.substring(posicion, longitud), "C"]);
            posicion++;
            setTimeout(function(){ document.getElementById("imagen").src = "automataQ1Ciclo.png";}, seg);
            seg=seg+1000;
            setTimeout(function(){ document.getElementById("imagen").src = "automataBase.png";}, seg);
                seg=seg+1000;
        }
        }
        if(cadena[posicion] == "b"){
            setTimeout(function(){ document.getElementById("imagen").src = "automataQ1Trancision.png";}, seg);
            seg=seg+1000;
            setTimeout(function(){ document.getElementById("imagen").src = "automataBase.png";}, seg);
            seg=seg+1000;
            lista.push(["Q1: ", cadena.substring(posicion, longitud), "L"]);
            posicion++;

            if(posicion == longitud && cadena[posicion] != "b"){
                lista.push(["Q1: ", "no pertenece al conjunto de los estados finales ", "T"]);
                return;
            }
            else{
                this.Q2(cadena, posicion, longitud, lista,seg);
            }
        }
        else{
            lista.push(["Q1: ", "no pertenece al conjunto de los estados finales ", "T"]);
            return;
        }
    }

    Q2(cadena, posicion, longitud, lista,seg){
        if(cadena[posicion] == "b"){
            lista.push(["Q2: ", cadena.substring(posicion, longitud), "L"]);
            posicion++;

            if(posicion == longitud){
                setTimeout(function(){ document.getElementById("imagen").src = "automataQ2Trancision.png";}, seg);
                seg=seg+1000;
                setTimeout(function(){ document.getElementById("imagen").src = "automataBase.png";}, seg);
                seg=seg+1000;
                lista.push(["Q3: ", "pertenece al conjunto de los estados finales ", "T"]);
                return;
            }
            else{
                setTimeout(function(){ document.getElementById("imagen").src = "automataQ2Trancision.png";}, seg);
                seg=seg+1000;
                setTimeout(function(){ document.getElementById("imagen").src = "automataBase.png";}, seg);
                seg=seg+1000;
                this.Q3(cadena, posicion, longitud, lista,seg);
            }
        }
        else if(cadena[posicion] == "a"){
            lista.push(["Q2: ", cadena.substring(posicion, longitud), "L"]);
            posicion++;

            if(posicion == longitud){
                lista.push(["Q2: ", "no pertenece al conjunto de los estados finales ", "T"]);
                return;
            }
            else{
                setTimeout(function(){ document.getElementById("imagen").src = "automataQ2Retorno.png";}, seg);
                seg=seg+1000;
                setTimeout(function(){ document.getElementById("imagen").src = "automataBase.png";}, seg);
                seg=seg+1000;
                this.Q1(cadena, posicion, longitud, lista,seg);
            }
        }
        else{
            lista.push(["Q2: ", "no pertenece al conjunto de los estados finales ", "T"]);
            return;
        }
    }

    Q3(cadena, posicion, longitud, lista,seg){
        if (cadena[posicion] == "b" || cadena[posicion] == "a"){
    
        while(cadena[posicion] == "b" || cadena[posicion] == "a"){
            lista.push(["Q3: ", cadena.substring(posicion, longitud), "C"]);
            posicion++;
            setTimeout(function(){ document.getElementById("imagen").src = "automataQ3Ciclo.png";}, seg);
        seg=seg+1000;
        setTimeout(function(){ document.getElementById("imagen").src = "automataBase.png";}, seg);
        seg=seg+1000;

        }
        
       }
        if(posicion == longitud){
            lista.push(["Q3: ", "pertenece al conjunto de los estados finales ", "T"]);
            return;
        }
        else{
            lista.push(["Q3: ", "no pertenece al conjunto de los estados finales ", "T"]);
            return;
        }
    }

    enviar_pantalla(lista){
        let auxiliar = "";
        for (let i = 0; i < lista.length; i++) {
            auxiliar =  auxiliar + lista[i][0] + lista[i][1];
            auxiliar = auxiliar + "<br>";
        }
        document.getElementById("salida").innerHTML = auxiliar;
    }
}

function recibir_funcion(){
    let entrada = document.getElementById("entrada").value;
    let objeto = new prueba();
    objeto.entrada(entrada);
}

function limpiar(){
    document.getElementById("entrada").value = "";
    document.getElementById("salida").innerHTML = "Esperando resultados...";
    document.getElementById("imagen").src = "automataBase.png.png";
}