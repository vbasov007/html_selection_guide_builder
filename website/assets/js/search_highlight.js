


function initTextHighlight() {

    $('#search_text').on('keyup', function (event) {

        let keycode = (event.keyCode ? event.keyCode : event.which);

        if(keycode === 13) {
            let search = $(this).val().toLowerCase();
            highlightText(search);
        }
    });

}

function highlightText(search){

    $('.search-highlight').toggleClass('search-highlight');
    $('.search-highlight-tree').toggleClass('search-highlight-tree');

    if (search.length > 1) {

        $('ul.tree li > div > span').each(function () {
            let val = $(this).text().toLowerCase();
            if (val.match(search)) {
                $(this).parent().parentsUntil('ul.tree').addClass('search-highlight-tree');
                $(this).addClass('search-highlight');
            }
        });

    }
}