
$(document).ready(function(){

    $("#neno_login_email").focusout(function () {


        if($(this).val() == "")
        {
            $(this).parent().parent().append("<div class=\"alert alert-warning alert-dismissible fade show\" role=\"alert\" id='neno_alert_empty_email'>\n" +
                "          <span class=\"alert-inner--icon\"><i class=\"ni ni-bell-55\"></i></span>\n" +
                "          <span class=\"alert-inner--text\"><strong>Warning!</strong> Enter Email</span>\n" +
                "          <button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">\n" +
                "            <span aria-hidden=\"true\">&times;</span>\n" +
                "          </button>\n" +
                "        </div>");


        }
        else
        {

            alert($(this).parent().parent().);
        }





    })

    $("#neno_login_login").click(function () {
        alert("Form Submitted");
    })

});