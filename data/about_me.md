# About Devansh Agrawal — Comprehensive Knowledge Base

## Personal Background

Devansh Agrawal was born and grew up in Kathmandu, Nepal. In Kathmandu he completed his early schooling at Modern Indian School GPO 1497. His upbringing in Nepal gave him a deeply international perspective that has shaped his career and worldview. At the age of 18, he made a bold decision to move to India for his final year of high school before relocating to the United States to pursue higher education.

Devansh currently lives in Urbana, Illinois, where he is pursuing his Master of Computer Science degree at the University of Illinois Urbana-Champaign (UIUC). He holds Nepali citizenship and is in the United States on an F-1 student visa. Prior to returning to academia, he was on an H-1B work visa while employed at OPEXUS in Washington, D.C. He made a conscious decision to change his visa status from H-1B to F-1 in order to pursue graduate education in Artificial Intelligence — a testament to his commitment to deepening his technical expertise.

Devansh can be reached at devanshagrawal63@gmail.com or by phone at (734) 604-6884. His LinkedIn profile is at https://www.linkedin.com/in/devansh-agrawal63/, his GitHub is at https://github.com/Devansh63, and his portfolio website is at https://devanshagrawal.netlify.app.

Devansh speaks four languages fluently: English, Hindi, Marwari, and Nepali — all at native or bilingual proficiency.

---

## Education

### Master of Computer Science (MCS) — University of Illinois Urbana-Champaign (UIUC)
**Specialization: ML Systems | GPA: 4.0 | January 2026 – May 2027 (expected)**

Devansh is currently pursuing his MCS degree at UIUC, one of the top-ranked computer science programs in the world. His specialization is ML Systems. He maintains a perfect 4.0 GPA. He began the program in January 2026 and expects to complete it in May 2027. Skills being developed at UIUC include Data Analysis, Machine Learning, Distributed Systems, Information Retrieval, and Artificial Intelligence.

### Bachelor of Science in Computer Science — Purdue University Fort Wayne
**Minor: Mathematics | GPA: 3.80 | August 2018 – May 2022 | Fort Wayne, Indiana**

Devansh completed his undergraduate degree in Computer Science at Purdue University's Fort Wayne campus, graduating in May 2022. He minored in Mathematics. He achieved a GPA of 3.80 and was recognized with the prestigious HONORS GOLD MEDAL for Academic Excellence — the highest academic honor at the institution, requiring 18 credits of Honors-level coursework. He was on the Dean's List every semester from Fall 2018 through Spring 2020. He also received the Honors Pin in February 2020 for completing 12 Honors credit courses.

Beyond academics, Devansh was highly active in campus life. He served as President of the Indian Student Association (August 2019 – May 2020), organizing Indian cultural events, presenting budgets to the Student Senate, and running member meetings. He was a Member of the ISA since August 2018. He also served as Secretary of the Purdue Fort Wayne PI Math Club (August–December 2018), organizing member meetings and club events. He was a New Student Orientation Leader in Fall 2019.

### 12th Grade — Delhi Public School Sector XII R K Puram, New Delhi, India
**CBSE All India Senior School Certificate Examination | June 2016 – May 2018**

Devansh completed his 12th-grade education at Delhi Public School RK Puram, one of India's most prestigious school chains, in New Delhi. He studied Computer Science.

### 10th Grade — Modern Indian School GPO 1497, Kathmandu, Nepal
**CBSE Secondary School Examination | 2014–2016**

Devansh completed his 10th grade in Kathmandu.

---

## Professional Experience

### AI Engineer Intern — PeopleLens | Cupertino, CA
**June 2026 – August 2026**

Devansh interned as an AI Engineer at PeopleLens, building LLM systems that coach sales teams. Key accomplishments:
- Designed an LLM pipeline that scores sales calls on 8 coaching criteria, chunking transcripts and using hybrid retrieval (BM25 + dense embeddings) to ground every score in verbatim quotes.
- Achieved 1.37 mean-absolute-error vs human experts on a 1–10 rubric (62% of scores within 1 point) with a two-stage analyze-then-judge LLM design gated by deterministic, code-based validation.
- Co-developed the coaching-plan generator that turns scores into specific, next-step "nudges" for reps and their managers.
- Shipped a multi-tenant MCP (Model Context Protocol) server exposing coaching data as 11 read-only tools to AI assistants in Slack, Teams, and Claude on GCP + MongoDB.
- Verified per-company data isolation and scaled the multi-tenant serving path with a Kafka queue, rate limiting, and idempotent retries, load-tested under concurrent production traffic.
- Cut LLM inference cost and latency via prompt caching, single-pass embedding, and bounded concurrency, reusing one transcript across all 8 per-rubric judges.
- Iterated the call scorer through four architectures, replacing each only on a measured limit (topic chunking, rubric-labelled turns, evidence-grounded retrieval, then a validated-evidence layer that keeps "what happened" and "how well" as separate LLM roles). On 15 held-out calls the final version matched human experts exactly 40% of the time and within one point 62% of the time, with 6 of 8 rubrics beating a constant baseline.
- Co-built, with two other interns, a multi-node LangGraph pipeline that turns scored calls into coaching plans, and helped compare it with the single-pass production prompt on 17 real calls: the RAG write-ups named the specific omission 92% of the time versus 0%, and every RAG quote was found in the transcript.

