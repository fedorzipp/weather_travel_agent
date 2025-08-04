import streamlit as st
from travel_agent import agent

st.set_page_config(page_title="🧳 Туристичний гід", page_icon="🌤️")

st.title("🧳 Туристичний гід-агент")
st.markdown("Порадить, що робити в місті з урахуванням погоди 🌤️")

city = st.text_input("Місто:", placeholder="Kyiv")
question = st.text_input("Що хочеш дізнатись?", placeholder="What to do today?")

if st.button("Запитати"):
    if city and question:
        query = f"""
        You are a helpful travel assistant. You can use a tool called 'Weather Info Tool' to get the weather.

        To use a tool, follow this format exactly:
        Action: Weather Info Tool
        Action Input: <city>

        Then based on the weather, provide suggestions what to do.

        Now answer the question: What to do today in {city}?
        """
        with st.spinner("Генеруємо відповідь..."):
            response = agent.invoke({"input": query})
            st.success("Відповідь:")
            st.write(response["output"])
    else:
        st.warning("Введи місто і питання.")
