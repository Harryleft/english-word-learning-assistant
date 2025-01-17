<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stars][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<div align="center">
  
English | [简体中文](./README.md)

</div>

<!-- Project Introduction -->
<div align="center">
  <h3 align="center">Harry Potter Series English Word Learning Assistant</h3>

  <p align="center">
    An English word learning assistant based on the Harry Potter series, helping learners study English vocabulary through the original novels.
    <br />
    <a href="https://github.com/Harryleft/english-word-learning-assistant"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Harryleft/english-word-learning-assistant/issues/new?labels=bug">Report Bug</a>
    ·
    <a href="https://github.com/Harryleft/english-word-learning-assistant/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#background">Background</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Background

This project aims to help English learners study vocabulary through the Harry Potter series.

By extracting example sentences from the original novels, downloading word pronunciations, and providing AI-powered visual analysis, it offers a convenient tool for English vocabulary learning.

## Features

- 📚 Extract example sentences from Harry Potter series
- 🔍 Support word variants and morphological recognition
- 🎧 Automatic word pronunciation download
- 🤖 AI-powered word analysis and memorization
- ✨ Support batch word processing

## Project Structure

```
.
├── main.py                 # Main program entry
├── find_sentence_with_word.py  # Sentence extraction module
├── english_pronounce_audio_download.py  # Audio download module
├── ai_explain.py          # AI analysis module
├── data/                  # Original text directory
├── output/               # Output directory
└── audio_downloads/      # Audio files directory
```

## Installation

1. Clone the project
```bash
git clone https://github.com/Harryleft/english-word-learning-assistant.git
cd english-word-learning-assistant
```

2. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

3. Configure environment variables
```bash
# Set OpenAI API Key (for AI analysis feature)
export OPENAI_API_KEY=your_api_key
```

## Usage

1. Run the program
```bash
python main.py
```

2. Select function
- 1: Find example sentences from text
- 2: Download word pronunciation
- 3: Analyze word usage
- 4: Execute complete learning process

3. Input words
- Support multiple words (space-separated)
- Automatically handle word variants

## Acknowledgments

- [spaCy](https://spacy.io/) - Natural Language Processing Library
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Audio Download Tool
- [OpenAI API](https://openai.com/blog/openai-api) - AI Analysis Support

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

<!-- Badge Links -->
[contributors-shield]: https://img.shields.io/github/contributors/Harryleft/english-word-learning-assistant.svg?style=for-the-badge
[contributors-url]: https://github.com/Harryleft/english-word-learning-assistant/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Harryleft/english-word-learning-assistant.svg?style=for-the-badge
[forks-url]: https://github.com/Harryleft/english-word-learning-assistant/network/members
[stars-shield]: https://img.shields.io/github/stars/Harryleft/english-word-learning-assistant.svg?style=for-the-badge
[stars-url]: https://github.com/Harryleft/english-word-learning-assistant/stargazers
[issues-shield]: https://img.shields.io/github/issues/Harryleft/english-word-learning-assistant.svg?style=for-the-badge
[issues-url]: https://github.com/Harryleft/english-word-learning-assistant/issues
[license-shield]: https://img.shields.io/github/license/Harryleft/english-word-learning-assistant.svg?style=for-the-badge
[license-url]: https://github.com/Harryleft/english-word-learning-assistant/blob/master/LICENSE 