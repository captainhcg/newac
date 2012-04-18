$(document).ready(function() {
    $("#global-search-field").focus();
    load_user_info();
});

function load_user_info(){
    // request("ac_index", "http://www.acfun.tv/user_check.aspx" );
    // var user_profile = request("user_profile", "http://www.acfun.tv/user_check.aspx" );
    // alert(user_profile.uid);
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
