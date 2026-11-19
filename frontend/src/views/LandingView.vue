<script setup>
import { useRouter } from 'vue-router'
import mspRf from '../assets/landing/msp-rf.png'
import gosuslugi from '../assets/landing/gosuslugi.webp'
import corpMsp from '../assets/landing/corp-msp.webp'

const router = useRouter()
const go = tab => router.push(tab === 'catalog' ? '/catalog' : localStorage.getItem('token') ? '/dashboard' : '/login')

const features = [
  { t: 'Умный подбор', d: 'Алгоритм сверяет форму, стадию, регион, ОКВЭД и цели с условиями каждой меры и считает баллы соответствия.', i: 'target' },
  { t: 'Цифровой паспорт', d: 'Профиль проекта вместо бесконечных анкет: измените одно поле и сразу увидите, какие меры появились или выпали.', i: 'card' },
  { t: 'Портфель мер', d: 'Суммарная выгода по всем подходящим мерам и подсказка, чего не хватает тем, что подошли почти.', i: 'case' },
]
const steps = [
  { t: 'Заполните анкету', d: 'Форма, стадия, регион, ОКВЭД и цели проекта.' },
  { t: 'Получите подборку', d: 'Меры отсортированы по соответствию профилю.' },
  { t: 'Подайте заявку', d: 'Оператор и условия меры собраны в одной карточке.' },
]
const sources = [
  { n: 'МСП.РФ', img: mspRf, c: 'msp' },
  { n: 'Госуслуги', img: gosuslugi, c: 'gos' },
  { n: 'Корпорация МСП', img: corpMsp, c: 'corp' },
]
</script>

<template>
  <div class="page">
    <header class="nav">
      <a class="logo" href="#top" aria-label="InvestNavigator">
        <svg class="mark" viewBox="0 0 100 100" preserveAspectRatio="none" fill="currentColor" aria-hidden="true"><path d="M50 0C50 30 62 50 100 50C62 50 50 70 50 100C50 70 38 50 0 50C38 50 50 30 50 0Z"/></svg>
        <span>InvestNavigator</span>
      </a>
      <nav class="links" aria-label="Разделы">
        <a href="#features">Возможности</a>
        <a href="#how">Как это работает</a>
        <a href="#" @click.prevent="go('catalog')">База мер</a>
      </nav>
      <div class="actions">
        <button class="login" @click="go()">Войти</button>
        <button class="pill white" @click="go()">Начать подбор</button>
      </div>
    </header>

    <main id="top">
      <section class="hero">
        <div class="hero-in">
          <h1 class="up d1">Все меры поддержки для вашего бизнеса в одном месте</h1>
          <p class="up d2">Умный алгоритм подберёт субсидии, гранты и льготы под профиль вашего проекта за 2 минуты.</p>
          <div class="cta up d3">
            <button class="pill navy lg" @click="go()">Подобрать меры</button>
            <button class="pill white lg" @click="go('catalog')">
              <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M10 8l6 4-6 4z" fill="currentColor"/></svg>
              Смотреть демо
            </button>
          </div>
        </div>
      </section>

      <section class="trust" aria-labelledby="trust-t">
                <h2 id="trust-t">Источники данных о мерах</h2>
        <ul>
          <li v-for="s in sources" :key="s.n">
            <span class="disc"><img :class="s.c" :src="s.img" alt="" loading="lazy"></span>
            <span class="name">{{ s.n }}</span>
          </li>
        </ul>
      </section>

      <section id="features" class="sec">
        <h2 class="sec-t">Возможности платформы</h2>
        <div class="cards">
          <article v-for="f in features" :key="f.t" class="card">
            <span class="ico" aria-hidden="true">
              <svg v-if="f.i==='target'" viewBox="0 0 32 32" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M8 4h11a3 3 0 0 1 3 3v7M8 4a3 3 0 0 0-3 3v18a3 3 0 0 0 3 3h9"/><path d="M10 10h7M10 15h7M10 20h4M22 18a5 5 0 1 0 0 10 5 5 0 0 0 0-10Zm4 8 3 3"/></svg>
              <svg v-else-if="f.i==='card'" viewBox="0 0 32 32" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M16 3 27 8v7c0 7-4.6 11.7-11 14-6.4-2.3-11-7-11-14V8l11-5Z"/><path d="m11 16 3 3 7-8"/></svg>
              <svg v-else viewBox="0 0 32 32" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 5v22h23M9 21l5-6 4 3 8-10"/></svg>
            </span>
            <h3>{{ f.t }}</h3>
            <p>{{ f.d }}</p>
          </article>
        </div>
      </section>

      <section id="how" class="how">
        <div class="how-in">
          <div class="how-title">
            <div class="art" aria-hidden="true"></div>
            <h2>Как это работает</h2>
          </div>
          <ol class="steps">
            <li v-for="(s, n) in steps" :key="s.t" :class="'s' + (n + 1)">
              <b>{{ n + 1 }}</b>
              <h3>{{ s.t }}</h3>
              <p>{{ s.d }}</p>
            </li>
          </ol>
        </div>
      </section>
    </main>

    <footer class="foot">
            <div class="cols">
        <div>
          <strong class="brand"><svg class="mark" viewBox="0 0 100 100" preserveAspectRatio="none" fill="currentColor" aria-hidden="true"><path d="M50 0C50 30 62 50 100 50C62 50 50 70 50 100C50 70 38 50 0 50C38 50 50 30 50 0Z"/></svg><span>InvestNavigator</span></strong>
          <p>Подбор мер государственной поддержки для малого и среднего бизнеса.</p>
        </div>
        <div><h4>Платформа</h4><a href="#features">Возможности</a><a href="#how">Как это работает</a><a href="#" @click.prevent="go('catalog')">База мер</a></div>
        <div><h4>Проект</h4><span>Курсовой проект, 2026</span><span>Vue 3 · FastAPI · PostgreSQL</span></div>
      </div>
      <p class="copy">© 2026 InvestNavigator. Условия и суммы мер справочные, уточняйте их у оператора.</p>
    </footer>
  </div>
