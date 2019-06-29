from generate.format import easyMail

email = '/Users/cpratt/Python/easymail/text/01072019-Border-Action-2.txt'
template = '/Users/cpratt/Python/easymail/templates/hero/hero_template.txt'
hero_image = 'https://aaf1a18515da0e792f78-c27fdabe952dfc357fe25ebf5c8897ee.ssl.cf5.rackcdn.com/1839/27062019-border-advocacy-590px.png?v=1561639801000'
preview_text = 'Independence Day, but not for kids in detention.'
url = 'campaignpage_url~152216~https://act.amnestyusa.org/page/44804/action/1?ac=W1907EARMR1'

f_email = easyMail(template=template, uf_email_filepath=email,
                   hero_image=hero_image, preview_text=preview_text, url=url, button=True, action=True)

f_email.create_email()
