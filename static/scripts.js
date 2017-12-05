$(document).ready(function(){

    // show ciphertext box when form is submitted
    $("#ciphertext").hide();

    $("#submit").click(function(){
        $("#ciphertext").slideDown();
    });

    // alert and prevent submit if any empty fields
    $("#inputForm").submit(function() {
        if ($.trim($("#plaintext").val()) == "" || $.trim($("#r0").val()) == "" || $.trim($("#r1").val()) == "" || $.trim($("#r2").val()) == "" ) {
            alert("Please fill all fields!");
            return false;
        }
    });

    // pass form via ajax to flask
    $('form').on('submit', function(e){
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
            $("#ciphertext").val(data.ciphertext);
        });

        e.preventDefault();

    });

});
