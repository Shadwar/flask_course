document.onreadystatechange = function() {
    initMainSlider();
}

function initMainSlider() {
    var main_banner = document.getElementById('main-banner');
    if (main_banner) {
        var current = 1;
        var slides = document.querySelectorAll('.main-banner__slide');
        var total = slides.length;
        var pages = document.querySelectorAll('.main-banner__page');

        function change_slide(delta) {
            current += delta;
            if (current < 1) current = total;
            else if (current > total) current = 1;

            slides.forEach(function(e) {
                e.classList.remove('main-banner__slide--current');
            });

            pages.forEach(function(e) {
                e.classList.remove('main-banner__page--current');
            });

            document.querySelector('.main-banner__slide[data-slide="'+current+'"]')
                    .classList.add('main-banner__slide--current');
            document.querySelector('.main-banner__page[data-slide="'+current+'"]')
                    .classList.add('main-banner__page--current');
        }

        var prev_control = main_banner.querySelector('.main-banner__control--prev');
        var next_control = main_banner.querySelector('.main-banner__control--next');
        prev_control.onclick = function(e) { change_slide(-1); }
        next_control.onclick = function(e) { change_slide(1); }

        function page_clicked(e) {
            var slide_id = e.target.getAttribute('data-slide');

            slides.forEach(function(e) {
                e.classList.remove('main-banner__slide--current');
            });

            pages.forEach(function(e) {
                e.classList.remove('main-banner__page--current');
            });

            document.querySelector('.main-banner__slide[data-slide="'+slide_id+'"]')
                    .classList.add('main-banner__slide--current');
            e.target.classList.add('main-banner__page--current');
        }

        pages.forEach(function(e) {
            e.onclick = page_clicked;
        });
    }
}