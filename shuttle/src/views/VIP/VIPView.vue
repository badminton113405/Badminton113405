<template>
  <div class="VIP">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class="container">
      <div class="title">會員中心</div>
      <div class="button-group">
        <button class="b-button">編輯個人資料</button>
        <router-link to="/login"><button class="l-button">登出</button></router-link>
      </div>
      <div class="profile-info">
        <div>
          <label>姓名:</label>
          <span>{{ user.full_name }}</span>
        </div>
        <div>
          <label>稱謂:</label>
          <span>{{ user.gender }}</span>
        </div>
        <div>
          <label>暱稱:</label>
          <span>{{ user.nickname }}</span>
        </div>
        <div>
          <label>出生年月日:</label>
          <span>{{ user.birth_date }}</span>
        </div>
        <div>
          <label>聯絡電話:</label>
          <span>{{ user.phone }}</span>
        </div>
        <div>
          <label>Email:</label>
          <span>{{ user.email }}</span>
        </div>
        <div>
          <label>密碼:</label>
          <span>XXXXXXXX</span>
        </div>
      </div>
      <div class="course-records">
        <div>課程紀錄:</div>
        <!-- Display the user's course records here -->
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {
        full_name: '',
        gender: '',
        nickname: '',
        birth_date: '',
        phone: '',
        email: ''
      }
    };
  },
  created() {
    this.fetchUserData();
  },
  methods: {
    async fetchUserData() {
      try {
        const token = localStorage.getItem('token'); 
        if (!token) {
            alert('No token found, please log in.');
          return;
        }
        const response = await axios.get('http://127.0.0.1:8000/api/profile/', {
          headers: {
            Authorization: `Token ${token}`
          }
        });
        this.user = response.data;
      } catch (error) {
        console.error('Failed to fetch user data:', error);
        if (error.response && error.response.status === 401) {
          alert('Unauthorized. Please log in again.');
          this.$router.push('/login');
        }
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

.VIP {
  font-family: "Zen Kurenaido", sans-serif;
  margin-top: 30px;
  margin-left: 10px;
  margin-right: 10px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  background-color: #fff;
}

.container {
  max-width: 600px;
  width: 100%;
  margin: 50px auto;
  padding: 20px;
  border-radius: 10px;
  background-color: #ffecd5;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
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
  display: inline-block;
  width: 100px;
  font-weight: bold;
}

.profile-info span {
  display: inline-block;
  word-wrap: break-word;
}

.button-group {
  text-align: right;
  margin-bottom: 20px;
}

.b-button, .l-button {
  font-family: "Zen Kurenaido", sans-serif;
  border-radius: 16px;
  color: #000;
  background-color: #ffecd5;
  margin-right: 15px;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}

.b-button:hover, .l-button:hover {
  background-color: #fde0a6;
}
</style>
