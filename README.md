# Aifa Question-Answering

🤖Ask questions to your Aifa in natural language🤖

💪 Built with [LangChain](https://github.com/hwchase17/langchain)

# 🌲 Environment Setup

In order to set your environment up to run the code here, first install all requirements:

```shell
pip install -r requirements.txt
```

Then set your OpenAI API key (if you don't have one, get one [here](https://beta.openai.com/playground))

```shell
export OPENAI_API_KEY=....
```

# 📄 What is in here?
- Code to deploy on StreamLit

# 🚧 Coming soon..
- Aifa starts chatting!
- Aifa grows a personality!
- Aifa remembers you!

## 💬 Ask a question
In order to ask a question, run a command like:

```shell
python qa.py "What are some home remedies for cough"
```

You can switch out `What are some home remedies for cough` for any question of your liking!

~~This exposes a chat interface for interacting with aifa.
IMO, this is a more natural and convenient interface for getting information.~~

## 🚀 Code to deploy on StreamLit

The code to run the StreamLit app is in `front.py`. 
Note that when setting up your StreamLit app you should make sure to add `OPENAI_API_KEY` as a secret environment variable.

```shell
streamlit run front.py
```
