// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import AboutView from '../views/meun/AboutView.vue';
import ReservationView from '../views/meun/ReservationView.vue';
import CommunityView from '../views/meun/CommunityView';
import VIPView from '../views/VIP/VIPView';
import BeginnerView from '../views/classviews/BeginnerView.vue';
import CompetitiveView from '../views/classviews/CompetitiveView.vue';
import OnetooneView from '../views/classviews/OnetooneView.vue';
import ZerodozenView from '../views/classviews/ZerodozenView.vue';
import CYZView from '../views/coachviews/CYZView.vue';
import ZZTView from '../views/coachviews/ZZTView.vue';
import ZBYView from '../views/coachviews/ZBYView.vue';
import HWHView from '../views/coachviews/HWHView.vue';
import PQView from '../views/teachviews/PQView.vue';
import TQXQView from '../views/teachviews/TQXQView.vue';
import SQView from '../views/teachviews/SQView.vue';
import LoginView from '../views/VIP/LoginView.vue';
import RegisterView from '../views/VIP/RegisterView.vue';
import ForgetView from '../views/VIP/ForgetView.vue';
import PasswordView from '../views/VIP/PasswordView.vue';


const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'About',
    component: AboutView
  },
  {
    path: '/reservation',
    name: 'Reservation',
    component: ReservationView
  },
  {
    path: '/community',
    name: 'Community',
    component: CommunityView
  },
  {
    path: '/vip',
    name: 'VIP',
    component: VIPView
  },
  {
    path: '/beginner',
    name: 'Beginner',
    component: BeginnerView
  },
  {
    path: '/competitive',
    name: 'Competitive',
    component: CompetitiveView
  },
  {
    path: '/onetoone',
    name: 'Onetoone',
    component: OnetooneView
  },
  {
    path: '/zerodozen',
    name: 'Zerodozen',
    component: ZerodozenView
  },
  {
    path: '/cyz',
    name: 'CYZ',
    component: CYZView
  },
  {
    path: '/zzt',
    name: 'ZZT',
    component: ZZTView
  },
  {
    path: '/zby',
    name: 'ZBY',
    component: ZBYView
  },
  {
    path: '/hwh',
    name: 'HWH',
    component: HWHView
  },
  {
    path: '/pq',
    name: 'PQ',
    component: PQView
  },
  {
    path: '/tqxq',
    name: 'TQXQ',
    component: TQXQView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView
  },
  {
    path: '/sq',
    name: 'SQ',
    component: SQView
  },
  {
    path: '/forget',
    name: 'Forget',
    component: ForgetView
  },
  {
    path: '/password',
    name: 'Password',
    component: PasswordView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
