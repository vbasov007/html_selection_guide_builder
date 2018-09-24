$(document).ready(function(){
        $(".selectable-view").hide()

        $(".change-view-but").click(function(){

            $(this).addClass("pressed")
            $(this).siblings("button").removeClass("pressed")

            $(this).siblings(".selectable-view").hide()
            //$(".selectable-view").hide()

            const v =  $(this).attr("view-id")
            $(this).siblings( `.selectable-view[view-id="${v}"]`).show()

        });

        $(".change-view-but:first-child").trigger('click')

    });

var tree = document.querySelectorAll('ul.tree a:not(:last-child)');
for(var i = 0; i < tree.length; i++){
    tree[i].addEventListener('click', function(e) {
                var parent = e.target.parentElement;
                var classList = parent.classList;
                if(classList.contains("open")) {
                    classList.remove('open');
                    var opensubs = parent.querySelectorAll(':scope .open');
                    for(var i = 0; i < opensubs.length; i++){
                        opensubs[i].classList.remove('open');
                    }
                } else {
                    classList.add('open');
                }
                e.preventDefault();
            });
        }

var x = document.getElementsByClassName('product_status');
for (var i = 0; i < x.length; i++){
    if (x[i].innerHTML=='not for new design' || x[i].innerHTML=='discontinued'){
        x[i].style.cssText= "color: red; font-weight: bold;";
    }
    else{
        x[i].style.cssText= "color: green; font-weight: bold;";
    }
}
