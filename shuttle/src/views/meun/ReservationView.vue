<template>
  <div>
    <h1>Reservation</h1>
    <form @submit.prevent="submitReservation">
      <label for="memberId">Member ID:</label>
      <input type="text" v-model="memberId" id="memberId" required />
      
      <label for="courseId">Course ID:</label>
      <input type="text" v-model="courseId" id="courseId" required />
      
      <label for="reservationDate">Reservation Date:</label>
      <input type="date" v-model="reservationDate" id="reservationDate" required />
      
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
      courseId: '',
      reservationDate: '',
      socket: null
    };
  },
  mounted() {
    this.socket = io('http://your_django_server/ws/reservation/');
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
    submitReservation() {
      this.socket.emit('message', {
        member_id: this.memberId,
        course_id: this.courseId,
        reservation_date: this.reservationDate
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
