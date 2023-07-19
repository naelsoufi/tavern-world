$(document).ready(function() {
    $("#get-level-two-information").click(function() {
        // Get the tavern's id
        const tavern_id = $(this).data('tavern-id');

        // Disable the button after it's clicked
        $(this).prop('disabled', true);

        // Make a POST request to the Flask route
        fetch('/get_tavern_level_two', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token() }}'
            },
            body: JSON.stringify({ tavern_id: tavern_id })
        })
        .then(response => response.json())
        .then(data => {
            // Create a list to append to
            const ul = document.createElement('ul');

            // Loop through the data and create a line for each item
            data.value.forEach(item => {
                const li = document.createElement('li');
                li.textContent = item;
                ul.appendChild(li);
            })
            // Update the value-container div with the returned value
            $("#level-two-information").append(ul);
        })
        .catch(error => console.log('Error:', error));
    });
});
