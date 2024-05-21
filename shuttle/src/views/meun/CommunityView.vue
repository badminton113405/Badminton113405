<template>
  <div>
    <h1>Community</h1>
    <form @submit.prevent="submitMessage">
      <label for="memberId">Member ID:</label>
      <input type="text" v-model="memberId" id="memberId" required />
      
      <label for="content">Message:</label>
      <textarea v-model="content" id="content" required></textarea>
      
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import { io } from 'socket.io-client';

export default {
  data() {
    return {
      memberId: '',
      content: '',
      socket: null
    };
  },
  mounted() {
    this.socket = io('http://127.0.0.1:8000//ws/community/');
    this.socket.on('connect', () => {
      console.log('Socket connected');
    });
    this.socket.on('message', data => {
      console.log('Message received:', data);
      if (data.error) {
        alert(`Error: ${data.error}`);
      } else {
        alert(`Success: ${data.message}`);
      }
    });
  },
  beforeUnmount() {
    if (this.socket) {
      this.socket.disconnect();
    }
  },
  methods: {
    submitMessage() {
      this.socket.emit('message', {
        member_id: this.memberId,
        content: this.content
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

.reservation {
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
</style>

