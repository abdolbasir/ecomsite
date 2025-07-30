
if (localStorage.getItem('cart') == null){
    var cart = {}
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
    document.querySelector("#cart").innerHTML = `Cart(${Object.keys(cart).length})`

}

$(document).on('click', '.btn-atc', function(){
    const item_id = this.id.toString();
    if(cart[item_id] != undefined){
        cart[item_id]['quantity'] += 1  
    }else{
       item_quantity = 1
       item_name = document.querySelector(`#pt${item_id}`).innerHTML
       item_price = document.querySelector(`#pp${item_id}`).innerHTML
       cart[item_id] = {
        "quantity": item_quantity,
        "price": item_price, 
        "title": item_name
       }

    }
    localStorage.setItem('cart', JSON.stringify(cart))
    document.querySelector("#cart").innerHTML = `Cart(${Object.keys(cart).length})`
 });

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
      popoverTriggerList.forEach(el => {
        new bootstrap.Popover(el, {
          trigger: 'click',
          html: true,
          customClass: 'custom-dark-popover'
        });
      });
cart_popover = document.querySelector('[data-bs-toggle="popover"]')
DisplayCart(cart)
cart_popover.setAttribute('data-bs-content', DisplayCart(cart))
function DisplayCart(cart){
    var cartString = "<ul class='list-group'>";
    var carIndex = 1

    Object.keys(cart).forEach(key => {
        cartString += `<li  class="list-group-item d-flex justify-content-between align-items-center">${carIndex}: ${cart[key]['title']}  <span class="bg-primary px-2 rounded-pill text-white" >Qty: ${cart[key]['quantity']} </span> </li>` 
        carIndex += 1
    })  
    cartString += "</ul>"
    cartString += "<a class='btn btn-dark align-center mt-2' href='/checkout'>Checkout</a>";
    return cartString
}
