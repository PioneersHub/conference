"""
Script to manually add the Pioneers Hub logo to the social cards of website.
This is not supported by the open version of mkdocs-material, yet.
"""
from pathlib import Path

from PIL import Image


def on_post_build(config):
    # Importing conf is not working in CI
    root = Path(__file__).parents[1]

    # config extra as no attributes, workaround
    xtra = dict(config.extra)
    path_to_logo = root / xtra["social_cards"]["logo_path"]
    the_logo_position = (960, 450)
    base_width = 175
    ph_logo = Image.open(path_to_logo)
    w_percent = (base_width / ph_logo.size[0])
    h_size = int(float(ph_logo.size[1]) * float(w_percent))
    ph_logo = ph_logo.resize((base_width, h_size), Image.Resampling.LANCZOS)
    for k, dir_from_project_root in xtra["social_cards"]["dirs"].items():
        read_dir = root / dir_from_project_root
        for social_card in read_dir.glob('*.png'):
            # Get the social card image
            social_card_image = Image.open(social_card)
            # Paste the Pioneers Hub logo onto the social card image
            social_card_image.paste(ph_logo, the_logo_position, mask=ph_logo)
            # Save the new social card image
            social_card_image.save(social_card, quality=95)