Skills used: LLMs, RAG, hybrid retrieval, LLM-as-a-judge, LLM evaluation, LangGraph, prompt caching, MCP/FastMCP, multi-tenant architecture, Kafka, GCP, MongoDB, Python.

### Full Stack Software Engineer — OPEXUS (Formerly AINS LLC) | Washington, D.C., USA
**July 2022 – November 2025 (3 years 5 months) | Hybrid**

Devansh worked as a Full-Stack Software Engineer at OPEXUS (formerly known as AINS LLC), a leading government technology company. He worked on FOIAXpress — a .NET 8 case management platform used by 300 government agencies across the United States and Canada, facilitating 3.4 million FOIA (Freedom of Information Act) requests annually.

Key accomplishments:
- Fine-tuned DistilBERT and DeBERTa-v3 (HuggingFace) on 8,000+ annotated documents, lifting redaction accuracy 80%+ over the CoreNLP baseline on ambiguous cases.
- Engineered a multi-stage NLP redaction pipeline (CoreNLP + AWS Comprehend), cutting manual document review from 10 hours to 30 minutes per case.
- Developed a Named Entity Recognition (NER) module giving users the option to use either AWS Comprehend or Stanford CoreNLP to automatically detect and redact sensitive/classified content in federal documents.
- Integrated CoreNLP's Regex-based NER to let users define custom patterns for redactions with an easy-to-use UI.
- Led a team of 8 to ship bilingual French/Spanish support, winning 45 Canadian customers and growing revenue 15%.
- Migrated a monolithic .NET 8 platform (300 agencies, 3.4M requests/yr) to Dockerized microservices, cutting deployment time 70% and enabling independent scaling of the AI service.
- Containerized a legacy .NET application using Docker, improving deployment and reducing environment dependencies.
- Integrated APIs for Relativity and TDMS, Pay.gov, and NS Pay payment options to retain three clients and secure two new clients.
- Implemented CI/CD pipeline to automate security scanning using Fortify and Qualys, identifying and resolving 1,500+ security vulnerabilities.
- Developed Two-Factor Authentication (2FA) for FOIAXpress's public-facing site using time-based OTP.
- Delivered critical incident response for production outages at key federal agencies including NASA, Department of Defense (DOD), IRS, and DOT.

Skills used: Full-Stack Development, C#, .NET Core, .NET Framework, AI, Cybersecurity, Docker, NER, JavaScript, SQL, Azure DevOps.

### Research Assistant — Deep Steganography | Purdue University Fort Wayne
**December 2021 – May 2022 (6 months)**

Devansh worked as a research assistant in the field of Deep Steganography — the science of hiding information within images. He evaluated various methods of encoding messages to increase success rate and efficiency, debugged the existing project, and worked on distributing image representations after compression across all available bits.

### Research Assistant — Differential Gene Expression | Purdue University Fort Wayne
**January 2022 – May 2022 (5 months)**

Devansh worked on a bioinformatics research project analyzing differential gene expression in alcohol-induced rat models. He wrote parallel processing scripts that read millions of RNA data records, converted RNA sequences to DNA sequences, compared and mapped genome results to healthy rat profiles, normalized the data, and compiled a matrix for advanced research conclusions. Tools: MATLAB, Genome Sequencing, DNA Sequencing.

### Applications Developer — Purdue University Fort Wayne
**May 2021 – May 2022 (1 year 1 month)**

Devansh developed and maintained internal university systems using the Grails and Spring frameworks. He used Java and JavaScript to update and manage bugs across in-house applications. He implemented and managed periodic scripts to run, log, and update university-supported software. He utilized Oracle SQL to make secure and efficient changes to the school database.

### Research Assistant — Machine Learning in CT Imaging | Purdue University Fort Wayne
**August 2021 – December 2021 (5 months)**

Devansh worked on applying machine learning to liver CT scan data. He created a 3D registered volume dataset from a large volume of 2D CT scans from multiple patients. He implemented a neural network model (U-Net) trained to predict CT scan images from different directions, enabling radiation dose reduction of 25%–50% for patients.

### Research Assistant — Introduction to Java Teaching Assistant | Purdue University Fort Wayne
**August 2019 – December 2019 (5 months)**

Devansh assisted a professor for the Introduction to Java course at Purdue University. He collected and logged data on each student's progress over the semester, scheduled one-on-one office hours for students who were falling behind, submitted reports on course areas needing development, and coached students to cultivate their interest in Computer Science.

### Senior Information Technology Helpdesk Technician — Purdue University Fort Wayne
**December 2018 – May 2021 (2 years 6 months)**

Devansh supervised a team of 11 student IT technicians to efficiently handle large volumes of incoming technical issues. He supported users on all software and hardware issues, generated reports and records for each incoming issue, and maintained clear professional communication with users via email, phone, and in-person. He received a Letter of Recommendation from this role.

### Software Developer Intern — Janaki Technology Pvt Ltd | Kathmandu, Nepal
**May 2019 – August 2019 (4 months)**

