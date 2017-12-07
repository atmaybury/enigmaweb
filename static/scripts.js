$(document).ready(function(){

    // hide ciphertext area on load
    $("#ciphertext").hide();

    // disable swap until after submit
    $("#swap").prop("disabled", true);

    // pass form via ajax to flask
    $('form').on('submit', function(e){
        if ($.trim($("#plaintext").val()) == "" || $.trim($("#r0").val()) == "" || $.trim($("#r1").val()) == "" || $.trim($("#r2").val()) == "" ) {
            alert("Please fill all fields!");
            return false;
        }

        var plaintext = $("#plaintext").val();
        var r0 = $("#r0").val();
        var r1 = $("#r1").val();
        var r2 = $("#r2").val();

        $.ajax({
            type: "POST",
            url: Flask.url_for("index"),
            data: {
                'r0':r0,
                'r1':r1,
                'r2':r2,
                'plaintext':plaintext,
                'ciphertext':""
            }
        })
        .done(function(data){
            $("#ciphertext").slideDown();
            $("#ciphertext").val(data.ciphertext);
            $("#swap").prop('disabled', false);
        });

        e.preventDefault();

    });

    // reset form, disabe swap button
    $('form').on('reset', function(){
        $("#ciphertext").slideUp();
        $("#swap").prop("disabled", true);
    });

    // swap ctext and ptext vals, disable swap
    $("#swap").on('click', function(){
        var ciphertext = $("#ciphertext").val();
        $("#plaintext").val(ciphertext);
        $("#ciphertext").val("");
        $("#swap").prop("disabled", true);
    });

});
