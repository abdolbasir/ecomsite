
if (localStorage.getItem('cart') == null){
    var cart = {};
} else {
    cart = JSON.parse(localStorage.getItem('cart'));
}

$(document).on('click', '.btn-atc', function(){
    const item_id = this.id.toString();
    if(cart[item_id] != undefined){
        cart[item_id] += 1
    }else{
        cart[item_id] = 1
    }
    localStorage.setItem('cart', JSON.stringify(cart))
    console.log(cart)
 });

