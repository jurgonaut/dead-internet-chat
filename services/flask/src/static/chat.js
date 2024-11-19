$(document).ready(function () {
    var out = $('#out');

    $.ajax({
        url: "/fetch_chat",
        dataType: "json",
        success: function (data) {
            console.log(data);
            $.each(data, function(index, value) {
                out.prepend($("<p></p>", { 'text': value.date + " | " + value.user + ": " + value.content }))
            });
        }
    });

    $('#in').keyup(function(e){
        if (e.keyCode == 13) {
            $.post('/send_message', {'message': $(this).val()});
            $(this).val('');
        }
    });

    function sse() {
        var source = new EventSource('/stream');
        source.onmessage = function(e) {
            data = JSON.parse(e.data);
            console.log(data);
            out.prepend($("<p></p>", { 'text': data.date + " | " + data.user + ": " + data.content }))
        };
    }
    sse();
})

