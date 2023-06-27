from dhooks import Webhook, Embed

embed = Embed(
        title='CfxHosting',
        url='https://cfxhosting.fr',
        description='**Attaque détectée sur :**\n``CfxHosting France``\n\n**ISP:**\n``CfxHosting``\n\n**RDNS:**\n``panel.cfxhosting.fr``\n\n**Location:**\n``Paris, FR``\n\n**Notre système de filtrage s en occuppe !**',
        color=0x00bbff,#=blue
        timestamp='now'
        )

embed.set_thumbnail('https://miro.medium.com/v2/resize:fit:1400/1*JY1afR9MoaK-Ih3DnIQ7WA.gif')

embed.set_image('https://cdn.discordapp.com/attachments/1101441921030836245/1120749747788070912/IMG_6370.png')

embed.set_footer(text="Attaque Détecté")

hook = Webhook('Votre Webhook')

hook.send(embed=embed)
