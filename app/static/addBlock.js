function newBlock() {
    supplier = document.getElementById('addBlock').elements['supplier'].value;
    cargo = document.getElementById('addBlock').elements['cargo'].value;
    amount = document.getElementById('addBlock').elements['amount'].value;
    destination = document.getElementById('addBlock').elements['destination'].value;

   const json_data = JSON.stringify({
        'supplier': supplier,
        'cargo': cargo,
        'amount': amount,
        'destination': destination,
    });

    url = "/updateBlock"
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: json_data
    })
    .then(response => response.json())
    .then(data => {
        if (data == "success") {
            // Get the table element
            const table = document.getElementById("Table");

            // Get the hash fragment of the table
            const hashFragment = table.getAttribute("data-hash-fragment");

            // Reload the page with the hash fragment
            window.location.reload(hashFragment);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
