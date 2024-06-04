<template>
  <div class="zzt">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <h2>教練團隊</h2>
    <img src="../../images/co-zhozhongting.jpg" alt="周仲庭">
    <div class="name-gender-specialty">
    <div class="name-gender">
        <div class="name">周仲庭</div>
        <div class="gender">/女</div>
    </div>
    <div class="specialty">
      <span>特質</span>
        <br>活潑、外向<br>
      <span>專長項目</span>
        <br>雙打輪轉<br>
    </div>
    </div>
    <div class="experience">
      <span>經歷：</span>
        <ul>
          <li>中華羽協A級教練</li>
          <li>中華民國羽球協會甲組球員</li>
          <li>恆耀羽球學院A及專業教練</li>        
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

.zzt {
  font-family: "Zen Kurenaido", sans-serif;
  margin-top: 30px;
  margin-left: 10px;
 
  margin-right: 10px;
 
  display: flex;
 
  justify-content: center;
 
  flex-direction: column;
 
  max-width: 500px;
}

.zzt img {
  border-radius: 5pt;
  object-fit: cover;
}

.name-gender {
  display: flex; 
  align-items: center;
  margin-left: 10pt;
}

.name-gender-specialty {
  display: flex;
  align-items: center;
  margin-top: 0px;
  gap: 130px; 
}

.name {
  font-size: 24px;
  display: flex;
}

.gender {
  font-size: 18px;
  margin-right: -2pt;
  margin-left: 5pt;
}

.specialty {
  background-color: rgba(255, 255, 255, 0.8);
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 0 5px rgba(0,0,0,0.1);
  text-align: center;
  justify-content: space-between;
  }

.specialty, .experience, .teaching-methods, .contact-info {
  text-align: left;
  margin-top: 10px;
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
