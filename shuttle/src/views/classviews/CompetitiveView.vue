<template>
  <div class="competitive">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class="title">
      <h1>競技班</h1>
      <div class="title1">(適合羽球階級6級以上)</div>
    </div>
    
    <img src="../../images/c-competitive.jpg" alt="初階班" class="class-img">

    <div class="about">
      <p>招生對象：球齡超過3年以上，有雙打輪轉的觀念。基本腳步也已熟能生巧</p>

      <h2>一般競技班(建議13歲以上)</h2>  
      適合觀念還需精進，動作還想調整的學生<br>    
      課程費用：4000/期(8堂課)<br>

      <h2>進階競技班(建議13歲以上)</h2>
      本班以學生對練及實戰為主，教練會下場陪同實戰訓練<br>     
      課程費用：4000/期(8堂課)<br>
    </div> 

    <div class="time">
      <h2>課程時段:</h2> 
      (一般)星期二下午2:00~4:00 & 4:00~6:00<br>
      (進階)星期四下午2:00~4:00 & 4:00~6:00<br>         
      <p>指導老師:胡玟翰 教練、張秉洋 教練</p>
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

  /* iPhone SE 的宽度 */
  /* 适应较小屏幕的调整 */
  .g-header-container.fixed {
    padding: 5px;
    /* 减少填充 */
  }

  .g-footer-container {
    padding: 5px;
    /* 减少填充 */
  }

  .m-button {
    margin-right: 5px;
    /* 减少边距 */
    font-size: 12px;
    /* 减少字体大小 */
  }
}

.competitive {
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

.competitive h2 {
  margin-top: 5;
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
  display:flex;
}

.title1 {
  margin-top: 28pt;
  margin-left: 5pt;
}

.about h3 {
  margin-top: 5px;
}

.time{
  font-size: 12pt;
  margin-top: 10pt;
}
</style>
