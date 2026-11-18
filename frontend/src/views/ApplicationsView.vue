<script setup>
import { ref, onMounted } from 'vue'
import { api, fmt, errText } from '../api'

const apps = ref([]); const error = ref(''); const loading = ref(true)
const cls = s => s === 'Одобрена' ? 'ok' : s === 'Отклонена' ? 'bad' : ''   // Новая — синий по умолчанию
onMounted(async () => {
  try { apps.value = (await api.get('/applications')).data } catch (e) { error.value = errText(e) } finally { loading.value = false }
})
</script>

<template>
  <h1>Мои заявки</h1>
  <p v-if="error" class="note bad">{{ error }}</p>
  <p v-if="loading" class="note">Загружаем заявки…</p>
  <p v-else-if="!apps.length && !error" class="note">Заявок пока нет. Выберите меру в <router-link to="/catalog">каталоге</router-link> и подайте первую.</p>
  <article v-for="a in apps" :key="a.id" class="panel row fade">
    <div><h3>{{ a.measure }}</h3><p>{{ a.operator }} · {{ fmt(a.max_sum) }} · подана {{ a.created }}</p></div>
    <span class="badge" :class="cls(a.status)">{{ a.status }}</span>
  </article>
</template>

<style scoped>
.row{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-bottom:12px}
h3{font-size:18px}p{margin:4px 0 0;color:var(--muted);font-size:14px}
</style>
