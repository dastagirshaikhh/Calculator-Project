function Result() {
    const inputString = document.getElementById('res').value;
    const requestData = { js_string: inputString };

    fetch('/result', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
    })
    .then(response => response.json())
    .then(data => {
        const inputElement = document.getElementById('res');
        inputElement.value = data.python_string;
        console.log(data.python_string)
    })
    .catch(error => console.error('Error:', error));
}
