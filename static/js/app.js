$(document).ready( function () {
    console.log( "ready!" );
    let pathname = window.location.pathname;
    console.log('pathname', pathname);

    if(pathname === '/') {
        setTimeout(function () {
            window.location = '/farm';
            }, 5000);
    }


$("#sidebar").mCustomScrollbar({
            theme: "minimal"
        });

        $('#dismiss, .overlay').on('click', function () {
            // hide sidebar
            $('#sidebar').removeClass('active');
            // hide overlay
            $('.overlay').removeClass('active');
        });

        $('#sidebarCollapse').on('click', function () {
            console.log('sidebarCollapse clicvk');
            // open sidebar
            $('#sidebar').addClass('active');
            // fade in the overlay
            $('.overlay').addClass('active');
            $('.collapse.in').toggleClass('in');
            $('a[aria-expanded=true]').attr('aria-expanded', 'false');
        });














});