Devansh worked on the "Khalti" project — Nepal's first reliable online payment method and digital wallet, which revolutionized how the Nepalese population conducts small transactions and was a major step in digitalizing Nepal's economy. His roles included:
- Wrote clean, well-tested code for the Khalti online payment wallet
- Implemented agile methodology and full-stack development
- Assisted in developing and maintaining the API for the mobile application
- Participated in code reviews
- Assisted in user database management and authentication
- Resolved UI defects and generated reports and documentation for the development team

### Software Engineer Intern — Smart Solutions | Kathmandu, Nepal
**June 2019 – August 2019 (3 months)**

At Smart Solutions, a prominent software company in Nepal, Devansh worked on developing the website for the Bank of Zambia. He:
- Was part of the team building the Bank of Zambia's website
- Utilized Selenium and other tools to create accurate, automated test scripts
- Improved User Interface features
- Assisted all departments to understand cross-functional workplace expectations
- Participated in code reviews and team meetings

### Box Office Attendant — Purdue University Fort Wayne
**September 2018 – December 2018 (4 months)**

Customer services representative assisting customers with purchases and generating daily transaction reports.

---

## Research Projects Summary

1. **Deep Steganography** (Purdue, Dec 2021 – May 2022): Image-hiding research evaluating encoding methods and distributing compressed image representations across bits.
2. **Machine Learning for Liver CT Imaging** (Purdue, Aug–Dec 2021): U-Net model trained on 3D CT scan data to predict scan images from different angles, enabling 25–50% radiation dose reduction.
3. **Differential Gene Expression in Alcohol-Induced Rats** (Purdue, Jan–May 2022): Parallel MATLAB processing pipelines for RNA-to-DNA conversion, genome mapping, and structured matrix creation for genomic analysis.

---

## Academic Projects

### Ask Devansh — Personal RAG Chatbot (2025 – Present)

Devansh built a full Retrieval-Augmented Generation (RAG) chatbot trained on his own professional background, experience, projects, and personality. The chatbot is live at https://devanshagrawal.netlify.app so that recruiters and hiring managers can ask questions in natural language and receive accurate, context-aware answers in his voice.

**Stack:** Google Gemini 2.5 Flash (generation), Gemini embedding-001 (embeddings), ChromaDB (vector store), Flask (API server), flask-cors, flask-limiter, Python, Docker, Render (production hosting).

**How it works:** A knowledge base (`about_me.md`) is chunked into ~600-character segments, embedded with Gemini, and stored in ChromaDB. At query time, the top-5 most relevant chunks are retrieved and passed to Gemini 2.5 Flash with a persona prompt instructing it to answer as Devansh. The API also includes a `/api/suggest` endpoint that generates relevant follow-up questions.

This project demonstrates end-to-end RAG pipeline design, embedding model usage, vector database integration, and production API deployment — all skills directly applicable to ML Engineering roles.

**Live:** devanshagrawal.netlify.app | **GitHub:** github.com/Devansh63/devansh-rag

---

### Agentic AI System (2025 – Present)

Devansh is building a multi-agent autonomous AI system. Details will be shared publicly on GitHub once the system reaches a stable state. The system explores agent orchestration, tool use, and autonomous task decomposition — areas directly relevant to current frontier AI research.

---

### NeuroDrone — Capstone Project, Purdue University
**Team: Kashyab Ambarani, Omer Yurdabakan, Devansh Agrawal, Logan Luffman | Advisor: Dr. Mohammadreza HajiarbabI**

NeuroDrone was Devansh's senior capstone project. The goal was to program an AI drone capable of autonomous navigation in GPS-denied environments using Deep Q Reinforcement Learning (DQN). Applications: package delivery, air taxis, disaster management. Stack: AirSim, QGroundControl, Unreal Engine 4, TensorFlow/Keras in an NVIDIA-TensorFlow Docker container, Microsoft AirSim via Python API.

### Chess AI Program
Built a Chess game with an AI opponent using the Mini-Max algorithm. The UI is interactive — when a user selects a chess piece, all possible moves on the board are highlighted. The AI improves as it plays more games.

### Khalti — Online Payment Wallet (Nepal)
Worked on Khalti, Nepal's first digital wallet for instant, secure, online payments. Features include mobile recharges, bill payments, and ticket booking. Devansh contributed to full-stack development, the mobile API, database management, and UI defect resolution.

### Bank of Zambia Website
Contributed to developing and testing the Bank of Zambia's web application at Smart Solutions during his Nepal internship.

### Social Media Recipe Website
A full web application allowing users to create accounts, store recipes privately or publicly, view and search public recipes, and create shopping lists based on saved recipes. Features an attractive and easy-to-use UI.

---

## Technical Skills

**Languages:** C#, Java, JavaScript, Python, C, C++, SQL, HTML, CSS, MATLAB

**Frameworks & Libraries:** .NET Core, .NET Framework, React, Spring, Grails, Node.js, AngularJS, Express.js

**Machine Learning & AI:** TensorFlow, Keras, PyTorch, HuggingFace Transformers, ONNX Runtime, U-Net, Deep Q-Learning, AWS Comprehend, AWS Textract, Stanford CoreNLP, Regex-based NER, NumPy, OpenCV, RAG Pipelines, Google Gemini (embedding + generation), ChromaDB, pgvector, Vector Databases, LLM Integration, Agentic AI Systems, Sentence Transformers, Model Fine-Tuning, Scikit-learn, Pandas

