$("form[name=criminalrec").submit(function(e) {


    e.preventDefault();

    var $form= $(this);
    var $error= $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url:"/criminal",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(res){
            //window.location.href = "/";
            window.alert("Record Inserted Successfully");
            window.location.href = "/";
        },
        error: function(res){
            //window.location.href = "/";
            window.alert("Record Inserted Successfully");
            window.location.href = "/insertcriminal";
        }
    })

});