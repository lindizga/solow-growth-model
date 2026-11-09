name: Run Tests

on:
  push:
  pull_request:

jobs:
  test:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - uses: mamba-org/setup-micromamba@v2
        with:
          environment-file: environment.yml

      - name: Run pytest
        shell: bash -l {0}
        run: pytest -v
