var updateBtns = document.getElementsByClassName('update-cart')
var updateBtnsCart = document.getElementsByClassName('update-cart-cart')
var changeQ = document.getElementsByClassName('increase')
var wishlist = document.getElementsByClassName('addWishlist')

for (i = 0; i < wishlist.length; i++) {
    wishlist[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        
        
        if (user == 'AnonymousUser'){
			Console.log('Not Logged in!')
		}else{
			addToWishlist(productId, action)
		}
    })
}
function addCookieItemWish(productId, action){
	console.log('User is not authenticated')
	var quantity = Number(document.querySelector('input[data-product="'+productId+'"]').value)
	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity': quantity}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId]
		}
	}
	if (action == 'delete'){
		cart[productId]['quantity'] == 0
			delete cart[productId]
	}
	
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}


function addToWishlist(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/add_wishlist/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		
		.then((data) => {
		    location.reload()
		})
}


for (i = 0; i < changeQ.length; i++) {
    changeQ[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        
        
        if (action == 'plus'){
            Increase(productId, action)
        }
        else if(action=='minus'){
            Decrease(productId, action)
  
        }
    })
}

function Increase(productId,action){
    var quantity = Number(document.querySelector('input[data-product="'+productId+'"]').value);
    quantity = quantity+1;
    document.querySelector('input[data-product="'+productId+'"]').value = quantity;
}


function Decrease(productId,action){
    var quantity = Number(document.querySelector('input[data-product="'+productId+'"]').value);
    quantity = quantity-1;
    if(quantity<1){
    	quantity=1;
    }
    document.querySelector('input[data-product="'+productId+'"]').value=quantity;

}



for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		var quantity = Number(document.querySelector('input[data-product="'+productId+'"]').value)
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(productId, action,quantity)
		}else{
			updateUserOrder(productId, action,quantity)
		}
	})
}

function updateUserOrder(productId, action, quantity){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action, 'quantity':quantity})
		})
		.then((response) => {
		   return response.json()
		})
		.then((data) => {
		    location.reload()
		})
}

function addCookieItem(productId, action){
	console.log('User is not authenticated')
	var quantity = Number(document.querySelector('input[data-product="'+productId+'"]').value)
	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity': quantity}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId]
		}
	}
	if (action == 'delete'){
		cart[productId]['quantity'] == 0
			delete cart[productId]
	}
	
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}

for (i = 0; i < updateBtnsCart.length; i++) {
	updateBtnsCart[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		var quantity = Number(document.querySelector("input[class='child']").value)
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem1(productId, action,quantity)
		}else{
			updateUserOrder1(productId, action,quantity)
		}
	})
}

function updateUserOrder1(productId, action, quantity){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action, 'quantity':quantity})
		})
		.then((response) => {
		   return response.json()
		})
		.then((data) => {
		    location.reload()
		})
}

function addCookieItem1(productId, action){
	console.log('User is not authenticated')
	var quantity = Number(document.querySelector('input[data-product="'+productId+'"]').value)
	var quantity1 = Number(document.querySelector("input[class='child']").value)
	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity': quantity1}

		}else{
			cart[productId]['quantity'] += quantity1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= quantity1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId]
		}
	}
	if (action == 'delete'){
		cart[productId]['quantity'] == 0
			delete cart[productId]
	}
	
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}