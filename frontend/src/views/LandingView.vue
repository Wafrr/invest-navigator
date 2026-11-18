
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const menuOpen = ref(false)

function goLogin() {
  menuOpen.value = false
  router.push('/login')
}

function goDashboard() {
  menuOpen.value = false
  router.push(localStorage.getItem('token') ? '/dashboard' : '/login')
}

function goCatalog() {
  menuOpen.value = false
  router.push(localStorage.getItem('token') ? '/catalog' : '/login')
}

function goApplications() {
  menuOpen.value = false
  router.push(localStorage.getItem('token') ? '/applications' : '/login')
}
</script>

<template>
  <div class="landing-page" id="top">
    <header class="landing-header">
      <div class="header-inner">
        <a class="brand" href="#top">
          <span class="brand-star"></span>
          <span>InvestNavigator</span>
        </a>

        <button
          class="menu-button"
          type="button"
          aria-label="Открыть меню"
          :aria-expanded="menuOpen"
          @click="menuOpen = !menuOpen"
        >
          <span></span>
          <span></span>
        </button>

        <nav class="landing-nav" :class="{ 'nav-open': menuOpen }">
          <a href="#features" @click="menuOpen = false">Возможности</a>
          <a href="#how" @click="menuOpen = false">Как это работает</a>
          <a href="#sources" @click="menuOpen = false">База мер</a>
          <button class="nav-login" @click="goLogin">Войти</button>
          <button class="button button-light nav-cta" @click="openMatcher">
            Начать подбор
          </button>
        </nav>
      </div>
    </header>

    <main>
      <!-- Первый экран -->
      <section class="hero-section">
        <img class="hero-art" src="/images/invest-hero.png" alt="">

        <div class="container hero-content">
          <p class="eyebrow">Навигатор господдержки</p>

          <h1>
            Все меры поддержки для вашего бизнеса в одном месте
          </h1>

          <p class="hero-copy">
            Умный алгоритм подберёт субсидии, гранты и льготы
            под профиль вашего проекта за 2 минуты.
          </p>

          <div class="hero-actions">
            <button class="button button-primary" @click="openMatcher">
              Подобрать меры
            </button>

            <a class="button button-outline" href="#how">
              <span class="play-icon">▶</span>
              Смотреть демо
            </a>
          </div>
        </div>
      </section>

      <!-- Источники -->
      <section class="sources-section orbit-background" id="sources">
        <div class="container">
          <h2>Источники данных о мерах</h2>

          <div class="source-grid">
            <a href="https://мсп.рф" target="_blank" rel="noreferrer" class="source-item">
              <img src="/images/msp-chart.png" alt="">
              <span>МСП.РФ</span>
            </a>

            <a href="https://www.gosuslugi.ru" target="_blank" rel="noreferrer" class="source-item">
              <img src="/images/gosuslugi.png" alt="">
              <span>Госуслуги</span>
            </a>

            <a href="https://corpmsp.ru" target="_blank" rel="noreferrer" class="source-item">
              <img src="/images/msp-corp.png" alt="">
              <span>Корпорация МСП</span>
            </a>
          </div>
        </div>
      </section>

      <!-- Возможности -->
      <section class="features-section" id="features">
        <div class="container">
          <p class="section-kicker">Всё необходимое в одном профиле</p>
          <h2>Возможности платформы</h2>

          <div class="feature-grid">
            <article class="feature-card">
              <span class="feature-icon">
                <svg viewBox="0 0 32 32" fill="none">
                  <path d="M8 4h11a3 3 0 0 1 3 3v7M8 4a3 3 0 0 0-3 3v18a3 3 0 0 0 3 3h9"/>
                  <path d="M10 10h7M10 15h7M10 20h4M22 18a5 5 0 1 0 0 10 5 5 0 0 0 0-10Zm4 8 3 3"/>
                </svg>
              </span>
              <h3>Умный подбор</h3>
              <p>
                Алгоритм сверяет форму, стадию, регион, ОКВЭД и цели
                с условиями каждой меры и считает баллы соответствия.
              </p>
            </article>

            <article class="feature-card">
              <span class="feature-icon">
                <svg viewBox="0 0 32 32" fill="none">
                  <path d="M16 3 27 8v7c0 7-4.6 11.7-11 14-6.4-2.3-11-7-11-14V8l11-5Z"/>
                  <path d="m11 16 3 3 7-8"/>
                </svg>
              </span>
              <h3>Цифровой паспорт</h3>
              <p>
                Профиль проекта вместо бесконечных анкет: измените одно
                поле и сразу увидите, какие меры появились или выпали.
              </p>
            </article>

            <article class="feature-card">
              <span class="feature-icon">
                <svg viewBox="0 0 32 32" fill="none">
                  <path d="M5 5v22h23M9 21l5-6 4 3 8-10"/>
                </svg>
              </span>
              <h3>Портфель мер</h3>
              <p>
                Суммарная выгода по всем подходящим мерам и подсказка,
                чего не хватает тем, что подошли почти.
              </p>
            </article>
          </div>
        </div>
      </section>

      <!-- Как это работает -->
      <section class="how-section" id="how">
        <div class="how-orbit how-orbit-one"></div>
        <div class="how-orbit how-orbit-two"></div>
        <span class="spark spark-blue"></span>
        <span class="spark spark-white"></span>

        <div class="container how-layout">
          <div class="how-heading">
            <p class="section-kicker">Три простых шага</p>
            <h2>Как это работает</h2>
            <p>
              Расскажите о проекте один раз — сервис сам найдёт
              подходящие программы.
            </p>
          </div>

          <div class="steps">
            <article class="step">
              <span class="step-number">1</span>
              <div>
                <h3>Заполните анкету</h3>
                <p>Форма, стадия, регион, ОКВЭД и цели проекта.</p>
              </div>
            </article>

            <article class="step">
              <span class="step-number">2</span>
              <div>
                <h3>Получите подборку</h3>
                <p>Меры отсортированы по соответствию профилю.</p>
              </div>
            </article>

            <article class="step">
              <span class="step-number">3</span>
              <div>
                <h3>Подайте заявку</h3>
                <p>Оператор и условия меры собраны в одной карточке.</p>
              </div>
            </article>
          </div>
        </div>
      </section>
    </main>

    <!-- Подвал -->
    <footer class="landing-footer orbit-background">
      <div class="container footer-grid">
        <div class="footer-about">
          <a class="brand" href="#top">
            <span class="brand-star"></span>
            <span>InvestNavigator</span>
          </a>
          <p>
            Подбор мер государственной поддержки для малого
            и среднего бизнеса.
          </p>
        </div>

        <div class="footer-column">
          <h3>Платформа</h3>
          <a href="#features">Возможности</a>
          <a href="#how">Как это работает</a>
          <a href="#sources">База мер</a>
        </div>

        <div class="footer-column">
          <h3>Проект</h3>
          <span>Курсовой проект, 2026</span>
          <span>Vue · FastAPI · PostgreSQL</span>
        </div>
      </div>

      <div class="container footer-bottom">
        © 2026 InvestNavigator. Условия и суммы мер справочные,
        уточняйте их у оператора.
      </div>
    </footer>

    <!-- Модальное окно -->
    <div
      v-if="modalOpen"
      class="modal-backdrop"
      @click.self="closeModal"
    >
      <div class="modal-window" role="dialog" aria-modal="true">
        <button class="modal-close" @click="closeModal" aria-label="Закрыть">
          ×
        </button>

        <template v-if="!submitted">
          <p class="section-kicker">Первый шаг</p>
          <h2>Расскажите о проекте</h2>
          <p class="modal-copy">
            Ответьте на три вопроса — мы подготовим персональную подборку мер.
          </p>

          <form @submit.prevent="submitForm">
            <label>
              Название проекта
              <input name="project" required placeholder="Например, новая кофейня">
            </label>

            <label>
              Регион
              <select name="region" required>
                <option value="" disabled selected>Выберите регион</option>
                <option>Москва</option>
                <option>Санкт-Петербург</option>
                <option>Республика Татарстан</option>
                <option>Другой регион</option>
              </select>
            </label>

            <label>
              Стадия проекта
              <select name="stage" required>
                <option value="" disabled selected>Выберите стадию</option>
                <option>Идея</option>
                <option>Запуск</option>
                <option>Действующий бизнес</option>
                <option>Масштабирование</option>
              </select>
            </label>

            <button class="button button-primary modal-submit" type="submit">
              Получить подборку
            </button>
          </form>
        </template>

        <div v-else class="success-state">
          <span class="success-mark">✓</span>
          <h2>Данные заполнены</h2>
          <p>
            Демонстрационная форма завершена. Для реального подбора
            мер её нужно подключить к backend.
          </p>
          <button class="button button-primary" @click="closeModal">
            Понятно
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;600;700&family=Playfair+Display:wght@600;700&display=swap');

