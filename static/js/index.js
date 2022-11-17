// test js
console.log('test js');
container = document.querySelector('.container');
palo = document.querySelector('.palo');
bd = document.querySelector('.bd');
blackdot = document.querySelector('.blackdot');
blacdot = document.querySelector('.sidebar .blacdot');
sidebar = document.querySelector('.sidebar');
loadbutn = document.querySelector('.loading');
loaddiv = document.querySelector('.loading div');
showstyle = document.querySelector('.showstyle');
// add onclick event

showstyle.addEventListener('click', function () {
    console.log('showstyle');
    container.classList.toggle('singleGrid');
    container.classList.toggle('doubleGrid');




});


function requ(paper, cat) {
    var data = JSON.stringify({
        "npaper": paper,
        "catagoty": cat
    });

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.open("POST", "/");
    xhr.setRequestHeader("content-type", "application/json");
    xhr.setRequestHeader("cache-control", "no-cache");

    return xhr.send(data);

}








container.addEventListener('click', function () {



    sidebar.style.left = '-500px';
    blacdot.style.right = '400px';

    blackdot.classList.remove('click');
    // remove('click');

});

palo.addEventListener('click', function () {

    document.querySelector('.paloclass ul').classList.toggle('palo-show');
});

lsts = document.querySelectorAll('.paloclass ul li');

for (let i = 0; i < lsts.length; i++) {
    lsts[i].addEventListener('click', function () {
        cat = lsts[i].textContent;
        lsts[i].querySelector('a').href = '../' + 'palo/' + cat;
        // document.querySelector('.paloclass ul').classList.remove('palo-show');
        paper = lsts[i].parentNode.parentNode.classList.value;

        requ(paper, cat);


        // document.querySelector('.paloclass span').innerHTML = this.innerHTML;
    });

}


blsts = document.querySelectorAll('.bdclass  ul li');
for (let i = 0; i < blsts.length; i++) {
    blsts[i].addEventListener('click', function () {
        cat = blsts[i].textContent;
        blsts[i].querySelector('a').href = '../' + 'bdn/' + cat;;
        // document.querySelector('.paloclass ul').classList.remove('palo-show');
        paper = blsts[i].parentNode.parentNode.classList.value;
        requ(paper, cat);
        // document.querySelector('.paloclass span').innerHTML = this.innerHTML;
    });

}


bd.addEventListener('click', function () {

    document.querySelector('.bdclass ul').classList.toggle('bd-show');

});

blackdot.addEventListener('click', function () {
    blackdot.classList.toggle('click');

    sidebar.style.left = '0px';
    blacdot.style.right = '40px';

});









blacdot.addEventListener('click', function () {
    blackdot.classList.toggle('click');

    sidebar.style.left = '-500px';
    blacdot.style.right = '400px';

});


// add timeout function with event listener



var len = 3
lst = document.querySelectorAll('.content');
loadbutn.addEventListener('click', function () {
    if (len >= lst.length) {
        loadbutn.style.display = 'none';
    }
    loaddiv.classList.toggle('loader');

    // console.log(lst);


    setTimeout(function () {
        loaddiv.classList.toggle('loader');
    }, 1000);

    for (i = len; i < len + 3 && i < lst.length; i++) {
        // if (i > lst.length)
        //     break;
        lst[i].style.display = 'grid';
    }
    len += 3;
});




