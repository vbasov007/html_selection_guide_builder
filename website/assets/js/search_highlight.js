
$('#search_text').on('keyup', function () {

    if(event.keyCode === 13) {

        let search = $(this).val().toLowerCase();
        $('.search-highlight').toggleClass('search-highlight');
        $('.search-highlight-tree').toggleClass('search-highlight-tree');

        if (search.length > 1) {

            $('ul.tree li > a > span').each(function () {
                let val = $(this).text().toLowerCase();
                if (val.match(search)) {
                    $(this).parent().parentsUntil('ul.tree').addClass('search-highlight-tree');
                    $(this).addClass('search-highlight');
                }
            })

        }
    }
});

