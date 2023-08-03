# ChatGPT Problem Solver

The ChatGPT Problem Solver is a Python script that uses "Chain Prompting" and the "Tree of Thoughts" principle to solve problems, inspired by [this](https://www.youtube.com/watch?v=j320H2LFx-U) YouTube video. The script leverages the [RevChatGPT](https://github.com/acheong08/ChatGPT) library under the hood to talk to ChatGPT.

> [!WARNING]
> As of now this doesn't work, the prompts need serious work to make it work.

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

4. Add your `OPENAI_ACCESS_TOKEN` value in the `.env` file. Obtain the access token value from [here](https://chat.openai.com/api/auth/session).

## Usage

### Running the Script

To run the script, use the following command:

```bash
poetry run python main.py
```

### Input the Problem

Once the script is running, input the problem you want to solve using ChatGPT.

## Docker Installation

Alternatively, you can use Docker to run the ChatGPT Problem Solver:

1. Build the Docker image:

```bash
docker build -t chatgpt-problem-solver .
```

2. Add your `OPENAI_ACCESS_TOKEN` value in the `.env` file.

3. Run the Docker container:

```bash
docker run -it --rm --env-file .env chatgpt-problem-solver
```

## Contributing

Contributions are welcome! If you encounter any issues, have ideas for improvements, or want to add new features, feel free to create issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE). Your feedback and contributions are invaluable in making this project better. Thank you for your support!
