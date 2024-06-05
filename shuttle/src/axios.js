
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL:  ' https://2228-60-250-79-113.ngrok-free.app/api/', 
  timeout: 10000, 
  headers: {
    'Content-Type': 'application/json',
  },
});

export default axiosInstance;
