function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');








const addToCartBtn = document.querySelectorAll('button')

addToCartBtn.forEach(function(item) {

item.addEventListener('click', function() {
   const product_id = this.dataset.product
  

   const url = '/update-items'


   fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});


})
    
})