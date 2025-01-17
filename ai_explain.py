# -*- coding: utf-8 -*-
import os
import json
from openai import OpenAI

def read_sentences_from_markdown(markdown_file):
    """从Markdown文件中读取单词和句子"""
    sentences_data = []
    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # 跳过表头和分隔线
        for line in lines[2:]:
            if '|' in line:
                parts = line.split('|')
                if len(parts) >= 3:
                    word = parts[1].strip()
                    sentence = parts[2].strip()
                    sentences_data.append({
                        'word': word,
                        'sentence': sentence
                    })
    return sentences_data

def analyze_word_usage(word, sentences):
    """使用LLM分析单词在句子中的用法"""
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://api.deepseek.com"
    )

    # 构建提示词
    prompt = f"""
            # Role
            Develop visual memory techniques for the English word "{word}"
            =========
            # Objective
            Requirements: Provide keywords and visual mnemonics, but don't directly reveal the Chinese meaning. Instead, incorporate the meaning into the mnemonic technique.
            ======
            # Rules
            Conditions: 
            1) The broken-down keywords must be simple and basic
            2) The imagery should be dramatic, exaggerated, specific, and vivid
            3) The Chinese meaning must be specially marked (e.g., in bold or within brackets)
            4) Follow the format shown in the Example section
            =======
            # Example：            
            - 英语：justice
            - 关键词：just（只）+ice（冰）
            - 图像描述：一个小孩跟妈妈抱怨被别的孩子打了。作为安慰，他只得到了一个冰激凌，但也算是**公平**地解决了。
            ---
            - 英语：tiptoe
            - 关键词：tip（脚尖）+ toe（脚趾）
            - 图像描述：一个小男孩踮着脚尖，偷偷摸摸地靠近一个柜子，柜子上放着他梦寐以求的饼干罐。他的脚尖几乎悬空，额头冒着汗，耳朵警惕地听着屋里的一切动静，生怕被妈妈发现。他的每一步都是那么小心翼翼，仿佛连空气都不敢打扰。
            ---
            """

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a visualization expert, skilled at converting abstract words into imagery to help students memorize vocabulary."},
                {"role": "user", "content": prompt}
            ],
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"分析过程中出现错误: {str(e)}"

def save_analysis(word, sentences_data, analysis, output_dir="output"):
    """保存分析结果到Markdown文件"""
    word_dir = os.path.join(output_dir, word)
    analysis_file = os.path.join(word_dir, f"{word}.md")
    
    with open(analysis_file, 'r', encoding='utf-8') as f:
        existing_content = f.readlines()
    
    with open(analysis_file, 'w', encoding='utf-8') as f:
        # 保持原有的表格内容
        for line in existing_content:
            if not line.startswith('## '): 
                f.write(line)
        
        # 写入助记分析
        f.write(f"\n## {word}单词图像助记\n\n")
        f.write(analysis)
