#!/usr/bin/env python3
"""Generate the static site (English at root, Chinese under zh/).

Edit the content below, then run:  python3 build.py
Facts come only from assets/data.js and the CV source (cv_A.tex).
"""
from pathlib import Path

ROOT = Path(__file__).parent

EMAIL = "sn.liu0323@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/snliu323"
GITHUB = "https://github.com/S-N-Lewis"
CV_PDF = "assets/Suning_Liu_CV.pdf"

NAV = [
    ("index.html", "Home", "首页"),
    ("about.html", "About", "关于"),
    ("projects.html", "Projects", "项目"),
    ("experience.html", "Experience", "经历"),
    ("notes/index.html", "Notes", "笔记"),
    ("cv.html", "CV", "简历"),
    ("contact.html", "Contact", "联系"),
]

PROJECTS = [
    ("kiwileap", f"{GITHUB}/kiwileap",
     "An AI agent pipeline for job hunting in New Zealand. It scans several job boards, scores listings against a profile and shows the results on a local dashboard. The data stays on your own machine.",
     "一套用于在新西兰找工作的 AI agent 流程：扫描多个招聘网站，按个人资料给岗位打分，结果显示在本地面板上。数据留在自己的电脑里。"),
    ("education-academic-editor-perspective", f"{GITHUB}/education-academic-editor-perspective",
     "A Claude Code skill that reviews an academic manuscript twice: once from a subject expert’s point of view and once from a journal editor’s.",
     "一个 Claude Code 技能，把一篇学术稿件审两遍：一遍从领域专家的角度，一遍从期刊编辑的角度。"),
    ("ielts-adhd", f"{GITHUB}/ielts-adhd",
     "An IELTS practice tool for speaking, writing, listening and vocabulary chunks, with progress tracking. It is designed to make starting a study session easier.",
     "雅思练习工具，包括口语、写作、听力和语块，并记录进度。设计重点是让人更容易开始学习。"),
    ("guiwei 归位", f"{GITHUB}/guiwei",
     "A macOS app that reads what is in a file, sorts it into a category, renames it and archives it. It runs offline.",
     "一个 macOS 应用：读取文件内容，分类、重命名并归档。全程离线运行。"),
    ("rewild", f"{GITHUB}/rewild",
     "A tool that detects common patterns of AI-generated writing and helps rewrite them.",
     "识别常见 AI 写作痕迹并帮助改写的工具。"),
    ("lugshare 顺路捎", f"{GITHUB}/lugshare",
     "A WeChat mini-program that matches travellers who have spare luggage allowance with people who need something carried.",
     "一个微信小程序：把有空余行李额的旅客，和需要请人带东西的人配对。"),
]

# (dates_en, dates_zh, title_en, title_zh, place_en, place_zh, note_en, note_zh)
TIMELINE = [
    ("2026", "2026",
     "Master of Education (Research)", "教育学硕士（研究型）",
     "University of Auckland", "奥克兰大学",
     "Thesis: a systematic review of generative AI in Chinese higher vocational education. Thesis submitted July 2026 and accepted; degree not yet conferred.",
     "论文：生成式 AI 在中国高职教育中的系统综述。论文于 2026 年 7 月提交并已通过，学位尚未授予。"),
    ("2023 – 2025", "2023 – 2025",
     "Student Programmes Coordinator (Senior)", "学生工作统筹（高级）",
     "Zhejiang Vocational Academy of Art, Hangzhou", "浙江艺术职业学院，杭州",
     "Coordinated student support, wellbeing and co-curricular programmes across seven faculties.",
     "统筹全校七个二级学院的学生支持、身心健康和第二课堂项目。"),
    ("2021 – 2023", "2021 – 2023",
     "Counsellor, School of Drama and Film", "辅导员，戏剧影视学院",
     "Zhejiang Vocational Academy of Art, Hangzhou", "浙江艺术职业学院，杭州",
     "One-to-one support for about 400 students and careers support for graduates. Designed and piloted conversational generative-AI tools for career planning.",
     "负责约 400 名学生的日常支持和毕业生就业指导。设计并试用了用于职业规划的对话式生成式 AI 工具。"),
    ("Jul – Sep 2021", "2021 年 7 – 9 月",
     "Course Instructor and Head Teacher (secondment)", "课程教师兼班主任（借调）",
     "Zhejiang Special Education Vocational College, Hangzhou", "浙江特殊教育职业学院，杭州",
     "Taught two cohorts of blind and visually impaired learners in a piano tuning programme, adapting materials to each learner.",
     "为钢琴调律专业的两届盲人和视障学员授课，并按每位学员的需要调整教材和教法。"),
    ("2018 – 2021", "2018 – 2021",
     "Student Engagement Officer", "学生工作干事",
     "Zhejiang Vocational Academy of Art, Hangzhou", "浙江艺术职业学院，杭州",
     "Homeroom teacher for a class of 49 and daily support in a student residence.",
     "担任一个 49 人班级的班主任，并负责学生宿舍的日常工作。"),
    ("2020", "2020",
     "Bachelor of Arts, Musicology (Arts Management)", "音乐学（艺术管理）学士",
     "Central Conservatory of Music, Beijing", "中央音乐学院，北京",
     "Completed alongside full-time work.", "在全职工作的同时完成。"),
]


