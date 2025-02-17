import re
import sys
from collections import defaultdict

# ----------- 自定义命令替换字典 -----------
cmd_map = {
    r'\\R\b': r'\\mathbb{R}',
    r'\\Z\b': r'\\mathbb{Z}',
    r'\\C\b': r'\\mathbb{C}',
    r'\\N\b': r'\\mathbb{N}',
    r'\\Q\b': r'\\mathbb{Q}',
    r'\\tr\{([^}]*)\}': r'',      # 红色文本转为加粗
    r'\\mydef\{([^}]*)\}': r'**\1**',   # 自定义定义加粗
    r'\\t\{([^}]*)\}': r'\\text{\1}',           # 移除\text命令
    r'\\label\{([^}]*)\}': r'',          # 删除label
    r'\\ref\{([^}]*)\}': r'',            # 删除ref
    r'\\tIm': r'\\text{Im}',            # tIm
    r'\\ti': r'\\text{i}',            # ti
    r'\\Arg': r'\\text{Arg}',            # Arg
    r'\\Ker': r'\\text{Ker}',            # Ker
    r'\\textbf\{(.*?)\}' : r'**\1**',
    # 添加更多命令替换规则...
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
    'definition*': {'title': '定义', 'counter': defaultdict(int)},
    'theorem*': {'title': '定理', 'counter': defaultdict(int)},
    'example*': {'title': '例', 'counter': defaultdict(int)},
    'proposition*': {'title': '命题', 'counter': defaultdict(int)},
    'corollary*': {'title': '推论', 'counter': defaultdict(int)},
    'remark*': {'title': '注', 'counter': defaultdict(int)},
    'proof*': {'title': '证明', 'counter': defaultdict(int)},
    'property*': {'title': '性质', 'counter': defaultdict(int)},
}


# ----------- 处理环境的函数 -----------


def process_begin(m,opt,cnt):
    if m.group(1) in theorem_envs:
        space = "    "
        print(m.group(1))
        env_config = theorem_envs[m.group(1)]
        if opt:
            title = f"**{env_config['title']} {m.group(3)}**"
        else:
            title = f"**{env_config['title']}**"
        content = m.group(2+opt).strip()
        return f"\n{space*cnt}{title}\n\n{space*cnt}- {content}\n"
    elif m.group(1) == "itemize":
        # return m.group(2+opt)
        return re.sub(r'((?:[^\S\n])*)\\item(\s*)\[(.*?)\]',lambda x: f'{x.group(3)}',m.group(2+opt))
    else:
        if opt:
            return f"\\begin{{{m.group(1)}}}[{m.group(3)}] {m.group(4)}\\end{{{m.group(1)}}}"
        else:
            return f"\\begin{{{m.group(1)}}}{m.group(2)}\\end{{{m.group(1)}}}"
def work_meta(m):
    s = m.group(1)
    s = re.sub(r'%','',s,flags=re.DOTALL)
    return f'---{s}---\n'
# ----------- 主处理函数 -----------
def latex_to_markdown(content):
    global current_section
    output = []
    content = re.sub(r'%---(.*?)%---',lambda m:work_meta(m),content,flags=re.DOTALL)
    # 处理定理环境
    cnt = 0
    while True:
        last = content
        content = re.sub(r'\\begin{(.*)}(\s*)\[(.*?)\](.*?)\\end{(\1)}', 
                        lambda m:process_begin(m,2,cnt),
                        content, flags=re.DOTALL)
        if last == content:
            break
        cnt += 1
    cnt = 0
    while True:
        last = content
        content = re.sub(r'\\begin{(.*)}(.*?)\\end{(\1)}', 
                        #lambda m: f'**{theorem_envs[m.group(1)]['title']}**\n {m.group(2)}\n', 
                        lambda m:process_begin(m,0,cnt),
                        content, flags=re.DOTALL)
        if last == content:
            break
        cnt += 1
    # print(content)
    # 处理标题
    content = re.sub(r'\\chapter{(.*)}',r'# \1',content)
    content = re.sub(r'\\section{(.*)}',r'## \1',content)
    content = re.sub(r'\\subsection{(.*)}',r'### \1',content)

    for pattern, replacement in cmd_map.items():
        content = re.sub(pattern, replacement, content)
    # 处理自定义命令

    # lines = content.split('\n')
    # print(content)
    # 处理章节结构
    # for line in lines:
    #     # 章节标题
    #     if line.startswith(r'\chapter'):
    #         title = re.sub(r'\\chapter{(.*?)}', r'# \1', line)
    #         output.append(title)
    #         current_section += 1
    #     elif line.startswith(r'\section'):
    #         title = re.sub(r'\\section{(.*?)}', r'## \1', line)
    #         output.append(title)
    #     elif line.startswith(r'\subsection'):
    #         title = re.sub(r'\\subsection{(.*?)}', r'### \1', line)
    #         output.append(title)
    #     else:
    #         # 处理定理环境
    #         theorem_match = re.search(r'\\begin{(\w+)}(.*?)\\end{\1}', line, flags=0)
    #         # print(theorem_match)
    #         if theorem_match:
    #             env_name = theorem_match.group(1)
    #             print(env_name)
    #             if env_name in theorem_envs:
    #                 print(1)
    #                 processed = process_theorem_env(theorem_match, env_name)
    #                 output.append(processed)
    #             else:
    #                 output.append(line)  # 非标准环境直接保留
    #         else:
    #             # 替换自定义命令
    #             processed_line = line
    #             for pattern, replacement in cmd_map.items():
    #                 processed_line = re.sub(pattern, replacement, processed_line)
    #             # 处理行内数学公式
    #             processed_line = re.sub(r'\$(.*?)\$', r'$\1$', processed_line)
    #             output.append(processed_line)
    output = content
    return output
# ----------- 执行转换 -----------
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python latex2md.py input.tex")
        sys.exit(1)
    
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        latex_content = f.read()
    
    markdown_content = latex_to_markdown(latex_content)
    
    with open('output.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print("转换完成，结果已保存到 output.md")