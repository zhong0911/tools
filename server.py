def genOne(sun):
    if sun == 'www':
        return f'antx.cc,www.antx.cc|/www/wwwroot/{sun}|1|1|74'
    else:
        return f'{sun}.antx.cc|/www/wwwroot/{sun}|1|1|74'


suns = ['api', 'captcha', 'cdn', 'docs', 'download', 'image', 'link', 'open', 'passport', 'php', 'resource', 'security',
        'server', 'test', 'tools', 'translate', 'www', 'help', 'sdk', 'dns', 'user', 'u', 'music', 'url', 'admin',
        'status']


def main():
    for sun in suns:
        print(genOne(sun))


if __name__ == '__main__':
    main()
