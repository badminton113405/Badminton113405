<template>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <div class="main">
    <div class="video-container">
      <video controls ref="videoPlayer">
        <source src="https://youtu.be/evJazpDJ7eQ?si=w12dIbthP8K6ubn9" type="video/mp4">
        介紹影片
      </video>
    </div>

    <div class="courses">
      <h2>課程展示</h2>

      <div class="class">
        <div class="class-item">
          <router-link to="/beginner"><img src="../images/c-bignner.jpg" alt="初階班" class="class-img">
            <p><button class="c-button">初階班</button></p>
          </router-link>
        </div>
        <div class="coach-item">
          <router-link to="/competitive"><img src="../images/c-competitive.jpg" alt="競技班" class="class-img">
            <p><button class="c-button">競技班</button></p>
          </router-link>
        </div>
      </div>

      <div class="coach">
        <div class="coach-item">
          <router-link to="/onetoone"><img src="../images/c-onetoone.jpg" alt="個別班" class="class-img" />
            <p><button class="c-button">個別班</button></p>
          </router-link>
        </div>
        <div class="coach-item">
          <router-link to="/zerodozen"><img src="../images/c-zerodozen.jpg" alt="零打班" class="class-img" />
            <p><button class="c-button">零打班</button> </p>
          </router-link>
        </div>
      </div>
    </div>



    <div id="about">
      <h2>教練團隊</h2>
      <div class="coach">
        <div class="coach-item">
          <router-link to="/cyz"><img src="../images/co-chaiyuanzheng.jpg" alt="蔡元振" class="coach-img">
            <p><button class="co-button">蔡元振</button></p>
          </router-link>
        </div>
        <div class="coach-item">
          <router-link to="/zzt"><img src="../images/co-zhozhongting.jpg" alt="周仲庭" class="coach-img">
            <p><button class="co-button">周仲庭</button></p>
          </router-link>
        </div>
      </div>

      <div class="coach">
        <div class="coach-item">
          <router-link to="/zby"><img src="../images/co-zhangbingying.jpg" alt="張秉洋" class="coach-img" />
            <p><button class="co-button">張秉洋</button></p>
          </router-link>
        </div>
        <div class="coach-item">
          <router-link to="/hwh"><img src="../images/co-huwenhan.jpg" alt="胡玟翰" class="coach-img" />
            <p><button class="co-button">胡玟翰</button></p>
          </router-link>
        </div>
      </div>
    </div>


    <div class="teach">
      <h2>羽球教學</h2>
      <div class="video-container">
        <video controls ref="videoPlayer">
          <source src="https://youtu.be/evJazpDJ7eQ?si=w12dIbthP8K6ubn9" type="video/mp4">
          介紹影片
        </video>
      </div>
    </div>
    殺球<br>
    左右平球<br>
    挑球小球<br>

    <div class="QA">
      <h2>羽球Q&A</h2>
      <h3><b>打羽球好處:</b></h3>
      <b>1.促進血液循環，提升新陳代謝</b><br>
      透過大量流汗、體溫升高，血流速度將會加速，長期持續運動也能消耗血糖與肝醣、鍛鍊肌肉，讓您更不易肥胖與出現三高的症狀。<br>
      <b>2.長高</b><br>
      運動中有許多的伸展與跳躍動作，有助於發育中孩童拉長身高，而對於已脫離發育期的大人，也能防止肌肉退化與鍛鍊下盤的效果。<br>
      <b>3.鍛鍊眼球肌肉</b><br>
      廣義上來說，所有球類運動都有類似的效果，只是羽球因為質量輕盈、體積小巧，因此目光在追蹤羽球時需耗費更多的注意力，間接起到鍛鍊眼部肌肉的效果。<br>
      <b>4.運動使你快樂</b><br>
      整天坐在辦公室裡，屁股都要坐開花了嗎？還是你是站在服務的第一線，面對客人的無理要求還要笑臉迎人呢？快來打羽毛球吧，每一次的揮拍都是一次的釋放，讓你日常累積的壓力bye~bye~。<br>
      <h3><b>打羽球常見的運動傷害:</b></h3>
      羽球屬於較激烈的球類運動，初學者不明就裡的亂打，可能對身體造成損傷，這些傷害雖不致命，卻因不易發現而持續累積，逐漸變成嚴重的運動傷害。為您整理以下幾種常見傷害，若有類似狀況，請儘速尋求教練或醫師協助。<br>
      <b>1.手部、腕部關節拉傷</b><br>
      揮拍是羽球重要動作，若肌肉強度不夠，急速揮拍容易對關節造成傷害。<br>
      <b>2.腰部肌肉拉傷</b><br>
      扭腰是運動常見的發力動作，羽球每次的發球、折返跑、殺球都需腰部肌肉的配合，因此若肌肉強度不夠或未掌握發力技巧，容易造成腰部肌肉受傷。<br>
      <b>3.椎間盤突出</b><br>
      常見症狀為放射狀的方式在臀部以下之處引起不適，或也可能出現上肢無力。椎間盤突出是相當嚴重的運動傷害，長期不處理可能會進一步引發神經病變與肌肉萎縮等。建議若有類似情況應立即尋求專業醫生協助。<br>
      <b>4.膝關節、韌帶、阿基里斯腱、腳踝傷害</b><br>
      羽球相當要求下盤肌肉的帶動，舉凡折返跑、急煞、跳躍發球或殺球，無一不是對下盤肌肉的殘酷試煉，因此，這些運動傷害在初學者中很常見。 <br>
    </div>

    <div class="communication">
      <h2>聯絡我們</h2>
      <img src="../images/lineicon.png" alt="Line" class="line-img">
      <p>透過行動條碼加入LINE好友<br>請在LINE應用程式上開啟「好友」分頁，點選畫面右上方用來加入好友的圖示，接著點選「行動條碼」，然後掃描此行動條碼。</p>
      <img src="../images/mailicon.png" alt="Mail" class="mail-img">
      <p>badminton@gmail.com</p>
      <img src="../images/TELicon.png" alt="TEL" class="tel-img">
      <p>0939779171</p>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.resizeVideo(); // 初始化调整视频大小
    window.addEventListener('resize', this.resizeVideo);
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.resizeVideo);
  },
  methods: {
    resizeVideo() {
      const videoPlayer = this.$refs.videoPlayer;
      const aspectRatio = videoPlayer.videoWidth / videoPlayer.videoHeight;
      const containerWidth = videoPlayer.parentElement.offsetWidth;
      videoPlayer.width = containerWidth;
      videoPlayer.height = containerWidth / aspectRatio;
    }
  }
};
</script>


