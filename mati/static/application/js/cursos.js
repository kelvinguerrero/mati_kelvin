$(document).ready(function() {
    
    var navListItems = $('ul.setup-panel li a');
    var navListItems2 = $('ul.setup-panel2 li a');
    allWells = $('.setup-content');
    allWells2 = $('.setup-content2');

    allWells.hide();
    allWells2.hide();

    navListItems2.click(function(e)
    {
        e.preventDefault();
        var $target = $($(this).attr('href')),
            $item = $(this).closest('li');
        
        if (!$item.hasClass('disabled')) {
            navListItems2.closest('li').removeClass('active');
            $item.addClass('active');
            allWells2.hide();
            $target.show();
        }
    });

    navListItems.click(function(e)
    {
        e.preventDefault();
        var $target = $($(this).attr('href')),
            $item = $(this).closest('li');

        if (!$item.hasClass('disabled')) {
            navListItems.closest('li').removeClass('active');
            $item.addClass('active');
            allWells.hide();
            $target.show();
        }
    });
    
    $('ul.setup-panel li.active a').trigger('click');
    $('ul.setup-panel2 li.active a').trigger('click');

    // DEMO ONLY //
    $('#activate-step-2').on('click', function(e) {
        $('ul.setup-panel li:eq(1)').removeClass('disabled');
        $('ul.setup-panel li a[href="#step-2"]').trigger('click');
        $(this).remove();
    })    
});

