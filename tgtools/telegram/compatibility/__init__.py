from tgtools.models.file_summary import FileSummary
from tgtools.telegram.compatibility.base import MediaCompatibility, MediaSummary, MediaType
from tgtools.telegram.compatibility.document import DocumentCompatibility
from tgtools.telegram.compatibility.gif import GifCompatibility
from tgtools.telegram.compatibility.image import ImageCompatibility
from tgtools.telegram.compatibility.video import VideoCompatibility

__all__ = ["make_tg_compatible"]


async def make_tg_compatible(
    file: MediaSummary, force_download: bool = False
) -> tuple[FileSummary | MediaSummary | None, MediaType]:
    """
    Make sure the file is compatible with Telegram.

    Args:
        file (MediaSummary): The media file to be checked for compatibility.
        force_download (bool): Force download the file (defaults to False).

    Returns:
        tuple[FileSummary | MediaSummary | None, MediaType]: A tuple containing either the adjusted file summary and
                                                             its type. None if the file is not compatible in any way.
    """
    compatibility: MediaCompatibility
    if file.is_image:
        compatibility = ImageCompatibility(file)
    elif file.is_video:
        compatibility = VideoCompatibility(file)
    elif file.is_gif:
        compatibility = GifCompatibility(file)
    else:
        compatibility = DocumentCompatibility(file)

    return await compatibility.make_compatible(force_download=force_download)
