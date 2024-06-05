<template>
  <div class="Login">
    <div class="container">
      <div class="title">會員中心</div>
      <div class="description">
        加入會員有什麼好處呢？只要加入我們就能共享豐富的折扣優惠！還能夠與我們其他的會員朋友們一起線上分享經驗、討論技巧，甚至組織羽球活動，進一步增強羽球愛好者之間的社群連結。
      </div>
      <div class="input-group">
        <label for="username">帳號</label>
        <input v-model="username" type="text" id="username" placeholder="請輸入帳號">
      </div>
      <div class="input-group">
        <label for="password">密碼</label>
        <input v-model="password" type="password" id="password" placeholder="請輸入密碼">
      </div>
      <div class="button-group">
        <router-link to="/register">
          <button class="success">註冊會員</button>
        </router-link>
        <button class="confirm" @click="login">登入</button>
      </div>
      <div class="forgot-password">
        <router-link to="/forget">忘記密碼？</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    /*
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/login/', {
          username: this.username,
          password: this.password
        });
        console.log('Login successful:', response.data);
        alert('登入成功');
        this.$router.push('/vip');
      } catch (error) {
        console.error('Login failed:', error.response?.data || error.message);
        const message = error.response?.data?.detail || error.message;
        alert('登入失敗: ' + message);
      }
    }
    */
    

    async login() {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/login/', {
        username: this.username,
        password: this.password
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      console.log('Login successful:', response.data);  
      this.$router.push('/vip');
    } catch (error) {
      console.error('Login failed:', error.response?.data || error.message);
      const message = error.response?.data?.detail || error.message;
      alert('登入失敗: ' + message);
    }
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

.Login {
  font-family: "Zen Kurenaido", sans-serif;
  margin-top: 30px;
  margin-left: 10px;
  margin-right: 10px;
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.container {
  margin-top: 50px;
}

.title {
  font-weight: bold;
  font-size: 24px;
  margin-bottom: 20px;
}

.description {
  font-size: 16px;
  margin-bottom: 30px;
  line-height: 1.6;
}

.input-group {
  margin-bottom: 15px;
}

.input-group label {
  display: block;
  margin-bottom: 5px;
}

.input-group input {
  width: 80%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin: 0 auto;
}

.button-group {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.button-group button {
  font-family: "Zen Kurenaido", sans-serif;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  margin: 5px;
  border-radius: 16px;
  color: #000;
  background-color: #ffecd5;
}

.button-group button:hover {
  background-color: #fde0a6;
}

.primary {
  background-color: #ffecd5;
}

.button-group .success {
  background-color: #a8e6cf;
}

.button-group .confirm {
  background-color: #ffecd5;
}

.forgot-password {
  margin-top: 10px;
  text-align: center;
}

.forgot-password a {
  color: #007bff;
  text-decoration: none;
}

.forgot-password a:hover {
  text-decoration: underline;
}
</style>
