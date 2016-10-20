import requests

from config import MashapeKey as mashape_key


# Urban Dictionary API
async def ud(cmd, message, args):
    ud_input = ' '.join(args)
    entry = ud_input[-2:]

    if entry.strip().isnumeric():
        ud_input = ud_input[:-2]  # stripping entry from the term
        if int(entry) > 10:
            await cmd.reply('Out of boundary, please select a number from `1` to `10`')
            return
        entry = int(entry) - 1  # converting the entry number
    else:
        entry = 0

    url = "https://mashape-community-urban-dictionary.p.mashape.com/define?term=" + ud_input
    headers = {'X-Mashape-Key': mashape_key, 'Accept': 'text/plain'}
    response = requests.get(url, headers=headers).json()
    result_type = str((response['result_type']))

    if result_type == 'exact':
        try:
            definition = str((response['list'][entry]['definition']))
            example = str((response['list'][0]['example']))
            await cmd.reply('Word: `' + ud_input + '`\n'
                                      'Definition:\n```' + definition + '```\n' +
                                      'Example:\n```' + example + '\n```')
        except IndexError:
            await cmd.reply('Something went wrong... The API dun goofed...')
    elif result_type == 'no_results':
        try:
            await cmd.reply('No results :cry:')
        except:
            await cmd.reply('Something went wrong, and we don\'t know what!')
