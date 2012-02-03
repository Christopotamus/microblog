logged_in = false;

/**
  begin django CSRF token workaround for AJAX requests
 **/
$(document).ajaxSend(function(event, xhr, settings) {
        function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
        }
        }
        }
        return cookieValue;
        }
        function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
        }
        function safeMethod(method) {
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
});
// end CSRF stuffz

$(function(){
        if(isLoggedIn()){
            $(".nav-link").click(function(){
                
            });
            $(".nav-link:#wuphf").click(function(){
                $("#new-wuphf-form").toggle('slow');
            });
            $("#new-wuphf-submit").click(function(){
                postNewWuphf();
                return false;
            });
            //$("#new-wuphf-form");
            //if current page is home, and we have some wuphfs to fetch
            requestHomepageWuphfs();
            
        }
});

function isLoggedIn(){
    return logged_in == true;
}
function requestHomepageWuphfs(){
    console.log("fetching homepage's wuphfs");
    $.get("/getmainwuphfs/",{limit:"10"},function(data){
        console.log(data);
    });
}
function requestWuphfs(){

}
function postNewWuphf(){
    console.log("Sending wuphf!");
    //var text = $('#new-wuphf-content');
    text = $("#new-wuphf-content")[0].value;
    $.post("/postnewwuphf/",{"content":text},function(data){
        console.log(data);
        $("#new-wuphf-form").toggle('slow');
    });
    

}
function requestPage(pageId){

}
