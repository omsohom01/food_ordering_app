document.addEventListener('DOMContentLoaded', () => {
    const products = [
        { id: 1, name: 'Pepperoni Pizza', category: 'pizza', price: 12.99, image: 'images/pizza.jpg' },
        { id: 2, name: 'Cheeseburger', category: 'burger', price: 8.99, image: 'images/burger.jpg' },
        { id: 3, name: 'California Roll', category: 'sushi', price: 10.99, image: 'images/sushi.jpg' }
    ];

    const productsContainer = document.getElementById('products');
    const categoryFilter = document.getElementById('category');
    const priceFilter = document.getElementById('price');
    const priceValue = document.getElementById('priceValue');

    function renderProducts() {
        productsContainer.innerHTML = '';
        const selectedCategory = categoryFilter.value;
        const maxPrice = priceFilter.value;

        products.forEach(product => {
            if ((selectedCategory === 'all' || product.category === selectedCategory) && product.price <= maxPrice) {
                const productElement = document.createElement('div');
                productElement.className = 'product';
                productElement.innerHTML = `
                    <img src="${product.image}" alt="${product.name}">
                    <h3>${product.name}</h3>
                    <p>$${product.price.toFixed(2)}</p>
                    <button onclick="addToCart(${product.id})">Add to Cart</button>
                `;
                productsContainer.appendChild(productElement);
            }
        });
    }

    function addToCart(productId) {
        alert(`Product ${productId} added to cart!`);
        // Add your cart logic here
    }

    categoryFilter.addEventListener('change', renderProducts);
    priceFilter.addEventListener('input', () => {
        priceValue.textContent = priceFilter.value;
        renderProducts();
    });

    renderProducts(); // Initial render
});