.landing-page {
  --blue: #071792;
  --blue-dark: #050f68;
  --ink: #0a0d1a;
  --paper: #eef0f5;
  --muted: #8e95bd;
  min-height: 100vh;
  background: var(--paper);
  color: var(--ink);
  font-family: 'IBM Plex Mono', monospace;
  overflow: hidden;
}

.landing-page * {
  box-sizing: border-box;
}

.landing-page button,
.landing-page input,
.landing-page select {
  font: inherit;
}

.landing-page a {
  text-decoration: none;
}

.container {
  width: min(1180px, calc(100% - 64px));
  margin: 0 auto;
}

/* Header */
.landing-header {
  height: 82px;
  background: var(--blue);
  color: white;
  position: relative;
  z-index: 10;
}

.header-inner {
  max-width: 1320px;
  height: 100%;
  margin: 0 auto;
  padding: 0 42px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 30px;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  color: white;
  font-family: 'Playfair Display', serif;
  font-size: 25px;
  font-weight: 700;
  white-space: nowrap;
}

.brand-star {
  width: 18px;
  height: 18px;
  background: white;
  display: inline-block;
  transform: rotate(45deg);
  clip-path: polygon(50% 0, 62% 38%, 100% 50%, 62% 62%, 50% 100%, 38% 62%, 0 50%, 38% 38%);
}

