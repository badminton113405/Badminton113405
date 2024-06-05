<template>
  <div class="container">
    <div class="title">會員註冊</div>
    <form @submit.prevent="submitForm">
      <div class="input-group">
        <label for="name">姓名 *</label>
        <input v-model="form.full_name" type="text" id="name" required>
      </div>
      <div class="input-group">
        <label for="nickname">暱稱 *</label>
        <input v-model="form.nickname" type="text" id="nickname" required>
      </div>
      <div class="input-group">
        <label for="gender">性別 *</label>
        <select v-model="form.gender" id="gender" required>
          <option value="" disabled>請選擇</option>
          <option value="male">男</option>
          <option value="female">女</option>
          <option value="other">其他</option>
        </select>
      </div>
      <div class="input-group">
        <label for="dob">生日 *</label>
        <div class="dob-container">
          <select v-model="form.year" id="year" required class="dob">
            <option value="" disabled>年</option>
            <option v-for="year in years" :key="year" :value="year">{{ year }}</option>
          </select>
          <select v-model="form.month" id="month" required class="dob">
            <option value="" disabled>月</option>
            <option v-for="month in months" :key="month" :value="month">{{ month }}</option>
          </select>
          <select v-model="form.day" id="day" required class="dob">
            <option value="" disabled>日</option>
            <option v-for="day in days" :key="day" :value="day">{{ day }}</option>
          </select>
        </div>
      </div>
      <div class="input-group">
        <label for="occupation">職業 *</label>
        <input v-model="form.occupation" type="text" id="occupation" required>
      </div>
      <div class="input-group">
        <label for="phone">電話 *</label>
        <input v-model="form.phone" type="text" id="phone" required>
      </div>
      <div class="input-group">
        <label for="email">電子郵件 *</label>
        <input v-model="form.email" type="email" id="email" required>
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
        full_name: '',
        nickname: '',
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
      },
      months: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    };
  },
  computed: {
    currentYear() {
      return new Date().getFullYear();
    },
    years() {
      const startYear = 1850;
      const endYear = this.currentYear;
      const years = [];
      for (let year = startYear; year <= endYear; year++) {
        years.push(year);
      }
      return years;
    },
    days() {
      const year = this.form.year;
      const month = this.form.month;
      if (!year || !month) {
        return [];
      }
      const daysInMonth = new Date(year, month, 0).getDate();
      return Array.from({ length: daysInMonth }, (_, i) => i + 1);
    }
  },
  methods: {
    async submitForm() {
      if (this.form.password !== this.form.confirmPassword) {
        alert('密碼不一致');
        return;
      }

      try {
        await axios.post(' https://2228-60-250-79-113.ngrok-free.app/api/register/', {
          username: this.form.username,
          password: this.form.password,
          full_name: this.form.full_name,
          nickname: this.form.nickname,
          gender: this.form.gender,
          birth_date: `${this.form.year}-${this.form.month}-${this.form.day}`,
          occupation: this.form.occupation,
          phone: this.form.phone,
          email: this.form.email
        });

        alert('註冊成功');
        this.$router.push('/login');
        } catch (error) {
          print(error)
          if (error.response && error.response.data) {
            alert('註冊失敗：' + (error.response.data.detail || JSON.stringify(error.response.data)));
          } else {
            alert('註冊失敗：' + error.message);
          }
      }
    },

    resetForm() {
      this.$router.push('/login');
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

.Register {
  font-family: "Zen Kurenaido", sans-serif;
  margin-top: 30px;
  margin-left: 10px;
  margin-right: 10px;
  display: flex;
  justify-content: center;
  flex-direction: column;
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
  padding: 10px 0px 10px 0px;
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
