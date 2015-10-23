import os
import base64
import cStringIO
import textwrap

from PIL import Image, ImageDraw, ImageFont

def generate_ad(ad):
    img = Image.new('RGB', (800,800), '#ff5a5f')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(os.path.dirname(os.path.abspath(__file__))+'/static/HelveticaNeue.ttf', 48)

    dear = 'Dear {0},'.format(ad.dear)
    message = '{0}'.format(ad.message)
    messages = textwrap.wrap(message, width=27)

    love = 'Love,'
    sender = ad.sender
    love_w, love_h = draw.textsize(love, font=font)
    sender_w, sender_h = draw.textsize(sender, font=font)

    draw.text((80, 40), dear, font = font)
    for idx, msg in enumerate(messages):
        draw.text((80, 150+(50*idx)), msg, font = font)
    draw.text((800-love_w-80, 800-(love_h*2)-40), love, font = font)
    draw.text((800-sender_w-80, 800-(sender_h)-40), sender, font = font)
    del draw

    buffer = cStringIO.StringIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue())
