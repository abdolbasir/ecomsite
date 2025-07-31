  
if (localStorage.getItem('cart') == null){
    var cart = {}
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
    document.querySelector("#cart").innerHTML = `Cart(${Object.keys(cart).length})`

}

let total_price = 0
for(item in cart){
    console.log(item)
    let title = cart[item]['title']
    let quantity = cart[item]['quantity']
    let price = cart[item]['price']
    let cleaned_price = parseInt(price.replace('$', '').replace('.0', ''))
    total_price += (cleaned_price * quantity) 
    itemString =  `<li class="list-group-item d-flex justify-content-between align-items-start py-3"><div class="ms-2 me-auto">
                   <div class="fw-bold">${title}</div></div><span class="text-success fw-bold">${quantity} x ${price} </span>
                   </li>`
    $("#cart_list").append(itemString)
}

itemString = `<div class="list-group-item d-flex justify-content-between align-items-start py-3 fw-bolder bg-primary text-white"><div class="ms-2 me-auto">
                <div>Total Price</div></div><span>$ ${total_price} </span>
                </div>`
$("#cart_list").append(itemString)

$("#items").val(JSON.stringify(cart));

