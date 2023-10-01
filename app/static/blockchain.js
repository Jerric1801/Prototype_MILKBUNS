import shipments from './get_chain.json' assert {type: 'json'};

console.log(shipments);

let table = document.getElementById('table');

for (let block in shipments.chain) {
    console.log(block);
    if (block == 0) {
        let row = document.createElement('div');
        row.setAttribute('id', 'row');
        let col1 = document.createElement('div');
        col1.setAttribute("class", "block")
        col1.innerText = 'Genesis';
        let col2 = document.createElement('div');
        let hash = shipments.chain[block]['current_hash'];
        let span = document.createElement("span");
        span.setAttribute("class", "collapsible");
        span.setAttribute("id","expand" + shipments.chain[block]['index']);
        span.addEventListener('click',change);
        span.textContent ='[+]';
        col2.appendChild(span)
        let hashshort = hash.slice(0,10) + "...";
        let shortspan = document.createElement('span');
        shortspan.setAttribute("id","shortspan" + shipments.chain[block]['index']);
        shortspan.setAttribute("style","display:inline;")
        shortspan.textContent = hashshort;
        let longspan = document.createElement('span');
        longspan.setAttribute("id","longspan" + shipments.chain[block]['index']);
        longspan.setAttribute("style","display:none;");
        longspan.textContent = hash;
        col2.appendChild(shortspan);
        col2.appendChild(longspan);
        col2.setAttribute("class", "hash");
        let col3 = document.createElement('div');
        col3.setAttribute("class", "supplier");
        let col4 = document.createElement('div');
        col4.setAttribute("class", "cargo");
        let col5 = document.createElement('div');
        col5.setAttribute("class", "amount");
        let col6 = document.createElement('div');
        col6.setAttribute("class", "destination");
        col3.innerText = '-';
        col4.innerText = '-';
        col5.innerText = '-';
        col6.innerText = '-';
        row.append(col1, col2, col3, col4, col5, col6);
        table.appendChild(row);
    }
    else {
        let row = document.createElement('div');
        row.setAttribute('id', 'row');
        let col1 = document.createElement('div');
        col1.innerText = shipments.chain[block]['index'];
        col1.setAttribute("class", "block")
        let col2 = document.createElement('div');
        let hash = shipments.chain[block]['current_hash'];
        let span = document.createElement("span");
        span.setAttribute("class", "collapsible");
        span.setAttribute("id","expand" + shipments.chain[block]['index']);
        span.addEventListener('click',change);
        span.textContent ='[+]';
        col2.appendChild(span)
        let hashshort = hash.slice(0,10) + "...";
        let shortspan = document.createElement('span');
        shortspan.setAttribute("id","shortspan" + shipments.chain[block]['index']);
        shortspan.setAttribute("style","display:inline;")
        shortspan.textContent = hashshort;
        let longspan = document.createElement('span');
        longspan.setAttribute("id","longspan" + shipments.chain[block]['index']);
        longspan.setAttribute("style","display:none;");
        longspan.textContent = hash;
        col2.appendChild(shortspan);
        col2.appendChild(longspan);
        col2.setAttribute("class", "hash");
        let col3 = document.createElement('div');
        col3.innerText = shipments.chain[block]['shipment'][0];
        col3.setAttribute("class", "supplier");
        let col4 = document.createElement('div');
        col4.innerText = shipments.chain[block]['shipment'][1];
        col4.setAttribute("class", "cargo");
        let col5 = document.createElement('div');
        col5.innerText = shipments.chain[block]['shipment'][2];
        col5.setAttribute("class", "amount");
        let col6 = document.createElement('div');
        col6.innerText = shipments.chain[block]['shipment'][3];
        col6.setAttribute("class", "destination");
        row.append(col1, col2, col3, col4, col5, col6);
        table.appendChild(row);
    }
    function change(){
    let link = event.target;
    let identifier = link.id.substring(6);
    console.log(identifier)
    if(link.innerText == '[+]'){
    document.getElementById('shortspan'+ identifier).setAttribute("style", 'display:none');
    //dnone hides the element d inline shows it therefore before toggle function toggle must be attached to watever text u need to click and make 2 different elemts one for short form one for long
    document.getElementById('longspan' + identifier).setAttribute("style","display:inline");
    link.innerText ='[-]';
    }
    else{
    document.getElementById('shortspan' + identifier).setAttribute("style","display:inline");
    document.getElementById('longspan' + identifier).setAttribute("style","display:none");
    link.innerText ='[+]';
    }
    };
}