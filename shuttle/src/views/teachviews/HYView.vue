<template>
  <div class="hy">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class="video-container">
      <video controls ref="videoPlayer">
        <!--<source src="../../images/t-hy.mp4" type="video/mp4"> -->
        橫移
      </video>
    </div>
  </div>
</template>
  
  <script>
  export default {
    mounted() {
    this.resizeVideo(); // 初始化调整视频大小
    window.addEventListener('resize', this.resizeVideo);
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
  
    .m-button {
      margin-right: 5px;
      /* 减少边距 */
      font-size: 12px;
      /* 减少字体大小 */
    }
  }
  
  .hy {
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
  </style>
  