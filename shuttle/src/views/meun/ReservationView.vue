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
import axios from 'axios';

export default {
  methods: {
  submitReservation() {
    const reservationData = {
      memberId: this.memberId,
      courseId: this.courseId,
      reservationDate: this.reservationDate
    };
    
    axios.post('http://127.0.0.1:8000/test', reservationData)
      .then(response => {
        if (response.data.success) {
          alert('Reservation successful!');
        } else {
          alert('Reservation failed: ' + response.data.message);
        }
      })
      .catch(error => {
        alert('Reservation failed: ' + error.message);
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
