<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const email = localStorage.getItem('email') || ''
const logout = () => { localStorage.removeItem('token'); localStorage.removeItem('email'); router.push('/') }
</script>

<template>
  <aside class="side">
    <router-link to="/" class="logo">★ InvestNavigator</router-link>
    <nav>
      <router-link to="/dashboard">Анкета</router-link>
      <router-link to="/catalog">Каталог</router-link>
      <router-link to="/applications">Заявки</router-link>
    </nav>
    <div class="user"><span>{{ email }}</span><button @click="logout">Выход</button></div>
  </aside>
</template>

<style scoped>
.side{background:var(--accent-dark);color:#fff;padding:24px 16px;display:flex;flex-direction:column;gap:24px;position:sticky;top:0;height:100vh}
.logo{color:#fff;text-decoration:none;font-weight:600;font-size:18px;padding:0 8px}
nav{display:flex;flex-direction:column;gap:4px}
nav a{color:#c7d2e8;text-decoration:none;padding:10px 12px;border-radius:8px}
nav a:hover{background:#ffffff14;color:#fff}
nav a.router-link-active{background:var(--accent-bright);color:#fff}
.user{margin-top:auto;display:flex;flex-direction:column;gap:8px;font-size:13px;color:#9db0c8;word-break:break-all}
.user button{background:none;border:1px solid #ffffff40;color:#fff;border-radius:8px;padding:8px;cursor:pointer}
.user button:hover{background:#ffffff14}
@media (max-width:768px){.side{flex-direction:row;flex-wrap:wrap;height:auto;position:static;align-items:center;padding:12px}.user{margin:0 0 0 auto;flex-direction:row;align-items:center}.user span{display:none}}
</style>
