import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os

# Set up Streamlit page
st.set_page_config(page_title="Fundraising Copywriter Agent", layout="centered")
st.title("🤖 Fundraising Copywriter AI Agent")
st.markdown("Generate persuasive fundraising emails, grant pitches, and donor appeals in seconds.")

# Input form
with st.form("fundraising_form"):
    org_name = st.text_input("🌍 Organization Name", placeholder="E.g., Clean Water Now")
    mission = st.text_area("📌 Mission Statement", placeholder="Describe what your organization does...")
    campaign_goal = st.text_area("🎯 Fundraising Goal", placeholder="E.g., Raise $50,000 by August 2025...")
    target_audience = st.text_input("👥 Target Audience", placeholder="e.g., individual donors, foundations, diaspora community")
    tone = st.selectbox("✍️ Tone of Voice", ["Inspiring", "Formal", "Urgent", "Heartfelt", "Professional"])
    submit = st.form_submit_button("Generate Copy")

# Build LangChain prompt
if submit and org_name and mission and campaign_goal and target_audience:
    template = PromptTemplate(
        input_variables=["org", "mission", "goal", "audience", "tone"],
        template="""
You are an expert fundraising copywriter. Write a compelling email or short pitch for {org}.

Mission: {mission}
Fundraising Goal: {goal}
Target Audience: {audience}
Tone of Voice: {tone}

Make it clear, persuasive, and aligned with nonprofit storytelling best practices.
"""
    )

    prompt = template.format(
        org=org_name,
        mission=mission,
        goal=campaign_goal,
        audience=target_audience,
        tone=tone
    )

    # Use ChatOpenAI
    llm = ChatOpenAI(temperature=0.7)
    with st.spinner("Writing your copy..."):
        response = llm.predict(prompt)

    st.markdown("### ✉️ Generated Fundraising Copy")
    st.text_area("Preview", response, height=300)

    # Option to download
    st.download_button("📥 Download Copy", data=response, file_name="fundraising_copy.txt")

elif submit:
    st.warning("Please fill out all fields to generate your fundraising copy.")

# Footer
st.markdown("---")
st.markdown("Crafted with 💡 by your AI copywriting assistant.")
