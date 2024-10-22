---
hide:
  - navigation
---

# :fontawesome-solid-building-user: Installation & Set-Up

## How to Use the Template

Fork the `PioneersHub/conference` repository and adapt everything to your needs.

These parts of the repository need to be customized to your conference:

##### GitHub

- [ ] Update the `README.md` with your conference name and description to avoid confusion.
  Remove anything that is not relevant to your conference.
  We appreciate if you keep the _Community Playbooks by Pioneers Hub_ section at the bottom.
- [ ] Update site configuration in the `mkdocs.yml`:
    - [ ] site_name: Your conference name
    - [ ] site_url: This is where your conference website will be
      hosted: https://your-github-nick.github.io/conference-3000/
    - [ ] site_author, site_description,
    - [ ] repo_name: your-github-nick/conference-3000
    - [ ] repo_url: https://github.com/your-github-nick/conference-3000
    - [ ] nav: Leave this for now. This is only required if you remove, rearrange or add pages.
    - [ ] copyright: Update with your name or organization.
- [ ] Update the conference configuration, [see below for detailed instructions](#configuration)
- [ ] Update the `pyproject.toml` file with your conference name and description.
- [ ] Replace the conference logo to the `assets/images/` folder with the file name `social_card_logo.png`.
- [ ] Follow the instructions in docs/installation.md to set up your [environment](#environment), see below.
      This is required to build the documentation.
- [ ] Create the website, see [Publishing below](#publishing).
- [ ] The website is hosted on GitHub pages. Enable GitHub pages in the repository settings.

## Environment

This project supports the great Pixi package management as well as a requirements.txt file
if you prefer to use a virtual environment.

```shell
# requires uv installed, alternatively you can use any other python virtual environment
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Pixi supports Windows, macOS, and Linux.
See the [Pixi documentation](https://pixi.sh/latest/) for more information how to install Pixi.

To install the environment, run the following command for the project root directory:

```shell
pixi install
```

### Configuration

The template automatically publishes information based on the settings in the `config.yml` file.

The configuration file is a crucial file especially for the timeline and committees. 
It stores all dates, emails, links, etc. in **once place** and makes it easy to update.

Configure your repository by editing the `config.yml` file.

#### 1. Set your site setting

```yaml
site_name: Put your event name here
site_url: Link to your github.io page, e.g. https://pioneershub.github.io/conference/
site_author: Author(s)
site_description: >-
  Add a custom description about your event.
``` 

#### 2. GitHub repository details

```yaml
repo_name: GitHub repository name, e.g., PioneersHub/conference
repo_url: GitHub repository URL, e.g., https://github.com/PioneersHub/conference
``` 

#### 3. Event details

```yaml
# Event details
event:
  event_name: "THE EVENT"
  start_date: "2025-04-23"
  end_date: "2025-04-26"
  location: "Somewhere, Germany"
  apply_url_committees: "https://example.com/apply"
  contact_email: "info@contact.org"
``` 

#### 4. Committees' details

Outline the expected workloads and milestones for each committee via the configuration file. 
Take your time to define the workload and milestones for each committee.

At the start, give your best guess for the workload and milestones.
This information is important so people interested in joining know what to expect.

The dates are published at the bottom of the [committees](committees/index.md) pages.

```yaml
committees:
  # Committee names must match the headers in the committees.md file
  # Expected workloads and milestones for each committee
  "coc": # key for the committee
    requirements:
      attend_conference: true
    workload:
      average: "1-2 hours per week"
      start: "start-date-here"
      peak: "During the conference"
      end: "Until all reports have been resolved"
``` 

Example snippet from committee page:

```markdown
### Timeline

:fontawesome-regular-calendar:  **start:**{{config.extra.committees.coc.workload.start}}
```

### Preview the Documentation

Run

```
mkdocs serve
```  

to start the live-reloading docs server.

The local website is run
on [http://127.0.0.1:8000/your_event/](http://127.0.0.1:8000/pytube/)

MacOS-Error
> no library called "cairo-2" was found…

can be fixed with:

```
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
mkdocs serve
```

[See here for details](https://t.ly/MfX6u)

### Publishing

The documentation website resides in a separate branch called `gh-pages`.
This branch is automatically updated by mkdocs.

The documentation website is hosted at GitHub pages. 
The documentation website is rendered if the `main` branch is updated. 

To deploy:

```
mkdocs gh-deploy
```

The repository also contains a GitHub action that automatically deploys the documentation to GitHub pages.

## Versioning Schema

The versioning schema is `{major}.{minor}.{patch}[{release}{build}]` where the
latter part (release and build) is optional.

It is recommended to do `--dry-run` prior to your actual run.

```bash
# increase version identifier
bumpversion [major/minor/patch/release/build]  # --verbose --dry-run

# e.g.
bumpversion minor  # e.g. 0.5.1 --> 0.6.0
bumpversion minor --new-version 0.7.0  # e.g. 0.5.1 --> 0.7.0
```
