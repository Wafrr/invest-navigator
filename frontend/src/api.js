import axios from 'axios'
import { reactive } from 'vue'

export const api = axios.create({ baseURL: 'http://localhost:8000/api' })
// Токен из localStorage добавляется ко всем запросам; при 401 — выход на /login
api.interceptors.request.use(c => { const t = localStorage.getItem('token'); if (t) c.headers.Authorization = 'Bearer ' + t; return c })
api.interceptors.response.use(r => r, e => {
  if (e.response?.status === 401 && localStorage.getItem('token')) { localStorage.removeItem('token'); location.href = '/login' }
  return Promise.reject(e)
})
export const errText = e => e.response?.data?.detail?.[0]?.msg || e.response?.data?.detail || 'Сервер не отвечает. Запустите backend.'

// Общее состояние: справочники и результаты подбора
export const store = reactive({
  meta: { forms: [], stages: [], goals: [], regions: [] }, results: [],
  async loadMeta() { if (!this.meta.forms.length) this.meta = (await api.get('/meta')).data },
  async recommend(p) { this.results = (await api.post('/recommend', p)).data },
})
export const fmt = n => n ? n.toLocaleString('ru-RU') + ' ₽' : 'без суммы'
