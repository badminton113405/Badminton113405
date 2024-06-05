<template>
  <div class="forget-container">
    <div class="title">忘記密碼</div>
    <form @submit.prevent="submitEmail">
      <div class="input-group">
        <label for="email">Email</label>
        <input v-model="email" type="email" id="email" placeholder="請輸入您的Email" required>
      </div>
      <div class="description">
        請輸入註冊時填寫的Email，用於驗證帳號。
      </div>
      <button class="submit-button" type="submit">設定密碼</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: ''
    };
  },
  methods: {
    submitEmail() {
      axios.post(' https://2228-60-250-79-113.ngrok-free.app/api/forgot-password/', { email: this.email })
        .then(() => {
          alert('驗證成功');
          this.$router.push({ name: 'ResetPassword' });
        })
        .catch(() => {
          alert('驗證失敗，請檢查您的Email');
        });
    }
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

  .m-button {
    margin-right: 5px;
    font-size: 12px;
  }
}

.VIP {
  font-family: "Zen Kurenaido", sans-serif;
  margin-top: 30px;
  margin-left: 10px;
  margin-right: 10px;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.forget-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.title {
  font-size: 24px;
  margin-bottom: 20px;
  font-family: "Zen Kurenaido", sans-serif;
}

.input-group {
  margin-bottom: 15px;
  text-align: left;
}

.input-group label {
  display: block;
  margin-bottom: 5px;
}

.input-group input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.description {
  font-size: 16px;
  margin-bottom: 20px;
}

.submit-button {
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background-color: #a8e6cf;
  font-family: "Zen Kurenaido", sans-serif;
}

.submit-button:hover {
  background-color: #81c784;
}
</style>
