<script>
  import { orders } from '../store.js';
  import { cancelOrder } from '../services.js';

  async function handleCancel(orderId) {
    await cancelOrder(orderId);
  }
</script>

<style>
  .order-item {
    padding: 10px;
    border-bottom: 1px solid #ddd;
    display: flex;
    justify-content: space-between;
  }

  button {
    background-color: #ff4d4d;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 4px;
    cursor: pointer;
  }
</style>

<div>
  {#each $orders as order}
    <div class="order-item">
      <div>
        Order #{order.id} - {order.burgers} Burgers, {order.fries} Fries, {order.drinks} Drinks
      </div>
      <button on:click={() => handleCancel(order.id)}>Cancel</button>
    </div>
  {/each}
</div>