def t(lang, en, zh):
    return en if lang == "en" else zh


def ext(href, label):
    return f'<a href="{href}" rel="me noopener">{label}</a>'


def page_home(lang, p):
    links = " · ".join([
        f'<a href="{p}{CV_PDF}">{t(lang, "CV (PDF)", "简历（PDF）")}</a>',
        ext(LINKEDIN, "LinkedIn"), ext(GITHUB, "GitHub"),
        f'<a href="mailto:{EMAIL}">{t(lang, "Email", "邮件")}</a>',
    ])
    if lang == "en":
        body = f"""
<h1 class="name">Suning (Simon) Liu</h1>
<p class="lead">I am an educator living in Auckland, New Zealand.</p>
<p>Before moving here I spent over six years (September 2018 to February 2025) at Zhejiang Vocational Academy of Art in Hangzhou, working in student support, careers guidance and programme coordination. I also taught blind and visually impaired learners at Zhejiang Special Education Vocational College. These days I am interested in how generative AI can help with learning and career planning, and I build small tools to try ideas out, such as <a href="{GITHUB}/kiwileap">kiwileap</a>. My Master of Education (Research) thesis at the University of Auckland has been accepted; the degree is not yet conferred.</p>"""
    else:
        body = f"""
<h1 class="name">Suning (Simon) Liu</h1>
<p class="lead">我是一名教育工作者，现在住在新西兰奥克兰。</p>
<p>来新西兰之前，我在杭州的浙江艺术职业学院工作了六年多（2018 年 9 月至 2025 年 2 月），做学生工作、就业指导和项目统筹，其间也在浙江特殊教育职业学院给盲人和视障学员上过课。现在我关心生成式 AI 怎样帮助学习和职业规划，也会自己动手做一些小工具来验证想法，比如 <a href="{GITHUB}/kiwileap">kiwileap</a>。我在奥克兰大学攻读教育学硕士（研究型），论文已经通过，学位尚未授予。</p>"""
    return t(lang, "Suning Liu", "Suning Liu"), body + f'\n<p class="links">{links}</p>'


