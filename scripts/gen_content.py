# -*- coding: utf-8 -*-
"""Web & App course ki English + Roman Urdu chapters banata hai: python scripts/gen_content.py"""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = os.path.join(ROOT, "docs")
UR = os.path.join(ROOT, "i18n", "ur-Latn", "docusaurus-plugin-content-docs", "current")

M = [
 dict(slug="module-01-web-designing", icon="🎨", t=("Web Designing", "Web Designing"),
  intro=("Build beautiful, responsive websites with HTML, CSS and Bootstrap, then put them online.",
         "HTML, CSS aur Bootstrap se khoobsurat, responsive websites banana aur unhein online karna."),
  topics=[
   ("HTML Text","Headings, paragraphs, bold, italic and the basic building blocks of a page.","Headings, paragraphs, bold, italic aur page ke bunyadi tukde."),
   ("HTML Images","Show pictures with the img tag, alt text and sizing.","img tag, alt text aur size ke sath tasveerein dikhana."),
   ("HTML Table","Present data in rows and columns.","Data ko rows aur columns mein dikhana."),
   ("HTML Forms","Collect user input with inputs, select boxes and buttons.","Inputs, select aur buttons se user se data lena."),
   ("HTML Audio/Video Tags","Embed audio and video with the audio and video tags.","audio aur video tags se media embed karna."),
   ("HTML Links","Connect pages with anchor tags and build navigation.","Anchor tags se pages ko jorna aur navigation banana."),
   ("Grid System","Lay out pages in rows and columns with CSS Grid.","CSS Grid se page ko rows aur columns mein saja-na."),
   ("Font Awesome","Add ready-made icons to your pages.","Tayyar icons apne pages mein lagana."),
   ("Bootstrap","Build responsive layouts fast with a UI framework.","UI framework se tez responsive layouts banana."),
   ("CSS3","Style pages with colors, spacing, borders and effects.","Colors, spacing, borders aur effects se page ko style karna."),
   ("Google Fonts","Use beautiful web fonts for your text.","Text ke liye khoobsurat web fonts lagana."),
   ("CSS Variables","Reuse colors and sizes with custom properties.","Custom properties se colors aur sizes dobara istemal karna."),
   ("Netlify Hosting","Put your site online for free with Netlify.","Netlify par apni site free mein online karna."),
   ("GitHub","Save code, track changes and collaborate with Git.","Code mehfooz karna, changes track karna aur mil kar kaam karna."),
   ("GitHub Hosting","Publish a site with GitHub Pages.","GitHub Pages se site publish karna."),
   ("CSS Animations","Bring elements to life with transitions and keyframes.","Transitions aur keyframes se elements ko harkat dena."),
   ("Media Queries","Make layouts adapt to phones, tablets and desktops.","Layout ko mobile, tablet aur desktop ke mutabiq dhalna."),
   ("Surge Hosting","Deploy static sites with one command using Surge.","Surge se ek command mein static site deploy karna."),
   ("Domain & Hosting Subscription (Deployment)","Buy a domain, connect hosting and go live.","Domain khareedna, hosting jorna aur site live karna."),
   ("Flexbox","Align and space items in one direction with ease.","Items ko aik rukh mein aasani se align aur space karna."),
  ]),
 dict(slug="module-02-front-end-development", icon="⚡", t=("Front-End Development", "Front-End Development"),
  intro=("Master JavaScript from the basics to advanced ideas, plus TypeScript, GSAP and ready-made backends.",
         "JavaScript ko buniyad se advanced tak seekhna, sath TypeScript, GSAP aur tayyar backends."),
  topics=[
   ("JavaScript Introduction","What JavaScript is, where it runs and how to write your first script.","JavaScript kya hai, kahan chalti hai aur pehla script kaise likhein."),
   ("JavaScript Chapters 1-60 and Quizzes 1-4","Work through the chapters in blocks of ten, with quizzes along the way and a completion test.","Chapters das das ke blocks mein, beech mein quizzes aur aakhir mein completion test."),
   ("Var vs Let vs Const","How the three ways of declaring variables differ in scope and reassignment.","Variables banane ke teenon tareeqon mein scope aur dobara value dene ka farq."),
   ("Template Literals","Build strings with backticks and embedded expressions.","Backticks aur embedded expressions se strings banana."),
   ("Arrow Functions","A shorter function syntax with a simpler this.","Chhota function syntax jismein this ka masla aasan hota hai."),
   ("Iterators & For..of","Loop over arrays, strings and other iterables.","Arrays, strings aur dusri iterables par loop chalana."),
   ("JavaScript Behind the Scenes","How the engine, call stack and execution context work.","Engine, call stack aur execution context andar se kaise kaam karte hain."),
   ("Destructuring, Rest & Spread Operators","Unpack values and copy or merge arrays and objects quickly.","Values nikalna aur arrays/objects ko copy ya merge karna."),
   ("SET, MAP","Collections for unique values and key-value pairs.","Unique values aur key-value jodon ke collections."),
   ("Default Parameters","Give function parameters fallback values.","Function parameters ko default values dena."),
   ("First-Class and Higher-Order Functions","Treat functions as values and pass them to other functions.","Functions ko value ki tarah istemal karna aur doosre functions ko dena."),
   ("Callback Functions","Run code after another task finishes.","Kisi kaam ke khatam hone ke baad code chalana."),
   ("Call, Apply, Bind","Control what this points to when calling a function.","Function chalate waqt this ko control karna."),
   ("Closures","Functions that remember the variables of the place they were created.","Aise functions jo apni jagah ke variables yaad rakhte hain."),
   ("OOP with JavaScript","Classes, objects, inheritance and prototypes.","Classes, objects, inheritance aur prototypes."),
   ("Asynchronous JavaScript","Promises, async/await and fetching data without freezing the page.","Promises, async/await aur page roke baghair data mangwana."),
   ("TypeScript","Add types to JavaScript to catch bugs early.","JavaScript mein types daal kar ghaltiyan pehle pakarna."),
   ("Advance GitHub","Branches, pull requests and team workflows.","Branches, pull requests aur team ke sath workflow."),
   ("GSAP Animations","Create smooth, professional web animations.","Smooth aur professional web animations banana."),
   ("Supabase or Firebase","Use a ready-made backend for auth, database and storage.","Auth, database aur storage ke liye tayyar backend istemal karna."),
  ]),
 dict(slug="module-03-modern-front-end", icon="⚛️", t=("Modern Front-End Development", "Modern Front-End Development"),
  intro=("Build modern single-page apps with React, Redux and Next.js, then deploy them.",
         "React, Redux aur Next.js se modern single-page apps banana aur deploy karna."),
  topics=[
   ("ReactJS Introduction & How to Create a React Project","What React is and how to start a new project.","React kya hai aur naya project kaise shuru karein."),
   ("Components, Props and JSX","Build the UI from reusable components and pass data with props.","Dobara istemal hone wale components se UI banana aur props se data dena."),
   ("State, Events, Forms","Make pages interactive with state, event handlers and forms.","State, events aur forms se pages ko interactive banana."),
   ("React in Depth and Behind the Scenes","Composition, re-usability and how React updates the screen.","Composition, re-usability aur React screen ko kaise update karta hai."),
   ("Effects and Data Fetching in React","Use useEffect to fetch data and react to changes.","useEffect se data mangwana aur tabdeeliyon par kaam karna."),
   ("Custom Hooks, Ref, useReducer etc.","Reuse logic with custom hooks and manage complex state.","Custom hooks se logic dobara istemal karna aur complex state sambhalna."),
   ("Class-based React (Optional)","Older class components, useful for reading legacy code.","Purane class components, legacy code samajhne ke liye."),
   ("Single Page Application (SPA) - React Router DOM","Navigate between pages without reloading.","Page reload kiye baghair pages ke darmiyan jana."),
   ("State Management - Context API","Share data across components without prop drilling.","Props ki zanjeer ke baghair components mein data share karna."),
   ("Performance Optimization","Memoization, lazy loading and avoiding extra renders.","Memoization, lazy loading aur ghair zaroori renders se bachna."),
   ("Redux & Redux Toolkit with Thunk","Predictable global state and async actions.","Global state aur async actions ka munazzam nizam."),
   ("Tailwind, Material UI, Styled Components Overview","Popular styling approaches for React apps.","React apps ke liye mash-hoor styling tareeqay."),
   ("Front-End Deployment through Vercel","Publish your React app to the web.","Apni React app ko web par publish karna."),
   ("Next.js","Full-stack React with routing, server rendering and SEO.","Routing, server rendering aur SEO ke sath full-stack React."),
  ]),
 dict(slug="module-04-back-end-development", icon="🛠️", t=("Back-End Development", "Back-End Development"),
  intro=("Create secure, scalable back-ends with Node.js, Express, databases, queues, Docker and CI/CD.",
         "Node.js, Express, databases, queues, Docker aur CI/CD se secure aur scalable back-end banana."),
  topics=[
   ("Node.js","Run JavaScript on the server.","Server par JavaScript chalana."),
   ("Express.js","Build REST APIs with routes and middleware.","Routes aur middleware ke sath REST APIs banana."),
   ("MongoDB","Store data in flexible documents.","Data ko flexible documents mein rakhna."),
   ("Security and Authentication","Hashing, JWT, sessions and protecting your API.","Hashing, JWT, sessions aur API ki hifazat."),
   ("Multer - Media Uploading","Accept image and file uploads.","Images aur files upload qabool karna."),
   ("Sockets","Real-time features like chat and live updates.","Chat aur live updates jaise real-time features."),
   ("GraphQL","Ask for exactly the data you need.","Sirf wahi data mangna jo zaroori ho."),
   ("PostgreSQL","A powerful relational (SQL) database.","Taqatwar relational (SQL) database."),
   ("Sequelize","Work with SQL databases using JavaScript objects.","JavaScript objects se SQL databases ke sath kaam."),
   ("Payment Integration","Accept online payments safely.","Online payments mehfooz tareeqe se lena."),
   ("Scalable System - Caching","Speed up responses by storing frequent results.","Aksar mangay jane wale nataij store kar ke jawab tez karna."),
   ("Scalable System - Messaging Queues","Handle heavy work in the background with queues.","Bhaari kaam queues ke zariye background mein karna."),
   ("CI / CD","Automate testing and deployment.","Testing aur deployment ko khudkar banana."),
   ("Node Production and Cloud Deployment","Run Node apps reliably in the cloud.","Node apps ko cloud par bharosemand tareeqe se chalana."),
   ("Node.js Optimization","Make your Node app faster and lighter.","Node app ko tez aur halka banana."),
   ("Docker - Containerization","Package your app so it runs the same everywhere.","App ko package karna taake har jagah yaksan chale."),
  ]),
]
TIP = (":::tip 💬 Ask the AI Tutor\nTap the chat button (bottom right) and ask about any topic below. It explains with examples, in English or Roman Urdu.\n:::",
       ":::tip 💬 AI Tutor se poochein\nNeeche right ke chat button par click karke kisi bhi topic ke bare mein poochein. Ye example ke sath English ya Roman Urdu mein samjhata hai.\n:::")

