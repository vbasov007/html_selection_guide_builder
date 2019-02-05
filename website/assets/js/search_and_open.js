
function OpenSubsByText(txt){


    let elements = $(`span.product:contains("${txt}")`);
    elements.each(function(){
        $(this).parent().parentsUntil('ul.tree').addClass('open');
    });



}