def page_about(lang, p):
    if lang == "en":
        return "About", f"""
<h1>About</h1>
<p>I worked at Zhejiang Vocational Academy of Art, a public arts college in Hangzhou, from September 2018 to February 2025. I held three roles there: Student Engagement Officer, then Counsellor in the School of Drama and Film, then Student Programmes Coordinator. Most of the work was looking after students: pastoral care, wellbeing, careers support and the programmes that run around their studies.</p>
<p>In 2021 I was seconded to Zhejiang Special Education Vocational College, where I taught blind and visually impaired learners in a piano tuning programme. Adapting materials for each learner taught me a lot about how teaching has to fit the person.</p>
<p>As a counsellor I designed and piloted conversational generative-AI tools for career planning. They were organised around the stages of career planning and helped students name their strengths, clarify their interests and map out possible paths. Since then I have kept building small tools, which are listed on the <a href="{p}projects.html">Projects</a> page.</p>
<p>I studied for a Master of Education (Research) at the University of Auckland. My thesis is a systematic review of generative AI in Chinese higher vocational education. It has been accepted, and the degree is not yet conferred. Before that I completed a Bachelor of Arts in Musicology (Arts Management) at the Central Conservatory of Music while working full-time.</p>
<p>In Auckland I volunteer as a cross-cultural conversation facilitator with Acquaint NZ and with the Motutapu Island Restoration Trust. I speak Mandarin and English.</p>"""
    return "关于", f"""
<h1>关于</h1>
<p>2018 年 9 月到 2025 年 2 月，我在杭州的公办艺术高职院校浙江艺术职业学院工作，先后做过学生工作干事、戏剧影视学院辅导员和学生工作统筹。大部分工作是照顾学生：日常关怀、身心健康、就业指导，以及围绕学业开展的各类项目。</p>
<p>2021 年我被借调到浙江特殊教育职业学院，给钢琴调律专业的盲人和视障学员上课。为每位学员调整教材的过程让我明白，教学必须贴合具体的人。</p>
<p>做辅导员期间，我设计并试用了用于职业规划的对话式生成式 AI 工具。工具按职业规划的各个阶段来组织，帮助学生说清自己的长处、理清兴趣、规划可能的方向。之后我一直在做一些小工具，列在<a href="{p}projects.html">项目</a>页。</p>
<p>我在奥克兰大学攻读教育学硕士（研究型），论文是关于生成式 AI 在中国高职教育中的系统综述，已经通过，学位尚未授予。此前我在全职工作的同时，完成了中央音乐学院音乐学（艺术管理）专业的本科学业。</p>
<p>在奥克兰，我在 Acquaint NZ 做跨文化对话志愿者，也参加 Motutapu Island Restoration Trust 的生态保护志愿活动。我会说普通话和英语。</p>"""


def page_projects(lang, p):
    items = []
    for name, url, en, zh in PROJECTS:
        items.append(f"""<li class="item">
  <h2><a href="{url}">{name}</a></h2>
  <p>{t(lang, en, zh)}</p>
  <p class="meta"><a href="{url}">{url.replace("https://", "")}</a></p>
</li>""")
    intro = t(lang, "Things I have built. All of them are public repositories on GitHub.",
              "我做过的东西，都是 GitHub 上的公开仓库。")
    title = t(lang, "Projects", "项目")
    return title, f'<h1>{title}</h1>\n<p class="intro">{intro}</p>\n<ul class="list">\n' + "\n".join(items) + "\n</ul>"


def page_experience(lang, p):
    rows = []
    for de, dz, te, tz, pe, pz, ne, nz in TIMELINE:
        rows.append(f"""<li>
  <p class="when">{t(lang, de, dz)}</p>
  <div>
    <h2>{t(lang, te, tz)}</h2>
    <p class="meta">{t(lang, pe, pz)}</p>
    <p>{t(lang, ne, nz)}</p>
  </div>
</li>""")
    title = t(lang, "Experience", "经历")
    more = t(lang, f'More detail is in my <a href="{p}cv.html">CV</a>.',
             f'更多细节见<a href="{p}cv.html">简历</a>。')
    return title, f'<h1>{title}</h1>\n<ol class="timeline">\n' + "\n".join(rows) + f'\n</ol>\n<p class="intro">{more}</p>'


def page_notes(lang, p):
    title = t(lang, "Notes", "笔记")
    empty = t(lang, "No notes yet. When I publish something, it will be listed here.",
              "暂时还没有文章。发布之后会列在这里。")
    tpl = t(lang, "Layout template (not a real post)", "版式模板（不是正式文章）")
    return title, f"""<h1>{title}</h1>
<div class="empty"><p>{empty}</p></div>
<ul class="posts">
  <li><span class="tag">{t(lang, "Template", "模板")}</span> <a href="template.html">{tpl}</a></li>
</ul>"""


def page_template(lang, p):
    if lang == "en":
        return "Post template", f"""<article class="post">
<p class="tag">Template — not a real post</p>
<h1>Post title</h1>
<p class="meta"><time>YYYY-MM-DD</time></p>
<p>This page only shows how a note will look. It has no real content. To write a post, copy this file, replace the title, date and text, and add a link to it on the <a href="index.html">Notes</a> page.</p>
<h2>A subheading</h2>
<p>A paragraph of body text goes here.</p>
<blockquote><p>A quotation looks like this.</p></blockquote>
<ul><li>A list item</li><li>Another list item</li></ul>
<p><a href="index.html">← Back to Notes</a></p>
</article>"""
    return "文章模板", f"""<article class="post">
<p class="tag">模板 · 不是正式文章</p>
<h1>文章标题</h1>
<p class="meta"><time>YYYY-MM-DD</time></p>
<p>这一页只用来展示文章的版式，没有真实内容。写新文章时，复制这个文件，替换标题、日期和正文，再到<a href="index.html">笔记</a>页加上链接。</p>
<h2>小标题</h2>
<p>这里是正文段落。</p>
<blockquote><p>引文是这个样子。</p></blockquote>
<ul><li>列表项</li><li>另一个列表项</li></ul>
<p><a href="index.html">← 返回笔记</a></p>
</article>"""


