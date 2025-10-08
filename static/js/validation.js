// This function runs when the document is ready
$(document).ready(function() {
    
    // Select the form by its tag and listen for the submit event
    $('form').on('submit', function(event) {
        
        let isValid = true;

        // --- 1. Get form values ---
        const name = $('#name').val().trim();
        const email = $('#email').val().trim();
        const message = $('#message').val().trim();

        // --- 2. Simple validation for empty fields ---
        if (name === '' || email === '' || message === '') {
            alert('Please fill out all fields.');
            isValid = false;
        }

        // --- 3. Email format validation using a regular expression ---
        // This is a simple regex for email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Please enter a valid email address.');
            isValid = false;
        }
        
        // --- 4. Prevent form submission if validation fails ---
        if (!isValid) {
            event.preventDefault(); // This stops the form from being submitted
        }
    });
});