.landing-nav {
  display: flex;
  align-items: center;
  gap: 30px;
}

.landing-nav a,
.nav-login {
  color: white;
  font-size: 12px;
  font-weight: 500;
  opacity: .9;
}

.landing-nav a:hover,
.nav-login:hover {
  opacity: 1;
}

.nav-login {
  border: 0;
  background: transparent;
  cursor: pointer;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  min-height: 48px;
  padding: 0 23px;
  border-radius: 3px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: .2s ease;
}

.button-light {
  background: white;
  color: var(--blue);
  border: 1px solid white;
}

.button-light:hover {
  background: #e9ecff;
}

.menu-button {
  display: none;
}

/* Hero */
.hero-section {
  min-height: 600px;
  position: relative;
  display: flex;
  align-items: center;
  overflow: hidden;
  background: #e5e7ee;
}

.hero-art {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

.hero-section::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, rgba(238,240,245,.98) 0%, rgba(238,240,245,.92) 38%, rgba(238,240,245,.12) 100%);
}

.hero-content {
  position: relative;
  z-index: 1;
  padding-top: 30px;
  padding-bottom: 30px;
}

.eyebrow,
.section-kicker {
  color: var(--blue);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  margin: 0 0 24px;
}

.hero-content h1 {
  max-width: 680px;
  font-family: 'Playfair Display', serif;
  font-size: clamp(42px, 5vw, 68px);
  line-height: 1.12;
  letter-spacing: -.035em;
  color: var(--blue);
  margin: 0;
}

.hero-copy {
  max-width: 560px;
  color: #333b64;
  font-size: 13px;
  line-height: 1.8;
  margin: 26px 0 30px;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
}

.button-primary {
  color: white;
  background: var(--blue);
  border: 1px solid var(--blue);
}

.button-primary:hover {
  background: var(--blue-dark);
  transform: translateY(-2px);
}

.button-outline {
  color: var(--blue);
  background: transparent;
  border: 1px solid #07179255;
}

.button-outline:hover {
  background: white;
}

.play-icon {
  font-size: 10px;
}