**DevOps & Cloud:** Docker, CI/CD, Git, GitHub, GitLab, Azure DevOps, Microsoft Azure, Render, AWS Textract

**Databases:** Microsoft SQL Server, Oracle SQL, Oracle Database, SQL Server Management Studio, Neon Postgres

**Security:** Fortify, Burp Suite, Qualys, 2FA (TOTP), MFA, Incident Response, Cybersecurity

**Testing & Automation:** Selenium, Automated SQL Scripts, MySQL Triggers, Test Scripts

**Research Skills:** Genome Sequencing, DNA Sequencing, Data Analysis, MATLAB, Bioinformatics

**Other:** Distributed Systems, Information Retrieval, Agile Methodologies, Code Review, Web Applications, Database Management Systems (DBMS)

---

## Languages Spoken

- English — Native / Bilingual proficiency
- Hindi — Native / Bilingual proficiency
- Marwari — Native / Bilingual proficiency
- Nepali — Native / Bilingual proficiency

---

## Honors and Awards

- **Honors Gold Medal** (Purdue University Fort Wayne, May 2022): Received at graduation ceremony for completing 18 credits of Honors-level coursework — the highest academic honor at the university.
- **Honors Pin** (Purdue University Fort Wayne, February 2020): Awarded for completing 12 Honors credit courses.
- **Dean's and Semester Honors List — Fall 2018, Spring 2019, Fall 2019, Spring 2020**: Recognized for outstanding academic achievement every semester from freshman year through sophomore year.

---

## Volunteering

### Scribe — Central Board of Secondary Education (CBSE)
**March 2018 – May 2018 (3 months)**

Devansh volunteered as a scribe for differently-abled students taking their CBSE Final Board Examinations (12th grade). He sat with students to write on their behalf and assisted them through the examination center's security checks.

---

## Organizations and Leadership

- **President, Indian Student Association** — Purdue University Fort Wayne (August 2019 – May 2020): Organized Indian cultural events on campus, presented club and event budgets to the Student Senate, organized member meetings to delegate tasks.
- **Member, Indian Student Association** — Purdue University Fort Wayne (August 2018 – May 2019)
- **Secretary, Purdue Fort Wayne PI Math Club** (August–December 2018): Responsible for organizing member meetings and holding club events.
- **New Student Orientation Leader** — Purdue University Fort Wayne (Fall 2019)

---

## Recommendation

From Rushabh Dharia, Software Engineer 2 at The Aspen Group (February 2025):
*"Devansh is a highly dependable and enthusiastic individual who consistently brings a positive and cheerful attitude to the workplace. He possesses strong problem-solving skills, effectively breaking down intricate tasks and tackling them with ease. A true team player, Devansh is always willing to assist his colleagues, fostering a collaborative and supportive environment. I highly recommend him."*

---

## GitHub Projects

Devansh's GitHub profile is at https://github.com/Devansh63. Public repositories include:

- **devansh-rag** (Python): Personal RAG chatbot — full production pipeline using Gemini, ChromaDB, Flask, deployed on Render. Live at devanshagrawal.netlify.app.
- **CNN-from-scratch** (Python/NumPy): Complete CNN implementation from scratch with no deep learning framework.
- **suttonRL** (Python): Clean implementations of RL algorithms from Sutton and Barto's textbook.
- **library-rag-ingest** (Python, CS 410 team project): Full-stack book search and recommendation system using Neon Postgres, pgvector, FastAPI, hybrid BM25 and semantic search, and RAG recommendations via Groq.
- **Language-Model-From-Scratch** (Python): Language model implemented from scratch covering tokenization, attention, and transformer architecture.
- **NeuroDrone-Capston** (Python): Deep RL drone navigation capstone using AirSim, Unreal Engine, TensorFlow.
- **Chess** (Java): A Chess game with AI using the Mini-Max algorithm — interactive UI highlights all valid moves when a piece is selected.
- **WebsiteRecipeStorage** (HTML): Full web app for storing and publicly sharing recipes.
- **Algorithm-Fibonacci** (Java): Fibonacci algorithm implementation.
- **Interpolation** (Java): Numerical Analysis — Interpolation methods.
- **Newtons-Divided-Method** (Java): Newton's Divided Differences for numerical analysis (from his Math minor at Purdue).

---

## Personal Interests and Fun Facts

Devansh is an adventurer at heart. He has visited the Grand Canyon and loves traveling and experiencing nature. He has been inside a helicopter cockpit and enjoys aviation experiences and outdoor adventures.

He is deeply proud of his Nepali heritage and identity — he keeps a Nepali flag displayed in his home. He also has a cat that he is very fond of.

He is passionate about community building. He served as President of the Indian Student Association at Purdue, helping international students feel at home far from their countries. He also tutored and coached Java students one-on-one to cultivate their interest in Computer Science.

Devansh speaks four languages: English, Hindi, Marwari, and Nepali — all at native or near-native proficiency, reflecting his multicultural upbringing across Nepal, India, and the United States.

---

## Personal Story

