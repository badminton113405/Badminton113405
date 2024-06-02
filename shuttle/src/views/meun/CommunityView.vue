<template>
  <div class="comment-board">
    <h1>社群空間</h1>
    <section class="comment-input">
      <h2>討論區</h2>
      <textarea v-model="newCommentText" placeholder="您在想什麼呢？有什麼想要跟我們分享的嗎"></textarea>
      <button @click="addComment">發布</button>
    </section>
    
    <section class="comment-list">
      <div v-for="(comment, index) in comments" :key="index" class="comment-item">
        <div class="comment-header">
          <span>使用者</span>
          <button @click="editComment(index)">編輯</button>
          <button @click="deleteComment(index)">刪除</button>
        </div>
        <div v-if="comment.editing">
          <textarea v-model="comment.text"></textarea>
          <button @click="saveComment(index)">保存</button>
        </div>
        <div v-else>
          <p>{{ comment.text }}</p>
        </div>
        <div class="comment-footer">
          <textarea placeholder="評論..."></textarea>
          <button>發送</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newCommentText: '',
      comments: [
        { text: '一起打球嗎', editing: false },
        { text: '有人要一起上團課嗎', editing: false }
      ]
    };
  },
  methods: {
    addComment() {
      if (this.newCommentText.trim()) {
        this.comments.push({ text: this.newCommentText, editing: false });
        this.newCommentText = '';
      }
    },
    editComment(index) {
      this.comments[index].editing = true;
    },
    saveComment(index) {
      this.comments[index].editing = false;
    },
    deleteComment(index) {
      this.comments.splice(index, 1);
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
.comment-board {
  font-family: Arial, sans-serif;
  margin: 20px;
}
h1 {
  color: #333;
}
.comment-input {
  background-color: #e3f2fd;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 10px;
}
.comment-input h2 {
  margin: 0;
}
.comment-input textarea {
  width: 100%;
  height: 100px;
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.comment-input button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.comment-input button:hover {
  background-color: #45a049;
}
.comment-list {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
.comment-item {
  background-color: white;
  padding: 15px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.comment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
.comment-header button {
  margin-left: 10px;
  background-color: #f1f1f1;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
}
.comment-header button:hover {
  background-color: #ddd;
}
.comment-footer {
  display: flex;
  align-items: center;
}
.comment-footer textarea {
  flex-grow: 1;
  height: 40px;
  margin-right: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.comment-footer button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.comment-footer button:hover {
  background-color: #45a049;
}
</style>

