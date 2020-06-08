function rooms(type){  
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
        },
        dataType: '',
     })
}

function join(slug){
    $.ajax({
        type: 'GET',
        async: true,
        url: "join/",
        data: {
            ajax: true,
            slug: slug
        },
        success: function (data) {
            $("body").html(data)
        },
        error: function (xhr, status, e) {
            
        },
        dataType: '',
     })
}