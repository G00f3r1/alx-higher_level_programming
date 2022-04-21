function translate () {
        $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), function (data) {
            $('DIV#hello').text(data.hello);
        });
}

$(document).ready(function () {
    $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
        $(this).keydown(function (e) {
            if (e.keyCode === 13) {
                translateHello();
            }
        });
    });
});