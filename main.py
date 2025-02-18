import re
import sys
from collections import defaultdict
import os
# ----------- 自定义命令替换字典 -----------
cmd_map = {
    r'\\R\b': r'\\mathbb{R}',
    r'\\Z\b': r'\\mathbb{Z}',
    r'\\C\b': r'\\mathbb{C}',
    r'\\N\b': r'\\mathbb{N}',
    r'\\Q\b': r'\\mathbb{Q}',
    r'\\tr\{([^}]*)\}': r'',      # 红色文本转为加粗
    r'\\mydef\{([^}]*)\}': r'**\1**',   # 自定义定义加粗,
    r'\\text\{([^}]*)\}': r'\$\\text{\1}\$',
    r'\\t\{([^}]*)\}': r'\\text{\1}',           # 移除\text命令
    r'\\t\b':r'\\text',
    r'\\label\{([^}]*)\}': r'',          # 删除label
    r'\\ref\{([^}]*)\}': r'',            # 删除ref
    r'\\textbf\{(.*?)\}' : r'**\1**',
    r'\\hr\{(.*?)\}' : r'\\text{\1}',
    r'\\Sy\[([0-9]*)\]':r'\\text{Sylow} \1-子群',
    r'\\lAbel' : r'有限 \\text{Abel}\\ ',
    r'\\chaptermark\{(.*?)\}':r'',
    r'\\newpage\b':r'',
    r'\\problem\[(.*?)\]':r'\n**\1**:',
    r'\\problem\b':r'\n- ',
    r'\\hfil\b':r'\ ',
    # 添加更多命令替换规则...
}
cmd_text = {
    'tIm':'Im',
    'Arg':'Arg',
    'Ker':'Ker',
    'ti':'i',
    'Aut':'Aut',
    'Inn':'Inn',
    'td':'d',
    'Abel':'Abel',
    'rad':'rad',
}

# ----------- 定理环境配置 -----------
theorem_envs = {
    'definition': {'title': '定义', 'counter': defaultdict(int)},
    'theorem': {'title': '定理', 'counter': defaultdict(int)},
    'example': {'title': '例', 'counter': defaultdict(int)},
    'proposition': {'title': '命题', 'counter': defaultdict(int)},
    'corollary': {'title': '推论', 'counter': defaultdict(int)},
    'remark': {'title': '注', 'counter': defaultdict(int)},
    'proof': {'title': '证明', 'counter': defaultdict(int)},
    'property': {'title': '性质', 'counter': defaultdict(int)},
    'lemma': {'title': '引理', 'counter': defaultdict(int)},
    'solution': {'title': '解:', 'counter': defaultdict(int)},
    'definition*': {'title': '定义', 'counter': defaultdict(int)},
    'theorem*': {'title': '定理', 'counter': defaultdict(int)},
    'example*': {'title': '例', 'counter': defaultdict(int)},
    'proposition*': {'title': '命题', 'counter': defaultdict(int)},
    'corollary*': {'title': '推论', 'counter': defaultdict(int)},
    'remark*': {'title': '注', 'counter': defaultdict(int)},
    'proof*': {'title': '证明', 'counter': defaultdict(int)},
    'property*': {'title': '性质', 'counter': defaultdict(int)},
    'lemma*': {'title': '引理', 'counter': defaultdict(int)},
}


# ----------- 处理环境的函数 -----------


def process_begin(m,cnt):
    global flag
    # print(m)
    if m.group(1) in theorem_envs:
        flag = True
        space = "    "
        # print(m.group(3))
        env_config = theorem_envs[m.group(1)]
        if m.group(2) != None:
            title = f"**{env_config['title']} {m.group(2)}**"
        else:
            title = f"**{env_config['title']}**"
        content = m.group(3).strip()
        return f"\n{space*cnt}{title}\n\n{space*cnt}- {content}\n"
    elif m.group(1) == "itemize":
        flag = True
        return re.sub(r'((?:[^\S\n])*)\\item(\s*)\[(.*?)\]',lambda x: f'{x.group(3)}',m.group(3))
    else:
        if m.group(2) != None:
            return f"\\begin{{{m.group(1)}}}[{m.group(2)}] {m.group(3)}\\end{{{m.group(1)}}}"
        else:
            return f"\\begin{{{m.group(1)}}} {m.group(3)}\\end{{{m.group(1)}}}"

def work_meta(m):
    s = m.group(1)
    s = re.sub(r'%','',s,flags=re.DOTALL)
    return f'---\n{s}\n---\n'
# ----------- 主处理函数 -----------
def latex_to_markdown(content,title):
    global current_section
    output = []
    meta = f'''---
title : {title}
author : uuku
date : 2024-06-30
tags : []
categories : [数学]
---

'''
    if re.search(r'%---(.*?)%---',content,flags=re.DOTALL):
        content = re.sub(r'%---(.*?)%---',lambda m:work_meta(m),content,flags=re.DOTALL)
    else:
        content = meta + content
    # 处理定理环境
    cnt = 0
    flag = True
    while flag:
        flag = False
        content = re.sub(r'\\begin{(.*)}(?:(?:\\)?)(?:(?:\[(.*?)\])?)(.*?)\\end{(\1)}', 
                        lambda m:process_begin(m,0),
                        content, flags=re.DOTALL)
        # print(len(content),len(last))
        cnt += 1
    # cnt = 0
    # flag = True
    # while flag:
    #     flag = False
    #     content = re.sub(r'\\begin{(.*)}(.*?)\\end{(\1)}',  
    #                     lambda m:process_begin(m,0,cnt),
    #                     content, flags=re.DOTALL)
    #     cnt += 1
    # print(content)
    # 处理标题
    content = re.sub(r'\\chapter{(.*)}',r'# \1',content)
    content = re.sub(r'\\section{(.*)}',r'## \1',content)
    content = re.sub(r'\\subsection{(.*)}',r'### \1',content)
    
    content = re.sub(r'\\chapter*{(.*)}',r'# \1',content)
    content = re.sub(r'\\section*{(.*)}',r'## \1',content)
    content = re.sub(r'\\subsection*{(.*)}',r'### \1',content)

    for pattern, replacement in cmd_map.items():
        content = re.sub(pattern, replacement, content)

    for pattern, replacement in cmd_text.items():
        content = re.sub(r'\\'+pattern+r'\b',r'\\text{'+replacement+r'}',content)
    output = content
    return output
# ----------- 执行转换 -----------
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python latex2md.py input.tex output.tex")
        sys.exit(1)
    # print(sys.argv[1])
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        latex_content = f.read()
    tmp,fileName = os.path.split(sys.argv[2])
    markdown_content = latex_to_markdown(latex_content,os.path.splitext(fileName)[0])
    filePath = os.path.dirname(sys.argv[2])
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"转换完成，结果已保存到 {sys.argv[2]}")