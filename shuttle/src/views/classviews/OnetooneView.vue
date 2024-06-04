<template>
  <div class="onetoone">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class="title">
      <h1>個別班</h1>
    </div>

    <img src="../../images/c-onetoone.jpg" alt="初階班" class="class-img">

    <div class="about">
      招生對象：程度不限制，只要想認真學習羽球，我們皆可以依需求安排教練及規劃客製化的訓練課表。<br>
      <p>(請依實際上課人數來報名課程項目)</p>

      <h3>一對一/一對二/一對三</h3>
      <h3>三人以上請報名團班</h3>
    </div>

    <div class="time">
      <p>課程費用&時間：請自行洽詢教練報價，或者點擊上方聯絡我們</p>
    </div>
    <router-link to="/"><button class="i-button">回首頁</button></router-link>
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

.onetoone {
  font-family: "Zen Kurenaido", sans-serif;
  margin-top: 30px;
  margin-left: 50px;

  margin-right: 50px;

  display: flex;

  justify-content: center;

  flex-direction: column;

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

.title {
  display: flex;
}

.about p {
  font-size: 13pt;
}

.time {
  display: flex;
  font-size: 12pt;
  color: #616161;
}
</style>
