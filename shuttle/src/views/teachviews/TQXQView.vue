<template>
  <div class="TQXQ">
    <h2>羽球教學</h2>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class="video">
      <div class="video-teach">
        <div class="video-container">
          <iframe :src="videoUrl" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen ref="videoPlayer"></iframe>
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

.TQXQ {
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
  padding: 10px 0px 10px 0px;

}

.video {
  margin-bottom: 20px;
}

video {
  width: 100%;

  height: auto;

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
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #AFCCDC;
  background-color: #93a9d8;
}
</style>
