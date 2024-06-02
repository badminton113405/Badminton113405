<template>
  <div class="container">
    <div class="title">會員註冊</div>
    <form @submit.prevent="submitForm">
      <div class="input-group">
        <label for="name">姓名 *</label>
        <input v-model="form.name" type="text" id="name" required>
      </div>

      <div class="input-group">
        <label for="username">設置帳號 *</label>
        <input v-model="form.username" type="text" id="username" required minlength="8">
      </div>
      <div class="input-group">
        <label for="password">設置密碼 *</label>
        <input v-model="form.password" type="password" id="password" required minlength="8">
      </div>
      <div class="input-group">
        <label for="confirmPassword">確認密碼 *</label>
        <input v-model="form.confirmPassword" type="password" id="confirmPassword" required minlength="8">
      </div>
      <div class="button-group">
        <button type="button" class="cancel" @click="resetForm">取消</button>
        <button type="submit" class="confirm">確認</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        name: '',
        gender: '',
        year: '',
        month: '',
        day: '',
        occupation: '',
        phone: '',
        email: '',
        username: '',
        password: '',
        confirmPassword: ''
      }
    };
  },
  methods: {
    submitForm() {
      alert("test");
      if (this.form.password !== this.form.confirmPassword) {
        alert('密碼不一致');
        return;
      }
      axios.post('http://127.0.0.1:8000/api/register/', {
        username: this.form.username,
        password: this.form.password,
        email: this.form.email
      })
        .then(response => {
          alert(response.data.message);
        })
        .catch(error => {
          alert(error.response.data.message);
        });
    },
    resetForm() {
      this.$router.push({ name: 'Login' }).catch(err => {
        if (err.name !== 'NavigationDuplicated') {
          console.error(err);
        }
      });
    }

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

  .m-button {
    margin-right: 5px;
    /* 减少边距 */
    font-size: 12px;
    /* 减少字体大小 */
  }
}

.Register {
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
  text-align: center;
  background-color: #f9f9f9;
}

.container {
  margin: 50px auto;
  width: 90%;
  max-width: 400px;
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 24px;
  margin-bottom: 20px;
}

.input-group {
  margin-bottom: 15px;
  text-align: left;
}

.input-group label {
  display: block;
  margin-bottom: 5px;
}

.input-group input,
.input-group select {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.dob-container {
  display: flex;
  justify-content: space-between;
}

.dob {
  width: 30%;
}

.button-group {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.button-group button {
  width: 48%;
  padding: 10px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.cancel {
  background-color: #ccc;
}

.confirm {
  background-color: #ffda44;
}
</style>
