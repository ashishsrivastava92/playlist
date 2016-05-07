$(document).ready(function(){
    $("#query").autocomplete({
        source: [],
        select: function( event, ui ) {
            event.preventDefault();
            $("#query").val(ui.item.label);
            window.location.href = ui.item.value;
        },
        focus: function( event, ui ) {
            $("#query").val(ui.item.label);
        },
        minLength: 3,
        delay: 500,
    });

    $("input#query").keyup(function(){
        var query = $(this).val();

        if(query.length>3){
            dataString = 'q=' + query;
            console.log(dataString);
            $.ajax({
                type: "POST",
                url: "/greedy/api/v1/ajaxsearch/",
                data: dataString,
                success: function(response){
                    var availableHints = [];
                    for (var i in response.tracks){
                        availableHints.push({
                            value: "/greedy/track/" + response.tracks[i].id + '/',
                            label: response.tracks[i].name
                        });
                    }
                    $("#query").autocomplete({
                        source: availableHints,
                    });
                }
            });
        }
    });
});