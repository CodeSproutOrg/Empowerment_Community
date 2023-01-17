/* Sections scroll */
let scroll_buttons = document.getElementsByClassName('sections-btn');
for (let button_number = 0; button_number < scroll_buttons.length; button_number++) {
    scroll_button = scroll_buttons[button_number];
    scroll_button.addEventListener('click', function down_scroll() {
        let scroll_to = document.getElementsByClassName('block');
        scroll_to[button_number].scrollIntoView({
            behavior: "smooth",
            block: "center"
        });
    });
}

/* Next slide */
let next_btn = document.getElementById('next-btn')
next_btn = next_btn.addEventListener('click', next_slide);
function next_slide() {
    let eo = document.getElementById('eo');
    let voh = document.getElementById('voh');

    if (eo.classList.contains('active')) {
        eo.classList.remove('active');
        voh.classList.add('active');
    }
    else {
        eo.classList.add('active');
        voh.classList.remove('active');
    }
}

/*  Scrolling */
window.addEventListener('scroll', scrolling);
function scrolling() {
    let scroll = window.scrollY;
    let up_btn = document.getElementById('up-btn');

    if (scroll > 550) {
        up_btn.classList.add('active-btn');
    } else {
        up_btn.classList.remove('active-btn');
    }
}

/*  Up Scroll */
let up_btn = document.getElementById('up-btn');
up_btn = up_btn.addEventListener('click', up_scroll);
function up_scroll() {
    let main = document.getElementsByTagName('header')[0];
    main.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}