def page_cv(lang, p):
    title = t(lang, "CV", "简历")
    if lang == "en":
        body = "<p>My CV covers my work in tertiary student support and teaching, my use of AI tools, and my education.</p>"
    else:
        body = "<p>简历包括我在高校学生工作和教学方面的经历、AI 工具的使用，以及教育背景。简历为英文版。</p>"
    dl = t(lang, "Download CV (PDF, 42 KB)", "下载简历（PDF，42 KB）")
    return title, f'<h1>{title}</h1>\n{body}\n<p class="links"><a class="button" href="{p}{CV_PDF}">{dl}</a></p>\n<p class="meta">{t(lang, "Updated November 2026.", "更新于 2026 年 11 月。")}</p>'


def page_contact(lang, p):
    title = t(lang, "Contact", "联系")
    intro = t(lang, "You can reach me here:", "可以通过以下方式联系我：")
    return title, f"""<h1>{title}</h1>
<p>{intro}</p>
<dl class="contact">
  <dt>{t(lang, "Email", "邮件")}</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
  <dt>LinkedIn</dt><dd>{ext(LINKEDIN, "linkedin.com/in/snliu323")}</dd>
  <dt>GitHub</dt><dd>{ext(GITHUB, "github.com/S-N-Lewis")}</dd>
</dl>"""


PAGES = {
    "index.html": page_home,
    "about.html": page_about,
    "projects.html": page_projects,
    "experience.html": page_experience,
    "notes/index.html": page_notes,
    "notes/template.html": page_template,
    "cv.html": page_cv,
    "contact.html": page_contact,
}


def render(path, lang):
    depth = path.count("/") + (1 if lang == "zh" else 0)
    p = "../" * depth                       # prefix to site root
    title, body = PAGES[path](lang, p)
    zh_href = f"{p}zh/{path}"
    en_href = f"{p}{path}"
    other = (zh_href, "中文", "zh-Hans") if lang == "en" else (en_href, "English", "en")
    here = (p if lang == "en" else p + "zh/")
    cur = ' aria-current="page"'
    nav = "".join(
        f'<a href="{here}{href}"{cur if (href == path or (path.startswith("notes/") and href == "notes/index.html")) else ""}>{t(lang, en, zh)}</a>'
        for href, en, zh in NAV)
    full_title = title if path == "index.html" else f"{title} · Suning Liu"
    robots = '\n<meta name="robots" content="noindex">' if "template" in path else ""
    desc = t(lang, "Suning (Simon) Liu, an educator in Auckland, New Zealand.",
             "Suning (Simon) Liu，新西兰奥克兰的教育工作者。")
    return f"""<!doctype html>
<html lang="{t(lang, "en", "zh-Hans")}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Simon.L">{robots}
<meta name="theme-color" content="#f8f4ec">
<link rel="alternate" hreflang="en" href="{en_href}">
<link rel="alternate" hreflang="zh-Hans" href="{zh_href}">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
<!--email_off-->
<a class="skip" href="#main">{t(lang, "Skip to content", "跳到正文")}</a>
<header class="site">
  <a class="home" href="{here}index.html">Suning Liu</a>
  <nav aria-label="{t(lang, "Main", "主导航")}">{nav}</nav>
  <a class="lang" href="{other[0]}" hreflang="{other[2]}" lang="{other[2]}">{other[1]}</a>
</header>
<main id="main">
{body}
</main>
<footer class="site">
  <p>© 2026 Suning Liu · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</footer>
<!--/email_off-->
</body>
</html>
"""


def main():
    for lang in ("en", "zh"):
        for path in PAGES:
            out = ROOT / (path if lang == "en" else f"zh/{path}")
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(render(path, lang), encoding="utf-8")
    print("built", len(PAGES) * 2, "pages")


if __name__ == "__main__":
    main()
