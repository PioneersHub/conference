# Conference

Playbook how to run a volunteer-driven conference

## How To Use

Fork this repository and adapt the content to your needs.

You need to add your event or conference name and contacts in the configuration.

Configure `config.yml` to your needs:

```yaml
event:
  event_name: "THE EVENT"
  coc_email: coc-reports@our-community.org
  team_members: |
    - Avery Sinclair
    - Morgan Ellis
    - Rowan Bennett
    - Taylor Monroe
  backup_team_members: |
    - Jordan Reese email@domain.com
    - Casey Whitman email@domain.com
```

add a custom logo to the social cards in the right bottom corner:

```yaml
social_cards:
  logo_path: "./docs/assets/images/social_card_logo.png"
```

## Attribution

This document draws on years of experience from organizing [PyCon DE](https://de.pycon.org/)
and [PyData Berlin](https://berlin.pydata.org) conferences.

# TODO: Tag main contributors

## Documentation

The documentation is written in Markdown and rendered with MKDocs.

MKDocs is used to generate the documentation.  
[Read the documentation](https://pioneershub.github.io/conference/)

Extra features are added with the Material for MkDocs theme.  
[MKDocs Material](https://squidfunk.github.io/mkdocs-material/)