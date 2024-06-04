<template>
  <div class="beginner">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class="title">
      <h1>初階班</h1>
      <div class="title1">(適合羽球階級1~5級)</div>
    </div>

    <img src="../../images/c-beginner.jpg" alt="初階班" class="class-img">

    <div class="about">
      <p>招生對象：剛接觸羽球，對於握拍及基礎動作還不熟悉，或是已接觸過一陣子想更加熟練或調整動作的學生。</p>

      <h2>兒童初階班(7~12歲)</h2>
      課程費用：4000/期(8堂課)<br>

      <h2>成人初階班(13歲以上)</h2>
      <p>課程費用：4000/期(8堂課)</p>
    </div>

    <div class="time">
      <h2>課程時段:</h2>
      (兒童)星期三下午2:00~3:30 & 3:30~5:00<br>
      (成人)星期一下午2:00~4:00 & 4:00~6:00 以及 星期三 晚上5:00~7:00<br>
      <P>指導教練:蔡元振 教練、周仲庭 教練</P>
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


.beginner {
  font-family: "Zen Kurenaido", sans-serif;
  margin-top: 30px;
  margin-left: 50px;
 
  margin-right: 50px;
 
  display: flex;
  
  justify-content: center;
 
  flex-direction: column;
  
}

.beginner h2 {
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
  display: flex;
}

.title1 {
  margin-top: 28pt;
  margin-left: 5pt;
}

.time {
  font-size: 12pt;
}
</style>
