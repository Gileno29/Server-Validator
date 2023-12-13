
async function getPermissions() {
    const permissions = await Notification.requestPermissions();
    return permissions
}

function copiarTexto() {
    let textoCopiado = document.getElementsByClassName("texto-a-copiar");
    let text=''
    permissions=getPermissions()
    console.log('This is my permissions: ', permissions)
    if (permissions.includes("clipboard-write")) {
        Array.prototype.forEach.call(textoCopiado, function(el) {
            text= text+el.innerText+ "\n"
            console.log(text)
          });
          navigator.clipboard.readText(text);
          //textoCopiado.setSelectionRange(0, 99999)
          //document.execCommand("copy");
      
          alert("O texto é: " + text);
      } else {
        console.log("Erro nas permissões")
      }

   

    
}
