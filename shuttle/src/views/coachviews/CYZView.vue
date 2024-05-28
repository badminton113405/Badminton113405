<template>
  <div class="cyz">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <h2>教練團隊</h2>
      <img src="../../images/co-chaiyuanzheng.jpg" alt="蔡元振">
    <div class="name-gender-specialty">
      <div class="name-gender">
        <div class="name">蔡元振</div>
        <div class="gender">/男</div>
    </div>
    <div class="specialty">
      <p>特質</p>活潑、外向
      <p>專長項目</p>單打四角拉吊
    </div>
    </div>
    <div class="experience">
      <span>經歷：</span>
        <ul>
          <li>中華羽協C級教練</li>
          <li>台北商業大學羽球校隊</li>
          <li>全國大專校院一班組男單16強</li>
          <li>全國大專校院校際大專中區男雙第五名</li>
          <li>大豐國小羽球校隊助教</li>
        </ul>
    </div>
    <div class="teaching-methods-contact-info">
    <div class="teaching-methods">
      <span>教學方式：</span>
        <ul>
          <li>基礎動作教學</li>
          <li>階段式訓練</li>
          <li>體能訓練</li>
          <li>實戰教學</li>
        </ul>
    </div>
    <div class="contact-info">
      <span>聯絡資訊：</span>
          <br>0987569423<br>
          <img src="../../images/LINE.jpg" alt="QR Code" width="100">
    </div> 
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

.cyz {
  font-family: "Zen Kurenaido", sans-serif;
  margin-top: 30px;
  margin-left: 10px;
  /* Add left margin */
  margin-right: 10px;
  /* Add right margin */
  display: flex;
  /* Center content */
  justify-content: center;
  /* Center content */
  flex-direction: column;
  /* Arrange content vertically */
  max-width: 500px;
}

.cyz img {
  border-radius: 5pt;
  object-fit: cover;
}

.name-gender {
  display: flex; 
  align-items: center;
  margin-top: 0px;
}

.name-gender-specialty {
  display: flex;
  align-items: center;
  margin-top: 0px;
  gap: 250px; /* 調整項目之間的間距 */
}

.name {
  font-size: 24px;
  margin-top: 10px;
}

.gender {
  font-size: 16px;
  display: flex;
}

.specialty {
  background-color: rgba(255, 255, 255, 0.8);
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 0 5px rgba(0,0,0,0.1);
  text-align: center;
  line-height: 0.7;
  }

.specialty, .experience, .teaching-methods, .contact-info {
  text-align: left;
  margin-top: 20px;
}

.experience span, .teaching-methods span, .contact-info span {
  font-weight: bold;
}

.contact-info{
  text-align: center;
}

.contact-info img {
  display: block;
  margin: 10px auto 0;
}

.teaching-methods-contact-info {
  display: flex;
  justify-content: space-between;
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
