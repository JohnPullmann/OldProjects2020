/*  Javascript  */

//#####################################################
//##################################################### Link označenie
//#####################################################

//zobratie elementov z html
let navigacia = document.querySelector("nav");
let link_oznacenie = document.getElementById("link_oznacenie");
let linky = document.querySelectorAll(".link");

//pridanie označenia linkov
function link_hover_zmena(link) {
    if (link.className != "link" && link.parentElement.className == "link") {
        link_oznacenie.style.width = link.parentElement.offsetWidth+10+"px";
        link_oznacenie.style.left = link.parentElement.offsetLeft-35+"px";
    }
}
//odstranenie označenia z linkov
function link_hover_zmiznutie(element) {
    if (element.nodeName == "NAV") {
        link_oznacenie.style.width = 0+"px";
    }
}
//hover nad linkom event listener
linky.forEach(link => {link.addEventListener("mouseover", function (event) {
    link_hover_zmena(event.target);
})});
//odchadzanie z navigacie event listener- odstranenie označenia z linkov
navigacia.addEventListener("mouseover", function (event) {
    link_hover_zmiznutie(event.target);
});

//#####################################################
//##################################################### Uvodný text postupne písanie
//#####################################################

//premenné a výber nadpisu z html
let rychlost = 300;
let nadpis = document.querySelector(".uvod h1");
let text = nadpis.innerText;
let idpismeno = 0;

//menenie a vypisovanie nadpisu v loope
function printText() {
    nadpis.innerText = text.slice(0,idpismeno);
    idpismeno++;
    if (idpismeno > text.length) {
        idpismeno = 0;
        setTimeout(printText, rychlost*6);
    } else if (text[idpismeno-1] == " ") {
        setTimeout(printText, 100);
    } else {
        setTimeout(printText, rychlost);
    }

}
printText();

//#####################################################
//##################################################### Hlavička meniaca sa pri scrolle
//#####################################################

// toggluje s classov "scrolnute" v navigacii, čím ju v css upravuje, pri scrollovaní(ak nie je úplne navrchu), a v prípade, že navigácia v mobilnej verzii je aktívna, tak sa classa nezmení
window.addEventListener("scroll", function () {
    navigacia.style.transitionDelay = 0 + "s";
    navigacia.classList.toggle("scrolnute", window.scrollY > 0);
    if (navigacia.className == "nav_aktivna") {
        navigacia.classList.add("scrolnute");
    }
})
//#####################################################
//##################################################### Fotogaléria expandujúce obrázky
//#####################################################

//mení classu slidu na ktorí klikneš, ktorý sa potom rozšíri
let slides = document.querySelectorAll(".slide")

slides.forEach(function (slide) {slide.addEventListener("click", function (event) {
    //deletnutie classy aktivny všetkym slidom
    slides.forEach(function (slide_remove) {
        slide_remove.classList.remove("aktivna");
    });
    slide.classList.add("aktivna");
})});

//#####################################################
//##################################################### Navigácia mobilná verzia ...
//#####################################################

// pri mobilnej verzii, pri kliknutí na ikonku navigacie sa toggluje classa v navigacii (tým sa s css transition vysúva), a v prípade, že stránka nebola scrolnuta, pridá navigacii classu (zošedivie) ...
let nav_icon_aktualna = "Obrazky/nav_icon.png";
let nav_icon = document.querySelector(".nav_icon");
let mobil_tien = document.querySelector(".mobil_tien");
nav_icon.addEventListener("click", function (event) {
    if (nav_icon_aktualna == "Obrazky/nav_icon.png") {
        nav_icon_aktualna = "Obrazky/nav_icon_exit.png";
        navigacia.style.transitionDelay = 0 + "s";
        navigacia.classList.add("nav_aktivna");
        navigacia.classList.add("scrolnute");
        mobil_tien.classList.add("aktivna_m_t");
    } else {
        nav_icon_aktualna = "Obrazky/nav_icon.png";
        navigacia.style.transitionDelay = 0.7 + "s";
        navigacia.classList.remove("nav_aktivna");
        navigacia.classList.toggle("scrolnute", window.scrollY > 0);
        mobil_tien.classList.remove("aktivna_m_t");
    }
    event.target.style.backgroundImage = "url(\"" + nav_icon_aktualna+"\")";
})

mobil_tien.addEventListener("click", function (event) {
    if (mobil_tien.className == "mobil_tien aktivna_m_t") {
        navigacia.style.transitionDelay = 0.7 + "s";
        navigacia.classList.remove("nav_aktivna");
        navigacia.classList.toggle("scrolnute", window.scrollY > 0);
        mobil_tien.classList.remove("aktivna_m_t");
        nav_icon_aktualna = "Obrazky/nav_icon.png";
        nav_icon.style.backgroundImage = "url(\"" + nav_icon_aktualna+"\")";
    }
});