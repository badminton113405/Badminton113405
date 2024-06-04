
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://your_django_server/api', 
  timeout: 10000, 
  headers: {
    'Content-Type': 'application/json',
  },
});

export default axiosInstance;
