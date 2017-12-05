$(document).ready(function(){

    // show ciphertext box when form is submitted
    // TODO: Ajax so no page reload
    //$("#ciphertext").hide();

    //$("#submit").click(function(){
    //    $("#ciphertext").slideDown();
    //});

    // alert and prevent submit if any empty fields
    $("#inputForm").submit(function() {
        if ($.trim($("#plaintext").val()) == "" || $.trim($("#r0").val()) == "" || $.trim($("#r1").val()) == "" || $.trim($("#r2").val()) == "" ) {
            alert("Please fill all fields!");
            return false;
        }
    });

});
