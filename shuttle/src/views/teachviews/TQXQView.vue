<template>
  <div class="TQXQ">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class="video-container">
      <video controls ref="videoPlayer">
        <source src="https://youtu.be/evJazpDJ7eQ?si=w12dIbthP8K6ubn9" type="video/mp4">
        橫移
      </video>
    </div>
    <div class="button-container">
      <router-link to="/pq"><button class="i-button">左右/正反平球</button></router-link>
      <router-link to="/sq"><button class="i-button">殺球</button></router-link>
      <router-link to="/"><button class="i-button">回首頁</button></router-link>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    this.resizeVideo(); // 初始化调整视频大小
    window.addEventListener('resize', this.resizeVideo);
  },
  methods: {
    resizeVideo() {
      // 添加 resizeVideo 函数的实际功能代码，用来调整视频大小
    }
  }
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
