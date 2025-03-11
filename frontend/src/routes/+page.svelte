<script>
  import { onMount } from 'svelte';
  import OrderSummary from '../components/OrderSummary.svelte';
  import OrderForm from '../components/OrderForm.svelte';
  import OrderHistory from '../components/OrderHistory.svelte';
  import { fetchSummary, fetchOrders } from '../services.js';

  // ✅ Fetch data on load
  onMount(() => {
    fetchSummary(); // ✅ Load total counts
    fetchOrders();  // ✅ Load orders
  });
</script>

<!-- ✅ Updated Title -->
<h1>Welcome to Voker Burger Place 🍔</h1>

<OrderSummary />
<OrderForm />
<OrderHistory />
