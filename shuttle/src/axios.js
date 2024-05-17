// src/axios.js
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://your_django_server/api', // 配置您的後端 API 基本 URL
  timeout: 10000, // 配置請求超時時間
  headers: {
    'Content-Type': 'application/json',
  },
});

export default axiosInstance;