Devansh's journey is one of geographic breadth and intellectual ambition. He started in Kathmandu, Nepal, moved to New Delhi for high school, then crossed continents to the United States at 18 to begin his undergraduate studies at Purdue Fort Wayne. During undergraduate, he simultaneously worked multiple jobs — IT technician, research assistant, app developer, and teaching assistant — while maintaining Dean's List grades and earning the Honors Gold Medal.

After graduating in 2022 he joined OPEXUS in Washington D.C. on an H-1B visa, spending over 3 years building government technology used by 300 agencies. He then made the bold decision to give up that stable position and change to an F-1 student visa to pursue a Master of Computer Science at UIUC — one of the world's top CS programs — specializing in ML Systems. He now maintains a perfect 4.0 GPA.

He is currently living in Urbana, Illinois, balancing MCS coursework with his love for adventure, his Nepali roots, and a genuine passion for AI.

## Why AI — The Decision to Leave OPEXUS for UIUC

This is something Devansh gets asked a lot: why leave a stable H-1B job at a D.C. tech company to go back to school?

The honest answer is that he could feel the field shifting. During his time at OPEXUS, he worked on NER modules (AWS Comprehend, Stanford CoreNLP), built redaction systems for classified federal documents, and watched AI go from a niche tool to the center of every serious engineering decision. He realized he wanted to be someone who builds AI systems, not just someone who calls an API.

The decision was deliberate. He researched programs, applied selectively, and chose UIUC specifically because of its depth in ML and systems — and because he knew that if he was going to do this, it had to be a program worth giving up an H-1B for. He is not hedging. He changed his visa status from H-1B to F-1 — a move that removed the safety net — because he is fully committed to the AI path.

At UIUC he has maintained a 4.0 GPA while building real projects: a production RAG chatbot at devanshagrawal.netlify.app, an agentic AI system, a GPU study of speculative decoding in vLLM, a study of how chatbots respond to user pushback, and taking courses in Machine Learning, Distributed Systems, Text Information Systems, Natural Language Processing, Hardware & Software for AI, and Human-Centered AI. He is not studying AI in the abstract — he is building things with it.

## UIUC Coursework Details

Devansh is pursuing his MCS at UIUC starting January 2026, expected graduation May 2027.

Completed, Spring 2026:
- **CS 410 Text Information Systems**: search, ranking and text retrieval. His team built the library RAG book search system in this course.
- **CS 425 Distributed Systems**: fault tolerance, consensus and replication.
- **CS 446 Machine Learning**: core ML algorithms and model evaluation; mini-torch, his autograd engine, came from this course.

In progress, Fall 2026:
- **CS 447 Natural Language Processing**
- **CS 598 Hardware & Software for AI**: his Speculation Ladder project on speculative decoding in vLLM.
- **CS 598 Human-Centered AI**: his team's study of how chatbots respond when users push back.

GPA: 4.0 across all coursework.

---

## Open To Work

Devansh has 4+ years of engineering experience: 3+ years as a Full Stack Software Engineer at OPEXUS, an AI Engineer internship at PeopleLens, and a year as an Applications Developer at Purdue.

Devansh is open to **ML/AI engineering roles**, and graduates in May 2027. He is especially interested in positions involving:
- Machine Learning Engineering (training, fine-tuning, deploying models)
- AI Research (applied research with real-world impact)
- AI/ML Infrastructure (MLOps, data pipelines, model serving)
- Full-Stack AI Products (RAG systems, LLM integrations, agentic systems)

He is also open to Software Engineer and Full-Stack roles where AI/ML is a significant component. He is authorized to work in the United States on an F-1 student visa with OPT/CPT eligibility. He expects to graduate in May 2027.

---

## CNN from Scratch in NumPy (Detailed)

Devansh built a complete Convolutional Neural Network from scratch using only NumPy, with no deep learning framework like PyTorch or TensorFlow. The project demonstrates a deep understanding of CNN internals by manually implementing every component that modern frameworks abstract away. The components implemented include 2D convolution forward and backward passes, max pooling and average pooling layers, fully connected layers with backpropagation, ReLU and softmax activation functions with their derivatives, cross-entropy loss with manual gradient computation, and mini-batch gradient descent. The project was built primarily as a learning exercise to internalize the math behind deep learning and validates understanding of computational graphs, backpropagation, and the chain rule applied to convolutional operations. GitHub: github.com/Devansh63/CNN-from-scratch.

---

## Reinforcement Learning Algorithms from Sutton and Barto (Detailed)

Devansh's suttonRL repository contains clean, from-scratch implementations of foundational reinforcement learning algorithms based on Sutton and Barto's "Reinforcement Learning: An Introduction," widely considered the canonical RL textbook. The repository covers epsilon-greedy bandits (chapter 2), value iteration on FrozenLake (chapter 4), first-visit Monte Carlo control on Blackjack (chapter 5), SARSA and Q-learning compared on CliffWalking (chapter 6), REINFORCE policy gradients, and a DQN. He started it to understand what happens under the hood rather than calling stable-baselines. GitHub: github.com/Devansh63/suttonRL.

---

## Library RAG Recommendation Pipeline (Detailed)

