
function initProductPageRedirect(){

    $('span.product').on('click', function(){
       productPageRedirect($(this).text());
    });
}

function productPageRedirect(part_name) {

    let url = getDataFromJS(productPageUrl, part_name, 'ProductPageUrl');

    if(isValidURL(url)){
        let win = window.open(url, '_blank');
        win.focus();
    }
}

function isValidURL(string) {
    let res = string.match(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g);
    return res != null;
}