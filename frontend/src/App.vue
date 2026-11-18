<script setup>
import { useRoute } from 'vue-router'
import Sidebar from './components/Sidebar.vue'
const route = useRoute()
</script>

<template>
  <!-- Авторизованные страницы: Sidebar + рабочая область; остальные страницы имеют собственные шапку и подвал -->
  <div v-if="route.meta.auth" class="layout"><Sidebar /><main class="work"><router-view :key="route.fullPath" /></main></div>
  <router-view v-else />
</template>

<style scoped>
.layout{display:grid;grid-template-columns:240px minmax(0,1fr);min-height:100vh}
@media (max-width:768px){.layout{grid-template-columns:1fr}}
</style>
