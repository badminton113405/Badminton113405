<template>
  <div class="about">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class="header">教練團隊</div>
    <div class="coach-container">
      <img src="../../images/co-chaiyuanzheng.jpg" alt="蔡元振">
      <router-link to="/cyz"><button class="coach-button">蔡元振</button></router-link>
    </div>
    <div class="coach-container">
      <img src="../../images/co-zhozhongting.jpg" alt="周仲庭">
      <router-link to="/zzt"><button class="coach-button">周仲庭</button></router-link>
    </div>
    <div class="coach-container">
      <img src="../../images/co-zhangbingying.jpg" alt="張秉洋">
      <router-link to="/zby"><button class="coach-button">張秉洋</button></router-link>
    </div>
    <div class="coach-container">
      <img src="../../images/co-huwenhan.jpg" alt="胡玟翊">
      <router-link to="/hwh"><button class="coach-button">胡玟翊</button></router-link>
    </div>

    <div class="button-container">
      <router-link to="/"><button class="i-button">回首頁</button></router-link>
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
@media screen and (max-width: 320px) {


  .g-header-container.fixed {
    padding: 5px;

  }

  .g-footer-container {
    padding: 5px;

  }

  .m-button {
    margin-right: 5px;

    font-size: 12px;

  }
}

.about {
  font-family: "Zen Kurenaido", sans-serif;
  margin-top: 30px;
  margin-left: 10px;

  margin-right: 10px;

  display: flex;

  justify-content: center;

  flex-direction: column;

}

.header {
  text-align: center;
  font-weight: bold;
  font-size: 24px;
  margin-bottom: 20px;

}

.coach-container {
  display: flex;
  align-items: center;
  gap: 20px;
}

.coach-container img {
  border-radius: 20px;
  width: 200px;
  height: 150px;
  object-fit: cover;
  border: 2px solid black;
  margin-top: 20px;
}

.coach-button {
  font-family: "Zen Kurenaido", sans-serif;
  background-color: #ffecd5;
  border: none;
  padding: 10px 20px;
  border-radius: 16px;
  color: #000;
  cursor: pointer;
}

.coach-button:hover {
  font-family: "Zen Kurenaido", sans-serif;
  color: #000;
  background-color: #fde0a6;
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.i-button {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #c2cae7;

}

.i-button:hover {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #93a9d8;
}
</style>
