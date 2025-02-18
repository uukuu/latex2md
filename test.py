import re
import sys
from collections import defaultdict
# s='''\\begin{proof}
#         考虑 $\\alpha$ 是实系数多项式 $P(z)$ 的一个根, 那么 $$
#         \\begin{aligned}
#         P(\\overline{\\alpha}) &= a_0\\overline{\\alpha}^n+\\cdots+a_n\\\\
#         &=a_0\\overline{\\alpha^n}+\\cdots+a_n\\\\
#         &=\\overline{a_0\\alpha^n+\\cdots+a_n}\\\\
#         &=\\overline{P(\\alpha)}=\\overline{0}=0.
#         \\end{aligned}$$
#  \\end{proof}'''
# # print(s)
# print(re.search(r'\\begin{(\w+)}(.*?)\\end{(\1)}',s,flags=re.DOTALL).span())
# s = re.sub(r'\\begin{(\w+)}(.*?)\\end{(\1)}', 
#                     lambda m: f'\\begin{{{m.group(1)}}} {re.sub('\n','',m.group(2),flags=re.M)} \\end{{{m.group(1)}}}', 
#                     s, flags=re.DOTALL)
# print(s)

# s2 = '\\begin{theorem} [棣莫弗 (De Moivre)]    $(\\cos\\theta+\\ti\\sin\\theta)^n=\\cos n\\theta+\\ti\\sin n\\theta$. \\end{theorem}'
# s2 = '''\\begin{itemize}[leftmargin=3cm]
# 	\\item[乘法:] 模长相乘, 辐角相加.
# 	\\item[除法:] 模长相除, 辐角相减.
# \\end{itemize}'''
# # print(re.search(r'\\begin{(\w+)}(.*?)\\end{(\1)}',s2,flags=0).span())
# # print(re.sub(r'\\begin{(\w+)}(.*?)\\end{(\1)}',s2,flags=0).span())
# theorem_envs = {
#     'definition': {'title': '定义', 'counter': defaultdict(int)},
#     'theorem': {'title': '定理', 'counter': defaultdict(int)},
#     'example': {'title': '例', 'counter': defaultdict(int)},
#     'proposition': {'title': '命题', 'counter': defaultdict(int)},
#     'corollary': {'title': '推论', 'counter': defaultdict(int)},
#     'remark': {'title': '注', 'counter': defaultdict(int)},
#     'proof': {'title': '证明', 'counter': defaultdict(int)},
#     'property': {'title': '性质', 'counter': defaultdict(int)},
#     'definition*': {'title': '定义', 'counter': defaultdict(int)},
#     'theorem*': {'title': '定理', 'counter': defaultdict(int)},
#     'example*': {'title': '例', 'counter': defaultdict(int)},
#     'proposition*': {'title': '命题', 'counter': defaultdict(int)},
#     'corollary*': {'title': '推论', 'counter': defaultdict(int)},
#     'remark*': {'title': '注', 'counter': defaultdict(int)},
#     'proof*': {'title': '证明', 'counter': defaultdict(int)},
#     'property*': {'title': '性质', 'counter': defaultdict(int)},
# }
# def process_begin(m,opt):
#     if m.group(1) in theorem_envs:
#         print(m.group(1))
#         env_config = theorem_envs[m.group(1)]
#         if opt:
#             title = f"**{env_config['title']} {m.group(3)}**"
#         else:
#             title = f"**{env_config['title']}**"
#         content = m.group(2+opt).strip()
#         return f"\n{title}\n\n{content}\n"
#     else:
#         if opt:
#             return f"\\begin{{{m.group(1)}}}[{m.group(3)}] {m.group(4)}\\end{{{m.group(1)}}}"
#         else:
#             return f"\\begin{{{m.group(1)}}}{m.group(2)}\\end{{{m.group(1)}}}"


# s2 = re.sub(r'\\begin{(.*)}(\s*)\[(.*?)\](.*?)\\end{(\1)}', 
#                     #lambda m: f'**{theorem_envs[m.group(1)]['title']}**\n {m.group(2)}\n', 
#                     lambda m:process_begin(m,2),
#                     s2, flags=re.DOTALL)
# print(s2)


s ='''	\\item[乘法:] 模长相乘, 辐角相加.
	\\item[除法:] 模长相除, 辐角相减.
'''

s = re.sub(r'(\s*)\\item(\s*)\[(.*?)\]',lambda x: f'{x.group(3)}',s)
print(s)

s = r'\\'+'a'
print(s)