## Pre-commit
Used to setup git hook scripts which are useful for identifying small issues before submission of code.

### Installation - https://pre-commit.com/
```pip install pre-commit```

### Add a pre-commit configuration
```Create file .pre-commit-config```

### Install the git hook script.
The following command will make pre-commit autmatically run before every git commit <br>
```pre-commit install```

### Manually trigger pre-commit checks on all files.
```pre-commit run --all-files```

### Finding hooks
#### Official hooks from pre-commit:
https://github.com/pre-commit/pre-commit-hooks
#### Otherwise, look
