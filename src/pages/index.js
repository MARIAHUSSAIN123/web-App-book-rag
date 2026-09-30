import React, {useState, useEffect} from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';

const CODE = [
  'const course = {',
  '  name: "Modern Web Development",',
  '  months: 12,',
  '  modules: 4,',
  '  stack: ["HTML", "CSS", "JS", "React", "Node"],',
  '  languages: ["English", "Roman Urdu"],',
  '  tutor: "AI chatbot 🤖",',
  '};',
  'course.start(); // 🚀',
];
const TECH = ['HTML5', 'CSS3', 'Bootstrap', 'JavaScript', 'TypeScript', 'React', 'Redux', 'Next.js', 'Node.js', 'Express', 'MongoDB', 'PostgreSQL', 'GraphQL', 'Docker', 'CI/CD'];
const MODS = [
  ['🎨', 'module-01-web-designing', 'Web Designing', 'Web Designing', 20, 'HTML · CSS · Bootstrap', '#ec4899'],
  ['⚡', 'module-02-front-end-development', 'Front-End Development', 'Front-End Development', 31, 'JavaScript · TypeScript · GSAP', '#f97316'],
  ['⚛️', 'module-03-modern-front-end', 'Modern Front-End', 'Modern Front-End', 14, 'React · Redux · Next.js', '#06b6d4'],
  ['🛠️', 'module-04-back-end-development', 'Back-End Development', 'Back-End Development', 16, 'Node · Express · Databases · Docker', '#8b5cf6'],
];
const T = {
  en: {title: 'Modern Web Application Development', sub: 'From your first HTML tag to deployed full-stack apps, explained in English and Roman Urdu with an AI tutor beside you.',
    start: 'Start Learning', ask: 'Ask the AI Tutor', by: 'Created by Maria Hussain', mods: 'Course Modules', topics: 'topics',
    stats: [['12', 'Months'], ['4', 'Modules'], ['81', 'Topics'], ['2', 'Languages']]},
  ur: {title: 'Modern Web Application Development', sub: 'Pehle HTML tag se deployed full-stack apps tak, English aur Roman Urdu mein, AI tutor ke sath.',
    start: 'Parhna Shuru Karein', ask: 'AI Tutor se Poochein', by: 'Created by Maria Hussain', mods: 'Course Modules', topics: 'topics',
    stats: [['12', 'Mahine'], ['4', 'Modules'], ['81', 'Topics'], ['2', 'Zubanein']]},
};

export default function Home() {
  const {i18n} = useDocusaurusContext();
  const t = i18n.currentLocale === 'en' ? T.en : T.ur;
  const i = i18n.currentLocale === 'en' ? 2 : 3;
  const [n, setN] = useState(0);
  useEffect(() => {
    const id = setInterval(() => setN((x) => (x < CODE.length ? x + 1 : x)), 650);
    return () => clearInterval(id);
  }, []);
  return (
    <Layout title={t.title} description={t.sub}>
      <header className={styles.hero}>
        <div className={styles.grid} />
        <div className={`container ${styles.heroIn}`}>
          <div className={styles.left}>
            <p className={styles.badge}>🚀 SMIT · {t.by}</p>
            <h1 className={styles.title}>{t.title}</h1>
            <p className={styles.sub}>{t.sub}</p>
            <div className={styles.btns}>
              <Link className={`button button--lg ${styles.cta}`} to="/docs/intro">{t.start} →</Link>
              <button className={`button button--lg ${styles.ghost}`} onClick={() => window.dispatchEvent(new Event('open-chatbot'))}>💬 {t.ask}</button>
            </div>
            <div className={styles.stats}>
              {t.stats.map(([a, b]) => <div key={b} className={styles.stat}><b>{a}</b><span>{b}</span></div>)}
            </div>
          </div>
          <div className={styles.win}>
            <div className={styles.bar}><i /><i /><i /><span>course.js</span></div>
            <pre className={styles.code}>{CODE.slice(0, n).map((l, k) => <div key={k}>{l}</div>)}<span className={styles.cursor} /></pre>
          </div>
        </div>
      </header>
      <div className={styles.marquee}><div className={styles.track}>
        {[...TECH, ...TECH].map((x, k) => <span key={k}>{x}</span>)}
      </div></div>
      <main className="container margin-vert--xl">
        <h2 className={styles.h2}>{t.mods}</h2>
        <div className={styles.cards}>
          {MODS.map((m, k) => (
            <Link key={m[1]} to={`/docs/${m[1]}`} className={styles.card} style={{'--c': m[6], animationDelay: `${k * 110}ms`}}>
              <span className={styles.num}>0{k + 1}</span>
              <span className={styles.icon}>{m[0]}</span>
              <h3>{m[i]}</h3>
              <p>{m[5]}</p>
              <em>{m[4]} {t.topics} →</em>
            </Link>
          ))}
        </div>
      </main>
    </Layout>
  );
}
