<template>
  <div class="HY">
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
    <h1>左右/正反平球</h1>
    <p>左右/正反 平球是羽球當中最常出現的球路之一，擊球後球會以跟球網差不多的高度飛過。</p>
    <div class="button-container">
      <router-link to="/sq"><button class="i-button">殺球</button></router-link>
      <router-link to="/tqxq"><button class="i-button">小球/挑球</button></router-link>
      <router-link to="/"><button class="i-button">回首頁</button></router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      videoUrl: 'https://www.youtube.com/embed/ppYeUspjgVY'
    };
  }
};
</script>

<style scoped>
@media screen and (max-width: 320px) {
  .g-header-container.fixed {
    padding: 5px;
  }
  .g-footer-container {
    padding: 5px;
  }
  .i-button {
    margin-right: 5px;
    font-size: 12px;
  }
}

.HY {
  font-family: "Zen Kurenaido", sans-serif;
  margin-top: 30px;
  margin-left: 10px;
  margin-right: 10px;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.video-container {
  width: 100%;
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
  padding: 10px 0;
}

.video {
  margin-bottom: 20px;
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.i-button {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #c2cae7;
  margin: 0 5px;
}

.i-button:hover {
  color: #AFCCDC;
  background-color: #93a9d8;
}
</style>
