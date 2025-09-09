

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const addToCart = document.querySelectorAll('.update-cart')

for (let i = 0; i < addToCart.length; i++) {
    addToCart[i].addEventListener('click', function() {

        const product_id = this.dataset.product

        fetch('/updatecart', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'product_id': product_id })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(data); // see the full response
            // ✅ update cart number immediately
            document.getElementById('cart-total').innerText = data.cartItems;
        })
        .catch(error => console.error('Error:', error));
    })
}
