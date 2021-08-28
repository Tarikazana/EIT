# EIT
Easily keep track of all Invites on your Server. This is "Easy Invite Tracker".

## How it works:
- The bot will create a list with all active invites, updating it automatically. As soon as a user joins it can tell, based on this list, who invited the user and what code the user joined with.
- By default, this information get's send to the sys channel of a server. You can change the channel with the following command: `eit.channel [channel-id/channel mention]`

## Hosting your own bot:
- fill in the file [config.json](https://github.com/Tarikazana/EIT/blob/main/config.json) with your token.
- Make sure you have python installed (developed in V3.9.6)
- Make sure to create following directories in the same Folder as the [main.py](https://github.com/Tarikazana/EIT/blob/main/main.py)
`/data` `/server_configs`
- Have "Privileged Gateway Intents" enabled
- you may need to change directory names based on where you'll run the bot
- start the bot by running the [main.py](https://github.com/Tarikazana/EIT/blob/main/main.py) file
