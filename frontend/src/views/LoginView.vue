<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { api, errText } from '../api'

const router = useRouter()
const mode = ref('login')            // login | register
const email = ref(''); const password = ref(''); const show = ref(false)
const error = ref(''); const touched = ref(false); const busy = ref(false)

// Клиентская валидация: простой формат e-mail и пароль от 6 символов
const emailErr = computed(() => touched.value && !/^\S+@\S+\.\S+$/.test(email.value) ? 'Введите e-mail в формате name@mail.ru' : '')
const passErr = computed(() => touched.value && password.value.length < 6 ? 'Пароль — не короче 6 символов' : '')

async function submit() {
  touched.value = true; error.value = ''
  if (emailErr.value || passErr.value || !email.value) return
  busy.value = true
  try {
    const { data } = await api.post(`/auth/${mode.value}`, { email: email.value, password: password.value })
    localStorage.setItem('token', data.token); localStorage.setItem('email', data.email)
    router.push('/dashboard')
  } catch (e) { error.value = errText(e) } finally { busy.value = false }
}
</script>

<template>
  <div class="split">
    <section class="left fade">
      <router-link to="/" class="logo">★ InvestNavigator</router-link>
      <form @submit.prevent="submit" novalidate>
        <h1>{{ mode === 'login' ? 'Вход в кабинет' : 'Создание аккаунта' }}</h1>
        <div class="tabs" role="tablist">
          <button type="button" :class="{on: mode==='login'}" @click="mode='login'; error=''">Вход</button>
          <button type="button" :class="{on: mode==='register'}" @click="mode='register'; error=''">Регистрация</button>
        </div>
        <label class="field">E-mail<input v-model="email" type="email" autocomplete="email" placeholder="name@mail.ru"><span class="err" v-if="emailErr">{{ emailErr }}</span></label>
        <label class="field">Пароль
          <span class="pw">
            <input v-model="password" :type="show ? 'text' : 'password'" :autocomplete="mode==='login' ? 'current-password' : 'new-password'">
            <button type="button" :aria-label="show ? 'Скрыть пароль' : 'Показать пароль'" @click="show = !show">
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/><path v-if="show" d="M4 4l16 16"/></svg>
            </button>
          </span>
          <span class="err" v-if="passErr">{{ passErr }}</span>
        </label>
        <p v-if="error" class="note bad">{{ error }}</p>
        <button class="btn-primary" :disabled="busy">{{ mode === 'login' ? 'Войти' : 'Создать аккаунт' }}</button>
      </form>
    </section>
    <aside class="right"><blockquote>Хорошая мера поддержки — та, о которой вы узнали вовремя.</blockquote></aside>
  </div>
</template>

<style scoped>
.split{display:grid;grid-template-columns:1fr 1fr;min-height:100vh}
.left{display:flex;flex-direction:column;padding:32px 6vw}
.logo{color:var(--accent-dark);text-decoration:none;font-weight:600;font-size:18px}
form{margin:auto 0;display:flex;flex-direction:column;gap:16px;max-width:400px;width:100%}
h1{font-size:32px}
.tabs{display:flex;border-bottom:1px solid var(--border)}
.tabs button{background:none;border:0;padding:10px 16px;color:var(--muted);cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-1px}
.tabs .on{color:var(--accent-bright);border-color:var(--accent-bright)}
.pw{position:relative;display:flex}.pw input{flex:1;padding-right:44px}
.pw button{position:absolute;right:6px;top:50%;transform:translateY(-50%);background:none;border:0;color:var(--muted);cursor:pointer;padding:6px}
.pw button:hover{color:var(--accent-bright)}
.right{display:grid;place-items:center;padding:48px;background:linear-gradient(135deg,var(--accent-bright),var(--accent-dark));background-size:200% 200%;animation:flow 14s ease-in-out infinite alternate}
blockquote{margin:0;color:#fff;font:600 clamp(26px,3vw,40px)/1.25 'Playfair Display',serif;max-width:460px}
@keyframes flow{to{background-position:100% 100%}}
@media (max-width:768px){.split{grid-template-columns:1fr}.right{display:none}}
</style>
