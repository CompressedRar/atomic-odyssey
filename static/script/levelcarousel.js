desc = [{
    "level": 1,
    "scope": "Hydrogen - Neon",
    "bg": "url('/static/Elements/23.Vanadium.png')"
},{
    "level": 2,
    "scope": "Sodium - Calcium",
    "bg": "url('/static/Elements/14.Silicon.png')"
},{
    "level": 3,
    "scope": "Scandium - Zinc",
    "bg": "url('/static/Elements/24.Chromium.png')"
},{
    "level": 4,
    "scope": "Gallium - Zirconium",
    "bg": "url('/static/Elements/26.Iron.jpg')"
},{
    "level": 5,
    "scope": "Niobium - Tin",
    "bg": "url('/static/Elements/31.Gallium.jpg')"
},{
    "level": 6,
    "scope": "Antimony - Neodymium",
    "bg": "url('/static/Elements/49.Indium.jpg')"
},{
    "level": 7,
    "scope": "Promethium - Ytterbium",
    "bg": "url('/static/Elements/69.Thulium.jpg')"
},{
    "level": 8,
    "scope": "Lutetium - Mercury",
    "bg": "url('/static/Elements/75.Rhenium.jpg')"
},{
    "level": 9,
    "scope": "Thallium - Thorium",
    "bg": "url('/static/Elements/92.Uranium.jpg')"
},{
    "level": 10,
    "scope": "Proctactinium - Fermium",
    "bg": "url('/static/Elements/106.Seaborgium.jpg')"
},{
    "level": 11,
    "scope": "Mendelevium - Darmstadtium",
    "bg": "url('/static/Elements/111.Roentgenium.jpg')"
},{
    "level": 12,
    "scope": "Roentgenium - Oganesson",
    "bg": "url('/static/Elements/102.Nobelium.jpg')"
}];

let carouselpointer = 0;
carousel = document.getElementsByClassName("carousel")[0];
leftbutton = document.getElementById("leftbutton");
rightbutton = document.getElementById("rightbutton");

function assign(){
    carouselChildren = document.getElementsByClassName("carousel");
    pointer = 0 + carouselpointer;
    for (const x of carouselChildren[0].children){
        x.style.backgroundImage = desc[pointer]["bg"];
        let lvl = x.children[0].children[0];
        let scope = x.children[0].children[1];
        let inputlvl = x.children[0].children[2];
        
        inputlvl.setAttribute('value', pointer + 1);
        console.log(inputlvl);
        lvl.textContent = "Level " + desc[pointer]["level"];
        scope.textContent = desc[pointer]["scope"];
        pointer++;
    }
    //carouselChildren[0].children[0].children[0].children[0].textContent

    
    
}
assign();
let lvl = document.getElementById("level");
let scope = document.getElementById("scope");
leftbutton.style.opacity = "0";

rightbutton.addEventListener("click", ()=>{
    leftbutton.style.opacity = "1";
    rightbutton.style.opacity= "0";
    carouselpointer = 6;
    assign();
    
});

leftbutton.addEventListener("click", ()=>{
    leftbutton.style.opacity = "0";
    rightbutton.style.opacity= "1";
    carouselpointer = 0;
    assign();
    
});