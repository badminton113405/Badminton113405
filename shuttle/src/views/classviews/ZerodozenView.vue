<template>
  <div class="zerodozen">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class="title">
      <h1>零打班</h1>
      <div class="title1">(適合羽球全階級)</div>
    </div>

    <img src="../../images/c-zerodozen.jpg" alt="初階班" class="class-img">

    <div class="about">
      <p>招生對象：不限制，只要想打羽球、想來揮灑汗水的所有人皆可以參加！</p>
      <p1>(需自備球具)</p1>

      <h2>基礎零打班：適用羽球階級7以下</h2>      
      <p2>課程費用：350/次</p2>

      <h2>進階零打班：適用羽球階級8以上</h2>
      <p2>課程費用：350/次</p2>
    </div> 

    <div class="time">
      <h2>課程時段:</h2> 
      <p>星期五&星期六&星期日 晚上7:00~10:00</p>
      <h2>指導教練:</h2>
      <li>蔡元振 教練、張秉洋 教練(五)</li>
      <li>林奕勝 教練、張詒婷 教練(六)</li>
      <li>張秉洋 教練、林奕勝 教練(日)</li>
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

.zerodozen h2 {
  margin-top: 5;
}

.i-button {
  margin-top: 10pt;
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
  display:flex;
}

.title1 {
  margin-top: 28pt;
  margin-left: 5pt;
}

.time{
  
  list-style-type: none;
  font-size: 12pt;
  margin-top: 10pt;
}

</style>
