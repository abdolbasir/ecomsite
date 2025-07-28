
if (localStorage.getItem('cart') == null){
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
    document.querySelector("#cart").innerHTML = `Cart(${Object.keys(cart).length})`

}

$(document).on('click', '.btn-atc', function(){
    const item_id = this.id.toString();
    if(cart[item_id] != undefined){
        cart[item_id] += 1
    }else{
        cart[item_id] = 1
    }
    localStorage.setItem('cart', JSON.stringify(cart))
    document.querySelector("#cart").innerHTML = `Cart(${Object.keys(cart).length})`
 });

const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
      popoverTriggerList.forEach(el => {
        new bootstrap.Popover(el, {
          trigger: 'hover',
          html: true,
          customClass: 'custom-dark-popover'
        });
      });
cart_popover = document.querySelector('[data-bs-toggle="popover"]')
cart_popover.setAttribute('data-bs-content', DisplayCart(cart))
function DisplayCart(cart){
    var cartString = "<ul class='list-group'>";
    var carIndex = 1

    Object.keys(cart).forEach(key => {
        product_title = document.querySelector("#pt"+key).innerHTML
        cartString += `<li  class="list-group-item d-flex justify-content-between align-items-center">${carIndex}: ${product_title}  <span class="bg-primary px-2 rounded-pill text-white" >Qty: ${cart[key]} </span> </li>` 
        carIndex += 1
    })   
    cartString += "</ul>"
    
    return cartString
}
