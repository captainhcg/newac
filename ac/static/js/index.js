$(document).ready(function() {
    $("#global-search-field").focus();
    add_listeners();
    escapeDesc();
});

function add_listeners(){
    $("a.cateLink").mouseover(function(){
        $(this).parent().addClass("cateLinkOn");
    });
    $("a.cateLink").mouseout(function(){
        $(this).parent().removeClass("cateLinkOn");
    });
    $(".cateOpt").click(function(){
        if($(this).attr("sel") == 1){
            $(this).addClass("cateDel");
            $(this).attr("sel", 0);
        }
        else{
            $(this).removeClass("cateDel");
            $(this).attr("sel", 1);           
        }
    });
}
function escapeDesc(){
    $(".newArtDesc").each(function(){
        a=$(this).text().length?$(this).text():"壮哉我大AcFun！";
        $(this).html(parseGet(parsePost(a.replace(/\<[\s\S]+?\>/g,""))));
    });
}

function showHot(type){
    $(".columnTopLi").removeClass('columnTopLiSelected');
    switch(type){
        case 1:
            $("#dayHot").hide();
            $("#monthHot").hide();
            $("#weekHot").show();
            $("#navWeekHot").addClass('columnTopLiSelected');
            break;
        case 2:
            $("#dayHot").hide();
            $("#weekHot").hide();
            $("#monthHot").show();
            $("#navMonthHot").addClass('columnTopLiSelected');
            break;
        default:
            $("#monthHot").hide();
            $("#weekHot").hide();
            $("#navDayHot").addClass('columnTopLiSelected');
            $("#dayHot").show();
    }
}
function flipPre(o){
    // show all preview
    if($(o).attr("sel") == 1){
        $(".newArtImg").show();
        $(o).attr("sel", 0);
        $(o).removeClass('cateDel');
        $(".newArtDesc").removeClass('newArtDescLong');
        $(".newArt").removeClass('newArtShort');
    }
    // hide all preview
    else{
        $(".newArtImg").hide();
        $(o).attr("sel", 1);
        $(o).addClass('cateDel')
        $(".newArtDesc").addClass('newArtDescLong');
        $(".newArt").addClass('newArtShort');
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

