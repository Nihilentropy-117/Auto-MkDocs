# Auto-MkDocs

Auto-MkDocs is a Docker-based application that automatically regenerates and serves your MkDocs site whenever changes are detected in your markdown documents, as a more stable replacement for the built-in testing server. It does not refresh the page in browser for now, due to performance concerns for little real-world gain.

## How It Works

Auto-MkDocs consists of two Docker services:

- `mkdocs_watcher`: A Python script that watches for file changes in your MkDocs markdown files and rebuilds the site using [`mkdocs build --clean`](https://www.mkdocs.org/user-guide/custom-themes/#local-building-with-multiple-themes) whenever a change is detected. 
- `mkdocs_server`: A Python Flask app that serves the compiled MkDocs site. 

The two services share the compiled MkDocs files through a Docker volume. 

## Usage

1. Clone this repository and navigate into the repository's root directory.

   ```bash
   git clone https://github.com/nihilentropy-117/auto-mkdocs.git
   cd auto-mkdocs
   
2. Build and run the Docker services:

   ```bash
   docker-compose up --build
   ```

3. Go to `http://localhost:5000` in your web browser to view your live MkDocs site.

   Any changes you make to your markdown files in the `docs` directory will automatically trigger a site rebuild and the changes will be immediately viewable.

## Note
- There is no added security of any sort, at the minumum I would recommend hosting behind a reverse proxy. 
- The `docs` directory in the project root is mapped as a volume to `/app/docs` in the Docker container. Place your MkDocs markdown files here.
- The `mkdocs.yml` file in the project root is mapped to `/app/mkdocs.yml` in the Docker container to configure your MkDocs site.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

