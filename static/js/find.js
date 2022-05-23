$("form[name=findcriminalrec").submit(function(e) {


    var $form= $(this);
    var $error= $form.find(".error");
    var data = $form.serialize();
    //var blobFile = $('#fileupload').files[0];
    //formData.append("fileToUpload", blobFile);

    $.ajax({
        url:"/imagesubmit",
        type: "POST",
        data: data,
        processData: false,
        contentType: false,
        //dataType: "json",
        success: function(res){
            //window.location.href = "/";
            console.log("Image Successfully inserted  "+ res)
        },
        error: function(res){
            //window.location.href = "/";
            console.log("Error in image insertion")
        }
    })
    //e.preventDefault();
});
