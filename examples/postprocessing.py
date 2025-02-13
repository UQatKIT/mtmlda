"""Executable script for MTMLDA run postprocessing.

This script is an executable wrapper for the Postprocessor class. It performs postprocessing of
an MTMLDA run according to the provided settings files.
For info on how to run the script, type `python run.py --help` in the command line.

Functions:
    process_cli_arguments: Read in command-line arguments for application to run.
    main: Main routine to be invoked when script is executed
"""

import argparse
import importlib
import warnings

from mtmlda.run import postprocessor


# ==================================================================================================
def process_cli_arguments() -> str:
    """Read in command-line arguments for postprocessing settings."""
    arg_parser = argparse.ArgumentParser(
        prog="postprocessing.py",
        usage="python %(prog)s [options]",
        description="Postprocessing file for parallel MLDA sampling",
    )

    arg_parser.add_argument(
        "-app",
        "--application",
        type=str,
        required=True,
        help="Application directory",
    )

    arg_parser.add_argument(
        "-s",
        "--settings",
        type=str,
        required=False,
        default="settings",
        help="Application settings file",
    )

    cli_args = arg_parser.parse_args()
    application_dir = cli_args.application.replace("/", ".").strip(".")
    settings_dir = f"{application_dir}.{cli_args.settings}"

    return settings_dir


# ==================================================================================================
def main() -> None:
    """Entry point for the script, constructs and runs the Postprocessor."""
    settings_dir = process_cli_arguments()
    settings_module = importlib.import_module(settings_dir)

    print("\n=== Start Postprocessing ===\n")
    pproc = postprocessor.Postprocessor(settings_module.postprocessor_settings)
    pproc.run()
    print("\n============================\n")


if __name__ == "__main__":
    warnings.simplefilter("ignore", FutureWarning)
    main()