<style scoped>
@media screen and (max-width: 320px) {

  /* iPhone SE 的寬度 */
  /* 適應較小屏幕的調整 */
  .g-header-container.fixed {
    padding: 5px;
    /* 減少填充 */
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

.main {
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

.video-container {
  margin-bottom: 20px;
  padding: 30px 0px 10px 0px;
  /* 內邊距 */
}

.video-teach {
  margin-bottom: 20px;
  padding: 10px 0px 10px 0px;
  /* 內邊距 */
}

.video {
  margin-bottom: 20px;
}

video {
  width: 100%;
  /* 設定視頻寬度 */
  height: auto;
  /* 高度自動縮訪 */
}

.coach {
  display: flex;
  /*flexbox布局*/
}

.coach-item {
  margin-right: 20px;
  /* 間距 */
  text-align: center;
  /* 文字置中 */
}

.coach-img {
  width: 200px;
  /*圖片寬度*/
  height: auto;
  /*圖片縮放*/
  border-radius: 10px;
  /*圓角 */
}

.coach-item p {
  margin-top: 15px;
  /* 調整文字與圖片間距 */
}

.class {
  display: flex;
  /*flexbox布局*/
}

.class-item {
  margin-right: 20px;
  /* 間距 */
  text-align: center;
  /* 文字置中 */
}

.class-img {
  width: 200px;
  /*圖片寬度*/
  height: auto;
  /*圖片縮放*/
  border-radius: 10px;
  /*圓角 */
}

.line-img {
  width: 50px;
  /*圖片寬度*/
  height: 50px;
  /*圖片縮放*/
  border-radius: 10px;
  /*圓角 */
}

.mail-img {
  width: 50px;
  /*圖片寬度*/
  height: 50px;
  /*圖片縮放*/
  border-radius: 10px;
  /*圓角 */
}

.tel-img {
  width: 50x;
  /*圖片寬度*/
  height: 80px;
  /*圖片縮放*/
  border-radius: 10px;
  /*圓角 */
}

.class-item p {
  margin-top: 10px;
  /* 調整文字與圖片間距 */
}

.c-button {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #c2cae7;
}

.c-button:hover {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #93a9d8;
}

.co-button {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #c2cae7;
}

.co-button:hover {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #93a9d8;
}
</style>
