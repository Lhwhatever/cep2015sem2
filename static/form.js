setup = function() {

    try {
        $(".datetimepicker").datetimepicker({
            format: 'Y-m-d H:i',
            inline: true
        });
    } catch(err) {
        console.log("skipping date time picker");
    }

    $("label").addClass("col-sm-2 control-label");
    $(".form-group>div>input, .form-group>div>textarea, .form-group>div>select").addClass("form-control");
    $(".form-group>div>input[type=checkbox]").removeClass("form-control").parent().addClass("checkbox");

    $(".form-group>div>input[type=text]").attr("placeholder", "Input text here. (Maximum 255 characters)");
    $(".form-group>div>.colorpicker-child").parent().removeClass("col-sm-10").addClass("colorpicker col-sm-4");

    $(".form-group>div>textarea").attr("placeholder", "Input text here.");

    try {
        $(".colorpicker>.temp").addClass("input-group-addon");
        $(".colorpicker").attr("placeholder", "Input color hex code.");
        $(".colorpicker").colorpicker();
    } catch(err) {
        console.log("skipping color picker");
    }
}