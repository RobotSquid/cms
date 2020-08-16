#!/usr/bin/env python3

"""Scratch programming language definition."""

from cms.grading import Language


__all__ = ["Scratch"]


class Scratch(Language):
    """This defines the Scratch programming language, interpreted with scratch-vm."""

    @property
    def name(self):
        """See Language.name."""
        return "Scratch"

    @property
    def source_extensions(self):
        """See Language.source_extensions."""
        return [".sb3", ".sb2", ".sb"]

    @property
    def time_multiplier(self):
        return 10

    def get_compilation_commands(self,
                                 source_filenames, executable_filename,
                                 for_evaluation=True):
        """See Language.get_compilation_commands."""
        return [["/bin/cp", source_filenames[0], executable_filename]]

    def get_evaluation_commands(
            self, executable_filename, main=None, args=None):
        """See Language.get_evaluation_commands."""
        args = args if args is not None else []
        return [["/usr/bin/node", "/home/ubuntu/scratch_sandbox/scratch-cli.js", executable_filename] + args]
