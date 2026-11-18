<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { api, store, fmt, errText } from '../api'

const step = ref(1); const done = ref(false); const error = ref(''); const loading = ref(true)
const p = reactive({ form: 'ИП', stage: 'Запуск', region: 'Москва', okved: '', goals: [] })
const names = ['Форма и стадия', 'Регион и ОКВЭД', 'Цели']

const okvedOk = computed(() => /^\d{2}(\.\d{1,2}){0,2}$/.test(p.okved))
const okvedErr = computed(() => p.okved && !okvedOk.value ? 'Формат: 62 или 62.01' : '')
const canNext = computed(() => step.value === 2 ? okvedOk.value : step.value === 3 ? p.goals.length > 0 : true)
const eligible = computed(() => store.results.filter(r => r.eligible))
const potential = computed(() => eligible.value.reduce((s, r) => s + r.max_sum, 0))
const toggleGoal = g => { const i = p.goals.indexOf(g); i < 0 ? p.goals.push(g) : p.goals.splice(i, 1) }

async function finish() {
  try { error.value = ''; await api.put('/profile', p); await store.recommend(p); done.value = true }
  catch (e) { error.value = errText(e) }
}
onMounted(async () => {
  try {
    await store.loadMeta()
    const { data } = await api.get('/profile')       // уже заполненная анкета → сразу результаты
    if (data) { Object.assign(p, data); await store.recommend(p); done.value = true }
  } catch (e) { error.value = errText(e) } finally { loading.value = false }
})
</script>

<template>
  <h1>Анкета проекта</h1>
  <p v-if="error" class="note bad">{{ error }}</p>
  <p v-if="loading" class="note">Загружаем данные…</p>

  <section v-else-if="done" class="panel fade">
    <h2>Результаты подбора</h2>
    <p class="sum"><b>{{ eligible.length }}</b> подходящих мер, до <b>{{ fmt(potential) }}</b> суммарно</p>
    <ul class="top"><li v-for="r in eligible.slice(0, 3)" :key="r.id"><span>{{ r.name }}</span><span class="badge">{{ r.score }} баллов</span></li></ul>
    <p v-if="!eligible.length" class="note">Ни одна мера не подошла. Попробуйте другой регион или стадию.</p>
    <div class="row"><router-link to="/catalog" class="btn-primary">Открыть каталог</router-link><button class="btn-outline" @click="done = false; step = 1">Пересчитать</button></div>
  </section>

  <section v-else class="panel fade">
    <div class="bar" role="progressbar" :aria-valuenow="step" aria-valuemin="1" aria-valuemax="3"><i :style="{width: step / 3 * 100 + '%'}"></i></div>
    <p class="stepname">Шаг {{ step }} из 3: {{ names[step - 1] }}</p>
    <div v-if="step === 1" class="grid">
      <label class="field">Форма<select v-model="p.form"><option v-for="f in store.meta.forms" :key="f">{{ f }}</option></select></label>
      <label class="field">Стадия<select v-model="p.stage"><option v-for="s in store.meta.stages" :key="s">{{ s }}</option></select></label>
    </div>
    <div v-if="step === 2" class="grid">
      <label class="field">Регион<select v-model="p.region"><option v-for="r in store.meta.regions" :key="r">{{ r }}</option></select></label>
      <label class="field">ОКВЭД<input v-model="p.okved" placeholder="62.01"><span class="err" v-if="okvedErr">{{ okvedErr }}</span></label>
    </div>
    <div v-if="step === 3"><p class="hint">Выберите одну или несколько целей:</p>
      <div class="chips"><button v-for="g in store.meta.goals" :key="g" :class="{on: p.goals.includes(g)}" @click="toggleGoal(g)">{{ g }}</button></div></div>
    <div class="row">
      <button class="btn-outline" :disabled="step === 1" @click="step--">Назад</button>
      <button v-if="step < 3" class="btn-primary" :disabled="!canNext" @click="step++">Далее</button>
      <button v-else class="btn-primary" :disabled="!canNext" @click="finish">Подобрать меры</button>
    </div>
  </section>
</template>

<style scoped>
.bar{height:6px;border-radius:99px;background:var(--soft);overflow:hidden}.bar i{display:block;height:100%;background:var(--accent-bright);transition:width .4s ease}
.stepname{margin:16px 0 20px;color:var(--muted)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips button{border:1px solid var(--border);background:#fff;border-radius:99px;padding:8px 16px;cursor:pointer}
.chips button:hover{border-color:var(--accent-bright)}
.chips .on{background:var(--accent-bright);border-color:var(--accent-bright);color:#fff}
.row{display:flex;gap:12px;margin-top:28px;flex-wrap:wrap}
.hint{margin:0 0 12px}.sum{font-size:17px}.sum b{color:var(--accent-dark)}
.top{list-style:none;padding:0;margin:16px 0 0}.top li{display:flex;justify-content:space-between;gap:12px;padding:12px 0;border-top:1px solid var(--border)}
</style>
