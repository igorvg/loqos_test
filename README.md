
# Test task for LoqosAI

Telegram bot with useful information for relocation to Cyprus 




## How to run locally

Clone the Repository:

```bash
  git clone https://github.com/igorvg/loqos_test.git
  cd your-repo-name
```
Create and Activate a Virtual Environment (optional but recommended):

```bash
 python -m venv venv
 source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install the Required Dependencies:

```bash
  pip install -r requirements.txt
```

Train the Model:

```bash
  rasa train
```
#### Run the Rasa Bot:

Expose your local server to the internet using ngrok:

*In a separate terminal, start ngrok to expose port 5005:*

```bash
  ngrok http 5005
```
*ngrok will provide a forwarding URL (something like http://xxxxxx.ngrok.io). You can use this URL to interact with your bot from external sources.*

Change the **credentials.yml** to run bot locally:

```yml
  telegram:
  access_token: "<TOKEN>"
  verify: "loqos_test_igor_bot"
  webhook_url: "<YOUR LINK FROM NGROK>/webhooks/telegram/webhook"
```
Set the link from ngrok to <YOUR LINK FROM NGROK> field

Run the Rasa bot:

```bash
  rasa run actions && rasa run --enable-api --cors "*" --debug

```
