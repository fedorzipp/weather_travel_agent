# 🧳 Туристичний Гід-Агент

Це локальний AI-агент, який допомагає туристам вирішити, що робити в місті залежно від погоди. Агент використовує безкоштовну LLM-модель GPT4All та кастомний weather tool, що звертається до публічного API.

---

## 🔧 Можливості

- ✅ Визначає місто, яке тебе цікавить
- ✅ Отримує актуальну погоду з [wttr.in](https://wttr.in/)
- ✅ Дає рекомендації щодо активностей у місті
- ✅ Працює повністю офлайн (модель запускається локально)
- ✅ Має зручний інтерфейс через Streamlit

---

## 📁 Структура проекту

```
weather_travel_agent/
├── streamlit_app.py         # Streamlit-інтерфейс
├── travel_agent.py          # Ініціалізація агента
├── weather_tool.py          # Tool для отримання погоди
├── models/
│   └── mistral-7b-instruct-v0.1.Q4_K_M.gguf  # GPT4All модель
├── requirements.txt
└── README.md
```

---

## ⚙️ Встановлення

### 1. Клонувати репозиторій

```bash
git clone https://github.com/yourusername/weather_travel_agent.git
cd weather_travel_agent
```

### 2. Створити віртуальне середовище та встановити залежності

```bash
python -m venv .venv
source .venv/bin/activate  # або .venv\Scripts\activate на Windows
pip install -r requirements.txt
```

### 3. Завантажити модель GPT4All

Скачай модель з HuggingFace:

📥 [Завантажити Mistral-7B-Instruct (GGUF, Q4_K_M)](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf)

Скопіюй її до папки `models/` у корені проєкту.

---

## 🚀 Запуск

```bash
streamlit run streamlit_app.py
```

Після запуску відкриється веб-інтерфейс, де можна ввести місто та отримати туристичні поради.

---

## 🧠 Приклад запиту

- **Місто:** Львів
- **Питання:** Що робити сьогодні?

**Приклад відповіді:**

> Погода у Львові: 🌤 +22°C. Сьогодні гарна погода! Радимо відвідати старе місто та випити каву на площі Ринок.

---

## 🧩 Як працює

1. Користувач вводить назву міста і запит
2. Агент викликає `weather_tool.py`, щоб отримати погоду
3. GPT4All формує відповідь на основі контексту
4. Streamlit виводить результат

---

## 📝 Залежності

Мінімальний список:
```text
langchain
langchain-community
streamlit
gpt4all
requests
```

---

## ⚠️ Примітки

- Якщо отримаєш помилку `Could not parse LLM output`, додай `handle_parsing_errors=True` в `initialize_agent(...)`
- LangChain рекомендує перехід на LangGraph — це не обов’язково, але рекомендовано для складніших проєктів

---

## 📜 Ліцензія

Проєкт поширюється під ліцензією MIT.
