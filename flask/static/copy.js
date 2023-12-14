
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



//FUNCAO UTILIZADA NO SGP
<script>
  function copyToClipboard(containerid) {
    var range = document.createRange();
    range.selectNode(containerid);

    window.getSelection().removeAllRanges(); 
    window.getSelection().addRange(range); 

    document.execCommand("copy");
    window.getSelection().removeAllRanges();

    toastr.options['timeOut'] = '1500';
    toastr["info"]("{% trans "Copiado!" %}");
    toastr.options['timeOut'] = '6000000';
    return false;
  };
</script>