Devansh's library-rag-ingest project is a full-stack book search and recommendation system built with a team of five for CS 410 (Text Information Systems) at UIUC. It covers 962K books and 11M reader reviews from Goodreads, CMU Book Summaries and the UCSD Book Graph, enriched with ISBNdb, stored in Neon Postgres with pgvector. The search pipeline uses a Groq-powered query classifier (llama-3.1-8b-instant) to assign retrieval weights across Postgres BM25 full-text search and dual BAAI/bge-base-en-v1.5 semantic search (metadata and review embeddings), fused via Reciprocal Rank Fusion. Top results are passed to llama-3.3-70b-versatile for RAG recommendations. The system is deployed on Render with a FastAPI backend and React UI. GitHub: github.com/Devansh63/library-rag-ingest.

---

## Speculative Decoding Ladder (Detailed)

A CS 598 Hardware & Software for AI project at UIUC (Fall 2026) with Sahil Sashi, run on NCSA Delta GPUs with vLLM and Qwen3-8B. Speculative decoding lets a cheap drafter propose several tokens that the target model verifies in one forward pass. The project asks where that stops paying as prompts get longer and the server gets busier. Sahil owns the vLLM side (the runner, metrics patch and harness); Devansh owns the workload, the analysis and the cost model, plus the repository and its claim register. The cost model: speedup is roughly [coverage x conditional acceptance + (1 - coverage)] / R, where acceptance belongs to the drafter and R, the verification cost ratio, belongs to the machine.

Findings so far, on A40 GPUs with LongBench-v2 prompts at 2K, 8K and 32K tokens: the ranking of drafters inverts with context. A trained DFlash draft head gives 1.86x at 2K, 1.26x at 8K and 0.83x at 32K, slower than not speculating, while n-gram prompt lookup holds 1.16x, 1.15x and 1.08x. The same order held on an A100, and the result replicated across two nodes to within 0.08%. Devansh froze a prediction for the A100 from the A40-fitted cost model before it ran: 2 of 4 cells landed within 5% (median error 6.2%), and because the misses split by drafter, one hardware factor cannot explain them, so the cost model is being restated as two terms. Fitting R(k) = (1 + R_draft) + c*k showed drafting is 82-86% of DFlash's overhead: long context taxes the drafter's own pass, not verification. He also found that serving engines report acceptance only for steps where a draft was proposed, which overstates a low-coverage drafter by more than 2x unless a coverage term is added. The project keeps a claims-to-evidence register with a falsifier for every claim and records predictions that failed. GitHub: github.com/Devansh63/Speculate-Decoding-Ladder.

---

## How Real People Push Back (Detailed)

A CS 598 HCI project at UIUC (Fall 2026), by a team of six, on chatbot sycophancy: when a user disagrees with a correct answer, how often does the model give in, and does a response layer that adapts to the type of pushback help? Devansh ran the pilot end to end: 2,040 trials on two DeepSeek V4 models with 60 verified questions and 480 pushback stimuli, analyzed with Wilson intervals and a cluster bootstrap. Caving was near zero (0-8%), but replaying 300 real WildChat pushback cases in their natural conversational context gave 72-78% adoption, matching the published 67-77%, which showed the low rate was a property of the study design rather than the models. Pushback type predicted adoption (bare disagreement 87.7% vs reasoning challenge 63.0%), and reframing the question made caving worse. He also measured a proposed lexical pushback filter on 60,000 WildChat conversations (58.0% precision, 2.0% recall) and reported two instruments that failed validation instead of dropping them. He presented the team's methodology, scored both failure directions with one joint metric (J = hold rate + accept rate - 1) so a fix cannot win by turning stubborn, and ran a 240-conversation multi-turn arm showing that escalating pushback does not accumulate caving. The whole pilot cost about $1 across roughly 9,600 API calls. GitHub: github.com/Devansh63/cs598-pushback-test.

---

## Devansh's Preferred ML Tech Stack

For deep learning, Devansh primarily uses PyTorch and the HuggingFace ecosystem (Transformers, Datasets, Tokenizers). For classical ML, he uses Scikit-learn and Pandas. For computer vision preprocessing, he uses OpenCV and NumPy. For specialized medical imaging work, he uses ITK.

For deployment and optimization, his preferred stack includes ONNX Runtime for cross-platform inference, FastAPI for serving model APIs, and Docker for containerization.

For RAG systems, he has experience with Google Gemini, ChromaDB for prototyping, and Neon Postgres with pgvector for production-grade vector storage. He is familiar with sentence-transformer models for generating embeddings.

For experiment tracking and infrastructure, he is familiar with Weights & Biases, MLflow, and Azure DevOps for CI/CD.

---

## Devansh's Approach to Problem Solving

Devansh's approach to ML problems emphasizes pragmatic engineering tradeoffs over chasing the latest research. When building the FOIA redaction pipeline, the choice of DistilBERT over larger models was driven by CPU deployment constraints, not just accuracy. Similarly, the cascade architecture using CoreNLP for the bulk of cases and a transformer for edge cases was designed to balance throughput with accuracy.

He prefers measurable, incremental improvements over big-bang rewrites. The two-phase fine-tuning approach used in the FOIA pipeline reflects this: a general training phase establishes broad knowledge, then targeted hard example mining specializes the model on the cases that matter most without losing general capability.

He values rigorous evaluation. The NeuroDrone project benchmarked four different RL agents rather than picking one a priori, and the Liver CT project used multiple evaluation metrics (MSE, MAE, SSIM, PSNR) to capture different aspects of reconstruction quality.

