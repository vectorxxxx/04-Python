with open('D:/workspace-demo/democode/[ggzyjy28-039218]关于组件外需求梳理工作及新组件推广事宜/ztb.properties', encoding='utf-8') as f:
    for line in f.readlines():
        v = line.strip()
        if v != '':
            print(v.split('='))
