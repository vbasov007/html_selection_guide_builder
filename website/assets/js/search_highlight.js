
$('#search_text').on('keyup', function () {

    if(event.keyCode === 13) {

        var search = $(this).val().toLowerCase();
        $('.search-highlight').toggleClass('search-highlight');

        if (search.length > 2) {

            $('ul.tree li > a').each(function () {
                var val = $(this).text().toLowerCase();
                if (val.match(search)) {
                    $(this).parentsUntil('ul.tree').addClass('search-highlight');
                }
            })

        }
    }
});

