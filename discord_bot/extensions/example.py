import hikari
import lightbulb

#name
plugin = lightbulb.Plugin('Example')

#listen type of event
@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print(event.content)

@plugin.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
    await context.respond('Pong!')

#function
def load(bot):
    bot.add_plugin(plugin)