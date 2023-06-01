document.addEventListener("keypress", function(e){

    if(e.shiftKey && e.which == 83) {
        const filename = '__innit__.py';
        const content = $('textarea#PainelCode').val();
        
        if (filename && content) {
            downloadFile(filename, content);
        }
    } 

    if(e.shiftKey && e.which == 13) {
        uploadFile();
    } 
})