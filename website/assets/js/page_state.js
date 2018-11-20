
function setStateAccordingInputVariables(){

    var category = getQueryVariable('category');
    var subcategory = getQueryVariable('subcategory');
    var view = getQueryVariable('view');
    var highlight = getQueryVariable('highlight');


    setState(category, subcategory, view, highlight, '')
}

function setState(category, subcategory, view, highlight, open_items){

    //$(`.selectable-view[view-id="${category}"]`).trigger('click');
    $(`.change-view-but[view-id*='${category}']`).trigger('click');

    $(`.change-view-but[view-id*='${subcategory}']`).trigger('click');

    $(`.change-view-but[view-id*='${view}']`).trigger('click');

    $(`#search_text`).val(highlight);
    highlightText(highlight);

}