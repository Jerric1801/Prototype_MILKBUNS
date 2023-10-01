//function to retrieve markers
function returnHome() {
    window.location.href = "/"
}

function createPortItem(data) {
    const country = data["country"]
    const image = data["image"]
    const location = data["port"]
    const date = data["date"]
    const cost = data["cost"]

    const portItem = document.createElement("div");
    portItem.classList.add("portItem");
    
    // Create the portItemImg container.
    const portItemImg = document.createElement("div");
    portItemImg.classList.add("portItemImg");
    portItemImg.innerHTML = `<img src="../static/img/${image}">`;
    
    const portItemDesc = document.createElement("div");
    portItemDesc.classList.add("portItemDesc");
    
    const portItemTitle = document.createElement("p");
    portItemTitle.innerHTML = `<span class="portItemTitle">${country}, ${location} <br> on ${date}</span>`;
    portItemDesc.appendChild(portItemTitle);

    portItemDesc.innerHTML += `<p>Berthing, Pilotage, Towage, Fueling, Repairs</p>`;
    portItemDesc.innerHTML += `<p style="text-align: right;"><span class="portItemCost">${cost}</span></p>`;
    
    portItem.appendChild(portItemImg);
    portItem.appendChild(portItemDesc);

    return portItem
}

async function getKey() {
    const response = await fetch(url);
    const key = await response.json();
    return key;
}

$(document).ready(async function() {

    //retrieve input data from localStorage
    var data = JSON.parse(localStorage.getItem("results"))

    //retrieve key from heroku env

    url = "/loadKey"
    const key = await getKey(url)

    mapboxgl.accessToken = key
    const map = new mapboxgl.Map({
      container: 'map',
      // Replace YOUR_STYLE_URL with your style URL.
      style: 'mapbox://styles/mapbox/navigation-day-v1', 
      center: [103.609478, 1.2420372],
      zoom: 15
    });

    for (index in data) {
        const el = document.createElement('div');
        el.className = "marker"

        const coord = data[index]["coord"]

        const title = data[index]["port"]

        const portItem = createPortItem(data[index])

        $("#portContainer").append(portItem)

        new mapboxgl.Marker(el).setLngLat(coord).setPopup(
            new mapboxgl.Popup({ offset: 25 }) // add popups
            .setHTML(
                `<h3>${title}</h3><p>Longitude:${coord[0]} Latitude:${coord[1]}</p>`
            )
            ).addTo(map);
    }

})
