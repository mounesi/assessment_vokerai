<script>
  import { placeOrder } from '../services.js';

  let message = '';

  async function handleSubmit() {
    if (!message) {
        alert('Please enter an order');
        return;
    }
    await placeOrder(message);
    message = '';
  }
</script>

<style>
  .form {
    display: flex;
    gap: 10px;
    margin-top: 20px;
  }

  input {
    flex: 1;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }

  button {
    background-color: #4CAF50;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.2s;
  }

  button:hover {
    background-color: #45a049;
  }

  button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
</style>

<div class="form">
  <input
    type="text"
    bind:value={message}
    placeholder="Ex: I want 2 burgers and 1 fries"
  />
  <button on:click={handleSubmit}>Run</button>
</div>
