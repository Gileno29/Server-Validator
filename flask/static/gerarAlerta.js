function gerarAlerta(conexao, x) {
    console.log("Fui chamado")
    // Cria o elemento HTML
    var alerta = document.createElement("div");
    alerta.className = "alert alert-danger alert-dismissible fade show";
    alerta.style = "z-index: 0; position: absolute;";
    alerta.id = "myAlert";
    alerta.role = "alert";
  
    // Adiciona o conteúdo ao elemento HTML
    alerta.innerHTML = conexao;
    console.log(conexao)
    // Adiciona o botão ao elemento HTML
    var botao = document.createElement("button");
    botao.className = "btn btn-dark";
    botao.title = "close";
    //botao.onclick = removeAlerta();
    botao.innerHTML = "x";
  
    // Adiciona o botão ao elemento HTML
    alerta.appendChild(botao);
  
    // Se a condição x for verdadeira, adiciona o elemento HTML ao documento
   
    document.body.appendChild(alerta);
    return alerta
  };
  