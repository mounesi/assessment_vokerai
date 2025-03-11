<script>
  import { burgers, fries, drinks } from '../store.js';
</script>

<style>
  .summary-container {
    display: flex;
    gap: 20px;
    margin-top: 20px;
  }

  .box {
    padding: 16px;
    border: 2px solid #ccc;
    border-radius: 8px;
    width: 150px;
    background-color: #f9f9f9;
    font-weight: bold;
    text-align: center;
    transition: transform 0.2s ease;
  }

  .box:hover {
    transform: scale(1.05);
  }

  .icon {
    margin-right: 8px;
  }
</style>

<div class="summary-container">
  <!-- ✅ Updated to display dynamic state values -->
  <div class="box">
    🍔 <span class="icon">Burgers:</span> {$burgers}
  </div>
  <div class="box">
    🍟 <span class="icon">Fries:</span> {$fries}
  </div>
  <div class="box">
    🥤 <span class="icon">Drinks:</span> {$drinks}
  </div>
</div>
