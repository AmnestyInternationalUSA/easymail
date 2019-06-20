from generate.format import easyMail
import re

email = '/Users/cpratt/Python/easymail/text/28062019-Nasrin-Cultivation.txt'
template = '/Users/cpratt/Python/easymail/templates/hero/hero_template.txt'
hero_image = 'https://aaf1a18515da0e792f78-c27fdabe952dfc357fe25ebf5c8897ee.ssl.cf5.rackcdn.com/1839/Nasrin405.png?v=1558031582000'
preview_text = 'One million people in 200 countries are demanding her freedom.'
url = 'https://www.amnesty.org/en/'

f_email = easyMail(template=template, uf_email_filepath=email,
                   hero_image=hero_image, preview_text=preview_text, url=url, button=False)
f_email.create_email()
