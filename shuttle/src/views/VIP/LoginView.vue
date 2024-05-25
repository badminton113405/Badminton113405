<template>
    <div class="Login">
        <div class="container">
            <div class="title">會員中心</div>
            <div class="description">
                加入會員有什麼好處呢？只要加入我們就能共享豐富的折扣優惠！還能夠與我們其他的會員朋友們一起線上分享經驗、討論技巧，甚至組織羽球活動，進一步增強羽球愛好者之間的社群連結。
            </div>
            <button class="primary" @click="login">會員登入</button>
            <div class="input-group">
                <label for="username">帳號</label>
                <input v-model="username" type="text" id="username" placeholder="請輸入帳號">
            </div>
            <div class="input-group">
                <label for="password">密碼</label>
                <input v-model="password" type="password" id="password" placeholder="請輸入密碼">
            </div>
            <div class="button-group">
                <button class="danger" @click="forgotPassword">忘記密碼</button>
                <router-link to="/register"><button class="success">註冊會員</button></router-link>
                <button class="confirm" @click="login">確認</button>
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
        login() {
            axios.post('/api/login/', {
                email: this.username,
                password: this.password
            })
            .then(response => {
                alert(response.data.message);
            })
            .catch(error => {
                alert(error.response.data.message);
            });
        },
        forgotPassword() {
            alert('忘記密碼');
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

.Login {
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
    margin-top: 50px;
}

.title {
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
    margin-right: 10px;
}
.button-group button:hover {
    font-family: "Zen Kurenaido", sans-serif;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    margin: 5px;
    border-radius: 16px;
    color: #000;
    background-color: #fde0a6;
    margin-right: 10px;
}


.primary {
    font-family: "Zen Kurenaido", sans-serif;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
    margin: 5px;
    border-radius: 16px;
    color: #000;
    background-color: #ffecd5;
    margin-right: 10px;
}

.button-group .success {
    background-color: #a8e6cf;
}

.button-group .confirm {
    background-color: #ffecd5;
}

</style>