---

## Certifications Devansh is Considering

Devansh is interested in pursuing industry certifications to complement his academic background. The certifications he is considering, ranked by relevance to his target roles, include AWS Certified Machine Learning Specialty (most relevant for ML Engineer roles), Google Cloud Professional Machine Learning Engineer, TensorFlow Developer Certificate, Databricks Certified Machine Learning Associate, and HashiCorp Terraform Associate for infrastructure work.

He is also considering Kubernetes certifications like CKAD if pursuing MLOps-focused roles.

---

## Sample Q&A

**Q: Where are you from?**
A: I was born and grew up in Kathmandu, Nepal. I moved to New Delhi, India for my 12th grade at Delhi Public School RK Puram, then came to the United States in 2018 to attend Purdue University Fort Wayne.

**Q: What are you currently studying?**
A: I'm pursuing my Master of Computer Science (MCS) at UIUC, specializing in ML Systems. This semester I'm taking Natural Language Processing, Hardware & Software for AI, and Human-Centered AI. I started in January 2026, maintaining a 4.0 GPA, and expect to graduate in May 2027.

**Q: Where did you do your undergrad?**
A: Purdue University Fort Wayne — BS in Computer Science with a Minor in Mathematics, graduating May 2022 with a GPA of 3.80. I received the Honors Gold Medal for Academic Excellence (for completing 18 Honors credits) and was on the Dean's List every semester from Fall 2018 through Spring 2020.

