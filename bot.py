from telethon.sync import TelegramClient, events ,Button,functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
import asyncio,requests,time,os
from bs4 import BeautifulSoup

api_id = 1772559
api_hash = '0c7244423d05e7e4c48b937763d2fd62'

sesname = os.path.basename(__file__)[:-3]

def botyap():
    with TelegramClient(sesname, api_id, api_hash) as client:
        client.send_message('@BitcoinClick_bot', '🖥 Visit sites')

        #client.send_message('@BitcoinClick_bot', '🤖 Message bots')
        # client.send_message('@BitcoinClick_bot', '📣 Join chats')

        @client.on(events.NewMessage(from_users=["BitcoinClick_bot"]))
        async def handler(event):
            time.sleep(1.5)
            if """Press the "Visit website" button to earn BTC.""" in event.message.message:
                visiturl = event.message.reply_markup.rows[0].buttons[0].url
                time.sleep(0.5)
                sitecontent = requests.get(visiturl)
                if "Please solve the " in sitecontent.text:
                    messages = await client.get_messages("BitcoinClick_bot")
                    await messages[0].click(1, 1)
                else:
                    soup = BeautifulSoup(sitecontent.text, 'html.parser')
                    datatoken = soup.find(id='headbar')["data-token"]
                    datacode = visiturl.split('/')[4]
                    if (datatoken != ""):
                        requests.get(visiturl)
                        time.sleep(1)
                        formdata = {
                            "code": datacode,
                            "token": datatoken
                        }
                        requests.post("https://dogeclick.com/reward", formdata).text
                        if "You must wait" in requests.post("https://dogeclick.com/reward", formdata).text:
                            await client.send_message('@BitcoinClick_bot', '🖥 Visit sites')
            elif """Press the "Message bot" botton below.""" in event.message.message:
                botname = event.message.reply_markup.rows[0].buttons[0].url.split('/')[3].split('?')[0]

                @client.on(events.NewMessage(from_users=[botname]))
                async def handler(evennt):
                    await client.forward_messages("@BitcoinClick_bot", evennt.message)
                    await client(functions.messages.DeleteHistoryRequest(
                        peer=botname,
                        max_id=0,
                        just_clear=False,
                        revoke=False
                    ))

                await client.send_message(botname, "/start")
            elif """press the "Joined" button.""" in event.message.message:
                grupname = event.message.reply_markup.rows[0].buttons[0].url.split('/')[3]
                await client(JoinChannelRequest(grupname))
                messages = await client.get_messages("BitcoinClick_bot")
                await messages[0].click(0, 1)
                time.sleep(1)
                await client(LeaveChannelRequest(grupname))
            elif """"There is a new site for you to visit! 🖥""" in event.message.message:
                await client.send_message('@BitcoinClick_bot', '🖥 Visit sites')
            elif """Sorry, there are no new ads available. 😟""" in event.message.message:
                await client.send_message('me', 'BTC Botu 15 Dakika Beklemeye Girdi')
                time.sleep(900)
                await client.send_message('@BitcoinClick_bot', '🖥 Visit sites')

        client.run_until_disconnected()

botyap()