def w(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w", encoding="utf-8").write(s)

for i, base in ((0, EN), (1, UR)):
    for n, m in enumerate(M, 1):
        out = ["---", f"sidebar_position: {n}", f"title: \"Module {n}: {m['t'][i]}\"", "---", "",
               f"# {m['icon']} Module {n}: {m['t'][i]}", "", m["intro"][i], "", TIP[i], ""]
        for k, t in enumerate(m["topics"], 1):
            out += [f"## {k}. {t[0]}", "", t[1 + i], ""]
        w(os.path.join(base, m["slug"] + ".md"), "\n".join(out))
    rows = "\n".join(f"| {n} | {m['icon']} {m['t'][i]} | {len(m['topics'])} |" for n, m in enumerate(M, 1))
    if i == 0:
        s = f"---\nsidebar_position: 0\ntitle: Introduction\n---\n\n# Modern Web Application Development\n\nA complete course book created by Maria Hussain.\n\n- **Duration:** 12 months\n- **Modules:** 4 (81 topics)\n- **Eligibility:** Matric\n\n## Roadmap\n\n| Module | Topic | Sections |\n|---|---|---|\n{rows}\n\nSwitch between English and Roman Urdu from the top bar, and use the chat button for an AI tutor.\n"
    else:
        s = f"---\nsidebar_position: 0\ntitle: Taaruf\n---\n\n# Modern Web Application Development\n\nYeh mukammal course book Maria Hussain ne banayi hai.\n\n- **Muddat:** 12 mahine\n- **Modules:** 4 (81 topics)\n- **Eligibility:** Matric\n\n## Roadmap\n\n| Module | Mauzoo | Sections |\n|---|---|---|\n{rows}\n\nUpar menu se English aur Roman Urdu badlein, aur chat button se AI tutor se poochein.\n"
    w(os.path.join(base, "intro.md"), s)
print("done")