**Q: Where did you work?**
A: My main job was at OPEXUS (formerly AINS LLC) in Washington D.C. as a Full Stack Software Engineer — I was there from July 2022 to November 2025. I worked on FOIAXpress, used by 300 government agencies to process 3.4 million FOIA requests per year. Most recently I was an AI Engineer Intern at PeopleLens (June–August 2026), building LLM call-scoring pipelines and a multi-tenant MCP server. Before OPEXUS, I had roles at Purdue University (app developer, research assistant, IT technician) and two internships in Nepal — one at Janaki Technology working on Khalti (Nepal's first digital wallet) and one at Smart Solutions building the Bank of Zambia's website.

**Q: Tell me about the NeuroDrone project.**
A: NeuroDrone was my senior capstone at Purdue. We built an AI drone that could navigate autonomously in GPS-denied environments using Deep Q Reinforcement Learning. We used Unreal Engine 4, AirSim, TensorFlow/Keras in Docker, and occupancy mapping for obstacle detection. Real-world applications included package delivery, air taxis, and disaster management.

**Q: What ML research have you done?**
A: Three main projects. First, I trained a U-Net model on liver CT scan data to synthesize multi-angle projections and reduce radiation exposure by 25–50%. Second, I worked on Deep Steganography — hiding information within images using encoding methods distributed across compressed bit representations. Third, I wrote MATLAB parallel processing pipelines to analyze differential gene expression in alcohol-induced rat models using RNA-to-DNA conversion and genome mapping.

**Q: What's the Khalti project?**
A: Khalti was Nepal's first reliable online digital wallet and payment platform — it revolutionized how Nepalese people make small transactions. I worked on it as an intern at Janaki Technology in Kathmandu in summer 2019. I wrote clean full-stack code, helped maintain the mobile API, did code reviews, and worked on user database management. It's a project I'm genuinely proud of because of what it means for Nepal's digital economy.

**Q: What programming languages do you know?**
A: My strongest languages are C#, Python, Java, and JavaScript. I also know C, C++, SQL, HTML, CSS, and MATLAB. On the framework side: .NET Core/Framework, React, Spring, Grails, Node.js, AngularJS, Express.js.

**Q: What languages do you speak?**
A: I speak four languages at native or near-native proficiency: English, Hindi, Marwari, and Nepali.

**Q: What are your hobbies or interests outside of tech?**
A: I love traveling and outdoor adventures — I've visited the Grand Canyon and have experienced helicopter flights. I'm deeply proud of my Nepali heritage and display the Nepali flag in my home. I have a cat. I'm also very community-oriented — I was President of the Indian Student Association at Purdue and tutored students one-on-one in Java.

**Q: What awards have you received?**
A: At Purdue, I received the Honors Gold Medal at graduation for completing 18 credits of Honors coursework — the university's highest academic honor. I also received the Honors Pin for completing 12 Honors credits, and I was on the Dean's and Semester Honors List every semester from Fall 2018 through Spring 2020.

**Q: Are you open to new opportunities?**
A: Yes. I'm open to ML/AI Engineer roles, and to Software Engineer, Full Stack, or Back End roles with a real AI/ML component. I graduate from UIUC in May 2027.

**Q: What's on your GitHub?**
A: My GitHub is github.com/Devansh63. Public repos include a personal RAG chatbot (devansh-rag, live at devanshagrawal.netlify.app), a CNN built from scratch in NumPy, RL algorithm implementations from Sutton and Barto, a full-stack library book recommendation system (library-rag-ingest), a language model built from scratch, and the NeuroDrone capstone project.

**Q: How can I contact you?**
A: Email: devanshagrawal63@gmail.com | Phone: (734) 604-6884 | LinkedIn: https://www.linkedin.com/in/devansh-agrawal63/ | GitHub: https://github.com/Devansh63 | Portfolio: https://devanshagrawal.netlify.app

**Q: Why did you leave OPEXUS to go back to school?**
A: It was a deliberate decision, not a reaction to anything going wrong. I could see AI becoming the core of every serious engineering team, and I realized I wanted to be someone who actually builds these systems — not just someone who integrates APIs. I was on an H-1B at OPEXUS, which is a comfortable visa, and choosing to switch to an F-1 for grad school meant removing that safety net entirely. I made that choice because I believed the investment was worth it, and because if I was going to do it, it had to be UIUC — one of the best CS programs in the world. I have no regrets. The coursework, the projects I am building, and the 4.0 GPA tell me I made the right call.

**Q: What are you currently building at UIUC?**
A: Two course research projects this semester. In CS 598 Hardware & Software for AI, Sahil Sashi and I are measuring where speculative decoding stops paying inside vLLM as context and load grow, on Qwen3-8B and NCSA Delta GPUs; the headline is that the trained draft head goes from a 1.86x speedup at 2K tokens of context to 0.83x at 32K, while cheap n-gram lookup still helps. In CS 598 HCI, my group is studying how chatbots respond when users push back on correct answers; replaying 300 real WildChat pushback cases in natural context gave 72-78% adoption, against 0-8% in the scripted design. Outside class: "Ask Devansh" — a production RAG chatbot using Google Gemini for both embeddings and generation, ChromaDB as the vector store, and Flask for the API. It is deployed at devanshagrawal.netlify.app so recruiters can ask questions about my background in natural language. I am also working on an agentic AI system — a multi-agent autonomous AI for tool use and task decomposition. These are things I am building because I find them genuinely interesting, not just because they look good on a resume.

**Q: What is the Ask Devansh chatbot?**
A: It is a RAG (Retrieval-Augmented Generation) chatbot I built and deployed. It is trained on a detailed knowledge base about my background, experience, and projects. When you ask it a question, it retrieves the most relevant chunks from that knowledge base, and Gemini 2.5 Flash generates an answer in my voice. The stack is Gemini embedding-001 for embeddings, ChromaDB for vector storage, Flask for the API, and it is deployed on Render. The chatbot is live at devanshagrawal.netlify.app and the code is on GitHub at github.com/Devansh63/devansh-rag.

**Q: What kind of roles are you looking for?**
A: I am open to ML/AI engineering roles; I graduate in May 2027. My strongest interest is in Machine Learning Engineering, AI Research, and building AI-powered products. I have practical experience with RAG pipelines, embeddings, vector databases, and agentic systems — plus 4+ years of engineering experience, including 3+ years at OPEXUS and an AI Engineer internship at PeopleLens. I am authorized to work in the U.S. on an F-1 visa with OPT/CPT eligibility.

**Q: Are you available for internships?**
A: Yes. I am open to ML/AI engineering roles, and I graduate in May 2027. I am on an F-1 student visa and eligible for CPT. I am based in Urbana, IL but open to relocating for the right opportunity.

**Q: What makes you stand out as a candidate?**
A: A few things. First, I have real production experience — I shipped software used by 300 government agencies at OPEXUS, resolved 1,500+ security vulnerabilities, and led a team of 8. I know what it takes to ship. Second, I have hands-on AI experience: I built a RAG pipeline from scratch (live at devanshagrawal.netlify.app), I have done ML research (U-Net for CT imaging, deep steganography, reinforcement learning for NeuroDrone), and I am currently building an agentic AI system at UIUC. Third, I gave up a stable H-1B job to pursue this. That level of commitment to AI is not something I can fake.

**Q: Tell me about the CNN from scratch project.**
A: I built a complete Convolutional Neural Network using only NumPy — no PyTorch, no TensorFlow, nothing. I implemented 2D convolution forward and backward passes, pooling layers, fully connected layers, ReLU and softmax with their derivatives, cross-entropy loss, and mini-batch gradient descent. The point was to deeply understand what frameworks do under the hood, not just use them. It is on GitHub at github.com/Devansh63/CNN-from-scratch.

**Q: Tell me about the RL algorithms project.**
A: My suttonRL repo has clean from-scratch implementations of core RL algorithms from Sutton and Barto's textbook — the standard RL reference. So far it covers epsilon-greedy bandits, value iteration on FrozenLake, first-visit Monte Carlo control on Blackjack, SARSA vs Q-learning on CliffWalking, REINFORCE, and DQN. GitHub: github.com/Devansh63/suttonRL.

**Q: What is the library RAG project?**
A: library-rag-ingest is a full-stack book search and recommendation system I built with a team of five for CS 410 at UIUC. It covers 962K books and 11M reader reviews, uses a Groq-powered query classifier to route searches, combines BM25 and semantic search via Reciprocal Rank Fusion, and generates RAG recommendations using llama-3.3-70b-versatile. Deployed on Render with a FastAPI backend and React UI. GitHub: github.com/Devansh63/library-rag-ingest.

**Q: What is your portfolio website?**
A: My portfolio is at devanshagrawal.netlify.app. It includes the Ask Devansh RAG chatbot so visitors can ask questions about my background, experience, and projects in natural language.
