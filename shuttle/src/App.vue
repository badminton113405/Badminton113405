<template>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <div class="g-header-container" :class="{ 'fixed': isFixed }" ref="headerContainer">
    <router-link to="/"><img src="./images/Logoicon.png" alt="badminton" class="icon" /></router-link>
    <router-link to="/"><button class="m-button">關於我們</button></router-link>
    <!--<router-link to="/about"><button class="m-button">教練團隊</button></router-link>-->
    <router-link to="/reservation"><button class="m-button">報名課程</button></router-link>
    <router-link to="/community"><button class="m-button">社群空間</button></router-link>
    <router-link to="/login"><button class="m-button">會員中心</button></router-link>

    <c-header />
  </div>

  <div class="g-content" :style="{ paddingTop: headerHeight + 'px', paddingBottom: footerHeight + 'px' }">
    <router-view @content-height-updated="updateContentHeight" />
  </div>

  <div class="g-footer-container" ref="footerContainer">
    地點:羽你同行羽球館 電話:0939779171<br>
    羽你動滋動 Webside © 2024
    <c-footer />
  </div>
</template>

<script>
export default {
  data() {
    return {
      isFixed: false,
      headerHeight: 0,
      footerHeight: 0,
      contentHeight: 0
    }
  },
  methods: {
    updateHeights() {
      this.headerHeight = this.$refs.headerContainer.clientHeight;
      this.footerHeight = this.$refs.footerContainer.clientHeight;
      this.handleScroll(); // 在更新高度后重新检查滚动位置
    },
    handleScroll() {
      let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
      let scrollOneOffsetTop = this.$refs.scrollOne ? this.$refs.scrollOne.offsetTop : 0;
      this.isFixed = scrollTop > scrollOneOffsetTop || scrollTop === 0 ? true : false;
    },
    handleResize() {
      this.updateHeights(); // 在窗口大小调整时更新高度
    }
  },
  mounted() {
    this.updateHeights(); // 初始化时获取高度
    window.addEventListener("scroll", this.handleScroll);
    window.addEventListener("resize", this.handleResize);
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.handleScroll);
    window.removeEventListener("resize", this.handleResize);
  },
  computed: {
    totalHeight() {
      return this.headerHeight + this.contentHeight + this.footerHeight;
    }
  }
};
</script>

<style>
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

body {
  font-family: "Zen Kurenaido", sans-serif;
  background-color: #FCFFE9;
  color: #000;
  margin: 0;
  padding: 0;
}

.icon {
  width: 100px;
  height: auto;
  margin-right: 10px;
}

.g-header-container.fixed {
  background-color: #AFCCDC;
  display: flex;
  align-items: center;
  font-family: "Zen Kurenaido", sans-serif;
  position: fixed;
  padding: 10px;
  left: 0;
  top: 0;
  width: 100%;
  z-index: 999;
}

.g-content {
  padding-top: 60px;
  /* Adjust according to the header height */
  padding-bottom: 60px;
  /* Adjust according to the footer height */
}

.g-footer-container {
  font-family: "Zen Kurenaido", sans-serif;
  background-color: #AFCCDC;
  font-size: 10px;
  text-align: center;
  width: 100%;
  padding: 10px;
  position: fixed;
  left: 0;
  bottom: 0;
  z-index: 999;
}

.m-button {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #ffecd5;
  margin-right: 10px;
}

.m-button:hover {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #fde0a6;
}
</style>
