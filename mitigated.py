from dhooks import Webhook, Embed

embed = Embed(
        description='**Attaque mitigée :**\n``CfxHosting France``\n\n**Server Provider :**\n``CfxHosting``\n\n**Location:**\n``Paris, FR``\n\n**L attaque a été atténuée avec succès, CfxHosting a été retiré de l infrastructure d atténuation**',
        color=0xfafcfa,
        timestamp='now'
        )

embed.set_thumbnail('https://www.seekpng.com/png/full/205-2059350_safe-black-and-white-verified.png')
embed.set_footer(text="Attack Mitigée")

hook = Webhook('VOTRE WEBHOOK')

hook.send(embed=embed)
