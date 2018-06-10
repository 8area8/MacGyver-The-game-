"""Core images file."""


from core.modules.images import collect_images


def test_collect_images():
    """Test if all images are collected."""
    images = collect_images()

    assert images["backgrounds"]["generic"]
