navigation = document.getElementById("active-bar");

/*window.onscroll = () => {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        
        navigation.style.opacity = "0.7";
        activebar.style.opacity = "0.7";
      }
    else if (document.body.scrollTop < 350 || document.documentElement.scrollTop < 350){
        navigation.style.backgroundColor = "#0f1e29";
        navigation.style.opacity = "1";
        activebar.style.opacity = "1";
        activebar.style.backgroundColor = "#0f1e29";
    }
}*/
navopen = false;

/*menu.addEventListener("click", ()=> {
    if(navopen){
        navigation.style.left = "-10%";
        navopen = false;
    }
    else {
        navigation.style.left = "0%";
        navopen = true;
    }
    
});*/

function showall(element){
    console.log(element);
    //document.getElementById("active-bar");
}
function active(element){
    
    console.log(element.children[0].attributes)
}
console.log(document.getElementById("vid-bg").children[0].children[0].src);
swit = false;
setInterval(()=>{
    console.log("switch");
    if (swit){
        swit = false;
        document.getElementById("vid-bg").style.opacity = "0";
        setTimeout(()=>{
            document.getElementById("vid-bg").children[0].setAttribute('src', "/static/Vids/1.mp4");
            document.getElementById("vid-bg").children[0].playbackRate = "0.7";
            document.getElementById("vid-bg").style.opacity = "0.5";
        }, 1000);
        
    }
    else {
        swit = true;
        document.getElementById("vid-bg").style.opacity = "0";
        setTimeout(()=>{
            document.getElementById("vid-bg").children[0].setAttribute('src', "/static/Vids/2.mp4");
            document.getElementById("vid-bg").children[0].playbackRate = "2";
            document.getElementById("vid-bg").style.opacity = "0.5";
        }, 1000);
        
    }
    console.log(document.getElementById("vid-bg").children[0].children[1].src);

}, 14000);
