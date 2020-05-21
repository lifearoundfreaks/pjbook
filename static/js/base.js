function rooms(type){ 
    // console.log(window.location.href)
     $.ajax({
        type: 'GET',
        async: true,
        url: "rooms",
        data: {
            ajax: true,
            type: type
        },
        success: function (data) {
            $("body").html(data)
        },
        error: function (xhr, status, e) {
            console.log(status);
        },
        dataType: '',
     })
}

function join(id_room){
    $.ajax({
        type: 'GET',
        async: true,
        url: "join/",
        data: {
            ajax: true,
            id_room: id_room
        },
        success: function (data) {
            $("body").html(data)
        },
        error: function (xhr, status, e) {
            console.log(status);
        },
        dataType: '',
     })
