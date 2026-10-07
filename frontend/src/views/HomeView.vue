<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const measures = ref([])
const loading = ref(true)
const error = ref(null)

const API_URL = 'http://localhost:8000'

async function loadMeasures() {
  try {
    loading.value = true
    const response = await axios.get(`${API_URL}/api/measures`)
    measures.value = response.data
  } catch (e) {
    error.value = 'Ошибка загрузки мер поддержки'
    console.error(e)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadMeasures()
})
</script>

<template>
  <div class="home">
    <h1>Инвестиционный навигатор</h1>
    <p class="subtitle">Подбор мер поддержки для вашего бизнеса</p>

    <div v-if="loading" class="loading">Загрузка...</div>
    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="measures">
      <div v-for="measure in measures" :key="measure.id" class="card">
        <h3>{{ measure.name }}</h3>
        <p><strong>Тип:</strong> {{ measure.type }}</p>
        <p><strong>Регион:</strong> {{ measure.region }}</p>
        <p><strong>Сумма:</strong> {{ measure.sum.toLocaleString() }} ₽</p>
        <p><strong>Макс. сотрудников:</strong> {{ measure.max_employees }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.subtitle {
  font-size: 1.2rem;
  color: #7f8c8d;
  margin-bottom: 2rem;
}

.loading, .error {
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
}

.error {
  color: #e74c3c;
}

.measures {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}

.card h3 {
  margin-top: 0;
  color: #2c3e50;
  font-size: 1.3rem;
}

.card p {
  margin: 0.5rem 0;
  color: #555;
}
</style>
