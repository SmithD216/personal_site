function updateNav(){
    var navlinks = document.querySelectorAll("ul.nav li a")
    for(i=0;navlinks.length>i;i++){
        var h = navlinks[i].href
        if(window.location.href == h){
            navlinks[i].classList.add("current")
        } else {
            navlinks[i].classList.remove("current")
            navlinks[i].classList.add("notCurrent")
        }
    }
}

function adjustSize() {
    console.log(window.innerWidth)
}