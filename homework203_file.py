with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read().replace('.','').replace(',','').replace('-',' ').split()
    print(content)
    print(str(len(content)) + ' слова в тексте')