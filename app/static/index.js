async function findPorts() {

    const inputs = $(".userInput")

    const toRaise = []
    var count = 0

    var date1 = $("#earliestArrival").val()
    var date2 = $("#latestArrival").val()

    //error handling
    inputs.each(function(){
        $(this).css({
            border: "1px solid grey"
        })
        if ($(this).val() == "" || $(this).val() == undefined ){
            toRaise.push(count)
        }
        count++
    })

    if (toRaise.length > 0) {
        $("#errorMessage").css({
            display: "block"
        })
        for(var e in toRaise) {
            inputs.eq(toRaise[e]).css({
                border: "1px solid red"
            })
        }
    }
    else if (date1 > date2){
        $("#errorMessage").html("Your latest arrival is earlier than your earliest arrival")
        $("#errorMessage").css({
            display: "block"
        })
    }
    else {

    // e.preventDefault()
    url = "/predict"
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"earliest": date1, "latest": date2})
    })
    .then(response => response.json())
    .then(data => {
        //store data
        localStorage.setItem("results", JSON.stringify(data))
        //redirect page
        window.location.href = "/results"
    })
    .catch(error => {
        console.error('Error:', error);
    });
    } //else statement
}