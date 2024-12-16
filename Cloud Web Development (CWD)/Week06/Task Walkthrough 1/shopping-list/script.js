let shoppingList = [];

function ShoppingItem(name, price, inCart=false) {
    this.name = name;
    this.price = price;
    this.inCart = inCart;
}

async function getShoppingListItems(){
    const response = await fetch("https://fakestoreapi.com/products");
    const shoppingItems = await response.json();
    const outputShoppingItems = [];

    for (let i = 0; i < shoppingItems.length; i++){
        const item = new ShoppingItem(shoppingItems[i].title, shoppingItems[i].price);
        outputShoppingItems.push(item)
    }

    return outputShoppingItems;
}

function getCartCost(){
    let totalCost = 0;

    for (let i = 0; i < shoppingList.length; i++){
        if (shoppingList[i].inCart){
            totalCost += shoppingList[i].price;
        }
    }

    const cartCost = document.getElementById("cart-cost");
    cartCost.innerText = `£${totalCost}`;
}

function createListItems(){
    const ul = document.getElementById("shopping-list");

    shoppingList.forEach((item, index) => {
        const li = createListItem(item, index);        
        ul.appendChild(li)
    })
}

function createListItem(shoppingItem, index){
    const li = document.createElement("li");
    li.className = "flex justify-between border-b-1 border-black"

    const p = document.createElement("p");
    p.innerText = `${shoppingItem.name} - £${shoppingItem.price}`;
    
    const btnAddedToCart = document.createElement("button");
    btnAddedToCart.innerText = "X";

    btnAddedToCart.addEventListener("click", () => {
        p.style.textDecoration = "line-through";
        shoppingList[index].inCart = true;
        getCartCost();
    });

    li.appendChild(p);
    li.appendChild(btnAddedToCart);

    return li;
}

function addListItem(){
    const name = prompt("Item name: ");
    const price = prompt("Item Price: ");

    const item = new ShoppingItem(name, Number(price));
    shoppingList.push(item);

    const ul = document.getElementById("shopping-list");
    const li = createListItem(item, shoppingList.length - 1)
    ul.appendChild(li);
}

function setImageOfTheDay(){
    fetch("https://picsum.photos/500/500")
    .then((res) => {
        console.log(res.url);

        const image = document.getElementById("img-of-the-day");
        image.setAttribute("src", res.url)
    })
}

async function main(){
    setImageOfTheDay();
    document.getElementById("add-item").addEventListener("click", () => addListItem());    
    shoppingList = await getShoppingListItems();
    createListItems();
}

main();