</template>

<style scoped>
.page{
  --navy:#010E87; --navy-2:#020F86; --navy-3:#010A5F; --bg:#E5E6E9; --line:#505AB8; --muted:#6B70A6;
  --hh:clamp(64px,6.8vw,131px);
  background:var(--bg); color:#000; min-height:100vh; overflow-x:clip;
  font-family:'Cousine','Liberation Mono',ui-monospace,monospace; font-weight:700;
}
h1,h2,h3{font-family:'Playfair Display',Georgia,serif;color:var(--navy);margin:0}
a,button{transition:all .3s ease-in-out;cursor:pointer}
section[id]{scroll-margin-top:var(--hh)}

/* Шапка */
.nav{position:sticky;top:0;z-index:20;height:var(--hh);display:flex;align-items:center;justify-content:space-between;gap:24px;padding:0 clamp(16px,4.7vw,90px);background:var(--navy)}
.logo{display:flex;align-items:center;gap:clamp(8px,.9vw,18px);color:#fff;text-decoration:none;font-family:'Playfair Display',Georgia,serif;font-weight:700;font-size:clamp(20px,1.9vw,36px)}
.mark{width:clamp(24px,3.1vw,58px);height:auto;aspect-ratio:4/5;flex:none}
.links{display:flex;gap:clamp(24px,5vw,96px)}
.links a{color:#fff;text-decoration:none;font-size:clamp(14px,1.25vw,24px);white-space:nowrap}
.links a{position:relative}.links a::after{content:'';position:absolute;left:0;right:0;bottom:-6px;height:2px;background:#fff;transform:scaleX(0);transition:transform .25s ease}.links a:hover::after,.links a:focus-visible::after{transform:scaleX(1)}
.actions{display:flex;align-items:center;gap:clamp(16px,2.4vw,44px)}
.login{background:none;border:0;padding:8px 0;color:#fff;font:inherit;font-size:clamp(14px,1.25vw,24px)}
.login:hover{opacity:.7}

/* Кнопки-«таблетки» */
.pill{display:inline-flex;align-items:center;justify-content:center;gap:10px;border:0;border-radius:50px;font:inherit;font-weight:700;font-size:clamp(14px,1.25vw,24px);padding:clamp(9px,.7vw,13px) clamp(20px,2.4vw,47px);white-space:nowrap}
.pill.white{background:#fff;color:var(--navy)}
.pill.navy{background:var(--navy);color:#fff}
.pill.lg{font-size:clamp(15px,1.35vw,26px);padding:clamp(13px,1.1vw,21px) clamp(26px,3.3vw,64px)}
.pill:hover{transform:translateY(-2px);box-shadow:0 8px 20px #010e8740}
.pill.white:hover{background:#f3f4ff}

/* Hero */
.hero{position:relative;min-height:clamp(560px,44vw,844px);display:flex;align-items:center;background:url('../assets/landing/hero.webp') center/cover no-repeat}
.hero-in{width:100%;padding:clamp(48px,6vw,110px) clamp(16px,4.7vw,90px)}
.hero h1{font-size:clamp(30px,3.33vw,64px);font-weight:800;line-height:1.2;max-width:min(100%,16em)}
.hero p{max-width:min(46vw,910px);margin:clamp(20px,3.2vw,60px) 0 clamp(28px,4.4vw,84px);color:var(--navy);font-size:clamp(15px,1.25vw,24px);line-height:1.35}
.cta{display:flex;flex-wrap:wrap;gap:clamp(12px,2vw,40px)}

/* Источники данных */
.trust{position:relative;overflow:hidden;background:var(--navy-2) url('../assets/landing/bg-sources.webp') center/cover no-repeat;padding:clamp(32px,3.6vw,70px) 5vw clamp(40px,4.5vw,86px);text-align:center}
.trust h2{color:#fff;font-weight:800;font-size:clamp(22px,1.9vw,36px);position:relative}
.trust ul{position:relative;list-style:none;margin:clamp(28px,3.2vw,60px) auto 0;padding:0;max-width:1500px;display:flex;justify-content:space-between;gap:24px}
.trust li{flex:1;display:flex;flex-direction:column;align-items:center;gap:clamp(12px,1.4vw,26px);color:#fff}
.disc{display:grid;place-items:center;width:clamp(84px,6.6vw,126px);height:clamp(84px,6.6vw,126px);border-radius:50%;background:#fff}
.disc img{display:block;object-fit:cover;height:auto}
.disc .msp{width:45%}.disc .gos{width:62%;aspect-ratio:78/82;height:auto}.disc .corp{width:79%}
.name{font-family:'Playfair Display',Georgia,serif;font-weight:600;font-size:clamp(18px,1.67vw,32px)}


/* Возможности */
.sec{padding:clamp(48px,6vw,114px) 4.6vw clamp(56px,7vw,134px)}
.sec-t{text-align:center;font-weight:600;font-size:clamp(28px,2.5vw,48px);margin-bottom:clamp(28px,4.2vw,80px)}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(14px,1.05vw,20px);max-width:1800px;margin:0 auto}
.card{background:#fff;border-radius:25px;box-shadow:0 10px 4px #010e8729;padding:clamp(24px,2.1vw,41px) clamp(22px,3.4vw,65px) clamp(28px,3vw,58px)}
.card:hover{transform:translateY(-4px);box-shadow:0 14px 10px #010e8733}
.ico{display:grid;place-items:center;width:clamp(64px,5.3vw,102px);height:clamp(64px,5.3vw,102px);border-radius:50%;background:var(--navy-2)}
.ico svg{width:46%;height:46%}
.card h3{font-family:'Cousine','Liberation Mono',monospace;color:#000;font-weight:700;font-size:clamp(22px,1.9vw,36px);margin:clamp(18px,2vw,38px) 0 clamp(10px,1vw,20px)}
.card p{margin:0;color:var(--muted);font-size:clamp(15px,1.25vw,24px);line-height:1.35}

/* Как это работает */
.how{position:relative;overflow:hidden;padding:clamp(40px,5vw,96px) 3vw clamp(56px,7vw,134px)}
.how-in{max-width:1800px;margin:0 auto;display:grid;grid-template-columns:1.1fr 1fr;align-items:center;gap:2vw}
.how-title{position:relative;aspect-ratio:2538/2102;display:flex;align-items:center}
.how-title h2{position:relative;z-index:2;font-weight:600;font-size:clamp(34px,4.5vw,86px);line-height:1.1;padding:0 0 6% 19%;max-width:100%;white-space:nowrap}
.art{position:absolute;inset:0;background:url('../assets/landing/bg-how.webp') left center/contain no-repeat}
.steps{--c:clamp(64px,5.3vw,102px);--r:calc(var(--c) / 2);list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr}
.steps li{position:relative;text-align:center;padding:0 clamp(8px,1.4vw,28px) clamp(28px,3.6vw,70px)}
.steps li.s1{grid-column:1;grid-row:1}.steps li.s2{grid-column:2;grid-row:2}.steps li.s3{grid-column:1;grid-row:3;padding-bottom:0}
.steps b{position:relative;z-index:1;display:inline-grid;place-items:center;width:var(--c);height:var(--c);border-radius:50%;background:var(--navy-2);color:#fff;font-family:'Playfair Display',Georgia,serif;font-weight:600;font-size:calc(var(--c) * .47)}
.steps h3{color:#000;font-weight:600;font-size:clamp(20px,1.9vw,36px);margin:clamp(10px,1vw,20px) 0 clamp(6px,.6vw,12px)}
.steps p{margin:0 auto;max-width:420px;color:#000;font-family:'Playfair Display',Georgia,serif;font-weight:600;font-size:clamp(15px,1.25vw,24px);line-height:1.3}
/* линии-соединители */
.steps li.s1::after,.steps li.s2::after{content:'';position:absolute;top:var(--r);height:calc(100% - var(--r));width:calc(100% - var(--r));border:0 solid var(--navy-2);border-top-width:3px}
.steps li.s1::after{left:calc(50% + var(--r));border-right-width:3px;border-top-right-radius:clamp(20px,2.6vw,50px)}
.steps li.s2::after{right:calc(50% + var(--r));border-left-width:3px;border-top-left-radius:clamp(20px,2.6vw,50px)}

/* Подвал */
.foot{position:relative;overflow:hidden;background:var(--navy-3) url('../assets/landing/bg-footer.webp') center/cover no-repeat;color:#fff;padding:clamp(40px,4.5vw,86px) 5vw clamp(24px,2vw,38px)}
.cols{position:relative;display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:32px;max-width:1500px;margin:0 auto}
.cols strong.brand{display:flex;align-items:center;gap:12px}
.cols strong{font-family:'Playfair Display',Georgia,serif;font-size:clamp(20px,1.6vw,30px)}
.cols p{color:#c7d2e8;font-size:clamp(13px,.95vw,17px);max-width:380px;margin:12px 0 0;line-height:1.45}
.cols h4{margin:0 0 14px;font-size:clamp(15px,1.1vw,20px)}
.cols a,.cols span{display:block;color:#c7d2e8;text-decoration:none;font-size:clamp(13px,.95vw,17px);margin-bottom:10px}
.cols a:hover{color:#fff}
.copy{position:relative;max-width:1500px;margin:clamp(28px,3vw,56px) auto 0;padding-top:20px;border-top:1px solid #ffffff2e;font-size:clamp(12px,.85vw,15px);color:#aab6d6}

/* Анимация появления */
.up{opacity:0;animation:up .8s ease-out forwards}.d1{animation-delay:.1s}.d2{animation-delay:.35s}.d3{animation-delay:.6s}
@keyframes up{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.up{opacity:1;animation:none}.pill:hover,.card:hover{transform:none}}

/* Планшет */
@media (max-width:900px){.links{display:none}}
@media (max-width:1100px){
  .how-title h2{white-space:normal;padding-left:22%}
  .how-in{grid-template-columns:1fr;gap:24px}
  .how-title{max-width:620px;width:100%;margin:0 auto}
  .steps{max-width:760px;margin:0 auto;width:100%}
}
/* Мобильный */
@media (max-width:768px){
  .links,.login{display:none}
  .nav{gap:12px}
  .hero{min-height:0;background-position:62% center}
  .hero::before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,#e5e6e9cc,#e5e6e988)}
  .hero-in{position:relative;padding:56px 5vw 64px}
  .hero h1{font-size:clamp(28px,8vw,40px);max-width:100%}
  .hero p{max-width:100%}
  .cta{flex-direction:column;align-items:stretch}.cta .pill{width:100%}
  .trust,.foot{background-position:80% center}
  .trust ul{flex-direction:column;align-items:center;gap:20px}
  .trust li{flex-direction:row;gap:18px;width:100%;max-width:340px;justify-content:flex-start}
  .disc{flex:none}.name{text-align:left}
  .cards{grid-template-columns:1fr}
  .card{text-align:center}.card .ico{margin:0 auto}
  .how{padding:40px 5vw 56px}
  .how-title{aspect-ratio:auto;display:block;text-align:center}
  .art{display:none}
  .how-title h2{padding:0;font-size:clamp(30px,8.5vw,40px)}
  .steps{grid-template-columns:1fr;margin-top:8px}
  .steps li.s1,.steps li.s2,.steps li.s3{grid-column:1;grid-row:auto;padding-bottom:44px}
  .steps li.s3{padding-bottom:0}
  .steps li.s1::after,.steps li.s2::after{left:calc(50% - 1.5px);right:auto;top:auto;bottom:0;width:0;height:44px;border:0;border-left:3px solid var(--navy-2);border-radius:0}
  .cols{grid-template-columns:1fr}
}
</style>
