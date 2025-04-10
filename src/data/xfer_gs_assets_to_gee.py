import argparse
import sys
from pathlib import Path

# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from src.utils.gee_utils import transfer_gs_assets_to_gee


def cli() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Transfer Google Cloud Storage assets to Google Earth Engine."
    )
    parser.add_argument(
        "--gs_bucket",
        type=str,
        help="The Google Cloud Storage bucket. E.g. 'global-traits'.",
    )
    parser.add_argument(
        "--gee_project",
        type=str,
        help="The Google Earth Engine project. E.g. 'projects/global-traits'.",
    )

    parser.add_argument(
        "--filter_string",
        type=str,
        help="The string to filter the files E.g. 'Tree_Grass_1km'.",
    )

    parser.add_argument(
        "--folder_name",
        type=str,
        help="The name of the folder to store the files in E.g. 'Tree_Grass'.",
    )


    return parser.parse_args()


def main(args: argparse.Namespace = cli()) -> None:
    """Transfer Google Cloud Storage assets to Google Earth Engine."""
    transfer_gs_assets_to_gee(args.gs_bucket, args.gee_project, args.filter_string, args.folder_name)


if __name__ == "__main__":
    main()
