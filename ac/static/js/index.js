$(document).ready(function() {
    $("#global-search-field").focus();
    add_listeners();
});

function add_listeners(){
    $("a.cateLink").mouseover(function(){
        $(this).parent().addClass("cateLinkOn");
    });
    $("a.cateLink").mouseout(function(){
        $(this).parent().removeClass("cateLinkOn");
    });
    
}

function showHot(type){
    switch(type){
        case 1:
            $("#dayHot").hide();
            $("#monthHot").hide();
            $("#weekHot").show();
            break;
        case 2:
            $("#dayHot").hide();
            $("#weekHot").hide();
            $("#monthHot").show();
            break;
        default:
            $("#monthHot").hide();
            $("#weekHot").hide();
            $("#dayHot").show();
    }
}

function request(id,url){
    oScript = document.getElementById(id);
    var head = document.getElementsByTagName("head").item(0);
    if (oScript) {
        head.removeChild(oScript);
    }
    oScript = document.createElement("script");
    oScript.setAttribute("src", url);
    oScript.setAttribute("id",id);
    oScript.setAttribute("type","text/javascript");
    head.appendChild(oScript);
    return oScript;
}

