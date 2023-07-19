# ChatGPT Problem Solver

The ChatGPT Problem Solver is a Python script that uses "Chain Prompting" and the "Tree of Thoughts" principle to solve problems, inspired by [this](https://www.youtube.com/watch?v=j320H2LFx-U) YouTube video. This script uses leverages the [RevChatGPT](https://github.com/acheong08/ChatGPT) library under the hood to talk to ChatGPT.

## Prerequisites

- **Poetry**: Install Poetry from the [official website](https://python-poetry.org/docs/#installation).

## Installation

1. Clone the repository:

```bash
git clone https://www.github.com/ashishbinu/chatgpt-problem-solver
cd chatgpt-problem-solver
```

2. Install dependencies using Poetry:

```bash
poetry install
```

3. Copy `.env.example` to `.env`.

```bash
cp .env.example .env
```

4. Add `OPENAI_ACCESS_TOKEN` value in `.env` file. Get the access token value from [here](https://chat.openai.com/api/auth/session).

## Usage

Run the script:

```bash
poetry run python main.py
```

Input the problem and get the answer.

## Contributing

Contributions are welcome! If you encounter any issues, have ideas for improvements, or want to add new features, feel free to create issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE). Your feedback and contributions are invaluable in making this project better. Thank you for your support!
