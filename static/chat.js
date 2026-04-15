/* =========================================================
   Ask Devansh — Chat UI
   ========================================================= */
'use strict';

const chatWindow = document.getElementById('chat-window');
const msgInput   = document.getElementById('message-input');
const sendBtn    = document.getElementById('send-btn');
const suggWrap   = document.getElementById('suggestions-wrap');
const suggCards  = document.getElementById('suggestion-cards');
const clearBtn   = document.getElementById('clear-btn');

let isWaiting  = false;
let typingEl   = null;
let suggHidden = false;

function nowTime() {
  return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function scrollBottom() {
  requestAnimationFrame(() => {
    chatWindow.scrollTo({ top: chatWindow.scrollHeight, behavior: 'smooth' });
  });
}

function makeBotAvatar() {
  const av = document.createElement('div');
  av.className = 'msg-avatar bot-avatar-msg';
  const img = new Image();
  img.src = '/static/images/profile.jpg';
  img.alt = 'DA';
  img.style.cssText = 'width:100%;height:100%;object-fit:cover;object-position:center top;display:block;border-radius:50%';
  img.onerror = () => { img.remove(); av.textContent = 'DA'; };
  av.appendChild(img);
  return av;
}

function makeUserAvatar() {
  const av = document.createElement('div');
  av.className = 'msg-avatar user-avatar-msg';
  av.textContent = 'You';
  return av;
}

function formatText(raw) {
  if (!raw) return '';
  let s = raw
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
  s = s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  s = s.replace(/\*(.+?)\*/g, '<em>$1</em>');
  const lines = s.split('\n');
  const out = [];
  let inUl = false, inOl = false;
  for (const line of lines) {
    if (/^[-•]\s/.test(line)) {
      if (!inUl) { if (inOl) { out.push('</ol>'); inOl = false; } out.push('<ul>'); inUl = true; }
      out.push('<li>' + line.replace(/^[-•]\s/, '') + '</li>');
      continue;
    }
    if (/^\d+\.\s/.test(line)) {
      if (!inOl) { if (inUl) { out.push('</ul>'); inUl = false; } out.push('<ol>'); inOl = true; }
      out.push('<li>' + line.replace(/^\d+\.\s/, '') + '</li>');
      continue;
    }
    if (inUl) { out.push('</ul>'); inUl = false; }
    if (inOl) { out.push('</ol>'); inOl = false; }
    if (line.trim() === '') out.push('<br/>');
    else out.push('<p>' + line + '</p>');
  }
  if (inUl) out.push('</ul>');
  if (inOl) out.push('</ol>');
  return out.join('');
}

function appendMessage(role, text, isWelcome = false) {
  const isBot = role !== 'user';
  const group = document.createElement('div');
  group.className = ['message-group', isBot ? 'bot-group' : 'user-group',
    role === 'error' ? 'error-group' : '', isWelcome ? 'welcome-group' : ''].filter(Boolean).join(' ');
  const inner = document.createElement('div');
  inner.className = 'msg-inner';
  const avatar = isBot ? makeBotAvatar() : makeUserAvatar();
  const body = document.createElement('div');
  body.className = 'msg-body';
  const sender = document.createElement('p');
  sender.className = 'msg-sender';
  sender.textContent = isBot ? 'Devansh AI' : 'You';
  const textEl = document.createElement('div');
  textEl.className = 'msg-text';
  textEl.innerHTML = formatText(text);
  const meta = document.createElement('div');
  meta.className = 'msg-meta';
  const time = document.createElement('span');
  time.className = 'msg-time';
  time.textContent = nowTime();
  meta.appendChild(time);
  if (isBot) {
    const copy = document.createElement('button');
    copy.className = 'copy-btn';
    const iconSVG = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>`;
    copy.innerHTML = iconSVG + ' Copy';
    copy.title = 'Copy to clipboard';
    copy.addEventListener('click', () => {
      navigator.clipboard.writeText(text).then(() => {
        copy.textContent = '✓ Copied!';
        copy.classList.add('copied');
        setTimeout(() => { copy.innerHTML = iconSVG + ' Copy'; copy.classList.remove('copied'); }, 2200);
      }).catch(() => {});
    });
    meta.appendChild(copy);
  }
  body.appendChild(sender);
  body.appendChild(textEl);
  body.appendChild(meta);
  inner.appendChild(avatar);
  inner.appendChild(body);
  group.appendChild(inner);
  chatWindow.appendChild(group);
  scrollBottom();
  return group;
}

function showTyping() {
  if (typingEl) return;
  const group = document.createElement('div');
  group.className = 'typing-group';
  const inner = document.createElement('div');
  inner.className = 'typing-inner';
  inner.appendChild(makeBotAvatar());
  const bubble = document.createElement('div');
  bubble.className = 'typing-bubble';
  for (let i = 0; i < 3; i++) {
    const dot = document.createElement('span');
    dot.className = 'dot';
    bubble.appendChild(dot);
  }
  inner.appendChild(bubble);
  group.appendChild(inner);
  chatWindow.appendChild(group);
  typingEl = group;
  scrollBottom();
}

function hideTyping() {
  if (typingEl) { typingEl.remove(); typingEl = null; }
}

function setWaiting(on) {
  isWaiting = on;
  msgInput.disabled = on;
  sendBtn.disabled = on;
  sendBtn.classList.toggle('loading', on);
  if (!on) msgInput.focus();
}

async function sendMessage() {
  if (isWaiting) return;
  const text = msgInput.value.trim();
  if (!text) return;
  msgInput.value = '';
  msgInput.style.height = 'auto';
  hideSuggestions();
  appendMessage('user', text);
  setWaiting(true);
  showTyping();
  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text }),
    });
    hideTyping();
    if (res.status === 429) {
      appendMessage('error', "You're sending messages a bit fast — wait a few seconds and try again.");
      return;
    }
    if (!res.ok) {
      let err = 'Something went wrong. Please try again.';
      try { const d = await res.json(); if (d.error) err = d.error; } catch (_) {}
      appendMessage('error', err);
      return;
    }
    const data = await res.json();
    appendMessage('assistant', data.response || 'Could not generate a response. Please try again.');
  } catch (e) {
    hideTyping();
    appendMessage('error', 'Connection error — make sure the Flask server is running and refresh.');
    console.error(e);
  } finally {
    setWaiting(false);
  }
}

const DEFAULT_QUESTIONS = [
  "Where did you grow up?",
  "What are you studying at UIUC?",
  "Tell me about the NeuroDrone project",
  "What did you build at OPEXUS?",
  "What's the Khalti project?",
  "What ML research have you done?",
  "What are your technical skills?",
  "What languages do you speak?",
];

function hideSuggestions() {
  if (!suggWrap || suggHidden) return;
  suggHidden = true;
  suggWrap.style.transition = 'opacity 0.28s ease, max-height 0.35s ease, padding 0.3s';
  suggWrap.style.opacity = '0';
  suggWrap.style.maxHeight = '0';
  suggWrap.style.padding = '0';
  suggWrap.style.overflow = 'hidden';
}

function showSuggestions() {
  if (!suggWrap) return;
  suggHidden = false;
  suggWrap.style.opacity = '1';
  suggWrap.style.maxHeight = '160px';
  suggWrap.style.padding = '';
  suggWrap.style.overflow = '';
}

function renderSuggestions(questions) {
  if (!suggCards) return;
  suggCards.innerHTML = '';
  questions.forEach(q => {
    const btn = document.createElement('button');
    btn.className = 'suggestion-card';
    btn.textContent = q;
    btn.addEventListener('click', () => {
      if (isWaiting) return;
      msgInput.value = q;
      autoResize();
      sendMessage();
    });
    suggCards.appendChild(btn);
  });
}

async function loadSuggestions() {
  let questions = DEFAULT_QUESTIONS;
  try {
    const res = await fetch('/api/suggest', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({}) });
    if (res.ok) {
      const d = await res.json();
      if (Array.isArray(d.questions) && d.questions.length > 0) questions = d.questions;
    }
  } catch (_) {}
  renderSuggestions(questions);
}

function clearChat() {
  chatWindow.innerHTML = '';
  typingEl = null;
  showSuggestions();
  showWelcome();
}

function autoResize() {
  msgInput.style.height = 'auto';
  msgInput.style.height = Math.min(msgInput.scrollHeight, 150) + 'px';
}

function showWelcome() {
  const msg =
    "Hey! I'm an AI assistant built to answer questions about **Devansh Agrawal**.\n\n" +
    "I run on a RAG pipeline — I retrieve relevant facts from Devansh's resume, research history, and personal bio, then generate grounded answers using Google Gemini.\n\n" +
    "Ask me anything: his background growing up in **Kathmandu, Nepal**, his MCS at **UIUC** (GPA 4.0), his work at **OPEXUS** building government software used by 200+ agencies, the **NeuroDrone** capstone, his research in medical imaging and steganography, or anything else. What would you like to know?";
  appendMessage('assistant', msg, true);
}

msgInput.addEventListener('keydown', e => {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
});
msgInput.addEventListener('input', autoResize);
sendBtn.addEventListener('click', sendMessage);
clearBtn && clearBtn.addEventListener('click', clearChat);

document.addEventListener('DOMContentLoaded', () => {
  showWelcome();
  loadSuggestions();
  msgInput.focus();
});
