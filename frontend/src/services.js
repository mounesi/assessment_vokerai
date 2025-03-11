import { burgers, fries, drinks, orders } from './store.js';

const BASE_URL = 'http://127.0.0.1:8000';

export async function fetchSummary() {
    const res = await fetch(`${BASE_URL}/summary/?tenant_id=test`);
    if (res.ok) {
        const data = await res.json();
        console.log('Summary:', data); // ✅ Debug log
        burgers.set(data.total_burgers);
        fries.set(data.total_fries);
        drinks.set(data.total_drinks);
    }
}

export async function fetchOrders() {
    const res = await fetch(`${BASE_URL}/orders/?tenant_id=test`);
    if (res.ok) {
        const data = await res.json();
        console.log('Orders:', data); // ✅ Debug log
        orders.set(data.orders);
    }
}

export async function placeOrder(message) {
    const res = await fetch(`${BASE_URL}/place_order/?tenant_id=test`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message })
    });

    if (res.ok) {
        console.log("✅ Order placed successfully");

        // ✅ Refresh state after successful order
        await fetchSummary();  // <-- Update totals
        await fetchOrders();   // <-- Update order list
    } else {
        const error = await res.json();
        alert(`❌ Error: ${error.detail}`);
    }
}

export async function cancelOrder(orderId) {
    const res = await fetch(`${BASE_URL}/cancel_order/?tenant_id=test`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: `Cancel order #${orderId}` })
    });

    if (res.ok) {
        console.log(`✅ Order ${orderId} canceled`);
        await fetchSummary();  // <-- Refresh totals
        await fetchOrders();   // <-- Refresh orders
    } else {
        const error = await res.json();
        alert(`❌ Error: ${error.detail}`);
    }
}

