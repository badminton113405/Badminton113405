<template>
  <div class="registration-form">
    <h1>報名課程</h1>
    <form @submit.prevent="submitForm">
      <!-- 填寫報名資料區 -->
      <section>
        <h2>填寫報名資料</h2>
        <div>
          <label>姓名</label>
          <input type="text" v-model="formData.name" required>
        </div>
        <div>
          <label>性別</label>
          <select v-model="formData.gender" required>
            <option value="" disabled>-- 請選擇 --</option>
            <option value="male">男</option>
            <option value="female">女</option>
            <option value="other">其他</option>
          </select>
        </div>
        <div>
          <label>聯絡電話</label>
          <input type="text" v-model="formData.phone" required>
        </div>
        <div>
          <label>Email</label>
          <input type="email" v-model="formData.email" required>
        </div>
      </section>

      <!-- 不會踢跆拳道的級段 -->
      <section>
        <h2>您有學習過羽球的經驗嗎?</h2>
        <input type="number" v-model="formData.grade" min="1" max="18" required>
      </section>

      <!-- 學習跆拳道的動機與目標 -->
      <section>
        <h2>您學習羽球的動機與目標</h2>
        <div>
          <label><input type="checkbox" v-model="formData.motivation" value="興趣與趣"> 興趣與趣</label>
          <label><input type="checkbox" v-model="formData.motivation" value="運動健身"> 運動健身</label>
          <label><input type="checkbox" v-model="formData.motivation" value="提升技巧"> 提升技巧</label>
          <label><input type="checkbox" v-model="formData.motivation" value="參加比賽"> 參加比賽</label>
        </div>
      </section>

      <!-- 選擇的技術 -->
      <section>
        <h2>您選擇的技術</h2>
        <div>
          <label><input type="checkbox" v-model="formData.techniques" value="發球與接發球"> 發球與接發球</label>
          <label><input type="checkbox" v-model="formData.techniques" value="雙打後場組織進攻"> 雙打後場組織進攻</label>
          <label><input type="checkbox" v-model="formData.techniques" value="單打四角拉吊"> 單打四角拉吊</label>
          <label><input type="checkbox" v-model="formData.techniques" value="其他"> 其他</label>
        </div>
      </section>

      <!-- 指定教練的性別 -->
      <section>
        <h2>需要指定教練的性別嗎?</h2>
        <div>
          <label><input type="radio" v-model="formData.coachGender" value="male"> 男生</label>
          <label><input type="radio" v-model="formData.coachGender" value="female"> 女生</label>
          <label><input type="radio" v-model="formData.coachGender" value="not-specified"> 不指定</label>
        </div>
      </section>

      <!-- 理想的教練特質 -->
      <section>
        <h2>理想的教練特質</h2>
        <div>
          <label><input type="checkbox" v-model="formData.coachTraits" value="有經驗"> 有經驗</label>
          <label><input type="checkbox" v-model="formData.coachTraits" value="理論基礎"> 理論基礎</label>
          <label><input type="checkbox" v-model="formData.coachTraits" value="有技術"> 有技術</label>
          <label><input type="checkbox" v-model="formData.coachTraits" value="專業"> 專業</label>
          <label><input type="checkbox" v-model="formData.coachTraits" value="嚴厲"> 嚴厲</label>
          <label><input type="checkbox" v-model="formData.coachTraits" value="多元"> 多元</label>
        </div>
      </section>

      <!-- 想參與的課程類型 -->
      <section>
        <h2>想參與的課程類型</h2>
        <div>
          <!-- 初階班 -->
          <label><input type="checkbox" v-model="formData.courseType" value="初階班"> 初階班 (4000/期)</label>
          <div v-if="formData.courseType.includes('初階班')" class="sub-options">
            <label><input type="checkbox" v-model="formData.subCourseType" value="兒童初階班(每週二14:00 - 15:30)"> 兒童初階班 (每週二 14:00 - 15:30)</label>
            <label><input type="checkbox" v-model="formData.subCourseType" value="兒童初階班(每週二15:30 - 17:00)"> 兒童初階班 (每週二 15:30 - 17:00)</label>
            <label><input type="checkbox" v-model="formData.subCourseType" value="成人初階班(每週一14:00 - 16:00)"> 成人初階班 (每週一 14:00 - 16:00)</label>
            <label><input type="checkbox" v-model="formData.subCourseType" value="成人初階班(每週一16:00 - 18:00)"> 成人初階班 (每週一 16:00 - 18:00)</label>
          </div>
          
          <!-- 競技班 -->
          <label><input type="checkbox" v-model="formData.courseType" value="競技班"> 競技班 (4000/期)</label>
          <div v-if="formData.courseType.includes('競技班')" class="sub-options">
            <label><input type="checkbox" v-model="formData.subCourseType" value="一般競技班(每週二14:00 - 16:00)"> 一般競技班 (每週二 14:00 - 16:00)</label>
            <label><input type="checkbox" v-model="formData.subCourseType" value="一般競技班(每週四16:00 - 18:00)"> 一般競技班 (每週四 16:00 - 18:00)</label>
            <label><input type="checkbox" v-model="formData.subCourseType" value="進階競技班(每週四14:00 - 16:00)"> 進階競技班 (每週四 14:00 - 16:00)</label>
            <label><input type="checkbox" v-model="formData.subCourseType" value="進階競技班(每週四16:00 - 18:00)"> 進階競技班 (每週四 16:00 - 18:00)</label>
          </div>
          
          <!-- 擊打班 -->
          <label><input type="checkbox" v-model="formData.courseType" value="擊打班"> 零打班 (350/堂)</label>
          <div v-if="formData.courseType.includes('零打班')" class="sub-options">
            <label><input type="checkbox" v-model="formData.subCourseType" value="基礎擊打班(每週五19:00 - 22:00)"> 基礎零打班 (每週五 19:00 - 22:00)</label>
            <label><input type="checkbox" v-model="formData.subCourseType" value="基礎擊打班(每週六19:00 - 22:00)"> 基礎零打班 (每週六 19:00 - 22:00)</label>
            <label><input type="checkbox" v-model="formData.subCourseType" value="進階擊打班(每週五19:00 - 22:00)"> 進階零打班 (每週五 19:00 - 22:00)</label>
            <label><input type="checkbox" v-model="formData.subCourseType" value="進階擊打班(每週六19:00 - 22:00)"> 進階零打班 (每週六 19:00 - 22:00)</label>
          </div>
          
          <!-- 個別班 -->
          <label><input type="checkbox" v-model="formData.courseType" value="個別班"> 個別班 (另付費協商)</label>
        </div>
      </section>

      <button type="submit">提交</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        name: '',
        gender: '',
        phone: '',
        email: '',
        grade: '',
        motivation: [],
        techniques: [],
        coachGender: '',
        coachTraits: [],
        courseType: [],
        subCourseType: []
      }
    };
  },
  methods: {
    submitForm() {
      console.log('Form data:', this.formData);
      // Handle form submission logic here
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

.registration-form {
  font-family: Arial, sans-serif;
  margin: 20px;
}
h1, h2 {
  color: #333;
}
form {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
div {
  margin-bottom: 10px;
}
label {
  display: block;
  margin-bottom: 5px;
}
input[type="text"], input[type="email"], input[type="number"], select {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
input[type="checkbox"], input[type="radio"] {
  margin-right: 10px;
}
button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  background-color: #45a049;
}
.sub-options {
  padding-left: 20px;
  margin-top: 10px;
}
</style>
