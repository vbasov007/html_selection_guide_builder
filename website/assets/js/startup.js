
$( function () {

    initCategorySwitches();

    initCollapsibleTree();

    initTextHighlight();

    initProductPageRedirect();

    /*t0 = performance.now();*/
    highlightDiscontinuedProducts();
    /*t1 = performance.now();
    alert(t1-t0);*/

    setStateAccordingInputVariables();

    showPage();
});

