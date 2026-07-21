<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vedant Karne | Software & AI/ML Engineer</title>
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#f5f3ff',
                            100: '#ede9fe',
                            200: '#ddd6fe',
                            300: '#c4b5fd',
                            400: '#a78bfa',
                            500: '#8b5cf6',
                            600: '#7c3aed',
                            700: '#6d28d9',
                            800: '#5b21b6',
                            900: '#4c1d95',
                            950: '#0f0524'
                        },
                        darkBg: '#090314',
                        cardBg: '#13092e',
                        borderBg: '#2a1754'
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace']
                    }
                }
            }
        }
    </script>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>

    <!-- Canvas Confetti -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #090314;
            color: #f3f4f6;
            overflow-x: hidden;
        }

        .bg-grid-pattern {
            background-size: 40px 40px;
            background-image: 
                linear-gradient(to right, rgba(139, 92, 246, 0.05) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(139, 92, 246, 0.05) 1px, transparent 1px);
        }

        .glow-blob {
            position: absolute;
            border-radius: 50%;
            filter: blur(90px);
            opacity: 0.35;
            pointer-events: none;
        }

        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #090314;
        }
        ::-webkit-scrollbar-thumb {
            background: #2a1754;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #6d28d9;
        }

        .glass-panel {
            background: rgba(19, 9, 46, 0.65);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(139, 92, 246, 0.18);
        }
        .glass-panel-hover:hover {
            border-color: rgba(167, 139, 250, 0.45);
            box-shadow: 0 10px 30px -10px rgba(109, 40, 217, 0.3);
        }

        @keyframes pulseGlow {
            0%, 100% { opacity: 0.4; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.08); }
        }
        .pulse-glow {
            animation: pulseGlow 3s infinite ease-in-out;
        }

        .gradient-text {
            background: linear-gradient(135deg, #e9d5ff 0%, #a78bfa 50%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
</head>
<body class="bg-darkBg text-slate-200 antialiased selection:bg-brand-600 selection:text-white relative min-h-screen">

    <div class="fixed inset-0 bg-grid-pattern pointer-events-none z-0"></div>
    <div class="glow-blob w-[500px] h-[500px] bg-brand-700 top-[-100px] left-[-100px] z-0"></div>
    <div class="glow-blob w-[600px] h-[600px] bg-indigo-900 top-[30%] right-[-150px] z-0"></div>
    <div class="glow-blob w-[450px] h-[450px] bg-purple-900 bottom-[10%] left-[20%] z-0"></div>

    <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2"></div>

    <header class="sticky top-0 z-40 w-full glass-panel border-b border-brand-900/40 px-4 lg:px-8 py-3 transition-all duration-300">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <a href="#" class="flex items-center gap-3 group">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-700 to-purple-500 flex items-center justify-center text-white font-mono font-bold text-lg shadow-lg shadow-brand-700/30 group-hover:scale-105 transition-transform">
                    VK
                </div>
                <div class="flex flex-col">
                    <span class="font-bold text-slate-100 tracking-tight text-base group-hover:text-brand-300 transition-colors">Vedant Karne</span>
                    <span class="text-xs font-mono text-brand-400">Software &amp; AI/ML Engineer</span>
                </div>
            </a>

            <nav class="hidden md:flex items-center gap-6 text-sm font-medium text-slate-300">
                <a href="#about" class="hover:text-brand-300 transition-colors">About</a>
                <a href="#expertise" class="hover:text-brand-300 transition-colors">AI/ML Expertise</a>
                <a href="#projects" class="hover:text-brand-300 transition-colors">Projects</a>
                <a href="#architecture" class="hover:text-brand-300 transition-colors">RAG Pipeline</a>
                <a href="#sandbox" class="hover:text-brand-300 transition-colors flex items-center gap-1.5 text-brand-300 font-mono text-xs bg-brand-950/80 px-2.5 py-1 rounded-full border border-brand-500/30">
                    <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-400"></i> Sandbox
                </a>
                <a href="#experience" class="hover:text-brand-300 transition-colors">Experience</a>
                <a href="#achievements" class="hover:text-brand-300 transition-colors">Achievements</a>
            </nav>

            <div class="flex items-center gap-3">
                <div class="hidden sm:flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-950/60 border border-emerald-500/30 text-xs text-emerald-300 font-mono">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                    Open for 2026 Roles
                </div>
                <a href="mailto:vedantkarne15@gmail.com" class="px-4 py-2 rounded-xl bg-brand-600 hover:bg-brand-500 text-white font-medium text-sm transition-all shadow-lg shadow-brand-600/30 hover:scale-105 flex items-center gap-2">
                    <i data-lucide="mail" class="w-4 h-4"></i>
                    <span>Contact</span>
                </a>
            </div>
        </div>
    </header>

    <main class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-24 pt-8 pb-20">

        <section id="hero" class="pt-8 md:pt-16 pb-8 flex flex-col items-center text-center relative">
            
            <div class="flex flex-wrap items-center justify-center gap-2 mb-8">
                <a href="https://pict.edu/" target="_blank" rel="noopener" class="px-3 py-1 rounded-full glass-panel border border-brand-500/30 text-brand-300 text-xs font-mono hover:border-brand-400 transition-colors flex items-center gap-1.5">
                    <i data-lucide="graduation-cap" class="w-3.5 h-3.5 text-brand-400"></i> PICT Pune '28
                </a>
                <span class="px-3 py-1 rounded-full bg-purple-950/80 border border-purple-800/50 text-purple-300 text-xs font-mono font-semibold">
                    CGPA 9.56 / 10.0
                </span>
                <span class="px-3 py-1 rounded-full bg-indigo-950/80 border border-indigo-800/50 text-indigo-300 text-xs font-mono flex items-center gap-1">
                    <i data-lucide="map-pin" class="w-3.5 h-3.5 text-indigo-400"></i> Pune, India
                </span>
                <a href="#achievements" class="px-3 py-1 rounded-full bg-amber-950/80 border border-amber-800/50 text-amber-300 text-xs font-mono flex items-center gap-1">
                    <i data-lucide="award" class="w-3.5 h-3.5 text-amber-400"></i> NPTEL Gold Medallist
                </a>
            </div>

            <h1 class="text-4xl sm:text-6xl md:text-7xl font-extrabold tracking-tight max-w-5xl text-slate-100 leading-[1.15] mb-6">
                Vedant Karne
            </h1>
            <p class="text-lg sm:text-2xl font-mono text-brand-300 mb-6 font-semibold">
                Software Engineer • AI/ML Engineer • Product Builder
            </p>

            <div class="h-12 flex items-center justify-center font-mono text-sm sm:text-lg text-slate-300 mb-8 max-w-3xl bg-brand-950/50 px-4 py-2 rounded-xl border border-brand-900/60">
                <span id="typing-text" class="border-r-2 border-brand-400 pr-1 py-1"></span>
            </div>

            <p class="text-slate-300 text-base sm:text-lg max-w-3xl font-light leading-relaxed mb-10">
                Computer Engineering undergraduate at <strong class="text-brand-300 font-medium">PICT Pune</strong>. Engineering software at the intersection of intelligent systems, backend engineering, and product design—specializing in agentic RAG platforms, ML pipelines, and full-stack products with measurable impact.
            </p>

            <div class="flex flex-wrap items-center justify-center gap-4 w-full max-w-md mb-12">
                <a href="#sandbox" class="w-full sm:w-auto px-6 py-3.5 rounded-xl bg-gradient-to-r from-brand-700 to-purple-600 hover:from-brand-600 hover:to-purple-500 text-white font-semibold text-sm transition-all shadow-xl shadow-brand-700/30 hover:scale-[1.02] flex items-center justify-center gap-2">
                    <i data-lucide="play-circle" class="w-4 h-4"></i>
                    Launch RAG Sandbox
                </a>
                <a href="#projects" class="w-full sm:w-auto px-6 py-3.5 rounded-xl glass-panel hover:bg-brand-900/40 text-slate-200 font-semibold text-sm transition-all border border-brand-500/30 hover:border-brand-400 flex items-center justify-center gap-2">
                    <i data-lucide="folder-git-2" class="w-4 h-4 text-brand-400"></i>
                    Explore Projects
                </a>
            </div>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 w-full max-w-4xl pt-4 border-t border-brand-900/40">
                <a href="https://github.com/VedantKarne" target="_blank" rel="noopener" class="glass-panel p-3.5 rounded-xl flex items-center justify-between group glass-panel-hover transition-all">
                    <div class="flex items-center gap-2.5">
                        <i data-lucide="github" class="w-5 h-5 text-slate-300 group-hover:text-brand-300"></i>
                        <span class="text-xs font-mono font-medium text-slate-300">GitHub</span>
                    </div>
                    <span class="text-xs font-mono text-brand-400 font-bold">400+ DSA</span>
                </a>

                <a href="https://www.linkedin.com/in/vedant-karne-31023b302/" target="_blank" rel="noopener" class="glass-panel p-3.5 rounded-xl flex items-center justify-between group glass-panel-hover transition-all">
                    <div class="flex items-center gap-2.5">
                        <i data-lucide="linkedin" class="w-5 h-5 text-slate-300 group-hover:text-brand-300"></i>
                        <span class="text-xs font-mono font-medium text-slate-300">LinkedIn</span>
                    </div>
                    <i data-lucide="arrow-up-right" class="w-4 h-4 text-slate-500 group-hover:text-brand-300"></i>
                </a>

                <a href="https://medium.com/@vedantkarne15" target="_blank" rel="noopener" class="glass-panel p-3.5 rounded-xl flex items-center justify-between group glass-panel-hover transition-all">
                    <div class="flex items-center gap-2.5">
                        <i data-lucide="book-open" class="w-5 h-5 text-slate-300 group-hover:text-brand-300"></i>
                        <span class="text-xs font-mono font-medium text-slate-300">Medium</span>
                    </div>
                    <span class="text-xs font-mono text-amber-400">Articles</span>
                </a>

                <button onclick="copyToClipboard('vedantkarne15@gmail.com', 'Email copied to clipboard!')" class="glass-panel p-3.5 rounded-xl flex items-center justify-between group glass-panel-hover transition-all text-left">
                    <div class="flex items-center gap-2.5">
                        <i data-lucide="copy" class="w-5 h-5 text-slate-300 group-hover:text-brand-300"></i>
                        <span class="text-xs font-mono font-medium text-slate-300">Email</span>
                    </div>
                    <span class="text-[10px] font-mono text-emerald-400">Copy</span>
                </button>
            </div>
        </section>

        <section id="about" class="space-y-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-brand-900/40 pb-4">
                <div>
                    <div class="flex items-center gap-2 text-brand-400 font-mono text-xs font-bold uppercase tracking-wider mb-1">
                        <span>// 01</span>
                        <span>Core Identity</span>
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold text-slate-100">About &amp; Engineering Mindset</h2>
                </div>
                <p class="text-xs font-mono text-slate-400">B.Tech Computer Engineering (AI/ML) @ PICT Pune '28</p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="lg:col-span-2 glass-panel p-6 sm:p-8 rounded-2xl space-y-5 border-l-4 border-l-brand-500">
                    <h3 class="text-xl font-bold text-slate-100 flex items-center gap-2">
                        <i data-lucide="cpu" class="w-5 h-5 text-brand-400"></i>
                        Translating Research into Dependable Products
                    </h3>
                    <p class="text-slate-300 leading-relaxed text-sm sm:text-base">
                        I approach engineering with a <strong class="text-brand-300 font-medium">product mindset</strong>: understand the real constraint, design the system boundary, make the result observable, validate under realistic conditions, and ship an experience people can actually use.
                    </p>
                    <p class="text-slate-300 leading-relaxed text-sm sm:text-base">
                        Across finance, regulatory intelligence, credit risk, fraud detection, and algorithm visualization, my focus is translating research-grade ideas into <span class="text-slate-100 font-medium underline decoration-brand-500/50">reliable, auditable, and measurable software products</span>. I care deeply about retrieval quality, data leakage prevention, explainability, fairness, latency, and system design.
                    </p>
                    
                    <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 pt-2">
                        <div class="p-3 rounded-xl bg-brand-950/60 border border-brand-900/60">
                            <div class="text-xs text-slate-400 font-mono">Current GPA</div>
                            <div class="text-lg font-bold text-brand-300 font-mono">9.56 / 10.0</div>
                        </div>
                        <div class="p-3 rounded-xl bg-brand-950/60 border border-brand-900/60">
                            <div class="text-xs text-slate-400 font-mono">Hackathon Ranking</div>
                            <div class="text-lg font-bold text-amber-300 font-mono">1st Place Winner</div>
                        </div>
                        <div class="p-3 rounded-xl bg-brand-950/60 border border-brand-900/60 col-span-2 sm:col-span-1">
                            <div class="text-xs text-slate-400 font-mono">NPTEL Rank</div>
                            <div class="text-lg font-bold text-emerald-300 font-mono">Gold (Top 2%)</div>
                        </div>
                    </div>
                </div>

                <div class="glass-panel p-6 rounded-2xl flex flex-col justify-between space-y-6 bg-gradient-to-br from-cardBg to-brand-950/80">
                    <div class="space-y-4">
                        <div class="flex items-center gap-2 text-emerald-400 text-xs font-mono font-bold uppercase tracking-wider">
                            <i data-lucide="compass" class="w-4 h-4"></i>
                            Open To Opportunities
                        </div>
                        <h4 class="text-lg font-bold text-slate-100">High-Impact Roles &amp; Collaborations</h4>
                        <ul class="space-y-2.5 text-xs text-slate-300 font-mono">
                            <li class="flex items-start gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-brand-400 shrink-0 mt-0.5"></i>
                                <span>Software &amp; AI/ML Engineering Internships</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-brand-400 shrink-0 mt-0.5"></i>
                                <span>Backend &amp; Applied AI Infrastructure</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-brand-400 shrink-0 mt-0.5"></i>
                                <span>Open-Source RAG &amp; Developer Tooling</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <i data-lucide="check-circle-2" class="w-4 h-4 text-brand-400 shrink-0 mt-0.5"></i>
                                <span>Hackathons &amp; High-Impact Product Teams</span>
                            </li>
                        </ul>
                    </div>

                    <div class="p-3 rounded-xl bg-brand-900/30 border border-brand-500/20 text-center">
                        <a href="mailto:vedantkarne15@gmail.com" class="text-xs font-mono text-brand-300 hover:text-white transition-colors flex items-center justify-center gap-1.5">
                            <i data-lucide="send" class="w-3.5 h-3.5"></i> vedantkarne15@gmail.com
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <section id="expertise" class="space-y-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-brand-900/40 pb-4">
                <div>
                    <div class="flex items-center gap-2 text-brand-400 font-mono text-xs font-bold uppercase tracking-wider mb-1">
                        <span>// 02</span>
                        <span>Technical Capabilities</span>
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold text-slate-100">Tech Stack &amp; AI/ML Expertise</h2>
                </div>
            </div>

            <!-- Languages & Tools Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="glass-panel p-5 rounded-xl space-y-3">
                    <span class="text-xs font-mono text-brand-400 font-bold uppercase block">Languages</span>
                    <div class="flex flex-wrap gap-2 text-xs font-mono text-slate-200">
                        <span class="px-2.5 py-1 rounded bg-brand-950 border border-brand-800">Python</span>
                        <span class="px-2.5 py-1 rounded bg-brand-950 border border-brand-800">C++</span>
                        <span class="px-2.5 py-1 rounded bg-brand-950 border border-brand-800">C</span>
                        <span class="px-2.5 py-1 rounded bg-brand-950 border border-brand-800">Java</span>
                        <span class="px-2.5 py-1 rounded bg-brand-950 border border-brand-800">JavaScript</span>
                        <span class="px-2.5 py-1 rounded bg-brand-950 border border-brand-800">TypeScript</span>
                    </div>
                </div>

                <div class="glass-panel p-5 rounded-xl space-y-3">
                    <span class="text-xs font-mono text-purple-400 font-bold uppercase block">Frontend &amp; Desktop</span>
                    <div class="flex flex-wrap gap-2 text-xs font-mono text-slate-200">
                        <span class="px-2.5 py-1 rounded bg-purple-950 border border-purple-800">React</span>
                        <span class="px-2.5 py-1 rounded bg-purple-950 border border-purple-800">Next.js</span>
                        <span class="px-2.5 py-1 rounded bg-purple-950 border border-purple-800">Tailwind CSS</span>
                        <span class="px-2.5 py-1 rounded bg-purple-950 border border-purple-800">Electron</span>
                        <span class="px-2.5 py-1 rounded bg-purple-950 border border-purple-800">HTML5/CSS3</span>
                    </div>
                </div>

                <div class="glass-panel p-5 rounded-xl space-y-3">
                    <span class="text-xs font-mono text-emerald-400 font-bold uppercase block">Backend &amp; Databases</span>
                    <div class="flex flex-wrap gap-2 text-xs font-mono text-slate-200">
                        <span class="px-2.5 py-1 rounded bg-emerald-950 border border-emerald-800">FastAPI</span>
                        <span class="px-2.5 py-1 rounded bg-emerald-950 border border-emerald-800">Spring Boot</span>
                        <span class="px-2.5 py-1 rounded bg-emerald-950 border border-emerald-800">Node.js</span>
                        <span class="px-2.5 py-1 rounded bg-emerald-950 border border-emerald-800">Express</span>
                        <span class="px-2.5 py-1 rounded bg-emerald-950 border border-emerald-800">PostgreSQL</span>
                        <span class="px-2.5 py-1 rounded bg-emerald-950 border border-emerald-800">SQLite</span>
                        <span class="px-2.5 py-1 rounded bg-emerald-950 border border-emerald-800">MongoDB</span>
                    </div>
                </div>

                <div class="glass-panel p-5 rounded-xl space-y-3">
                    <span class="text-xs font-mono text-amber-400 font-bold uppercase block">DevOps &amp; Infrastructure</span>
                    <div class="flex flex-wrap gap-2 text-xs font-mono text-slate-200">
                        <span class="px-2.5 py-1 rounded bg-amber-950 border border-amber-800">Docker</span>
                        <span class="px-2.5 py-1 rounded bg-amber-950 border border-amber-800">Git / GitHub</span>
                        <span class="px-2.5 py-1 rounded bg-amber-950 border border-amber-800">GitHub Actions</span>
                        <span class="px-2.5 py-1 rounded bg-amber-950 border border-amber-800">Linux</span>
                        <span class="px-2.5 py-1 rounded bg-amber-950 border border-amber-800">Postman</span>
                    </div>
                </div>
            </div>

            <!-- Detailed AI/ML Expertise Table -->
            <div class="glass-panel rounded-2xl overflow-hidden border border-brand-900/60">
                <div class="p-4 bg-brand-950/80 border-b border-brand-900/60 font-mono text-xs text-slate-300 font-bold flex items-center gap-2">
                    <i data-lucide="sparkles" class="w-4 h-4 text-brand-400"></i> AI/ML Specialization Breakdown
                </div>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs font-sans">
                        <thead class="bg-brand-950/40 font-mono text-slate-400 border-b border-brand-900/40">
                            <tr>
                                <th class="p-3.5">Domain</th>
                                <th class="p-3.5">Level</th>
                                <th class="p-3.5">Implementation Details</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-brand-900/30 text-slate-300">
                            <tr class="hover:bg-brand-900/10 transition-colors">
                                <td class="p-3.5 font-semibold text-brand-300 font-mono">Agentic AI &amp; RAG</td>
                                <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-brand-900 text-brand-300 font-mono text-[10px]">Advanced</span></td>
                                <td class="p-3.5">LangGraph, LangChain, multi-agent routing workflows, Human-in-the-Loop (HITL), structured outputs, execution traces.</td>
                            </tr>
                            <tr class="hover:bg-brand-900/10 transition-colors">
                                <td class="p-3.5 font-semibold text-purple-300 font-mono">Retrieval Engineering</td>
                                <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-purple-900 text-purple-300 font-mono text-[10px]">Advanced</span></td>
                                <td class="p-3.5">ChromaDB dense search, BM25 lexical search, Hybrid Reciprocal Rank Fusion (RRF), Cross-Encoder reranking, RAPTOR trees, BGE-M3 embeddings.</td>
                            </tr>
                            <tr class="hover:bg-brand-900/10 transition-colors">
                                <td class="p-3.5 font-semibold text-emerald-300 font-mono">Machine Learning</td>
                                <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-emerald-900 text-emerald-300 font-mono text-[10px]">Advanced</span></td>
                                <td class="p-3.5">XGBoost, LightGBM, CatBoost, TabNet, ensemble soft-voting, chronological validation splits, temporal feature engineering.</td>
                            </tr>
                            <tr class="hover:bg-brand-900/10 transition-colors">
                                <td class="p-3.5 font-semibold text-amber-300 font-mono">Model Optimization</td>
                                <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-amber-900 text-amber-300 font-mono text-[10px]">Advanced</span></td>
                                <td class="p-3.5">Bayesian optimization with Optuna, decision threshold calibration, error analysis, temporal data leakage detection and mitigation.</td>
                            </tr>
                            <tr class="hover:bg-brand-900/10 transition-colors">
                                <td class="p-3.5 font-semibold text-cyan-300 font-mono">Explainable &amp; Fair AI</td>
                                <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-cyan-900 text-cyan-300 font-mono text-[10px]">Advanced</span></td>
                                <td class="p-3.5">SHAP feature attribution, demographic group fairness analysis, auditable decision logic, citation-grounded response generation.</td>
                            </tr>
                            <tr class="hover:bg-brand-900/10 transition-colors">
                                <td class="p-3.5 font-semibold text-indigo-300 font-mono">Document Intelligence</td>
                                <td class="p-3.5"><span class="px-2 py-0.5 rounded bg-indigo-900 text-indigo-300 font-mono text-[10px]">Proficient</span></td>
                                <td class="p-3.5">PyMuPDF, Docling, Tesseract OCR fallback, PDF structure routing, metadata-aware chunking, hierarchical document tree indexing.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <section id="projects" class="space-y-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-brand-900/40 pb-4">
                <div>
                    <div class="flex items-center gap-2 text-brand-400 font-mono text-xs font-bold uppercase tracking-wider mb-1">
                        <span>// 03</span>
                        <span>Engineering Portfolio</span>
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold text-slate-100">Featured Systems &amp; Projects</h2>
                </div>
                <p class="text-xs font-mono text-slate-400">Deployed platforms, hackathon winners, &amp; research systems</p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">

                <!-- Project 1: AURA -->
                <div class="glass-panel rounded-2xl p-6 sm:p-8 space-y-6 flex flex-col justify-between glass-panel-hover transition-all border-l-4 border-l-brand-500">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between flex-wrap gap-2">
                            <span class="px-3 py-1 rounded-full bg-brand-950 text-brand-300 border border-brand-700/50 text-xs font-mono font-bold flex items-center gap-1.5">
                                <i data-lucide="cpu" class="w-3.5 h-3.5 text-brand-400"></i> Financial RAG Platform
                            </span>
                            <span class="text-xs font-mono text-emerald-400 flex items-center gap-1">
                                <i data-lucide="check-circle" class="w-3.5 h-3.5"></i> Citation Traceable
                            </span>
                        </div>

                        <div>
                            <h3 class="text-2xl font-bold text-slate-100">
                                AURA — Agentic Financial Intelligence
                            </h3>
                            <p class="text-xs font-mono text-brand-400 mt-1">
                                Tri-Store Retrieval (SQLite KPI + ChromaDB Dense + BM25 Lexical)
                            </p>
                        </div>

                        <p class="text-slate-300 text-sm leading-relaxed">
                            Multi-company financial intelligence platform transforming earnings reports into source-grounded analysis and investment briefings. Built with a tri-store architecture preventing entity starvation, orchestrated via LangGraph DAGs with live React Flow execution traces.
                        </p>

                        <div class="grid grid-cols-2 gap-2 text-xs font-mono pt-2">
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Retrieval Stack</span>
                                <span class="text-brand-300 font-bold">Hybrid RRF + Cross-Encoder</span>
                            </div>
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Interfaces</span>
                                <span class="text-purple-300 font-bold">FastAPI + React Flow + SSE</span>
                            </div>
                        </div>

                        <div class="flex flex-wrap gap-2 pt-1">
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">LangGraph</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">FastAPI</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">ChromaDB</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">SQLite</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">Docker</span>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-brand-900/40 flex items-center justify-between">
                        <a href="https://github.com/VedantKarne/AURA-Financial-Intelligence" target="_blank" rel="noopener" class="text-xs font-mono text-brand-300 hover:text-white flex items-center gap-1.5 transition-colors">
                            <i data-lucide="github" class="w-4 h-4"></i> VedantKarne/AURA-Financial-Intelligence
                        </a>
                        <span class="text-[11px] font-mono text-slate-500">NVDA · AAPL · MSFT</span>
                    </div>
                </div>

                <!-- Project 2: Nirmaan AI -->
                <div class="glass-panel rounded-2xl p-6 sm:p-8 space-y-6 flex flex-col justify-between glass-panel-hover transition-all border-l-4 border-l-purple-500">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between flex-wrap gap-2">
                            <span class="px-3 py-1 rounded-full bg-brand-950 text-purple-300 border border-purple-700/50 text-xs font-mono font-bold flex items-center gap-1.5">
                                <i data-lucide="landmark" class="w-3.5 h-3.5 text-purple-400"></i> National SEBI Hackathon PS-04
                            </span>
                            <span class="text-xs font-mono text-amber-400 flex items-center gap-1">
                                <i data-lucide="shield-check" class="w-3.5 h-3.5"></i> HITL Validated
                            </span>
                        </div>

                        <div>
                            <h3 class="text-2xl font-bold text-slate-100">
                                Nirmaan AI — Agentic DRHP Platform
                            </h3>
                            <p class="text-xs font-mono text-purple-400 mt-1">
                                Regulatory Compliance Drafting &amp; RAPTOR Hierarchical Trees
                            </p>
                        </div>

                        <p class="text-slate-300 text-sm leading-relaxed">
                            Regulatory intelligence platform for SME IPO offer-document preparation against SEBI ICDR guidelines, DRHPs, and MCA filings. Integrates adaptive PDF parsing, OCR fallback, RAPTOR hierarchical trees, and Human-in-the-Loop approval checkpoints.
                        </p>

                        <div class="grid grid-cols-2 gap-2 text-xs font-mono pt-2">
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Indexing Method</span>
                                <span class="text-purple-300 font-bold">RAPTOR Hierarchical Trees</span>
                            </div>
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Parsing Layer</span>
                                <span class="text-emerald-300 font-bold">Docling + PyMuPDF OCR</span>
                            </div>
                        </div>

                        <div class="flex flex-wrap gap-2 pt-1">
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">LangGraph</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">PostgreSQL</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">Pydantic</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">FastAPI</span>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-brand-900/40 flex items-center justify-between">
                        <a href="https://github.com/VedantKarne/SME-IPO-DRHP-Generator" target="_blank" rel="noopener" class="text-xs font-mono text-purple-300 hover:text-white flex items-center gap-1.5 transition-colors">
                            <i data-lucide="github" class="w-4 h-4"></i> VedantKarne/SME-IPO-DRHP-Generator
                        </a>
                        <span class="text-[11px] font-mono text-slate-500">SEBI Regulatory Corpus</span>
                    </div>
                </div>

                <!-- Project 3: CredX -->
                <div class="glass-panel rounded-2xl p-6 sm:p-8 space-y-6 flex flex-col justify-between glass-panel-hover transition-all border-l-4 border-l-amber-500">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between flex-wrap gap-2">
                            <span class="px-3 py-1 rounded-full bg-brand-950 text-amber-300 border border-amber-700/50 text-xs font-mono font-bold flex items-center gap-1.5">
                                <i data-lucide="trophy" class="w-3.5 h-3.5 text-amber-400"></i> 1st Place Winner — ALCISTA '25
                            </span>
                            <span class="text-xs font-mono text-emerald-400 font-bold">ROC-AUC: 93.54%</span>
                        </div>

                        <div>
                            <h3 class="text-2xl font-bold text-slate-100">
                                CredX — Fair Credit Scoring Platform
                            </h3>
                            <p class="text-xs font-mono text-amber-400 mt-1">
                                Demographic Fairness-Aware Credit Risk Modeling (&lt; 2s Inference)
                            </p>
                        </div>

                        <p class="text-slate-300 text-sm leading-relaxed">
                            Fairness-constrained credit risk system built for ALCISTA HackTheBank (Team MoneyHeist). Boosted ROC-AUC from 68% to 93.54% by fixing data leakage, tuning feature ensembles, and enforcing fairness constraints across gender and region.
                        </p>

                        <div class="grid grid-cols-2 gap-2 text-xs font-mono pt-2">
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Validation Strategy</span>
                                <span class="text-amber-300 font-bold">Chronological Splits</span>
                            </div>
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Response Latency</span>
                                <span class="text-emerald-300 font-bold">&lt; 2.0s Real-time</span>
                            </div>
                        </div>

                        <div class="flex flex-wrap gap-2 pt-1">
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">XGBoost</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">Fairness ML</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">Python</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">FastAPI</span>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-brand-900/40 flex items-center justify-between">
                        <a href="https://medium.com/@vedantkarne15/-704f3c7e7549" target="_blank" rel="noopener" class="text-xs font-mono text-amber-300 hover:text-white flex items-center gap-1.5 transition-colors">
                            <i data-lucide="book-open" class="w-4 h-4"></i> Read Case Study
                        </a>
                        <span class="text-[11px] font-mono text-slate-500">Seniors Category Champions</span>
                    </div>
                </div>

                <!-- Project 4: Sentinel AI -->
                <div class="glass-panel rounded-2xl p-6 sm:p-8 space-y-6 flex flex-col justify-between glass-panel-hover transition-all border-l-4 border-l-cyan-500">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between flex-wrap gap-2">
                            <span class="px-3 py-1 rounded-full bg-brand-950 text-cyan-300 border border-cyan-700/50 text-xs font-mono font-bold flex items-center gap-1.5">
                                <i data-lucide="siren" class="w-3.5 h-3.5 text-cyan-400"></i> Ignisia AI Hackathon (Top 77/600)
                            </span>
                            <span class="text-xs font-mono text-cyan-300">18 Pune Hospitals Routed</span>
                        </div>

                        <div>
                            <h3 class="text-2xl font-bold text-slate-100">
                                Sentinel AI — Emergency Triage &amp; Routing
                            </h3>
                            <p class="text-xs font-mono text-cyan-400 mt-1">
                                Golden-Hour Triage Ensemble + Real-Road Dispatch Routing
                            </p>
                        </div>

                        <p class="text-slate-300 text-sm leading-relaxed">
                            Golden-hour emergency platform combining an 8-class diagnosis ensemble (XGBoost/LightGBM) with capability-aware ambulance routing across 18 Pune hospitals using MapLibre GL, WebSockets, Three.js, and OSRM.
                        </p>

                        <div class="grid grid-cols-2 gap-2 text-xs font-mono pt-2">
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Routing Engine</span>
                                <span class="text-cyan-300 font-bold">OSRM + Real-road Routing</span>
                            </div>
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Dispatch Sync</span>
                                <span class="text-purple-300 font-bold">Live WebSockets</span>
                            </div>
                        </div>

                        <div class="flex flex-wrap gap-2 pt-1">
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">React</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">FastAPI</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">MapLibre GL</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">Three.js</span>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-brand-900/40 flex items-center justify-between">
                        <a href="https://github.com/AkshatPatil101/Eternum_HC03" target="_blank" rel="noopener" class="text-xs font-mono text-cyan-300 hover:text-white flex items-center gap-1.5 transition-colors">
                            <i data-lucide="github" class="w-4 h-4"></i> AkshatPatil101/Eternum_HC03
                        </a>
                        <span class="text-[11px] font-mono text-slate-500">24hr National Hackathon</span>
                    </div>
                </div>

                <!-- Project 5: Fraud Guard -->
                <div class="glass-panel rounded-2xl p-6 sm:p-8 space-y-6 flex flex-col justify-between glass-panel-hover transition-all border-l-4 border-l-rose-500">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between flex-wrap gap-2">
                            <span class="px-3 py-1 rounded-full bg-brand-950 text-rose-300 border border-rose-700/50 text-xs font-mono font-bold flex items-center gap-1.5">
                                <i data-lucide="shield-alert" class="w-3.5 h-3.5 text-rose-400"></i> TechFiesta 2026
                            </span>
                            <span class="text-xs font-mono text-rose-400">235 Features • 22.5k Test Set</span>
                        </div>

                        <div>
                            <h3 class="text-2xl font-bold text-slate-100">
                                Fraud Guard — Cascaded Fraud &amp; Risk Pipeline
                            </h3>
                            <p class="text-xs font-mono text-rose-400 mt-1">
                                30 Rules / 9 Tiers + Optuna Bayesian Gray-Zone Ensemble
                            </p>

                        </div>

                        <p class="text-slate-300 text-sm leading-relaxed">
                            Two-stage risk management system resolving clear cases via a 30-rule engine and channeling ambiguous gray-zone transactions into a Bayesian Neural Network + XGBoost/LightGBM/CatBoost ensemble (89.0% leakage-corrected ROC-AUC).
                        </p>

                        <div class="grid grid-cols-2 gap-2 text-xs font-mono pt-2">
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Rule Controls</span>
                                <span class="text-rose-300 font-bold">30 Rules / 9 Tiers</span>
                            </div>
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Tuning Engine</span>
                                <span class="text-purple-300 font-bold">Optuna Bayesian Optimization</span>
                            </div>
                        </div>

                        <div class="flex flex-wrap gap-2 pt-1">
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">XGBoost</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">CatBoost</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">Optuna</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">FastAPI</span>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-brand-900/40 flex items-center justify-between">
                        <a href="https://github.com/AkshatPatil101/Fraud-Guard" target="_blank" rel="noopener" class="text-xs font-mono text-rose-300 hover:text-white flex items-center gap-1.5 transition-colors">
                            <i data-lucide="github" class="w-4 h-4"></i> AkshatPatil101/Fraud-Guard
                        </a>
                        <span class="text-[11px] font-mono text-slate-500">Team Anomaly.exe</span>
                    </div>
                </div>

                <!-- Project 6: RouteRush Island -->
                <div class="glass-panel rounded-2xl p-6 sm:p-8 space-y-6 flex flex-col justify-between glass-panel-hover transition-all border-l-4 border-l-emerald-500">
                    <div class="space-y-4">
                        <div class="flex items-center justify-between flex-wrap gap-2">
                            <span class="px-3 py-1 rounded-full bg-brand-950 text-emerald-300 border border-emerald-700/50 text-xs font-mono font-bold flex items-center gap-1.5">
                                <i data-lucide="gamepad-2" class="w-3.5 h-3.5 text-emerald-400"></i> Desktop Product &amp; Simulation
                            </span>
                            <span class="text-xs font-mono text-emerald-400">Electron Desktop App</span>
                        </div>

                        <div>
                            <h3 class="text-2xl font-bold text-slate-100">
                                RouteRush Island — Pathfinding Simulator
                            </h3>
                            <p class="text-xs font-mono text-emerald-400 mt-1">
                                Interactive Shortest-Path Graph Algorithm Visualizer
                            </p>
                        </div>

                        <p class="text-slate-300 text-sm leading-relaxed">
                            Cross-platform desktop application converting shortest-path algorithms (Dijkstra, Bidirectional Dijkstra, Bellman-Ford, BMSSP) into an interactive tropical-island simulation under traffic, dynamic rerouting, and obstacle obstacles.
                        </p>

                        <div class="grid grid-cols-2 gap-2 text-xs font-mono pt-2">
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Algorithms</span>
                                <span class="text-emerald-300 font-bold">Dijkstra, Bellman-Ford, BMSSP</span>
                            </div>
                            <div class="p-2 rounded bg-brand-950/80 border border-brand-900">
                                <span class="text-slate-400 block">Packaging</span>
                                <span class="text-brand-300 font-bold">Electron Cross-Platform</span>
                            </div>
                        </div>

                        <div class="flex flex-wrap gap-2 pt-1">
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">Electron</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">JavaScript</span>
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-slate-300 text-[11px] font-mono">Graph Algorithms</span>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-brand-900/40 flex items-center justify-between">
                        <a href="https://github.com/VedantKarne/routerush-island" target="_blank" rel="noopener" class="text-xs font-mono text-emerald-300 hover:text-white flex items-center gap-1.5 transition-colors">
                            <i data-lucide="github" class="w-4 h-4"></i> VedantKarne/routerush-island
                        </a>
                        <span class="text-[11px] font-mono text-slate-500">Windows · macOS · Linux</span>
                    </div>
                </div>

            </div>
        </section>

        <section id="architecture" class="space-y-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-brand-900/40 pb-4">
                <div>
                    <div class="flex items-center gap-2 text-brand-400 font-mono text-xs font-bold uppercase tracking-wider mb-1">
                        <span>// 04</span>
                        <span>Interactive Pipeline Visualizer</span>
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold text-slate-100">Multi-Agent Tri-Store RAG Architecture</h2>
                </div>
                <p class="text-xs font-mono text-slate-400">Click any pipeline stage to inspect technical execution details</p>
            </div>

            <div class="glass-panel p-6 sm:p-8 rounded-2xl relative overflow-hidden space-y-6">
                <div class="flex flex-wrap items-center justify-between gap-3 text-xs font-mono text-slate-400 pb-4 border-b border-brand-900/40">
                    <span class="flex items-center gap-1.5 text-brand-300">
                        <i data-lucide="layers" class="w-4 h-4"></i> AURA &amp; Nirmaan AI Directed Acyclic Graph (DAG)
                    </span>
                    <span class="bg-brand-950 px-2.5 py-1 rounded text-brand-400 border border-brand-800/40">
                        LangGraph Directed Flow
                    </span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-5 gap-4 relative">
                    <button onclick="inspectNode('ingestion')" id="node-ingestion" class="p-4 rounded-xl glass-panel text-left transition-all hover:scale-[1.02] border-brand-500/40 bg-brand-900/20 active-node">
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-[10px] font-mono text-brand-400 font-bold uppercase">Stage 01</span>
                            <i data-lucide="file-text" class="w-4 h-4 text-brand-300"></i>
                        </div>
                        <h4 class="font-bold text-slate-100 text-sm mb-1">Adaptive Ingestion</h4>
                        <p class="text-[11px] text-slate-400 font-mono">PyMuPDF / Docling + OCR Fallback</p>
                    </button>

                    <button onclick="inspectNode('tristore')" id="node-tristore" class="p-4 rounded-xl glass-panel text-left transition-all hover:scale-[1.02] border-brand-900/60">
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-[10px] font-mono text-brand-400 font-bold uppercase">Stage 02</span>
                            <i data-lucide="database" class="w-4 h-4 text-purple-400"></i>
                        </div>
                        <h4 class="font-bold text-slate-100 text-sm mb-1">Tri-Store Indexing</h4>
                        <p class="text-[11px] text-slate-400 font-mono">ChromaDB + BM25 + PostgreSQL/SQLite</p>
                    </button>

                    <button onclick="inspectNode('fusion')" id="node-fusion" class="p-4 rounded-xl glass-panel text-left transition-all hover:scale-[1.02] border-brand-900/60">
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-[10px] font-mono text-brand-400 font-bold uppercase">Stage 03</span>
                            <i data-lucide="git-merge" class="w-4 h-4 text-emerald-400"></i>
                        </div>
                        <h4 class="font-bold text-slate-100 text-sm mb-1">Hybrid Retrieval &amp; RRF</h4>
                        <p class="text-[11px] text-slate-400 font-mono">Reciprocal Rank Fusion + BGE-M3</p>
                    </button>

                    <button onclick="inspectNode('rerank')" id="node-rerank" class="p-4 rounded-xl glass-panel text-left transition-all hover:scale-[1.02] border-brand-900/60">
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-[10px] font-mono text-brand-400 font-bold uppercase">Stage 04</span>
                            <i data-lucide="sliders" class="w-4 h-4 text-amber-400"></i>
                        </div>
                        <h4 class="font-bold text-slate-100 text-sm mb-1">Cross-Encoder Rerank</h4>
                        <p class="text-[11px] text-slate-400 font-mono">RAPTOR Trees &amp; Context Pruning</p>
                    </button>

                    <button onclick="inspectNode('audit')" id="node-audit" class="p-4 rounded-xl glass-panel text-left transition-all hover:scale-[1.02] border-brand-900/60">
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-[10px] font-mono text-brand-400 font-bold uppercase">Stage 05</span>
                            <i data-lucide="shield-check" class="w-4 h-4 text-cyan-400"></i>
                        </div>
                        <h4 class="font-bold text-slate-100 text-sm mb-1">Grounded Synthesis</h4>
                        <p class="text-[11px] text-slate-400 font-mono">Pydantic Schema + Citation Trace</p>
                    </button>
                </div>

                <div id="inspector-card" class="p-5 rounded-xl bg-brand-950/80 border border-brand-500/30 space-y-3 transition-all"></div>
            </div>
        </section>

        <section id="sandbox" class="space-y-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-brand-900/40 pb-4">
                <div>
                    <div class="flex items-center gap-2 text-brand-400 font-mono text-xs font-bold uppercase tracking-wider mb-1">
                        <span>// 05</span>
                        <span>Live Pipeline Simulation</span>
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold text-slate-100">Agentic RAG Execution Sandbox</h2>
                </div>
                <p class="text-xs font-mono text-slate-400">Simulate multi-agent reasoning, search fusion, and citation tracing</p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                <div class="lg:col-span-5 glass-panel p-6 rounded-2xl space-y-5 flex flex-col justify-between">
                    <div class="space-y-4">
                        <h3 class="text-lg font-bold text-slate-100 flex items-center gap-2">
                            <i data-lucide="terminal" class="w-5 h-5 text-brand-400"></i>
                            Select Query Scenario
                        </h3>

                        <div class="space-y-2">
                            <button onclick="runRagSandbox('finance')" class="w-full p-3 rounded-xl bg-brand-900/30 hover:bg-brand-800/40 border border-brand-700/40 text-left transition-all flex items-start justify-between group">
                                <div>
                                    <div class="text-xs font-bold text-slate-200 group-hover:text-brand-300">AURA Financial Analysis</div>
                                    <div class="text-[11px] font-mono text-slate-400 mt-0.5">"Compare NVIDIA Q3 operating margins vs Apple with SEC 10-K citations"</div>
                                </div>
                                <span class="px-2 py-0.5 rounded bg-brand-950 text-[10px] font-mono text-brand-400 border border-brand-800">AURA</span>
                            </button>

                            <button onclick="runRagSandbox('sebi')" class="w-full p-3 rounded-xl bg-brand-900/30 hover:bg-brand-800/40 border border-brand-700/40 text-left transition-all flex items-start justify-between group">
                                <div>
                                    <div class="text-xs font-bold text-slate-200 group-hover:text-brand-300">Nirmaan SEBI DRHP Compliance</div>
                                    <div class="text-[11px] font-mono text-slate-400 mt-0.5">"Verify promoter lock-in period compliance against SEBI ICDR guidelines"</div>
                                </div>
                                <span class="px-2 py-0.5 rounded bg-brand-950 text-[10px] font-mono text-purple-400 border border-purple-800">Nirmaan</span>
                            </button>

                            <button onclick="runRagSandbox('fraud')" class="w-full p-3 rounded-xl bg-brand-900/30 hover:bg-brand-800/40 border border-brand-700/40 text-left transition-all flex items-start justify-between group">
                                <div>
                                    <div class="text-xs font-bold text-slate-200 group-hover:text-brand-300">Fraud Guard Gray-Zone Audit</div>
                                    <div class="text-[11px] font-mono text-slate-400 mt-0.5">"Evaluate gray-zone transaction #8492 with SHAP feature attributions"</div>
                                </div>
                                <span class="px-2 py-0.5 rounded bg-brand-950 text-[10px] font-mono text-rose-400 border border-rose-800">Fraud Guard</span>
                            </button>
                        </div>
                    </div>

                    <div class="space-y-3 pt-4 border-t border-brand-900/40">
                        <div class="flex justify-between items-center text-xs font-mono">
                            <span class="text-slate-300">Hybrid Search Weight (Dense / Lexical):</span>
                            <span id="alpha-val" class="text-brand-400 font-bold">0.65 Dense / 0.35 Lexical</span>
                        </div>
                        <input type="range" min="0" max="1" step="0.05" value="0.65" id="alpha-slider" oninput="updateAlphaVal(this.value)" class="w-full accent-brand-500 bg-brand-950 h-2 rounded-lg cursor-pointer">
                    </div>
                </div>

                <div class="lg:col-span-7 glass-panel p-6 rounded-2xl font-mono text-xs space-y-4 flex flex-col justify-between bg-darkBg/90 border-brand-500/30 min-h-[380px]">
                    <div class="flex items-center justify-between border-b border-brand-900/60 pb-3">
                        <div class="flex items-center gap-2">
                            <span class="w-3 h-3 rounded-full bg-red-500/80"></span>
                            <span class="w-3 h-3 rounded-full bg-amber-500/80"></span>
                            <span class="w-3 h-3 rounded-full bg-emerald-500/80"></span>
                            <span class="text-slate-400 text-[11px] ml-2">langgraph-engine // stdout_stream</span>
                        </div>
                        <span id="sandbox-status" class="px-2 py-0.5 rounded bg-brand-950 text-brand-300 border border-brand-800 text-[10px]">
                            READY
                        </span>
                    </div>

                    <div id="sandbox-console" class="space-y-2 text-slate-300 overflow-y-auto max-h-[280px] pr-2 leading-relaxed">
                        <p class="text-slate-500 italic">// Click a scenario on the left to trigger the execution trace...</p>
                    </div>

                    <div class="pt-3 border-t border-brand-900/60 flex items-center justify-between text-[11px] text-slate-400">
                        <span id="metric-latency">Latency: -- ms</span>
                        <span id="metric-precision">Recall@k: --</span>
                        <span id="metric-citations">Grounded Citations: --</span>
                    </div>
                </div>
            </div>
        </section>

        <section id="experience" class="space-y-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-brand-900/40 pb-4">
                <div>
                    <div class="flex items-center gap-2 text-brand-400 font-mono text-xs font-bold uppercase tracking-wider mb-1">
                        <span>// 06</span>
                        <span>Leadership &amp; Roles</span>
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold text-slate-100">Experience &amp; Community Engagement</h2>
                </div>
            </div>

            <div class="relative border-l-2 border-brand-900/80 ml-3 md:ml-6 space-y-8 pl-6 md:pl-10">
                <div class="relative group">
                    <span class="absolute -left-[31px] md:-left-[47px] top-1 w-4 h-4 rounded-full bg-brand-500 border-4 border-darkBg group-hover:scale-125 transition-transform"></span>
                    <div class="glass-panel p-6 rounded-2xl space-y-3 glass-panel-hover transition-all">
                        <div class="flex items-center justify-between flex-wrap gap-2">
                            <h3 class="text-lg font-bold text-slate-100">Student Member — PICT CSI Student Branch</h3>
                            <span class="text-xs font-mono px-2.5 py-1 rounded bg-brand-950 text-brand-300 border border-brand-800">October 2024 – Present</span>
                        </div>
                        <div class="text-xs font-mono text-brand-400">Pune Institute of Computer Technology</div>
                        <p class="text-slate-300 text-sm leading-relaxed">
                            Co-organize technical workshops and student outreach initiatives across technical and operational teams to deliver engaging computing events and foster knowledge sharing.
                        </p>
                    </div>
                </div>

                <div class="relative group">
                    <span class="absolute -left-[31px] md:-left-[47px] top-1 w-4 h-4 rounded-full bg-purple-500 border-4 border-darkBg group-hover:scale-125 transition-transform"></span>
                    <div class="glass-panel p-6 rounded-2xl space-y-3 glass-panel-hover transition-all">
                        <div class="flex items-center justify-between flex-wrap gap-2">
                            <h3 class="text-lg font-bold text-slate-100">Class Representative — First Year Computer Engineering</h3>
                            <span class="text-xs font-mono px-2.5 py-1 rounded bg-brand-950 text-purple-300 border border-purple-800">October 2024 – February 2025</span>
                        </div>
                        <div class="text-xs font-mono text-purple-400">Pune Institute of Computer Technology</div>
                        <p class="text-slate-300 text-sm leading-relaxed">
                            Coordinated academic communication between students, faculty, and the computer engineering department. Consolidated feedback and kept the cohort aligned on academic milestones.
                        </p>
                    </div>
                </div>

                <div class="relative group">
                    <span class="absolute -left-[31px] md:-left-[47px] top-1 w-4 h-4 rounded-full bg-amber-500 border-4 border-darkBg group-hover:scale-125 transition-transform"></span>
                    <div class="glass-panel p-6 rounded-2xl space-y-3 glass-panel-hover transition-all">
                        <div class="flex items-center justify-between flex-wrap gap-2">
                            <h3 class="text-lg font-bold text-slate-100">Team Lead &amp; ML Engineer — Competition Teams</h3>
                            <span class="text-xs font-mono px-2.5 py-1 rounded bg-brand-950 text-amber-300 border border-amber-800">2024 – Present</span>
                        </div>
                        <div class="text-xs font-mono text-amber-400">Team MoneyHeist (CredX) • Team Anomaly.exe (Fraud Guard) • Eternum (Sentinel AI)</div>
                        <p class="text-slate-300 text-sm leading-relaxed">
                            Led ML strategy and end-to-end architecture across national hackathons. Spearheaded leakage elimination, fairness optimization, real-time API integrations, and hybrid RAG system designs.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <section id="achievements" class="space-y-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-brand-900/40 pb-4">
                <div>
                    <div class="flex items-center gap-2 text-brand-400 font-mono text-xs font-bold uppercase tracking-wider mb-1">
                        <span>// 07</span>
                        <span>Honors &amp; Stats</span>
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold text-slate-100">Achievements, Credentials &amp; Profiles</h2>
                </div>
            </div>

            <!-- Honors Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div class="glass-panel p-6 rounded-2xl space-y-3 border-t-2 border-t-amber-400">
                    <div class="flex items-center justify-between text-amber-400">
                        <i data-lucide="trophy" class="w-6 h-6"></i>
                        <span class="text-xs font-mono text-amber-300 font-bold">1st Place Winner</span>
                    </div>
                    <h4 class="font-bold text-slate-100 text-base">ALCISTA '25 HackTheBank</h4>
                    <p class="text-xs text-slate-400 font-mono">Seniors Category Champion • Team MoneyHeist</p>
                    <p class="text-xs text-slate-300 pt-1">Led ML development for CredX, raising ROC-AUC from 68% to 93.54% with demographic fairness checks.</p>
                </div>

                <div class="glass-panel p-6 rounded-2xl space-y-3 border-t-2 border-t-brand-400">
                    <div class="flex items-center justify-between text-brand-400">
                        <i data-lucide="award" class="w-6 h-6"></i>
                        <span class="text-xs font-mono text-emerald-400 font-bold">Gold Medallist</span>
                    </div>
                    <h4 class="font-bold text-slate-100 text-base">NPTEL Algorithms Examination</h4>
                    <p class="text-xs text-slate-400 font-mono">Top 2% Nationally • Fundamental Algorithms</p>
                    <p class="text-xs text-slate-300 pt-1">Achieved Gold Medal standing in Design &amp; Analysis of Algorithms nationwide testing. Also scored 94% in Cyber Security.</p>
                </div>

                <div class="glass-panel p-6 rounded-2xl space-y-3 border-t-2 border-t-purple-400">
                    <div class="flex items-center justify-between text-purple-400">
                        <i data-lucide="star" class="w-6 h-6"></i>
                        <span class="text-xs font-mono text-purple-300 font-bold">Perfect 100% Score</span>
                    </div>
                    <h4 class="font-bold text-slate-100 text-base">Machine Learning Specialization</h4>
                    <p class="text-xs text-slate-400 font-mono">Andrew Ng • DeepLearning.AI / Coursera</p>
                    <p class="text-xs text-slate-300 pt-1">Achieved a perfect 100% score across all modules covering supervised learning, neural networks, and decision trees.</p>
                </div>

                <div class="glass-panel p-6 rounded-2xl space-y-3 border-t-2 border-t-indigo-400">
                    <div class="flex items-center justify-between text-indigo-400">
                        <i data-lucide="zap" class="w-6 h-6"></i>
                        <span class="text-xs font-mono text-indigo-300 font-bold">Top 77 / ~600 Teams</span>
                    </div>
                    <h4 class="font-bold text-slate-100 text-base">Ignisia National AI Hackathon</h4>
                    <p class="text-xs text-slate-400 font-mono">MIT World Peace University</p>
                    <p class="text-xs text-slate-300 pt-1">Built Sentinel AI — real-time emergency triage and 18-hospital dispatch routing platform in 24 hours.</p>
                </div>

                <div class="glass-panel p-6 rounded-2xl space-y-3 border-t-2 border-t-emerald-400">
                    <div class="flex items-center justify-between text-emerald-400">
                        <i data-lucide="code-2" class="w-6 h-6"></i>
                        <span class="text-xs font-mono text-emerald-300 font-bold">400+ LeetCode Solved</span>
                    </div>
                    <h4 class="font-bold text-slate-100 text-base">Competitive Programming</h4>
                    <p class="text-xs text-slate-400 font-mono">5★ C++ • 5★ Java • 4★ Python</p>
                    <p class="text-xs text-slate-300 pt-1">Solid DSA background across graph theory, dynamic programming, tree traversals, and algorithmic optimization.</p>
                </div>

                <div class="glass-panel p-6 rounded-2xl space-y-3 border-t-2 border-t-cyan-400">
                    <div class="flex items-center justify-between text-cyan-400">
                        <i data-lucide="target" class="w-6 h-6"></i>
                        <span class="text-xs font-mono text-cyan-300 font-bold">99.67 Percentile</span>
                    </div>
                    <h4 class="font-bold text-slate-100 text-base">Engineering Entrance Exams</h4>
                    <p class="text-xs text-slate-400 font-mono">MHT-CET: AIR 812 • JEE Main: 96.96%ile</p>
                    <p class="text-xs text-slate-300 pt-1">Demonstrated academic excellence in national and state-level engineering examinations.</p>
                </div>
            </div>

            <!-- Coding Profiles Bar -->
            <div class="glass-panel p-6 rounded-2xl space-y-4">
                <h4 class="text-sm font-bold font-mono text-slate-200 flex items-center gap-2">
                    <i data-lucide="terminal" class="w-4 h-4 text-brand-400"></i> Coding Profiles &amp; Verification Links
                </h4>
                <div class="flex flex-wrap gap-3">
                    <a href="https://leetcode.com/u/Vedant_Karne_2/" target="_blank" rel="noopener" class="px-4 py-2 rounded-xl bg-brand-950 border border-brand-800 hover:border-brand-500 transition-colors text-xs font-mono text-slate-200 flex items-center gap-2">
                        <i data-lucide="code" class="w-4 h-4 text-amber-400"></i> LeetCode Profile
                    </a>
                    <a href="https://www.hackerrank.com/" target="_blank" rel="noopener" class="px-4 py-2 rounded-xl bg-brand-950 border border-brand-800 hover:border-brand-500 transition-colors text-xs font-mono text-slate-200 flex items-center gap-2">
                        <i data-lucide="check-square" class="w-4 h-4 text-emerald-400"></i> HackerRank Profile
                    </a>
                    <a href="https://www.geeksforgeeks.org/" target="_blank" rel="noopener" class="px-4 py-2 rounded-xl bg-brand-950 border border-brand-800 hover:border-brand-500 transition-colors text-xs font-mono text-slate-200 flex items-center gap-2">
                        <i data-lucide="book" class="w-4 h-4 text-purple-400"></i> GeeksforGeeks Profile
                    </a>
                    <a href="https://github.com/VedantKarne" target="_blank" rel="noopener" class="px-4 py-2 rounded-xl bg-brand-950 border border-brand-800 hover:border-brand-500 transition-colors text-xs font-mono text-slate-200 flex items-center gap-2">
                        <i data-lucide="github" class="w-4 h-4 text-brand-400"></i> GitHub Repositories
                    </a>
                </div>
            </div>
        </section>

        <section id="contact" class="glass-panel p-8 sm:p-12 rounded-3xl text-center space-y-8 relative overflow-hidden bg-gradient-to-b from-cardBg to-brand-950/90 border border-brand-500/30">
            <div class="max-w-2xl mx-auto space-y-4">
                <span class="px-3 py-1 rounded-full bg-brand-900/60 text-brand-300 border border-brand-700/50 text-xs font-mono font-bold">
                    Let's Build Software Together
                </span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-100 tracking-tight">
                    Interested in <span class="gradient-text">intelligent software products</span>?
                </h2>
                <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
                    I am actively seeking Software Engineering and AI/ML Engineering internships, open-source collaborations, and high-impact project opportunities.
                </p>
            </div>

            <div class="flex flex-wrap items-center justify-center gap-4 pt-2">
                <button onclick="copyToClipboard('vedantkarne15@gmail.com', 'Copied vedantkarne15@gmail.com to clipboard!')" class="px-6 py-3.5 rounded-xl bg-brand-600 hover:bg-brand-500 text-white font-semibold text-sm transition-all shadow-xl shadow-brand-600/30 flex items-center gap-2 group">
                    <i data-lucide="copy" class="w-4 h-4 group-hover:scale-110 transition-transform"></i>
                    <span>Copy vedantkarne15@gmail.com</span>
                </button>
                <a href="https://www.linkedin.com/in/vedant-karne-31023b302/" target="_blank" rel="noopener" class="px-6 py-3.5 rounded-xl glass-panel hover:bg-brand-900/40 text-slate-200 font-semibold text-sm transition-all border border-brand-500/30 flex items-center gap-2">
                    <i data-lucide="linkedin" class="w-4 h-4 text-brand-400"></i>
                    <span>Connect on LinkedIn</span>
                </a>
            </div>

            <div class="pt-8 border-t border-brand-900/40 text-xs font-mono text-slate-500 flex flex-col sm:flex-row items-center justify-between gap-4">
                <span>© 2026 Vedant Karne • Built with HTML5, Tailwind CSS, Lucide &amp; JS</span>
                <span class="italic text-slate-400">"Architecture is the difference between a model in a notebook and a system in production."</span>
            </div>
        </section>

    </main>

    <script>
        lucide.createIcons();

        // 1. Dynamic Typing Effect
        const phrases = [
            "Engineering reliable AI systems from research to product",
            "Building agentic RAG, ML platforms and full-stack products",
            "Turning complex problems into measurable engineering impact"
        ];
        let phraseIdx = 0;
        let charIdx = 0;
        let isDeleting = false;
        const typingSpeed = 50;
        const typingElement = document.getElementById("typing-text");

        function typeLoop() {
            const currentPhrase = phrases[phraseIdx];
            if (isDeleting) {
                typingElement.textContent = currentPhrase.substring(0, charIdx - 1);
                charIdx--;
            } else {
                typingElement.textContent = currentPhrase.substring(0, charIdx + 1);
                charIdx++;
            }

            let delta = typingSpeed;
            if (isDeleting) delta /= 2;

            if (!isDeleting && charIdx === currentPhrase.length) {
                delta = 2200;
                isDeleting = true;
            } else if (isDeleting && charIdx === 0) {
                isDeleting = false;
                phraseIdx = (phraseIdx + 1) % phrases.length;
                delta = 400;
            }

            setTimeout(typeLoop, delta);
        }
        typeLoop();

        // 2. Interactive Pipeline Inspector Node Details
        const nodeDetails = {
            ingestion: {
                title: "Stage 01: Adaptive Document Ingestion & Routing",
                description: "Ingests raw financial filings, earnings transcripts, and SEBI regulatory documents using PyMuPDF and Docling with intelligent OCR fallback routing for scanned tables and diagrams.",
                tech: ["PyMuPDF", "Docling", "Tesseract OCR", "Metadata-Aware Chunking"],
                metric: "Zero layout breakdown on complex financial tables"
            },
            tristore: {
                title: "Stage 02: Tri-Store Multi-Index Architecture",
                description: "Maintains three distinct storage layers: SQLite/PostgreSQL for deterministic relational KPI lookups, ChromaDB for vector dense search, and BM25 for exact financial term precision.",
                tech: ["ChromaDB", "BM25 Index", "PostgreSQL", "SQLite"],
                metric: "Prevents entity starvation across financial earnings"
            },
            fusion: {
                title: "Stage 03: Hybrid Search & Reciprocal Rank Fusion (RRF)",
                description: "Fuses dense semantic similarity scores with BM25 lexical scores using Reciprocal Rank Fusion (RRF) with dynamic alpha weighting.",
                tech: ["RRF Algorithm", "BGE-M3 Embeddings", "Sentence-Transformers"],
                metric: "Recall@k improved by +28% over pure vector search"
            },
            rerank: {
                title: "Stage 04: RAPTOR & Cross-Encoder Reranking",
                description: "Scans candidates through a Cross-Encoder reranker backed by RAPTOR hierarchical tree summarization for multi-hop reasoning over long legal and financial texts.",
                tech: ["Cross-Encoder", "RAPTOR Trees", "Contextual Pruning"],
                metric: "Eliminates 92% of non-relevant context chunks"
            },
            audit: {
                title: "Stage 05: Citation Grounding & Pydantic Schema Output",
                description: "Supplies reranked context to LLM agents which enforce strict Pydantic JSON schema outputs with exact page, table, and section citation metadata.",
                tech: ["Pydantic", "LangGraph Nodes", "Citation Auditing"],
                metric: "0% hallucination on verified financial metrics"
            }
        };

        function inspectNode(nodeKey) {
            const data = nodeDetails[nodeKey];
            if (!data) return;

            document.querySelectorAll('#architecture button').forEach(btn => {
                btn.classList.remove('border-brand-500/40', 'bg-brand-900/20', 'active-node');
                btn.classList.add('border-brand-900/60');
            });
            const clickedBtn = document.getElementById(`node-${nodeKey}`);
            if (clickedBtn) {
                clickedBtn.classList.add('border-brand-500/40', 'bg-brand-900/20', 'active-node');
            }

            const card = document.getElementById("inspector-card");
            card.innerHTML = `
                <div class="flex items-center justify-between">
                    <h4 class="font-bold text-slate-100 text-sm">${data.title}</h4>
                    <span class="text-[10px] font-mono text-emerald-400 bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-800">${data.metric}</span>
                </div>
                <p class="text-xs text-slate-300 leading-relaxed font-sans">${data.description}</p>
                <div class="flex flex-wrap gap-2 pt-1">
                    ${data.tech.map(t => `<span class="px-2 py-0.5 rounded bg-brand-900/50 text-brand-300 text-[10px] font-mono border border-brand-800/40">${t}</span>`).join('')}
                </div>
            `;
            lucide.createIcons();
        }
        inspectNode('ingestion');

        // 3. Sandbox Simulation Engine
        const scenarios = {
            finance: [
                { text: "[AGENT_ROUTER] Routing query to Financial Intelligence LangGraph Node...", delay: 250 },
                { text: "[TRI_STORE_SEARCH] Querying SQLite KPI Store + ChromaDB Dense + BM25 Lexical...", delay: 650 },
                { text: "[HYBRID_RRF] Reciprocal Rank Fusion synthesized top 5 reranked context candidates.", delay: 1100 },
                { text: "[CROSS_ENCODER] Cross-encoder scored NVDA operating margin @ 0.964 confidence.", delay: 1500 },
                { text: "[GROUNDED_OUTPUT] Result: NVDA Q3 operating margin (62.2%, Form 10-Q p.24) vs AAPL (30.1%, Form 10-K p.18).", delay: 2000 }
            ],
            sebi: [
                { text: "[AGENT_ROUTER] Regulatory Compliance query routed to Nirmaan Graph Node.", delay: 250 },
                { text: "[RAPTOR_TREE] Traversing RAPTOR tree level 2 summary nodes for SEBI ICDR regulations...", delay: 700 },
                { text: "[RULE_CHECK] Rule 14.2: Promoter Lock-in period requirement = 18 months for SME IPO.", delay: 1200 },
                { text: "[HITL_CHECKPOINT] Executing Pydantic schema validation for Draft DRHP clause 4.1...", delay: 1700 },
                { text: "[OUTPUT] Compliance Verified: Lock-in clause meets SEBI ICDR Regulation 2018 guidelines.", delay: 2200 }
            ],
            fraud: [
                { text: "[FRAUD_GUARD] Transaction #8492 passed through 30-rule pre-filter engine.", delay: 250 },
                { text: "[GRAY_ZONE] Classified as Gray-Zone (Risk Score: 0.612). Triggering Bayesian Classifier.", delay: 750 },
                { text: "[SHAP_EXPLAIN] Top SHAP Drivers: Velocity_1h (+0.32), Geo_Distance_Mismatch (+0.24).", delay: 1300 },
                { text: "[DECISION] Optuna-calibrated threshold triggered Step-Up Auth requirement.", delay: 1800 }
            ]
        };

        function updateAlphaVal(val) {
            const dense = (parseFloat(val)).toFixed(2);
            const lexical = (1.0 - parseFloat(val)).toFixed(2);
            document.getElementById('alpha-val').textContent = `${dense} Dense / ${lexical} Lexical`;
        }

        function runRagSandbox(type) {
            const consoleBox = document.getElementById("sandbox-console");
            const statusBox = document.getElementById("sandbox-status");
            consoleBox.innerHTML = "";
            statusBox.textContent = "EXECUTING...";
            statusBox.className = "px-2 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800 text-[10px] animate-pulse";

            const steps = scenarios[type];
            steps.forEach((step, idx) => {
                setTimeout(() => {
                    const p = document.createElement("p");
                    p.className = "text-slate-200 border-l-2 border-brand-500 pl-2 py-0.5 text-[11px]";
                    p.textContent = step.text;
                    consoleBox.appendChild(p);
                    consoleBox.scrollTop = consoleBox.scrollHeight;

                    if (idx === steps.length - 1) {
                        statusBox.textContent = "COMPLETED";
                        statusBox.className = "px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 text-[10px]";
                        
                        document.getElementById("metric-latency").textContent = `Latency: ${(Math.random() * 60 + 110).toFixed(0)} ms`;
                        document.getElementById("metric-precision").textContent = `Recall@k: 0.982`;
                        document.getElementById("metric-citations").textContent = `Grounded Citations: Verified`;

                        confetti({
                            particleCount: 25,
                            spread: 50,
                            origin: { y: 0.8 }
                        });
                    }
                }, step.delay);
            });
        }

        // 4. Toast Notifications
        function copyToClipboard(text, message) {
            const el = document.createElement('textarea');
            el.value = text;
            document.body.appendChild(el);
            el.select();
            document.execCommand('copy');
            document.body.removeChild(el);

            showToast(message);
        }

        function showToast(msg) {
            const container = document.getElementById("toast-container");
            const toast = document.createElement("div");
            toast.className = "glass-panel p-3.5 rounded-xl border border-brand-400/50 text-slate-100 text-xs font-mono shadow-xl flex items-center gap-2 transform transition-all duration-300 translate-y-2 opacity-0";
            toast.innerHTML = `<i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-400"></i> ${msg}`;
            container.appendChild(toast);

            setTimeout(() => toast.classList.remove('translate-y-2', 'opacity-0'), 10);
            setTimeout(() => {
                toast.classList.add('opacity-0', 'translate-y-2');
                setTimeout(() => toast.remove(), 300);
            }, 3000);

            lucide.createIcons();
        }
    </script>
</body>
</html>
