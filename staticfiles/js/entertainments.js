var myIndex2 = 0;

carousel2();

function carousel2() {
    var i;
    var x = document.getElementsByClassName("mySlides_Ent");
   

    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";  
       
    }
    myIndex2++;
    if (myIndex2 > x.length) {myIndex2 = 1}    
    x[myIndex2-1].style.display = "block";  
    setTimeout(carousel2, 4000);    
}
