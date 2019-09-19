from generate.format import easyMail

email = '/Users/cpratt/Python/easymail/text/09102019-Nasrin.txt'
template = '/Users/cpratt/Python/easymail/templates/hero/hero_template.txt'
hero_image = 'https://aaf1a18515da0e792f78-c27fdabe952dfc357fe25ebf5c8897ee.ssl.cf5.rackcdn.com/1839/06282019-Nasrin-600x300.png?v=1561066921000'
preview_text = 'You can help get Nasrin back to her family. Add your name right now.'
url = 'campaignpage_url~143333~https://act.amnestyusa.org/page/40634/action/1?ac=W1910EDIAR1'
donate_footer_url = 'campaignpage_url~150295~https://donate.amnestyusa.org/page/43415/donate/1?ac=W1910EDIAR1'
credit = ''

f_email = easyMail(template=template, uf_email_filepath=email,
                   hero_image=hero_image, preview_text=preview_text, url=url, donate_footer_url=donate_footer_url, button=True, action=True, credit=credit)

f_email.create_email()


