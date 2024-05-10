
// username already taken

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('username').addEventListener('input', function() {
        var username = this.value;
        var errorMessage = document.getElementById('username-check');

        if (username) {
            $.ajax({
                type: "GET",
                url: "{% url 'login:check_username' %}",
                data: {'username': username},
                dataType: 'json',
                success: function(data) {
                    if (data.available) {
                        errorMessage.innerHTML = '';
                        errorMessage.style.color = 'green';
                        document.getElementById('registerButton').disabled = false;
                    } else {
                        errorMessage.innerHTML = 'Username already exists';
                        errorMessage.style.color = 'red';
                        document.getElementById('registerButton').disabled = true;
                    }
                }
            });
        } else {
            errorMessage.innerHTML = '';
            document.getElementById('registerButton').disabled = true;
        }
    });
});


// email already taken

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('email').addEventListener('input', function() {
        var email = this.value;
        var errorMessage = document.getElementById('email-check');

        if (email) {
            $.ajax({
                type: "GET",
                url: "{% url 'login:check_email' %}",
                data: {'email': email},
                dataType: 'json',
                success: function(data) {
                    if (data.available) {
                        errorMessage.innerHTML = '';
                        errorMessage.style.color = 'green';
                        document.getElementById('registerButton').disabled = false;
                    } else {
                        errorMessage.innerHTML = 'Email already exists';
                        errorMessage.style.color = 'red';
                        document.getElementById('registerButton').disabled = true;
                    }
                }
            });
        } else {
            errorMessage.innerHTML = '';
            document.getElementById('registerButton').disabled = true;
        }
    });
});



// password matching and strength

function checkPasswordStrength() {
    var password = document.getElementById('password').value;
    var strengthText = document.getElementById('strengthText');

    var missingCriteria = [];
    if (!/[A-Z]/.test(password)) missingCriteria.push('A-Z');
    if (!/[a-z]/.test(password)) missingCriteria.push('a-z');
    if (!/\d/.test(password)) missingCriteria.push('0');
    if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) missingCriteria.push('@');
    if (password.length < 8) missingCriteria.push('8 digits');

    strengthText.innerHTML = missingCriteria.length > 0 ? 'Password must have: ' + missingCriteria.join(', ') : '';
}

function checkPasswordMatch() {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
    var matchText = document.getElementById('matchText');

    matchText.innerHTML = password !== confirmPassword ? 'Passwords do not match' : '';
}

function validatePassword() {
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
    var strengthText = document.getElementById('strengthText');
    var matchText = document.getElementById('matchText');

    // Check if the password is strong and matches
    if (/[A-Z]/.test(password) && /[a-z]/.test(password) && /\d/.test(password) &&
        /[!@#$%^&*(),.?":{}|<>]/.test(password) && password.length >= 8 && password === confirmPassword) {
        // Display success message or perform any desired action
        document.getElementById('successMessage').innerHTML = "Password is valid!";
    } else {
        // Display error message
        document.getElementById('errorMessage').innerHTML = password !== confirmPassword
            ? 'Passwords do not match.'
            : 'Password must have A-Z, a-z, 0, @, 8 digits.';
    }
}



// validate signup form

function validateSignupForm() {
    var username = document.getElementById('username').value.trim();
    var email = document.getElementById('email').value.trim();
    var password = document.getElementById('password').value.trim();
    var confirmPassword = document.getElementById('confirmPassword').value.trim();

    // Check if username, email, and password are not empty
    if (username === '' || email === '' || password === '' || confirmPassword === '') {
        // If any of the fields is empty, return false to prevent form submission
        return false;
    }

    // Check if username is already taken
    var usernameErrorMessage = document.getElementById('username-check').innerHTML;
    if (usernameErrorMessage && usernameErrorMessage.includes('already exists')) {
        return false;
    }

    // Check if email is already taken
    var emailErrorMessage = document.getElementById('email-check').innerHTML;
    if (emailErrorMessage && emailErrorMessage.includes('already exists')) {
        return false;
    }

    // Check if password meets strength criteria
    var strengthErrorMessage = document.getElementById('strengthText').innerHTML;
    if (strengthErrorMessage && strengthErrorMessage !== '') {
        return false;
    }

    // Check if password and confirm password match
    var matchErrorMessage = document.getElementById('matchText').innerHTML;
    if (matchErrorMessage && matchErrorMessage !== '') {
        return false;
    }

    // If all conditions are met, return true to allow form submission
    return true;
}


// country code mobile number
const phoneInputField = document.querySelector("#inputPhone");
const phoneInput = window.intlTelInput(phoneInputField, {
  utilsScript:
    "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});