
function initCategorySwitches() {

    $('.selectable-view').hide();

    $('.change-view-but').on('click', function(){

        $(this).addClass("pressed");
        $(this).siblings("button").removeClass("pressed");

        $(this).siblings(".selectable-view").hide();

        const v =  $(this).attr("view-id");
        $(this).siblings( `.selectable-view[view-id="${v}"]`).show();

    });

    $('.change-view-but:first-child').trigger('click');

}

function initCollapsibleTree() {
    $('ul.tree div.branch:not(:last-child)').on('click', function(){
        $(this).parent().toggleClass('open');
    });

}

function highlightDiscontinuedProducts() {
    let x = document.getElementsByClassName('product_status');
    for (let i = 0; i < x.length; i++){
        if (x[i].innerHTML=='not for new design' || x[i].innerHTML=='discontinued'){
            x[i].style.cssText= "color: red; font-weight: bold;";
        }
        else{
            x[i].style.cssText= "color: green; font-weight: bold;";
        }
    }
}

function showPage() {
    $('#load-message').hide();
    $('#body').show();
}