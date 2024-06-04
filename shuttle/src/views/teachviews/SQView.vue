<template>
  <div class="SQ">
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
    <h1>殺球</h1>
    <p>殺球是羽球最具攻擊性的球路，透過手腕下扣瞬間發力並在高點擊到球，使球過往後有一定的威力並下墜。</p>
    <div class="button-container">
      <router-link to="/pq"><button class="i-button">左右/正反平球</button></router-link>
      <router-link to="/tqxq"><button class="i-button">小球/挑球</button></router-link>
      <router-link to="/"><button class="i-button">回首頁</button></router-link>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      videoUrl: 'https://youtu.be/NzJzkENB7GE?si=j3jLLp7iAJxiX7E7'
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

.SQ {
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
