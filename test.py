#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ansibleci.config import Config
from ansibleci.runner import Runner

def main(config=False):

    # Create config instance.
    config = Config(load_defaults=True)

    # Load user-defined settings into config instance.
    try:
        import settings
        config.add_module(settings)
    except ImportError:
        pass

    # Start runner.
    Runner(config).run()

if __name__ == '__main__':
    main()