/* Sources */
.orbit-background {
  background-color: var(--blue);
  background-image:
    radial-gradient(ellipse at 10% 20%, transparent 0 90px, #ffffff0b 91px 92px, transparent 93px),
    radial-gradient(ellipse at 90% 80%, transparent 0 180px, #ffffff0b 181px 182px, transparent 183px);
}

.sources-section {
  padding: 48px 0 54px;
  color: white;
  text-align: center;
}

.sources-section h2 {
  font-family: 'Playfair Display', serif;
  font-size: 30px;
  font-weight: 600;
  color: white;
  margin: 0 0 34px;
}

.source-grid {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: clamp(40px, 8vw, 110px);
  flex-wrap: wrap;
}

.source-item {
  min-height: 58px;
  display: flex;
  align-items: center;
  gap: 13px;
  color: white;
  font-size: 14px;
  font-weight: 600;
}

.source-item img {
  width: auto;
  max-width: 130px;
  height: 48px;
  object-fit: contain;
}

/* Features */
.features-section {
  padding: 94px 0 105px;
  background: #eef0f5;
  text-align: center;
}

.features-section > .container > h2 {
  color: var(--blue);
  font-family: 'Playfair Display', serif;
  font-size: clamp(34px, 3.4vw, 46px);
  margin: 0 0 48px;
}

.features-section .section-kicker {
  margin-bottom: 12px;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
  text-align: left;
}

.feature-card {
  min-height: 285px;
  padding: 30px;
  background: white;
  border: 1px solid #dfe2ec;
  transition: transform .25s, box-shadow .25s;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 18px 40px #07179212;
}

.feature-icon {
  width: 54px;
  height: 54px;
  display: grid;
  place-items: center;
  color: var(--blue);
  background: #e9ecff;
  border-radius: 50%;
}

.feature-icon svg {
  width: 30px;
  height: 30px;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.feature-card h3 {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 17px;
  color: #111642;
  margin: 28px 0 12px;
}

.feature-card p {
  color: #777d9d;
  font-size: 11px;
  line-height: 1.8;
  margin: 0;
}

/* How it works */
.how-section {
  position: relative;
  overflow: hidden;
  padding: 95px 0 100px;
  background: #e2e5ef;
}

.how-layout {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: .9fr 1.1fr;
  gap: 90px;
  align-items: center;
}

.how-heading h2 {
  color: var(--blue);
  font-family: 'Playfair Display', serif;
  font-size: clamp(36px, 4vw, 52px);
  line-height: 1.15;
  margin: 0 0 20px;
}

.how-heading > p:last-child {
  max-width: 390px;
  color: #626987;
  font-size: 12px;
  line-height: 1.9;
}

.steps {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.step {
  display: flex;
  align-items: flex-start;
  gap: 25px;
  padding-bottom: 25px;
  border-bottom: 1px solid #bfc5d9;
}

.step:last-child {
  border-bottom: 0;
  padding-bottom: 0;
}

.step-number {
  color: var(--blue);
  font-family: 'Playfair Display', serif;
  font-size: 43px;
  line-height: 1;
}

.step h3 {
  color: #111642;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 15px;
  margin: 0 0 9px;
}

.step p {
  color: #777d9d;
  font-size: 11px;
  line-height: 1.7;
  margin: 0;
}

.how-orbit {
  position: absolute;
  border: 1px solid #07179218;
  border-radius: 50%;
  pointer-events: none;
}

.how-orbit-one {
  width: 540px;
  height: 540px;
  right: -220px;
  top: -230px;
}

.how-orbit-two {
  width: 700px;
  height: 700px;
  right: -300px;
  top: -310px;
}

.spark {
  position: absolute;
  width: 8px;
  height: 8px;
  transform: rotate(45deg);
}

.spark-blue {
  background: var(--blue);
  top: 80px;
  right: 16%;
}

.spark-white {
  background: white;
  bottom: 90px;
  right: 10%;
}

/* Footer */
.landing-footer {
  padding: 55px 0 24px;
  color: white;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.7fr 1fr 1fr;
  gap: 50px;
  padding-bottom: 42px;
}

.footer-about p {
  max-width: 310px;
  color: #c3c9ed;
  font-size: 11px;
  line-height: 1.8;
  margin-top: 18px;
}

.footer-column {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
}

.footer-column h3 {
  color: white;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12px;
  margin: 0 0 4px;
}

.footer-column a,
.footer-column span {
  color: #c3c9ed;
  font-size: 11px;
}

.footer-column a:hover {
  color: white;
}

.footer-bottom {
  border-top: 1px solid #ffffff30;
  padding-top: 20px;
  color: #aeb7dc;
  font-size: 9px;
  line-height: 1.7;
}

/* Modal */
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 100;
  display: grid;
  place-items: center;
  padding: 20px;
  background: #070b27b8;
  backdrop-filter: blur(5px);
}

.modal-window {
  position: relative;
  width: min(100%, 490px);
  max-height: 90vh;
  overflow-y: auto;
  padding: 42px;
  background: #f7f8fc;
  box-shadow: 0 25px 90px #0004;
}

.modal-close {
  position: absolute;
  top: 13px;
  right: 18px;
  border: 0;
  background: transparent;
  color: var(--blue);
  font-size: 29px;
  cursor: pointer;
}

.modal-window h2 {
  color: var(--blue);
  font-family: 'Playfair Display', serif;
  font-size: 31px;
  line-height: 1.2;
  margin: 0 0 12px;
}

.modal-copy,
.success-state p {
  color: #737a9a;
  font-size: 11px;
  line-height: 1.8;
  margin: 0 0 25px;
}

.modal-window form,
.modal-window label {
  display: flex;
  flex-direction: column;
}

.modal-window form {
  gap: 17px;
}

.modal-window label {
  gap: 8px;
  color: #333b64;
  font-size: 11px;
  font-weight: 600;
}

.modal-window input,
.modal-window select {
  width: 100%;
  min-height: 44px;
  padding: 0 12px;
  border: 1px solid #d7dbea;
  border-radius: 2px;
  background: white;
  color: #202747;
  font-size: 11px;
}

.modal-window input:focus,
.modal-window select:focus {
  outline: 2px solid #07179250;
  border-color: var(--blue);
}

.modal-submit {
  width: 100%;
  margin-top: 8px;
}

.success-state {
  text-align: center;
  padding: 18px 0 4px;
}

.success-mark {
  display: grid;
  place-items: center;
  width: 55px;
  height: 55px;
  margin: 0 auto 23px;
  border-radius: 50%;
  background: #e5eaff;
  color: var(--blue);
  font-size: 25px;
}

.success-state p {
  margin: 0 auto 24px;
  max-width: 340px;
}

/* Responsive */
@media (max-width: 900px) {
  .header-inner {
    padding: 0 25px;
  }

  .landing-nav {
    gap: 17px;
  }

  .landing-nav a,
  .nav-login {
    font-size: 10px;
  }

  .brand {
    font-size: 21px;
  }

  .how-layout {
    gap: 45px;
  }

  .feature-card {
    padding: 23px;
  }
}

@media (max-width: 640px) {
  .container {
    width: calc(100% - 40px);
  }

  .landing-header {
    height: 70px;
  }

  .header-inner {
    padding: 0 20px;
  }

  .brand {
    font-size: 19px;
  }

  .brand-star {
    width: 15px;
    height: 15px;
  }

  .menu-button {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 6px;
    width: 40px;
    height: 40px;
    border: 0;
    background: transparent;
    cursor: pointer;
  }

  .menu-button span {
    width: 23px;
    height: 2px;
    background: white;
  }

  .landing-nav {
    display: none;
    position: absolute;
    top: 70px;
    left: 0;
    right: 0;
    padding: 22px;
    background: var(--blue);
    flex-direction: column;
    align-items: stretch;
    gap: 20px;
  }

  .landing-nav.nav-open {
    display: flex;
  }

  .landing-nav a,
  .nav-login {
    font-size: 13px;
    text-align: left;
  }

  .nav-cta {
    width: 100%;
  }

  .hero-section {
    min-height: 650px;
    align-items: flex-start;
    padding: 75px 0 55px;
  }

  .hero-art {
    object-position: 60% center;
  }

  .hero-section::after {
    background: linear-gradient(180deg, rgba(238,240,245,.96), rgba(238,240,245,.85) 65%, rgba(238,240,245,.4));
  }

  .hero-content h1 {
    font-size: clamp(38px, 10vw, 49px);
  }

  .hero-copy {
    max-width: 360px;
    font-size: 12px;
  }

  .hero-actions {
    align-items: flex-start;
    flex-direction: column;
  }

  .sources-section {
    padding: 43px 0;
  }

  .sources-section h2 {
    font-size: 25px;
  }

  .source-grid {
    gap: 25px 30px;
  }

  .source-item {
    font-size: 11px;
  }

  .source-item img {
    max-width: 90px;
    height: 39px;
  }

  .features-section {
    padding: 68px 0 75px;
  }

  .features-section > .container > h2 {
    font-size: 34px;
    margin-bottom: 32px;
  }

  .feature-grid {
    grid-template-columns: 1fr;
    gap: 14px;
  }

  .feature-card {
    min-height: 230px;
    padding: 25px;
  }

  .feature-card h3 {
    font-size: 16px;
    margin-top: 22px;
  }

  .feature-card p {
    font-size: 11px;
  }

  .how-section {
    padding: 70px 0;
  }

  .how-layout {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .how-heading h2 {
    font-size: 37px;
  }

  .steps {
    gap: 27px;
  }

  .step-number {
    font-size: 38px;
  }

  .footer-grid {
    grid-template-columns: 1fr 1fr;
    gap: 30px 20px;
  }

  .footer-about {
    grid-column: 1 / -1;
  }

  .footer-bottom {
    font-size: 9px;
  }

  .modal-window {
    padding: 35px 23px 27px;
  }

  .modal-window h2 {
    font-size: 27px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .landing-page *,
  .landing-page *::before,
  .landing-page *::after {
    transition: none !important;
    animation: none !important;
  }
}
</style>
