<template>
    <div class="password">
        <div class="reset-container">
            <div class="title">重設密碼</div>
            <form @submit.prevent="submitPassword">
                <div class="input-group">
                    <label for="password">新密碼</label>
                    <input v-model="password" type="password" id="password" placeholder="請輸入新密碼" required minlength="8">
                </div>
                <div class="input-group">
                    <label for="confirmPassword">確認新密碼</label>
                    <input v-model="confirmPassword" type="password" id="confirmPassword" placeholder="請再次輸入新密碼"
                        required minlength="8">
                </div>
                <button class="submit-button" type="submit">重設密碼</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            password: '',
            confirmPassword: ''
        };
    },
    methods: {
        submitPassword() {
            if (this.password !== this.confirmPassword) {
                alert('密碼不一致');
                return;
            }

            axios.post('http://127.0.0.1:8000/api/reset-password/', { password: this.password })
                .then(() => {
                    alert('密碼重設成功');
                    this.$router.push({ name: 'Login' });
                })
                .catch(() => {
                    alert('密碼重設失敗，請稍後再試');
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

.password {
    font-family: "Zen Kurenaido", sans-serif;
    margin-top: 30px;
    margin-left: 10px;
    margin-right: 10px;
    display: flex;
    justify-content: center;
    flex-direction: column;
}

.reset-container {
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
