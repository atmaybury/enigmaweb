$(document).ready(function(){

    // show ciphertext box when form is submitted
    // TODO: Ajax so no page reload
    $("#ciphertext").hide();

    $("#submit").click(function(){
        $("#ciphertext").slideDown();
    });
 
});
