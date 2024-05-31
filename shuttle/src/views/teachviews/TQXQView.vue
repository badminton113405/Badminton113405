<template>
  <div class="TQXQ">
    <h2>羽球教學</h2>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class="video">
      <div class="video-teach">
        <div class="video-container">
          <iframe
          :src="videoUrl"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          ref="videoPlayer"
          ></iframe>
        </div>
      </div>
    </div>
    <h1>挑球/小球</h1>
    <p>挑球是在前場由下往上擊球，並把球擊高至後場的球路，小球則是在前場約在自身肩膀的高度擊球，並打至對方前場的位置。</p>
    <div class="button-container">
      <router-link to="/pq"><button class="i-button">左右/正反平球</button></router-link>
      <router-link to="/sq"><button class="i-button">殺球</button></router-link>
      <router-link to="/"><button class="i-button">回首頁</button></router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      videoUrl: 'https://youtu.be/H0DOUQEFX_A?si=tddJSDCbLJBtwArl'
    };
  }
};
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

  .i-button {
    margin-right: 5px;
    /* 减少边距 */
    font-size: 12px;
    /* 减少字体大小 */
  }
}

.TQXQ {
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
  width: 80%;
  max-width: 800px;
  aspect-ratio: 16 / 9;
}

iframe {
  width: 100%;
  height: 100%;
  border-radius: 10pt;
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

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 10px;
  /* Add space between video container and buttons */
}

.i-button {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #AFCCDC;
  margin: 0 5px;
  /* Add space between buttons */

}

.i-button:hover {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #AFCCDC;
  background-color: #000;
}
</style>
