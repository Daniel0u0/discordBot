import hikari
import lightbulb

bot = lightbulb.BotApp(
    token='',
    default_enabled_guilds=()
    )

#load all .py files in the path
bot.load_extensions_from('./extensions')






'''
#create event
@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')

#create slash command
@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(context):
    await context.respond('Pong!')

#create grp, cannot run grp command itself
@bot.command
@lightbulb.command('group', 'This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(context): #pass= do nothing
    pass 

#create subcommand
@my_group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(context):
    await context.respond('I am a subcommand!')

@bot.command#using option here has no 's'
@lightbulb.option('num1', 'This first number', type=float)
@lightbulb.option('num2', 'The seconde number',type=float)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(context):#using option here has 's'
    await context.respond(context.options.num1 + context.options.num2)

'''


bot.run()
