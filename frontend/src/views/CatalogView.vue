<script setup>
import { ref, computed, onMounted } from 'vue'
import { api, store, fmt, errText } from '../api'

const q = ref(''); const goal = ref(''); const region = ref('')
const applied = ref(new Set()); const msg = ref(''); const error = ref(''); const hasProfile = ref(true)

// Фильтры: текст, цель, регион (мера без региональных ограничений подходит всем)
const list = computed(() => store.results.filter(r =>
  r.name.toLowerCase().includes(q.value.toLowerCase()) && (!goal.value || r.goal === goal.value) &&
  (!region.value || !r.regions.length || r.regions.includes(region.value))))

async function apply(r) {
  msg.value = ''
  try { await api.post('/applications', null, { params: { measure_id: r.id } }); applied.value.add(r.id); msg.value = `Заявка на «${r.name}» подана` }
  catch (e) { msg.value = errText(e) }
}
onMounted(async () => {
  try {
    await store.loadMeta()
    const profile = (await api.get('/profile')).data
    hasProfile.value = !!profile
    await store.recommend(profile || { form: 'ИП', stage: 'Запуск', region: 'Москва', okved: '', goals: [] })
    applied.value = new Set((await api.get('/applications')).data.map(a => a.measure_id ?? 0))
  } catch (e) { error.value = errText(e) }
})
</script>

<template>
  <h1>Каталог мер</h1>
  <p v-if="error" class="note bad">{{ error }}</p>
  <p v-if="!hasProfile" class="note">Заполните <router-link to="/dashboard">анкету</router-link>, чтобы шкала показывала соответствие вашему проекту.</p>
  <p v-if="msg" class="note" role="status">{{ msg }}</p>
  <div class="filters">
    <input v-model="q" class="input" placeholder="Поиск по названию">
    <select v-model="goal" class="input"><option value="">Все цели</option><option v-for="g in store.meta.goals" :key="g">{{ g }}</option></select>
    <select v-model="region" class="input"><option value="">Все регионы</option><option v-for="r in store.meta.regions" :key="r">{{ r }}</option></select>
  </div>
  <div class="grid">
    <article v-for="r in list" :key="r.id" class="panel card fade">
      <header><h3>{{ r.name }}</h3><span class="badge">{{ r.goal }}</span></header>
      <p class="op">{{ r.operator }} · {{ fmt(r.max_sum) }}</p>
      <div class="scale" :aria-label="'Соответствие ' + r.score + '%'"><i :style="{width: r.score + '%'}"></i></div>
      <div class="tags">
        <span v-for="t in r.reasons" :key="t" class="badge ok">{{ t }}</span>
        <span v-if="!r.eligible" class="badge bad">{{ r.blockers[0].text }}</span>
      </div>
      <button class="btn-primary" :disabled="applied.has(r.id)" @click="apply(r)">{{ applied.has(r.id) ? 'Заявка подана' : 'Подать заявку' }}</button>
    </article>
  </div>
  <p v-if="!list.length && !error" class="note">Ничего не найдено. Сбросьте фильтры.</p>
</template>

<style scoped>
.filters{display:grid;grid-template-columns:2fr 1fr 1fr;gap:12px;margin-bottom:20px}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.card{display:flex;flex-direction:column;gap:12px}.card:hover{transform:translateY(-4px);border-color:var(--accent-bright)}
.card header{display:flex;justify-content:space-between;gap:12px;align-items:start}h3{font-size:18px}
.op{margin:0;color:var(--muted);font-size:14px}
.scale{height:8px;border-radius:99px;background:var(--soft);overflow:hidden}.scale i{display:block;height:100%;background:var(--accent-bright)}
.tags{display:flex;flex-wrap:wrap;gap:6px;flex:1;align-content:flex-start}
.card .btn-primary{align-self:flex-start}
@media (max-width:900px){.grid,.filters{grid-template-columns:1fr}}
</style>
