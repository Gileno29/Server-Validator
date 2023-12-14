
async function getPermissions() {
    const permissions = await Notification.requestPermissions();
    return permissions
}

function copiarTexto(containerid) {
 
    var range = document.createRange();
    range.selectNode(containerid);

    window.getSelection().removeAllRanges(); 
    window.getSelection().addRange(range); 

    document.execCommand("copy");
    window.getSelection().removeAllRanges();

    //toastr.options['timeOut'] = '1500';
    //toastr["info"]("{% trans "Copiado!" %}");
    //toastr.options['timeOut'] = '6000000';
    return false;
  };
    