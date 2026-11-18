import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', component: () => import('../views/LandingView.vue') },
  { path: '/login', component: () => import('../views/LoginView.vue') },
  { path: '/dashboard', component: () => import('../views/DashboardView.vue'), meta: { auth: true } },
  { path: '/catalog', component: () => import('../views/CatalogView.vue'), meta: { auth: true } },
  { path: '/applications', component: () => import('../views/ApplicationsView.vue'), meta: { auth: true } },
  { path: '/:p(.*)*', redirect: '/' },
]
const router = createRouter({ history: createWebHistory(), routes, scrollBehavior: () => ({ top: 0 }) })

// Защищённые страницы доступны только при наличии токена
router.beforeEach(to => {
  const token = localStorage.getItem('token')
  if (to.meta.auth && !token) return '/login'
  if (to.path === '/login' && token) return '/dashboard'
})
export default router
