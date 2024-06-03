<template>
  <div class="VIP">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <body>
    <div class="container">
        <div class="title">會員中心</div>
        <div class="button">
            <button class="b-button">編輯個人資料</button>
            <router-link to="/login"><button class="l-button">登出</button></router-link>
        </div>
        <div class="profile-info">
          <div>
                <label for="name">姓名:</label>
                <input type="text" id="name" name="name">
            </div>
            <div>
                <label for="title">稱謂:</label>
                <input type="text" id="title" name="title">
            </div>
            <div>
                <label for="nickname">暱稱:</label>
                <input type="text" id="nickname" name="nickname">
            </div>
            <div>
                <label for="dob">出生年月日:</label>
                <input type="date" id="dob" name="dob">
            </div>
            <div>
                <label for="phone">聯絡電話:</label>
                <input type="text" id="phone" name="phone">
            </div>
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email">
            </div>
            <div>
                <label for="password">密碼:</label>
                <input type="password" id="password" name="password">
            </div>
        </div>
        <div class="course-records">
            <div>課程紀錄:</div>
        </div>
    </div>
</body>
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

.VIP {
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

.container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  border-radius: 10px;
}

.title {
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
}

.profile-info, .course-records {
  text-align: left;
  margin-bottom: 20px;
}

.profile-info div, .course-records div {
  margin-bottom: 10px; 
}

.profile-info label {
  display: block;
  margin-bottom: 5px;
}

.profile-info input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.button {
  text-align: right;
}

.b-button {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #ffecd5;
  margin-right: 15px;
}

.b-button:hover {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #fde0a6;
}

.l-button {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #ffecd5;
  margin-right: 15px;
}

.l-button:hover {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #fde0a6;
}
</style>
