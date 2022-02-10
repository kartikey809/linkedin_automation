from http import client
import discum 
disc_bot = discum.Client(token="NTg5ODcwODM4NTM1NDIxOTYy.YWm9AQ.DG0dqlmFZcQyQzXb7bytyFdhIeU")

def mine_members(resp, guild_id):
    if disc_bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(disc_bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        disc_bot.gateway.removeCommand({'function': mine_members, 'params': {'guild_id': guild_id}})
        disc_bot.gateway.close()

def get_members_list(guild_id, channel_id):
    disc_bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    disc_bot.gateway.command({'function': mine_members, 'params': {'guild_id': guild_id}})
    disc_bot.gateway.run()
    disc_bot.gateway.resetSession()
    return disc_bot.gateway.session.guild(guild_id).members

members = get_members_list('867805499180318760', '867805499180318765')
memberslist = []

for memberID in members:
    memberslist.append(memberID)
    print(memberID)
    user = client.fetch_user(memberID)
    print(user)



# f = open('users.txt', "a")
# for element in memberslist:
#     f.write(element + '\n')
# f.close()