<template>
  <div class="beginner">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <h2>課程介紹</h2>
    <nav1><h1>初階班</h1><p>(適合羽球階級1~5級)</p></nav1>

    <nav2>
      <p>招生對象：剛接觸羽球，對於握拍及基礎動作還不熟悉，或是已接觸過一陣子想更加熟練或調整動作的學生。</p>
      <p>兒童初階班(7~12歲)</p>
      <l>課程費用：4000/期(8堂課)</l>
      <p>成人初階班(13歲以上)</p>
      <l>課程費用：4000/期(8堂課)</l>
    </nav2> 

    <nav3>
      <p>課程時段:</p> 
        <p>(兒童)星期三下午2:00~3:30 & 3:30~5:00</p>
        <p>(成人)星期一下午2:00~4:00 & 4:00~6:00 以及 星期三 晚上5:00~7:00</p>
         
        <P>指導教練:蔡元振 教練、周仲庭 教練</P>
    </nav3> 

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


.beginner {
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
  background-color: #c2cae7;
}

.i-button:hover {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #93a9d8;
}
</style>
