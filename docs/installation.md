---
hide:
  - navigation
---

# Installation & Set-Up

## How to Use the Template

Fork the `PioneersHub/conference` repository and adapt everything to your needs.

Feel free to suggest improvements or contribute to project
by [opening an issue or pull request](https://github.com/PioneersHub/conference/pulls) at `PioneersHub/conference`.

## Environment

This project uses the Pixi package management.
Pixi supports Windows, macOS, and Linux.
See the [Pixi documentation](https://pixi.sh/latest/) for more information how to install Pixi.

To install the environment, run the following command for the project root directory:

```shell
pixi install
```

### Configuration

The template automatically publishes information based on the settings in the `config.yml` file.

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
  apply_url: "https://example.com/apply"
  contact_email: "info@contact.org"
``` 

#### 4. Committees' details

Outline the expected workloads and milestones for each committee via the configuration file.

The dates are published at the bottom of the [committees](committees/index.md) pages.

```yaml
committees:
  # Committee names must match the headers in the committees.md file
  # Expected workloads and milestones for each committee
  "coc":  # key for the committee
    requirements:
      attend_conference: true
    workload:
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

The documentation website is hosted at GitHub pages.

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
