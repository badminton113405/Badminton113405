<template>
  <div class="hwh">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <h2>教練團隊</h2>
    <img src="shuttle/src/images/co-chaiyuanzheng.jpg" alt="胡玟翰">
    <div class="name-gender">
        <div class="name">胡玟翰</div>
        <div class="gender">/男</div>
    </div>
    <div class="specialty">
      <p>特質</p>外向、熱情
      <p>專長項目</p>平球壓抽擋
    </div>
    <div class="experience">
      <span>經歷：</span>
        <ul>
          <li>中華羽協C級教練</li>
          <li>輔大學體育系乙組羽球隊</li>
          <li>高中羽球團體組第一</li>
          <li>大專院校男團第二</li>          
        </ul>
    </div>
    <div class="teaching-methods">
      <span>教學方式：</span>
        <ul>
          <li>基礎動作教學</li>
          <li>進階技術教學</li>
          <li>實戰觀念技巧</li>
          <li>體能訓練</li>
          <li>實戰教學</li>
        </ul>
    </div>
    <div class="contact-info">
      <span>聯絡資訊：</span>
          <br>電話：0987569423<br>
          <img src="your-qr-code-source.jpg" alt="QR Code" width="100">
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

.hwh {
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
}
.name-gender {
  display: flex; 
  align-items: center;
  margin-top: 10px;
}
.name {
  font-size: 24px;
  margin-top: 10px;
}

.gender {
  font-size: 18px;
  margin-left: 10px;
}

.specialty {
  position: absolute;
  top: 100px; /* 根據圖片的實際位置調整 */
  left: 160px; /* 根據圖片的實際位置調整 */
  background-color: rgba(255, 255, 255, 0.8);
  padding: 10px;
  border-radius: 8px;
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
