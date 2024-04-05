<template>
  <div class="zerodozen">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <h1>This is an zerodozen page</h1>
    <router-link to="/"><button class="i-button">回首頁</button></router-link>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
@media screen and (max-width: 320px) {

  /* iPhone SE 的寬度 */
  /* 適應較小屏幕的調整 */
  .g-header-container.fixed {
    padding: 5px;
    /* 減少內間距 */
  }

  .g-footer-container {
    padding: 5px;
    /* 減少內間距 */
  }

  .m-button {
    margin-right: 5px;
    /* 減少間距 */
    font-size: 12px;
    /* 縮小字體大小 */
  }
}

.zerodozen {
  font-family: "Zen Kurenaido", sans-serif;
  margin-top: 30px;
  margin-left: 50px;
  /* Add left margin */
  margin-right: 50px;
  /* Add right margin */
  display: flex;
  /* Center content */
  justify-content: center;
  /* Center content */
  flex-direction: column;
  /* Arrange content vertically */
}

.i-button {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #AFCCDC;
}

.i-button:hover {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #AFCCDC;
  background-color: #000;
}
</style>
