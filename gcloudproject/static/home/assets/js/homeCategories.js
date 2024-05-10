


// normal category

$(document).ready(function() {
    // Hide all portfolio items
    $('.normal-list-item').hide();

    // Show only the first 5 portfolio items
    $('.normal-list-item:lt(5)').show();

    // Show the portfolio item links initially

    $('.button').click(function() {
        var category = $(this).attr('class').split(' ')[1];
        $('.normal-list-item').hide();

        if (category === 'all') {
            // Show only the first 5 items when 'All' is selected
            $('.normal-list-item:lt(5)').show();
        } else {
            // Show only the first 5 items of the selected category
            $('.normal-list-item.' + category + ':lt(5)').show();
            // Hide the portfolio item links for the selected category
        }
        $('.button').removeClass('active');
        $(this).addClass('active');
    });
});


$(document).ready(function() {
    // Hide all portfolio items initially
    $('.normal-category-item').hide();

    // Show the portfolio item links initially
    $('.normal-category-item').show();

    $('.button').click(function() {
        var category = $(this).attr('class').split(' ')[1];
        $('.normal-category-item').hide();

        if (category === 'all') {
            // Show all items when 'All' is selected
            $('.normal-category-item').show();
        } else {
            // Show items of the selected category
            $('.normal-category-item.' + category).show();
            // Hide the portfolio item links for the selected category
        }
        $('.button').removeClass('active');
        $(this).addClass('active');
    });
});



// premium category

$(document).ready(function() {
    // Hide all portfolio items
    $('.premium-list-item').hide();

    // Show only the first 5 portfolio items
    $('.premium-list-item:lt(5)').show();

    // Show the portfolio item links initially

    $('.pbutton').click(function() {
        var category = $(this).attr('class').split(' ')[1];
        $('.premium-list-item').hide();

        if (category === 'all') {
            // Show only the first 5 items when 'All' is selected
            $('.premium-list-item:lt(5)').show();
        } else {
            // Show only the first 5 items of the selected category
            $('.premium-list-item.' + category + ':lt(5)').show();
            // Hide the portfolio item links for the selected category
        }
        $('.pbutton').removeClass('active');
        $(this).addClass('active');
    });
});


$(document).ready(function() {
    // Hide all portfolio items initially
    $('.premium-category-item').hide();

    // Show the portfolio item links initially
    $('.premium-category-item').show();

    $('.pbutton').click(function() {
        var category = $(this).attr('class').split(' ')[1];
        $('.premium-category-item').hide();

        if (category === 'all') {
            // Show all items when 'All' is selected
            $('.premium-category-item').show();
        } else {
            // Show items of the selected category
            $('.premium-category-item.' + category).show();
            // Hide the portfolio item links for the selected category
        }
        $('.pbutton').removeClass('active');
        $(this).addClass('active');
    });
});


// all category

$(document).ready(function() {
    // Hide all portfolio items
    $('.all-list-item').hide();

    // Show only the first 5 portfolio items
    $('.all-list-item:lt(5)').show();

    // Show the portfolio item links initially

    $('.abutton').click(function() {
        var category = $(this).attr('class').split(' ')[1];
        $('.all-list-item').hide();

        if (category === 'all') {
            // Show only the first 5 items when 'All' is selected
            $('.all-list-item:lt(5)').show();
        } else {
            // Show only the first 5 items of the selected category
            $('.all-list-item.' + category + ':lt(5)').show();
            // Hide the portfolio item links for the selected category
        }
        $('.abutton').removeClass('active');
        $(this).addClass('active');
    });
});


$(document).ready(function() {
    // Hide all portfolio items initially
    $('.all-category-item').hide();

    // Show the portfolio item links initially
    $('.all-category-item').show();

    $('.abutton').click(function() {
        var category = $(this).attr('class').split(' ')[1];
        $('.all-category-item').hide();

        if (category === 'all') {
            // Show all items when 'All' is selected
            $('.all-category-item').show();
        } else {
            // Show items of the selected category
            $('.all-category-item.' + category).show();
            // Hide the portfolio item links for the selected category
        }
        $('.abutton').removeClass('active');
        $(this).addClass('active');
    });
});



// hide all, normal and premium

function category(){
    document.getElementById("all-show").style.display = "block" ;
    document.getElementById("normal-show").style.display = "none" ;
    document.getElementById("premium-show").style.display = "none" ;
}

function normal(){
    document.getElementById("normal-show").style.display = "block" ;
    document.getElementById("all-show").style.display = "none" ;
    document.getElementById("premium-show").style.display = "none" ;
}

function premium(){
    document.getElementById("premium-show").style.display = "block" ;
    document.getElementById("all-show").style.display = "none" ;
    document.getElementById("normal-show").style.display = "none" ;
}





// Get all the buttons for each sub category type
var buttonsAll = document.querySelectorAll('.btnx');
var buttonsPremium = document.querySelectorAll('.btnxp');
var buttonsNormal = document.querySelectorAll('.btnxn');

// Function to remove 'active' class from all buttons
function removeAllActive(buttons) {
    buttons.forEach(function(btn) {
        btn.classList.remove('activ');
        btn.classList.remove('activp');
        btn.classList.remove('activn');
    });
}

// Add click event listeners to each category type
buttonsAll.forEach(function(button) {
    button.addEventListener('click', function() {
        // Remove 'active' class from all buttons
        removeAllActive(buttonsAll);
        // Add 'active' class to the clicked button
        this.classList.add('activ');
    });
});

buttonsPremium.forEach(function(button) {
    button.addEventListener('click', function() {
        // Remove 'active' class from all buttons
        removeAllActive(buttonsPremium);
        // Add 'active' class to the clicked button
        this.classList.add('activp');
    });
});

buttonsNormal.forEach(function(button) {
    button.addEventListener('click', function() {
        // Remove 'active' class from all buttons
        removeAllActive(buttonsNormal);
        // Add 'active' class to the clicked button
        this.classList.add('activn');
    });
});


